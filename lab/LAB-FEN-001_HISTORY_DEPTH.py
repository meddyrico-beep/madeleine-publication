from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import math
import platform
import random
import subprocess

from collections import Counter, defaultdict
from pathlib import Path


VERSION = "HISTORY-DEPTH-v1"

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
RESULTS = ROOT / "results"

SPEC_PATH = (
    ROOT
    / "LAB-FEN-001_HISTORY_DEPTH_SPEC_v1.md"
)

SELF_PATH = Path(__file__).resolve()

D0_RESULT = (
    RESULTS
    / "LAB-FEN-001_D0_v1_results.json"
)

D1_RESULT = (
    RESULTS
    / "LAB-FEN-001_D1_v1_results.json"
)

D2_RESULT = (
    RESULTS
    / "LAB-FEN-001_D2_v1_results.json"
)

ABL_RESULT = (
    RESULTS
    / "LAB-FEN-001_D2_ABLATIONS_v1_results.json"
)

D0_SERIES = (
    RESULTS
    / "LAB-FEN-001_D0_v1_series.csv.gz"
)

D1_SERIES = (
    RESULTS
    / "LAB-FEN-001_D1_v1_series.csv.gz"
)

D2_SERIES = (
    RESULTS
    / "LAB-FEN-001_D2_v1_series.csv.gz"
)

ABL_SERIES = (
    RESULTS
    / "LAB-FEN-001_D2_ABLATIONS_v1_series.csv.gz"
)

OUTPUT_JSON = (
    RESULTS
    / "LAB-FEN-001_HISTORY_DEPTH_v1_results.json"
)

OUTPUT_CSV = (
    RESULTS
    / "LAB-FEN-001_HISTORY_DEPTH_v1_summary.csv"
)


ALPHABET = (0, 1, 2, 3, 4)

SEEDS = (
    11,
    23,
    37,
    51,
    79,
    101,
    131,
    173,
)

ALPHA = 0.5
NULL_PERMUTATIONS = 64
NULL_Q = 0.95

USEFUL_TRANSITIONS = 30_000
TRAIN_BOUNDARY = 18_000
TEST_TRANSITIONS = 12_000
EXPECTED_STATES = 30_001

ORDERS = (2, 3, 4)

SYSTEMS = {
    "HD-D0": {
        "series": D0_SERIES,
        "ablation": None,
        "expected": "k*=1",
    },

    "HD-D1": {
        "series": D1_SERIES,
        "ablation": None,
        "expected": "k*=2",
    },

    "HD-D2": {
        "series": D2_SERIES,
        "ablation": None,
        "expected": "k*=2",
    },

    "HD-DELAYED": {
        "series": ABL_SERIES,
        "ablation": "ABL-DELAYED-PAST-v1",
        "expected": "k*=3",
    },
}


# ============================================================
# UTILIDADES
# ============================================================

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as fh:
        while True:
            block = fh.read(1024 * 1024)

            if not block:
                break

            h.update(block)

    return h.hexdigest()


def read_json(path: Path):
    return json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )


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


def quantile_nearest_rank(values, q: float) -> float:
    xs = sorted(
        float(value)
        for value in values
    )

    if not xs:
        raise ValueError(
            "quantile sobre lista vacia"
        )

    if not (
        0.0 < q <= 1.0
    ):
        raise ValueError(
            "q fuera de (0,1]"
        )

    rank = math.ceil(
        q * len(xs)
    )

    return xs[
        rank - 1
    ]


def deterministic_seed(
    system: str,
    seed: int,
    order: int,
    permutation: int,
    split: str,
) -> int:
    token = (
        f"{VERSION}|"
        f"{system}|"
        f"{seed}|"
        f"k={order}|"
        f"perm={permutation}|"
        f"{split}"
    )

    digest = hashlib.sha256(
        token.encode("utf-8")
    ).digest()

    return int.from_bytes(
        digest[:8],
        "big",
        signed=False,
    )


# ============================================================
# LECTURA DE SERIES CONGELADAS
# ============================================================

def read_series_file(
    path: Path,
    ablation: str | None = None,
):
    by_seed = {
        seed: []
        for seed in SEEDS
    }

    times = {
        seed: []
        for seed in SEEDS
    }

    with gzip.open(
        path,
        "rt",
        encoding="utf-8",
        newline="",
    ) as fh:
        reader = csv.DictReader(fh)

        required = {
            "version",
            "seed",
            "t",
            "state",
        }

        if not required.issubset(
            set(reader.fieldnames or [])
        ):
            raise AssertionError(
                f"header invalido en {path.name}: "
                f"{reader.fieldnames}"
            )

        if (
            ablation is not None
            and
            "ablation"
            not in (
                reader.fieldnames
                or []
            )
        ):
            raise AssertionError(
                "falta columna ablation"
            )

        for row in reader:
            if (
                ablation is not None
                and
                row["ablation"] != ablation
            ):
                continue

            seed = int(
                row["seed"]
            )

            if seed not in by_seed:
                continue

            t = int(
                row["t"]
            )

            state = int(
                row["state"]
            )

            if state not in ALPHABET:
                raise AssertionError(
                    f"estado fuera del alfabeto: "
                    f"{state}"
                )

            times[seed].append(t)
            by_seed[seed].append(state)

    for seed in SEEDS:
        states = by_seed[seed]
        ts = times[seed]

        if len(states) != EXPECTED_STATES:
            raise AssertionError(
                f"{path.name} seed={seed}: "
                f"{len(states)} estados, "
                f"esperados {EXPECTED_STATES}"
            )

        if ts != list(
            range(EXPECTED_STATES)
        ):
            raise AssertionError(
                f"{path.name} seed={seed}: "
                "indice temporal no contiguo"
            )

    return by_seed


# ============================================================
# EJEMPLOS PARA G_k
# ============================================================

def gain_examples(
    states,
    order: int,
    split: str,
):
    if order not in ORDERS:
        raise ValueError(
            f"orden no soportado: {order}"
        )

    if split == "train":
        start = order - 1
        stop = TRAIN_BOUNDARY

    elif split == "test":
        start = TRAIN_BOUNDARY
        stop = USEFUL_TRANSITIONS

    else:
        raise ValueError(
            f"split invalido: {split}"
        )

    examples = []

    for target_transition in range(
        start,
        stop,
    ):
        # target_transition=i representa:
        #
        # x[i] -> x[i+1]
        #
        # El contexto largo tiene 'order'
        # estados y termina en x[i].

        context_start = (
            target_transition
            - order
            + 1
        )

        full_context = tuple(
            states[
                context_start:
                target_transition + 1
            ]
        )

        if len(full_context) != order:
            raise AssertionError(
                "contexto incompleto"
            )

        oldest = full_context[0]

        short_context = (
            full_context[1:]
        )

        nxt = states[
            target_transition + 1
        ]

        examples.append(
            {
                "oldest": oldest,
                "short": short_context,
                "full": full_context,
                "next": nxt,
            }
        )

    return examples


# ============================================================
# MODELO CATEGORICO
# ============================================================

def fit_counts(
    examples,
    field: str,
):
    counts = defaultdict(
        lambda: [
            0
            for _ in ALPHABET
        ]
    )

    for example in examples:
        context = tuple(
            example[field]
        )

        nxt = example["next"]

        counts[
            context
        ][nxt] += 1

    return dict(counts)


def mean_log_loss(
    counts,
    examples,
    field: str,
):
    losses = []

    for example in examples:
        context = tuple(
            example[field]
        )

        nxt = example["next"]

        row = counts.get(
            context
        )

        if row is None:
            numerator = ALPHA
            denominator = (
                ALPHA
                * len(ALPHABET)
            )

        else:
            total = sum(row)

            numerator = (
                row[nxt]
                + ALPHA
            )

            denominator = (
                total
                + ALPHA
                * len(ALPHABET)
            )

        probability = (
            numerator
            / denominator
        )

        losses.append(
            -math.log(
                probability
            )
        )

    if not losses:
        raise AssertionError(
            "test vacio"
        )

    return sum(losses) / len(losses)


# ============================================================
# NULO CONDICIONAL
# ============================================================

def permute_oldest_within_short(
    examples,
    rng: random.Random,
):
    grouped_indices = defaultdict(
        list
    )

    for index, example in enumerate(
        examples
    ):
        grouped_indices[
            tuple(
                example["short"]
            )
        ].append(index)

    permuted = [
        {
            "oldest": example["oldest"],
            "short": tuple(
                example["short"]
            ),
            "full": tuple(
                example["full"]
            ),
            "next": example["next"],
        }
        for example in examples
    ]

    for short_context in sorted(
        grouped_indices
    ):
        indices = grouped_indices[
            short_context
        ]

        oldest_values = [
            examples[index][
                "oldest"
            ]
            for index in indices
        ]

        rng.shuffle(
            oldest_values
        )

        for index, new_oldest in zip(
            indices,
            oldest_values,
        ):
            short = tuple(
                examples[index][
                    "short"
                ]
            )

            permuted[index][
                "oldest"
            ] = new_oldest

            permuted[index][
                "full"
            ] = (
                new_oldest,
                *short,
            )

    return permuted


# ============================================================
# G_k
# ============================================================

def evaluate_gain(
    system: str,
    seed: int,
    states,
    order: int,
):
    train = gain_examples(
        states,
        order,
        "train",
    )

    test = gain_examples(
        states,
        order,
        "test",
    )

    short_counts = fit_counts(
        train,
        "short",
    )

    long_counts = fit_counts(
        train,
        "full",
    )

    L_short = mean_log_loss(
        short_counts,
        test,
        "short",
    )

    L_long = mean_log_loss(
        long_counts,
        test,
        "full",
    )

    observed_gain = (
        L_short
        - L_long
    )

    null_gains = []

    for permutation in range(
        NULL_PERMUTATIONS
    ):
        train_rng = random.Random(
            deterministic_seed(
                system,
                seed,
                order,
                permutation,
                "train",
            )
        )

        test_rng = random.Random(
            deterministic_seed(
                system,
                seed,
                order,
                permutation,
                "test",
            )
        )

        null_train = (
            permute_oldest_within_short(
                train,
                train_rng,
            )
        )

        null_test = (
            permute_oldest_within_short(
                test,
                test_rng,
            )
        )

        null_long_counts = fit_counts(
            null_train,
            "full",
        )

        null_L_long = mean_log_loss(
            null_long_counts,
            null_test,
            "full",
        )

        null_gain = (
            L_short
            - null_L_long
        )

        null_gains.append(
            null_gain
        )

    null_p95 = quantile_nearest_rank(
        null_gains,
        NULL_Q,
    )

    hit = (
        observed_gain > 0.0
        and
        observed_gain > null_p95
    )

    return {
        "order": order,

        "train_examples": len(
            train
        ),

        "test_examples": len(
            test
        ),

        "L_short": L_short,

        "L_long": L_long,

        "G": observed_gain,

        "null_p95": null_p95,

        "hit": hit,

        "null_gains": null_gains,
    }


# ============================================================
# CLASIFICACION DE PROFUNDIDAD
# ============================================================

def classify_depth(gains):
    hits = {
        order: bool(
            gains[
                str(order)
            ][
                "hit"
            ]
        )
        for order in ORDERS
    }

    # Un hit en k=4 sin hit en k=3 queda
    # marcado como patron separado/no monotono.
    #
    # Esto preserva la clausula DEPTH COMPLEX
    # del protocolo sin impedir que DELAYED
    # pueda tener G3 aunque G2 sea debil.

    if (
        hits[4]
        and
        not hits[3]
    ):
        return "DEPTH COMPLEX"

    if hits[4]:
        return "k*=4"

    if hits[3]:
        return "k*=3"

    if hits[2]:
        return "k*=2"

    return "k*=1"


# ============================================================
# EVALUACION POR SISTEMA
# ============================================================

def evaluate_system(
    system_name,
    contract,
    all_series,
):
    expected = contract[
        "expected"
    ]

    seed_results = []

    for seed in SEEDS:
        states = all_series[
            seed
        ]

        gains = {}

        for order in ORDERS:
            result = evaluate_gain(
                system_name,
                seed,
                states,
                order,
            )

            gains[
                str(order)
            ] = result

        classification = (
            classify_depth(
                gains
            )
        )

        seed_results.append(
            {
                "seed": seed,
                "classification": (
                    classification
                ),
                "expected": expected,
                "expected_match": (
                    classification
                    == expected
                ),
                "gains": gains,
            }
        )

    expected_count = sum(
        1
        for result in seed_results
        if result[
            "expected_match"
        ]
    )

    classifications = Counter(
        result[
            "classification"
        ]
        for result in seed_results
    )

    system_pass = (
        expected_count >= 7
    )

    return {
        "system": system_name,
        "expected": expected,
        "expected_count": (
            expected_count
        ),
        "required": 7,
        "system_pass": (
            system_pass
        ),
        "classification_counts": dict(
            sorted(
                classifications.items()
            )
        ),
        "seeds": seed_results,
    }


# ============================================================
# CONTROL ESTRUCTURAL
# ============================================================

def check_structure():
    required_paths = (
        SPEC_PATH,
        D0_RESULT,
        D1_RESULT,
        D2_RESULT,
        ABL_RESULT,
        D0_SERIES,
        D1_SERIES,
        D2_SERIES,
        ABL_SERIES,
        SELF_PATH,
    )

    missing = [
        str(path)
        for path in required_paths
        if not path.exists()
    ]

    if missing:
        raise AssertionError(
            "faltan archivos: "
            + ", ".join(missing)
        )

    d0 = read_json(
        D0_RESULT
    )

    d1 = read_json(
        D1_RESULT
    )

    if float(
        d0.get(
            "alpha",
            -1.0,
        )
    ) != ALPHA:
        raise AssertionError(
            "alpha D0 distinto de 0.5"
        )

    if float(
        d1.get(
            "alpha",
            -1.0,
        )
    ) != ALPHA:
        raise AssertionError(
            "alpha D1 distinto de 0.5"
        )

    percentile_method = (
        d0.get(
            "percentile_method"
        )
    )

    if percentile_method != "nearest-rank":
        raise AssertionError(
            "percentile_method esperado "
            f"'nearest-rank', observado "
            f"{percentile_method!r}"
        )

    headers = {}

    for name, contract in (
        SYSTEMS.items()
    ):
        path = contract[
            "series"
        ]

        with gzip.open(
            path,
            "rt",
            encoding="utf-8",
            newline="",
        ) as fh:
            reader = csv.DictReader(
                fh
            )

            headers[name] = (
                reader.fieldnames
            )

            required = {
                "version",
                "seed",
                "t",
                "state",
            }

            if not required.issubset(
                set(
                    reader.fieldnames
                    or []
                )
            ):
                raise AssertionError(
                    f"{name}: header invalido"
                )

            if (
                contract[
                    "ablation"
                ]
                is not None
                and
                "ablation"
                not in (
                    reader.fieldnames
                    or []
                )
            ):
                raise AssertionError(
                    f"{name}: falta ablation"
                )

    effective_train = {
        "G2": (
            TRAIN_BOUNDARY
            - 1
        ),
        "G3": (
            TRAIN_BOUNDARY
            - 2
        ),
        "G4": (
            TRAIN_BOUNDARY
            - 3
        ),
    }

    effective_test = {
        "G2": TEST_TRANSITIONS,
        "G3": TEST_TRANSITIONS,
        "G4": TEST_TRANSITIONS,
    }

    return {
        "alpha": ALPHA,

        "percentile_method": (
            percentile_method
        ),

        "null_permutations": (
            NULL_PERMUTATIONS
        ),

        "null_q": NULL_Q,

        "systems": list(
            SYSTEMS
        ),

        "headers": headers,

        "train_boundary": (
            TRAIN_BOUNDARY
        ),

        "effective_train_examples": (
            effective_train
        ),

        "effective_test_examples": (
            effective_test
        ),

        "simulation_calls": 0,
    }


# ============================================================
# EJECUCION COMPLETA
# ============================================================

def run_experiment():
    structure = check_structure()

    loaded_series = {}

    for system_name, contract in (
        SYSTEMS.items()
    ):
        loaded_series[
            system_name
        ] = read_series_file(
            contract["series"],
            contract["ablation"],
        )

    systems = {}

    for system_name, contract in (
        SYSTEMS.items()
    ):
        print()
        print(system_name)
        print("-" * 104)

        result = evaluate_system(
            system_name,
            contract,
            loaded_series[
                system_name
            ],
        )

        systems[
            system_name
        ] = result

        for seed_result in (
            result["seeds"]
        ):
            g2 = seed_result[
                "gains"
            ]["2"]

            g3 = seed_result[
                "gains"
            ]["3"]

            g4 = seed_result[
                "gains"
            ]["4"]

            print(
                f"seed={seed_result['seed']:3d}  "
                f"G2={g2['G']:+.6f} "
                f"Q95={g2['null_p95']:+.6f} "
                f"H2={'Y' if g2['hit'] else 'N'}  "
                f"G3={g3['G']:+.6f} "
                f"Q95={g3['null_p95']:+.6f} "
                f"H3={'Y' if g3['hit'] else 'N'}  "
                f"G4={g4['G']:+.6f} "
                f"Q95={g4['null_p95']:+.6f} "
                f"H4={'Y' if g4['hit'] else 'N'}  "
                f"{seed_result['classification']}"
            )

        print(
            "SYSTEM RESULT: "
            f"{result['expected_count']}/8 "
            f"expected={result['expected']}  "
            + (
                "PASS"
                if result[
                    "system_pass"
                ]
                else "FAIL"
            )
        )

    global_pass = all(
        result[
            "system_pass"
        ]
        for result in systems.values()
    )

    payload = {
        "version": VERSION,

        "contract": {
            "alphabet": ALPHABET,
            "seeds": SEEDS,
            "alpha": ALPHA,
            "null_permutations": (
                NULL_PERMUTATIONS
            ),
            "null_q": NULL_Q,
            "percentile_method": (
                "nearest-rank"
            ),
            "useful_transitions": (
                USEFUL_TRANSITIONS
            ),
            "train_boundary": (
                TRAIN_BOUNDARY
            ),
            "test_transitions": (
                TEST_TRANSITIONS
            ),
            "orders": ORDERS,
            "required_per_system": 7,
        },

        "edge_accounting": {
            "G2_train_examples": 17_999,
            "G3_train_examples": 17_998,
            "G4_train_examples": 17_997,
            "test_examples_each": 12_000,
            "reason": (
                "frozen useful series begin at t=0; "
                "k-1 left-edge targets lack complete "
                "history. Short and long models for "
                "each G_k use identical target sets."
            ),
        },

        "trace": {
            "git_head": git_head(),
            "python": platform.python_version(),
            "spec_sha256": sha256_file(
                SPEC_PATH
            ),
            "executable_sha256": sha256_file(
                SELF_PATH
            ),
            "D0_result_sha256": sha256_file(
                D0_RESULT
            ),
            "D1_result_sha256": sha256_file(
                D1_RESULT
            ),
            "D2_result_sha256": sha256_file(
                D2_RESULT
            ),
            "ablation_result_sha256": (
                sha256_file(
                    ABL_RESULT
                )
            ),
            "D0_series_sha256": sha256_file(
                D0_SERIES
            ),
            "D1_series_sha256": sha256_file(
                D1_SERIES
            ),
            "D2_series_sha256": sha256_file(
                D2_SERIES
            ),
            "ablation_series_sha256": (
                sha256_file(
                    ABL_SERIES
                )
            ),
        },

        "structure": structure,

        "systems": systems,

        "summary": {
            "system_passes": sum(
                1
                for result
                in systems.values()
                if result[
                    "system_pass"
                ]
            ),
            "system_total": 4,
            "history_depth_v1_pass": (
                global_pass
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
            "system",
            "seed",
            "expected",
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
        )

        writer.writeheader()

        for system_name in SYSTEMS:
            system = payload[
                "systems"
            ][system_name]

            for seed_result in (
                system["seeds"]
            ):
                g2 = seed_result[
                    "gains"
                ]["2"]

                g3 = seed_result[
                    "gains"
                ]["3"]

                g4 = seed_result[
                    "gains"
                ]["4"]

                writer.writerow(
                    {
                        "version": VERSION,
                        "system": system_name,
                        "seed": (
                            seed_result[
                                "seed"
                            ]
                        ),
                        "expected": (
                            seed_result[
                                "expected"
                            ]
                        ),
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
                        "G2": g2["G"],
                        "G2_p95": (
                            g2[
                                "null_p95"
                            ]
                        ),
                        "G2_hit": (
                            g2["hit"]
                        ),
                        "G3": g3["G"],
                        "G3_p95": (
                            g3[
                                "null_p95"
                            ]
                        ),
                        "G3_hit": (
                            g3["hit"]
                        ),
                        "G4": g4["G"],
                        "G4_p95": (
                            g4[
                                "null_p95"
                            ]
                        ),
                        "G4_hit": (
                            g4["hit"]
                        ),
                    }
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
            "verifica contratos y headers "
            "sin evaluar las series"
        ),
    )

    args = parser.parse_args()

    structure = check_structure()

    if args.check_structure:
        print(
            "HISTORY-DEPTH-v1 "
            "— STRUCTURE CHECK"
        )

        print("=" * 92)

        print(
            "alpha:                    "
            f"{structure['alpha']}"
        )

        print(
            "percentile method:        "
            f"{structure['percentile_method']}"
        )

        print(
            "null permutations:        "
            f"{structure['null_permutations']}"
        )

        print(
            "systems:                  "
            f"{len(structure['systems'])}"
        )

        print(
            "train boundary:           "
            f"{structure['train_boundary']}"
        )

        print(
            "G2 effective train:       "
            f"{structure['effective_train_examples']['G2']}"
        )

        print(
            "G3 effective train:       "
            f"{structure['effective_train_examples']['G3']}"
        )

        print(
            "G4 effective train:       "
            f"{structure['effective_train_examples']['G4']}"
        )

        print(
            "test examples each:       "
            f"{structure['effective_test_examples']['G2']}"
        )

        print(
            "simulation calls:         "
            f"{structure['simulation_calls']}"
        )

        print()
        print(
            "STRUCTURE CHECK: PASS"
        )

        return

    payload = run_experiment()

    print()
    print(
        "HISTORY-DEPTH-v1 — RESUMEN"
    )

    print("=" * 104)

    for system_name in SYSTEMS:
        result = payload[
            "systems"
        ][system_name]

        print(
            f"{system_name:12s} "
            f"{result['expected_count']}/8 "
            f"expected={result['expected']:4s} "
            + (
                "PASS"
                if result[
                    "system_pass"
                ]
                else "FAIL"
            )
        )

    print()

    if payload[
        "summary"
    ][
        "history_depth_v1_pass"
    ]:
        print(
            "RESULTADO FINAL: "
            "HISTORY-DEPTH-v1 PASS"
        )
    else:
        print(
            "RESULTADO FINAL: "
            "HISTORY-DEPTH-v1 FAIL"
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
        "summary"
    ][
        "history_depth_v1_pass"
    ]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()