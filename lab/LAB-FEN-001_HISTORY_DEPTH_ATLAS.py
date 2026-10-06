from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import platform
import subprocess

from collections import Counter, defaultdict
from pathlib import Path


VERSION = "HISTORY-DEPTH-ATLAS-v1"

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
RESULTS = ROOT / "results"

SPEC_PATH = (
    ROOT
    / "LAB-FEN-001_HISTORY_DEPTH_ATLAS_SPEC_v1.md"
)

SELF_PATH = Path(__file__).resolve()

HD_EXEC = (
    ROOT
    / "LAB-FEN-001_HISTORY_DEPTH.py"
)

HD_RESULT = (
    RESULTS
    / "LAB-FEN-001_HISTORY_DEPTH_v1_results.json"
)

ATLAS_RESULT = (
    RESULTS
    / "LAB-FEN-001_D2_ATLAS_v1_results.json"
)

ATLAS_SERIES = (
    RESULTS
    / "LAB-FEN-001_D2_ATLAS_v1_series.csv.gz"
)

D2_SERIES = (
    RESULTS
    / "LAB-FEN-001_D2_v1_series.csv.gz"
)

OUTPUT_JSON = (
    RESULTS
    / "LAB-FEN-001_HISTORY_DEPTH_ATLAS_v1_results.json"
)

OUTPUT_CSV = (
    RESULTS
    / "LAB-FEN-001_HISTORY_DEPTH_ATLAS_v1_summary.csv"
)


EXPECTED_ATLAS_POINTS = 20
EXPECTED_EXECUTED_POINTS = 19
EXPECTED_SEEDS = 8
EXPECTED_STATES = 30_001
EXPECTED_ATLAS_GROUPS = 152
EXPECTED_ATLAS_ROWS = 4_560_152

BASELINE_KEY = "beta=+0.00|epsilon=0.00"

CORE_BETAS = {
    -0.05,
    0.00,
    0.05,
}

CORE_EPSILONS = {
    0.00,
    0.05,
    0.10,
}


# ============================================================
# UTILIDADES
# ============================================================

def read_json(path: Path):
    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as fh:
        while True:
            block = fh.read(
                1024 * 1024
            )

            if not block:
                break

            h.update(block)

    return h.hexdigest()


def git_head() -> str:
    completed = subprocess.run(
        [
            "git",
            "rev-parse",
            "HEAD",
        ],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )

    return completed.stdout.strip()


def load_frozen_history_depth():
    spec = importlib.util.spec_from_file_location(
        "lab_fen_001_history_depth_frozen",
        HD_EXEC,
    )

    if spec is None or spec.loader is None:
        raise RuntimeError(
            "no se pudo cargar HISTORY-DEPTH-v1"
        )

    module = importlib.util.module_from_spec(
        spec
    )

    spec.loader.exec_module(
        module
    )

    return module


HD = load_frozen_history_depth()


def point_key(
    beta: float,
    epsilon: float,
) -> str:
    return (
        f"beta={beta:+.2f}"
        f"|epsilon={epsilon:.2f}"
    )


def is_core(
    beta: float,
    epsilon: float,
) -> bool:
    return (
        round(beta, 2)
        in CORE_BETAS
        and
        round(epsilon, 2)
        in CORE_EPSILONS
    )


# ============================================================
# VERIFICACION DEL INSTRUMENTO CONGELADO
# ============================================================

def verify_frozen_instrument():
    hd_result = read_json(
        HD_RESULT
    )

    trace = hd_result.get(
        "trace",
        {},
    )

    executable_sha = sha256_file(
        HD_EXEC
    )

    declared_exec_sha = trace.get(
        "executable_sha256"
    )

    if executable_sha != declared_exec_sha:
        raise AssertionError(
            "el ejecutable HISTORY-DEPTH-v1 "
            "ya no coincide con su hash congelado"
        )

    if (
        hd_result.get(
            "summary",
            {}
        ).get(
            "history_depth_v1_pass"
        )
        is not True
    ):
        raise AssertionError(
            "HISTORY-DEPTH-v1 congelado "
            "no figura como PASS"
        )

    systems = hd_result.get(
        "systems",
        {}
    )

    baseline = systems.get(
        "HD-D2"
    )

    if baseline is None:
        raise AssertionError(
            "falta HD-D2 en HISTORY-DEPTH-v1"
        )

    if (
        baseline.get(
            "expected"
        )
        != "k*=2"
    ):
        raise AssertionError(
            "expectativa basal distinta de k*=2"
        )

    if (
        baseline.get(
            "expected_count"
        )
        != 8
    ):
        raise AssertionError(
            "el basal congelado no obtuvo 8/8"
        )

    if (
        baseline.get(
            "system_pass"
        )
        is not True
    ):
        raise AssertionError(
            "HD-D2 basal congelado no es PASS"
        )

    seed_records = baseline.get(
        "seeds",
        []
    )

    if len(seed_records) != 8:
        raise AssertionError(
            "HD-D2 basal no contiene 8 semillas"
        )

    if not all(
        record.get(
            "classification"
        )
        == "k*=2"
        for record in seed_records
    ):
        raise AssertionError(
            "el basal no es k*=2 en 8/8"
        )

    return {
        "history_depth_result": (
            hd_result
        ),
        "baseline": baseline,
        "executable_sha256": (
            executable_sha
        ),
    }


# ============================================================
# ATLAS JSON
# ============================================================

def inspect_atlas_contract():
    atlas = read_json(
        ATLAS_RESULT
    )

    points = atlas.get(
        "points",
        []
    )

    if len(points) != EXPECTED_ATLAS_POINTS:
        raise AssertionError(
            f"atlas JSON contiene {len(points)} "
            f"puntos; esperados "
            f"{EXPECTED_ATLAS_POINTS}"
        )

    by_key = {}

    for point in points:
        key = point.get(
            "key"
        )

        if not key:
            raise AssertionError(
                "punto del atlas sin key"
            )

        if key in by_key:
            raise AssertionError(
                f"key duplicada: {key}"
            )

        by_key[key] = point

    if BASELINE_KEY not in by_key:
        raise AssertionError(
            "falta punto basal en atlas JSON"
        )

    baseline = by_key[
        BASELINE_KEY
    ]

    if (
        baseline.get(
            "source"
        )
        != "frozen LAB-D2-v1 result"
    ):
        raise AssertionError(
            "source basal inesperado"
        )

    if len(
        baseline.get(
            "results"
        )
        or []
    ) != 0:
        raise AssertionError(
            "el basal no debe contener "
            "resultados regenerados"
        )

    executed = [
        point
        for point in points
        if point[
            "key"
        ] != BASELINE_KEY
    ]

    if (
        len(executed)
        != EXPECTED_EXECUTED_POINTS
    ):
        raise AssertionError(
            "numero inesperado de puntos "
            "ejecutados del atlas"
        )

    core = [
        point
        for point in points
        if is_core(
            float(
                point["beta"]
            ),
            float(
                point["epsilon"]
            ),
        )
    ]

    if len(core) != 9:
        raise AssertionError(
            "el nucleo no contiene 9 puntos"
        )

    region = atlas.get(
        "region",
        {}
    )

    if (
        region.get(
            "core_points"
        )
        != 9
    ):
        raise AssertionError(
            "core_points declarado != 9"
        )

    if (
        region.get(
            "full_grid_points"
        )
        != 20
    ):
        raise AssertionError(
            "full_grid_points declarado != 20"
        )

    return {
        "atlas": atlas,
        "by_key": by_key,
        "core_keys": sorted(
            point["key"]
            for point in core
        ),
    }


# ============================================================
# SERIES DEL ATLAS
# ============================================================

def stream_atlas_structure():
    groups = Counter()
    points = Counter()

    total_rows = 0

    with gzip.open(
        ATLAS_SERIES,
        "rt",
        encoding="utf-8",
        newline="",
    ) as fh:
        reader = csv.DictReader(
            fh
        )

        expected_header = [
            "version",
            "beta",
            "epsilon",
            "seed",
            "t",
            "state",
        ]

        if (
            reader.fieldnames
            != expected_header
        ):
            raise AssertionError(
                "header atlas inesperado: "
                f"{reader.fieldnames}"
            )

        for row in reader:
            beta = round(
                float(
                    row["beta"]
                ),
                2,
            )

            epsilon = round(
                float(
                    row["epsilon"]
                ),
                2,
            )

            seed = int(
                row["seed"]
            )

            if seed not in HD.SEEDS:
                raise AssertionError(
                    f"seed inesperada: {seed}"
                )

            state = int(
                row["state"]
            )

            if state not in HD.ALPHABET:
                raise AssertionError(
                    f"estado inesperado: {state}"
                )

            key = (
                beta,
                epsilon,
                seed,
            )

            groups[key] += 1

            points[
                (
                    beta,
                    epsilon,
                )
            ] += 1

            total_rows += 1

    if (
        total_rows
        != EXPECTED_ATLAS_ROWS
    ):
        raise AssertionError(
            f"filas atlas={total_rows}, "
            f"esperadas={EXPECTED_ATLAS_ROWS}"
        )

    if (
        len(points)
        != EXPECTED_EXECUTED_POINTS
    ):
        raise AssertionError(
            f"puntos materializados={len(points)}, "
            f"esperados={EXPECTED_EXECUTED_POINTS}"
        )

    if (
        len(groups)
        != EXPECTED_ATLAS_GROUPS
    ):
        raise AssertionError(
            f"grupos={len(groups)}, "
            f"esperados={EXPECTED_ATLAS_GROUPS}"
        )

    unique_counts = set(
        groups.values()
    )

    if unique_counts != {
        EXPECTED_STATES
    }:
        raise AssertionError(
            "conteo por grupo inesperado: "
            f"{sorted(unique_counts)}"
        )

    if (
        (0.0, 0.0)
        in points
    ):
        raise AssertionError(
            "el basal no debe estar "
            "materializado en atlas series"
        )

    return {
        "rows": total_rows,
        "points": len(points),
        "groups": len(groups),
        "states_per_group": (
            EXPECTED_STATES
        ),
    }


def load_atlas_series():
    groups = defaultdict(
        bytearray
    )

    expected_t = defaultdict(
        int
    )

    with gzip.open(
        ATLAS_SERIES,
        "rt",
        encoding="utf-8",
        newline="",
    ) as fh:
        reader = csv.DictReader(
            fh
        )

        for row in reader:
            beta = round(
                float(
                    row["beta"]
                ),
                2,
            )

            epsilon = round(
                float(
                    row["epsilon"]
                ),
                2,
            )

            seed = int(
                row["seed"]
            )

            t = int(
                row["t"]
            )

            state = int(
                row["state"]
            )

            key = (
                beta,
                epsilon,
                seed,
            )

            if t != expected_t[key]:
                raise AssertionError(
                    f"t no contiguo en {key}: "
                    f"{t} != {expected_t[key]}"
                )

            expected_t[key] += 1

            groups[key].append(
                state
            )

    if len(groups) != 152:
        raise AssertionError(
            "load atlas: grupos != 152"
        )

    for key, states in groups.items():
        if (
            len(states)
            != EXPECTED_STATES
        ):
            raise AssertionError(
                f"{key}: "
                f"{len(states)} estados"
            )

    return dict(
        groups
    )


# ============================================================
# PUNTO BASAL CONGELADO
# ============================================================

def frozen_baseline_point(
    baseline,
):
    seeds = []

    for source_record in baseline[
        "seeds"
    ]:
        seeds.append(
            {
                "seed": (
                    source_record[
                        "seed"
                    ]
                ),
                "classification": (
                    source_record[
                        "classification"
                    ]
                ),
                "expected": "k*=2",
                "expected_match": (
                    source_record[
                        "classification"
                    ]
                    == "k*=2"
                ),
                "gains": (
                    source_record[
                        "gains"
                    ]
                ),
                "source": (
                    "frozen HISTORY-DEPTH-v1 "
                    "HD-D2 result"
                ),
            }
        )

    count = sum(
        1
        for record in seeds
        if record[
            "classification"
        ]
        == "k*=2"
    )

    return {
        "key": BASELINE_KEY,
        "beta": 0.0,
        "epsilon": 0.0,
        "core": True,
        "source": (
            "frozen HISTORY-DEPTH-v1 "
            "HD-D2 result"
        ),
        "expected": "k*=2",
        "k2_count": count,
        "required": 7,
        "depth_point_pass": (
            count >= 7
        ),
        "classification_counts": {
            "k*=2": count,
        },
        "seeds": seeds,
    }


# ============================================================
# EVALUACION DE UN PUNTO
# ============================================================

def evaluate_point(
    beta: float,
    epsilon: float,
    series_groups,
):
    key = point_key(
        beta,
        epsilon,
    )

    seed_results = []

    for seed in HD.SEEDS:
        series_key = (
            round(beta, 2),
            round(epsilon, 2),
            seed,
        )

        if (
            series_key
            not in series_groups
        ):
            raise AssertionError(
                f"falta serie para {series_key}"
            )

        states = series_groups[
            series_key
        ]

        gains = {}

        for order in HD.ORDERS:
            # Importante:
            #
            # se conserva el identificador HD-D2
            # del instrumento congelado.
            #
            # De esta forma la secuencia
            # determinista de permutaciones
            # nulas no se redefine por punto
            # del atlas.

            result = HD.evaluate_gain(
                "HD-D2",
                seed,
                states,
                order,
            )

            gains[
                str(order)
            ] = result

        classification = (
            HD.classify_depth(
                gains
            )
        )

        seed_results.append(
            {
                "seed": seed,
                "classification": (
                    classification
                ),
                "expected": "k*=2",
                "expected_match": (
                    classification
                    == "k*=2"
                ),
                "gains": gains,
                "source": (
                    "frozen ATLAS-v1 series"
                ),
            }
        )

        g2 = gains["2"]
        g3 = gains["3"]
        g4 = gains["4"]

        print(
            f"  seed={seed:3d}  "
            f"G2={g2['G']:+.6f} "
            f"H2={'Y' if g2['hit'] else 'N'}  "
            f"G3={g3['G']:+.6f} "
            f"H3={'Y' if g3['hit'] else 'N'}  "
            f"G4={g4['G']:+.6f} "
            f"H4={'Y' if g4['hit'] else 'N'}  "
            f"{classification}"
        )

    counts = Counter(
        record[
            "classification"
        ]
        for record
        in seed_results
    )

    k2_count = counts.get(
        "k*=2",
        0,
    )

    point_pass = (
        k2_count >= 7
    )

    g2_values = [
        record["gains"]["2"]["G"]
        for record in seed_results
    ]

    g3_values = [
        record["gains"]["3"]["G"]
        for record in seed_results
    ]

    g4_values = [
        record["gains"]["4"]["G"]
        for record in seed_results
    ]

    return {
        "key": key,
        "beta": beta,
        "epsilon": epsilon,
        "core": is_core(
            beta,
            epsilon,
        ),
        "source": (
            "frozen ATLAS-v1 series"
        ),
        "expected": "k*=2",
        "k2_count": k2_count,
        "required": 7,
        "depth_point_pass": (
            point_pass
        ),
        "classification_counts": dict(
            sorted(
                counts.items()
            )
        ),
        "G2_min": min(
            g2_values
        ),
        "G2_max": max(
            g2_values
        ),
        "G3_min": min(
            g3_values
        ),
        "G3_max": max(
            g3_values
        ),
        "G4_min": min(
            g4_values
        ),
        "G4_max": max(
            g4_values
        ),
        "seeds": seed_results,
    }


# ============================================================
# STRUCTURE CHECK
# ============================================================

def check_structure():
    required = (
        SPEC_PATH,
        HD_EXEC,
        HD_RESULT,
        ATLAS_RESULT,
        ATLAS_SERIES,
        D2_SERIES,
        SELF_PATH,
    )

    missing = [
        str(path)
        for path in required
        if not path.exists()
    ]

    if missing:
        raise AssertionError(
            "faltan archivos: "
            + ", ".join(missing)
        )

    frozen = (
        verify_frozen_instrument()
    )

    atlas_contract = (
        inspect_atlas_contract()
    )

    series_structure = (
        stream_atlas_structure()
    )

    if tuple(
        HD.SEEDS
    ) != (
        11,
        23,
        37,
        51,
        79,
        101,
        131,
        173,
    ):
        raise AssertionError(
            "seeds del instrumento cambiaron"
        )

    if HD.ALPHA != 0.5:
        raise AssertionError(
            "alpha del instrumento cambio"
        )

    if (
        HD.NULL_PERMUTATIONS
        != 64
    ):
        raise AssertionError(
            "numero de nulos cambio"
        )

    if HD.NULL_Q != 0.95:
        raise AssertionError(
            "Q del instrumento cambio"
        )

    if tuple(
        HD.ORDERS
    ) != (
        2,
        3,
        4,
    ):
        raise AssertionError(
            "ordenes del instrumento cambiaron"
        )

    return {
        "history_depth_executable_sha256": (
            frozen[
                "executable_sha256"
            ]
        ),
        "atlas_json_points": 20,
        "core_points": len(
            atlas_contract[
                "core_keys"
            ]
        ),
        "materialized_atlas_points": (
            series_structure[
                "points"
            ]
        ),
        "materialized_groups": (
            series_structure[
                "groups"
            ]
        ),
        "materialized_rows": (
            series_structure[
                "rows"
            ]
        ),
        "states_per_group": (
            series_structure[
                "states_per_group"
            ]
        ),
        "baseline_materialized": False,
        "baseline_source": (
            "frozen HISTORY-DEPTH-v1 "
            "HD-D2 result"
        ),
        "null_rng_identity": "HD-D2",
        "alpha": HD.ALPHA,
        "null_permutations": (
            HD.NULL_PERMUTATIONS
        ),
        "null_q": HD.NULL_Q,
        "orders": list(
            HD.ORDERS
        ),
        "simulation_calls": 0,
    }


# ============================================================
# EJECUCION
# ============================================================

def run_experiment():
    structure = check_structure()

    frozen = (
        verify_frozen_instrument()
    )

    atlas_contract = (
        inspect_atlas_contract()
    )

    series_groups = (
        load_atlas_series()
    )

    atlas_points = (
        atlas_contract[
            "atlas"
        ][
            "points"
        ]
    )

    results_by_key = {}

    baseline = frozen_baseline_point(
        frozen[
            "baseline"
        ]
    )

    results_by_key[
        BASELINE_KEY
    ] = baseline

    print()
    print(
        BASELINE_KEY
        + "  [FROZEN BASELINE]"
    )

    print("-" * 104)

    for seed_record in baseline[
        "seeds"
    ]:
        gains = seed_record[
            "gains"
        ]

        g2 = gains["2"]
        g3 = gains["3"]
        g4 = gains["4"]

        print(
            f"  seed={seed_record['seed']:3d}  "
            f"G2={g2['G']:+.6f} "
            f"H2={'Y' if g2['hit'] else 'N'}  "
            f"G3={g3['G']:+.6f} "
            f"H3={'Y' if g3['hit'] else 'N'}  "
            f"G4={g4['G']:+.6f} "
            f"H4={'Y' if g4['hit'] else 'N'}  "
            f"{seed_record['classification']}"
        )

    print(
        "POINT RESULT: "
        f"{baseline['k2_count']}/8 "
        "k*=2  "
        + (
            "PASS"
            if baseline[
                "depth_point_pass"
            ]
            else "FAIL"
        )
    )

    for point in atlas_points:
        key = point[
            "key"
        ]

        if key == BASELINE_KEY:
            continue

        beta = float(
            point[
                "beta"
            ]
        )

        epsilon = float(
            point[
                "epsilon"
            ]
        )

        print()
        print(
            key
            + (
                "  [CORE]"
                if is_core(
                    beta,
                    epsilon,
                )
                else "  [EXTENDED]"
            )
        )

        print("-" * 104)

        result = evaluate_point(
            beta,
            epsilon,
            series_groups,
        )

        results_by_key[
            key
        ] = result

        print(
            "POINT RESULT: "
            f"{result['k2_count']}/8 "
            "k*=2  "
            + (
                "PASS"
                if result[
                    "depth_point_pass"
                ]
                else "FAIL"
            )
        )

    ordered_points = [
        results_by_key[
            point[
                "key"
            ]
        ]
        for point in atlas_points
    ]

    core_points = [
        point
        for point in ordered_points
        if point[
            "core"
        ]
    ]

    extended_points = [
        point
        for point in ordered_points
        if not point[
            "core"
        ]
    ]

    core_passes = sum(
        1
        for point in core_points
        if point[
            "depth_point_pass"
        ]
    )

    full_grid_passes = sum(
        1
        for point in ordered_points
        if point[
            "depth_point_pass"
        ]
    )

    global_pass = (
        len(core_points) == 9
        and
        core_passes == 9
    )

    all_classifications = Counter()

    for point in ordered_points:
        for seed_result in point[
            "seeds"
        ]:
            all_classifications[
                seed_result[
                    "classification"
                ]
            ] += 1

    payload = {
        "version": VERSION,

        "contract": {
            "formal_core_points": 9,
            "required_k2_per_point": 7,
            "required_core_point_passes": 9,
            "expected_classification": (
                "k*=2"
            ),
            "full_grid_points": 20,
            "extended_points_descriptive": 11,
            "instrument": (
                "HISTORY-DEPTH-v1"
            ),
            "null_rng_identity": (
                "HD-D2"
            ),
        },

        "trace": {
            "git_head": git_head(),
            "python": (
                platform.python_version()
            ),
            "spec_sha256": sha256_file(
                SPEC_PATH
            ),
            "executable_sha256": (
                sha256_file(
                    SELF_PATH
                )
            ),
            "history_depth_executable_sha256": (
                sha256_file(
                    HD_EXEC
                )
            ),
            "history_depth_result_sha256": (
                sha256_file(
                    HD_RESULT
                )
            ),
            "atlas_result_sha256": (
                sha256_file(
                    ATLAS_RESULT
                )
            ),
            "atlas_series_sha256": (
                sha256_file(
                    ATLAS_SERIES
                )
            ),
            "d2_series_sha256": (
                sha256_file(
                    D2_SERIES
                )
            ),
        },

        "structure": structure,

        "points": ordered_points,

        "region": {
            "core_points": len(
                core_points
            ),
            "core_depth_point_passes": (
                core_passes
            ),
            "history_depth_atlas_v1_pass": (
                global_pass
            ),
            "extended_points": len(
                extended_points
            ),
            "full_grid_points": len(
                ordered_points
            ),
            "full_grid_depth_point_passes": (
                full_grid_passes
            ),
            "classification_counts": dict(
                sorted(
                    all_classifications.items()
                )
            ),
        },
    }

    return payload


# ============================================================
# SALIDAS
# ============================================================

def write_outputs(payload):
    RESULTS.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_JSON.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as fh:
        json.dump(
            payload,
            fh,
            ensure_ascii=False,
            indent=2,
        )

        fh.write("\n")

    with OUTPUT_CSV.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as fh:
        fieldnames = [
            "version",
            "key",
            "beta",
            "epsilon",
            "core",
            "seed",
            "classification",
            "expected_match",
            "G2",
            "G2_p95",
            "G2_hit",
            "G3",
            "G3_p95",
            "G3_hit",
            "G4",
            "G4_p95",
            "G4_hit",
        ]

        writer = csv.DictWriter(
            fh,
            fieldnames=fieldnames,
            lineterminator="\n",
        )

        writer.writeheader()

        for point in payload[
            "points"
        ]:
            for seed_result in point[
                "seeds"
            ]:
                gains = seed_result[
                    "gains"
                ]

                g2 = gains["2"]
                g3 = gains["3"]
                g4 = gains["4"]

                writer.writerow(
                    {
                        "version": VERSION,
                        "key": point[
                            "key"
                        ],
                        "beta": point[
                            "beta"
                        ],
                        "epsilon": point[
                            "epsilon"
                        ],
                        "core": point[
                            "core"
                        ],
                        "seed": seed_result[
                            "seed"
                        ],
                        "classification": (
                            seed_result[
                                "classification"
                            ]
                        ),
                        "expected_match": (
                            seed_result[
                                "expected_match"
                            ]
                        ),
                        "G2": g2[
                            "G"
                        ],
                        "G2_p95": g2[
                            "null_p95"
                        ],
                        "G2_hit": g2[
                            "hit"
                        ],
                        "G3": g3[
                            "G"
                        ],
                        "G3_p95": g3[
                            "null_p95"
                        ],
                        "G3_hit": g3[
                            "hit"
                        ],
                        "G4": g4[
                            "G"
                        ],
                        "G4_p95": g4[
                            "null_p95"
                        ],
                        "G4_hit": g4[
                            "hit"
                        ],
                    }
                )


# ============================================================
# IMPRESION FINAL
# ============================================================

def print_summary(payload):
    region = payload[
        "region"
    ]

    print()
    print(
        "HISTORY-DEPTH-ATLAS-v1 — RESUMEN"
    )

    print("=" * 104)

    for point in payload[
        "points"
    ]:
        print(
            f"{point['key']:30s} "
            f"{point['k2_count']}/8 "
            f"k*=2  "
            f"{'CORE' if point['core'] else 'EXT '}  "
            + (
                "PASS"
                if point[
                    "depth_point_pass"
                ]
                else "FAIL"
            )
        )

    print()
    print(
        "CORE: "
        f"{region['core_depth_point_passes']}"
        f"/{region['core_points']} "
        "DEPTH POINT PASS"
    )

    print(
        "FULL GRID: "
        f"{region['full_grid_depth_point_passes']}"
        f"/{region['full_grid_points']} "
        "DEPTH POINT PASS"
    )

    print(
        "CLASSIFICATIONS: "
        f"{region['classification_counts']}"
    )

    print()

    if region[
        "history_depth_atlas_v1_pass"
    ]:
        print(
            "RESULTADO FINAL: "
            "HISTORY-DEPTH-ATLAS-v1 PASS"
        )
    else:
        print(
            "RESULTADO FINAL: "
            "HISTORY-DEPTH-ATLAS-v1 FAIL"
        )


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--check-structure",
        action="store_true",
        help=(
            "verifica instrumento, atlas y "
            "series sin evaluar G_k"
        ),
    )

    args = parser.parse_args()

    structure = check_structure()

    if args.check_structure:
        print(
            "HISTORY-DEPTH-ATLAS-v1 "
            "— STRUCTURE CHECK"
        )

        print("=" * 96)

        print(
            "atlas JSON points:          "
            f"{structure['atlas_json_points']}"
        )

        print(
            "core points:                "
            f"{structure['core_points']}"
        )

        print(
            "materialized atlas points:  "
            f"{structure['materialized_atlas_points']}"
        )

        print(
            "materialized groups:        "
            f"{structure['materialized_groups']}"
        )

        print(
            "materialized rows:          "
            f"{structure['materialized_rows']}"
        )

        print(
            "states per group:           "
            f"{structure['states_per_group']}"
        )

        print(
            "baseline materialized:      "
            f"{structure['baseline_materialized']}"
        )

        print(
            "baseline source:            "
            f"{structure['baseline_source']}"
        )

        print(
            "null RNG identity:          "
            f"{structure['null_rng_identity']}"
        )

        print(
            "alpha:                      "
            f"{structure['alpha']}"
        )

        print(
            "null permutations:          "
            f"{structure['null_permutations']}"
        )

        print(
            "orders:                     "
            f"{structure['orders']}"
        )

        print(
            "simulation calls:           "
            f"{structure['simulation_calls']}"
        )

        print()
        print(
            "STRUCTURE CHECK: PASS"
        )

        return

    payload = run_experiment()

    print_summary(
        payload
    )

    write_outputs(
        payload
    )

    print()
    print("TRAZAS")
    print("=" * 104)
    print(OUTPUT_JSON)
    print(OUTPUT_CSV)

    if not payload[
        "region"
    ][
        "history_depth_atlas_v1_pass"
    ]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()