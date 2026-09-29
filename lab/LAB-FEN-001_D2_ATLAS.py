from __future__ import annotations

import argparse
import csv
import gzip
import importlib.util
import io
import json
import random
import sys

from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path


VERSION = "LAB-D2-ATLAS-v1"

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"

SELF_PATH = Path(__file__).resolve()

D2_PATH = ROOT / "LAB-FEN-001_D2.py"
D2_RESULT_PATH = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_v1_results.json"
)

ATLAS_SPEC_PATH = (
    ROOT
    / "LAB-FEN-001_D2_ATLAS_SPEC_v1.md"
)

THRESHOLDS_PATH = (
    ROOT
    / "LAB-FEN-001_THRESHOLDS_v1.md"
)

METRICS_SPEC_PATH = (
    ROOT
    / "LAB-FEN-001_METRICS_v1.md"
)

METRICS_EXEC_PATH = (
    ROOT
    / "LAB-FEN-001_METRICS_v1.py"
)

OUTPUT_JSON = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_ATLAS_v1_results.json"
)

OUTPUT_SERIES = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_ATLAS_v1_series.csv.gz"
)


# ============================================================
# CARGA DE INSTRUMENTOS CONGELADOS
# ============================================================

def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(
        name,
        path,
    )

    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"No se pudo cargar {path}"
        )

    module = importlib.util.module_from_spec(
        spec
    )

    sys.modules[name] = module
    spec.loader.exec_module(module)

    return module


D2 = load_module(
    "lab_d2_v1_frozen_for_atlas",
    D2_PATH,
)

D0 = D2.D0
METRICS = D2.METRICS

Example = D0.Example


ALPHABET = tuple(D2.ALPHABET)
N_STATES = D2.N_STATES
SEEDS = tuple(D2.SEEDS)

BURN_IN = D2.BURN_IN
USEFUL_TRANSITIONS = D2.USEFUL_TRANSITIONS
TRAIN_TRANSITIONS = D2.TRAIN_TRANSITIONS
TEST_TRANSITIONS = D2.TEST_TRANSITIONS

T_P = D2.T_P
T_N = D2.T_N
T_U = D2.T_U


assert ALPHABET == (
    0,
    1,
    2,
    3,
    4,
)

assert SEEDS == (
    11,
    23,
    37,
    51,
    79,
    101,
    131,
    173,
)

assert BURN_IN == 1_000
assert USEFUL_TRANSITIONS == 30_000
assert TRAIN_TRANSITIONS == 18_000
assert TEST_TRANSITIONS == 12_000


# ============================================================
# MALLA CONGELADA
# ============================================================

BETAS = (
    Fraction(-1, 10),
    Fraction(-1, 20),
    Fraction(0, 1),
    Fraction(1, 20),
    Fraction(1, 10),
)

EPSILONS = (
    Fraction(0, 1),
    Fraction(1, 20),
    Fraction(1, 10),
    Fraction(3, 20),
)

CORE_BETAS = (
    Fraction(-1, 20),
    Fraction(0, 1),
    Fraction(1, 20),
)

CORE_EPSILONS = (
    Fraction(0, 1),
    Fraction(1, 20),
    Fraction(1, 10),
)

BASELINE = (
    Fraction(0, 1),
    Fraction(0, 1),
)


assert len(BETAS) == 5
assert len(EPSILONS) == 4

assert len(
    tuple(
        product(
            BETAS,
            EPSILONS,
        )
    )
) == 20

assert len(
    tuple(
        product(
            CORE_BETAS,
            CORE_EPSILONS,
        )
    )
) == 9


# ============================================================
# REPRESENTACION
# ============================================================

def signed_decimal(
    value: Fraction,
) -> str:
    return f"{float(value):+.2f}"


def unsigned_decimal(
    value: Fraction,
) -> str:
    return f"{float(value):.2f}"


def point_key(
    beta: Fraction,
    epsilon: Fraction,
) -> str:
    return (
        "beta="
        + signed_decimal(beta)
        + "|epsilon="
        + unsigned_decimal(epsilon)
    )


def point_numeric(
    beta: Fraction,
    epsilon: Fraction,
):
    return {
        "beta": float(beta),
        "epsilon": float(epsilon),
    }


# ============================================================
# DISTRIBUCION PARAMETRICA
# ============================================================

def transition_distribution(
    prev: int,
    current: int,
    beta: Fraction,
    epsilon: Fraction,
):
    one = Fraction(1, 1)

    weights = (
        Fraction(1, 3) + beta,
        Fraction(1, 3),
        Fraction(1, 3) - beta,
    )

    probs = [
        epsilon / N_STATES
        for _ in ALPHABET
    ]

    base = D2.family_base(
        prev,
        current,
    )

    for offset, weight in enumerate(
        weights
    ):
        state = (
            base + offset
        ) % N_STATES

        probs[state] += (
            (one - epsilon)
            * weight
        )

    return tuple(probs)


def categorical_sample(
    probabilities,
    rng: random.Random,
) -> int:
    # random.random() queda preservado como fuente.
    # Fraction.from_float permite comparar el valor
    # generado con umbrales racionales exactos.
    u = Fraction.from_float(
        rng.random()
    )

    cumulative = Fraction(
        0,
        1,
    )

    for state, probability in enumerate(
        probabilities
    ):
        cumulative += probability

        if u < cumulative:
            return state

    raise AssertionError(
        "distribucion categorica "
        "no alcanzo probabilidad 1"
    )


# ============================================================
# VERIFICACION ESTRUCTURAL
# ============================================================

def verify_structure():
    contexts = tuple(
        product(
            ALPHABET,
            repeat=2,
        )
    )

    assert len(contexts) == 25

    points_checked = 0
    context_distributions_checked = 0

    minimum_probability = Fraction(
        1,
        1,
    )

    maximum_probability = Fraction(
        0,
        1,
    )

    for beta, epsilon in product(
        BETAS,
        EPSILONS,
    ):
        points_checked += 1

        for prev, current in contexts:
            probs = transition_distribution(
                prev,
                current,
                beta,
                epsilon,
            )

            context_distributions_checked += 1

            if len(probs) != 5:
                raise AssertionError(
                    "cada distribucion debe "
                    "tener cinco probabilidades"
                )

            if sum(
                probs,
                Fraction(0, 1),
            ) != Fraction(1, 1):
                raise AssertionError(
                    "la distribucion no suma 1"
                )

            if any(
                probability < 0
                for probability in probs
            ):
                raise AssertionError(
                    "probabilidad negativa"
                )

            if any(
                probability > 1
                for probability in probs
            ):
                raise AssertionError(
                    "probabilidad mayor que 1"
                )

            minimum_probability = min(
                minimum_probability,
                *probs,
            )

            maximum_probability = max(
                maximum_probability,
                *probs,
            )

    # La dependencia de h respecto del pasado
    # permanece inyectiva para cada presente.
    distinct_h_by_current = {}

    for current in ALPHABET:
        bases = {
            D2.family_base(
                prev,
                current,
            )
            for prev in ALPHABET
        }

        distinct_h_by_current[
            str(current)
        ] = len(bases)

    if any(
        count != 5
        for count
        in distinct_h_by_current.values()
    ):
        raise AssertionError(
            "h ha perdido dependencia "
            "estructural respecto al pasado"
        )

    # Coincidencia analitica exacta del basal.
    for prev, current in contexts:
        observed = transition_distribution(
            prev,
            current,
            Fraction(0, 1),
            Fraction(0, 1),
        )

        expected = [
            Fraction(0, 1)
            for _ in ALPHABET
        ]

        for state in D2.allowed_successors(
            prev,
            current,
        ):
            expected[state] = Fraction(
                1,
                3,
            )

        if observed != tuple(expected):
            raise AssertionError(
                "el punto basal no coincide "
                "con la distribucion D2"
            )

    return {
        "grid_points": 20,
        "new_points_to_execute": 19,
        "core_points": 9,
        "contexts_per_point": 25,
        "context_distributions_checked": (
            context_distributions_checked
        ),
        "minimum_probability": float(
            minimum_probability
        ),
        "maximum_probability": float(
            maximum_probability
        ),
        "distinct_h_by_current": (
            distinct_h_by_current
        ),
        "baseline_distribution_exact_match": (
            True
        ),
    }


# ============================================================
# GENERACION
# ============================================================

def generate_point(
    beta: Fraction,
    epsilon: Fraction,
    seed: int,
):
    rng = random.Random(
        seed
    )

    initial_prev = rng.choice(
        ALPHABET
    )

    initial_current = rng.choice(
        ALPHABET
    )

    prev = initial_prev
    current = initial_current

    raw_states = [
        prev,
        current,
    ]

    for _ in range(
        BURN_IN
        + USEFUL_TRANSITIONS
    ):
        probabilities = (
            transition_distribution(
                prev,
                current,
                beta,
                epsilon,
            )
        )

        nxt = categorical_sample(
            probabilities,
            rng,
        )

        raw_states.append(
            nxt
        )

        prev, current = (
            current,
            nxt,
        )

    assert len(raw_states) == (
        BURN_IN
        + USEFUL_TRANSITIONS
        + 2
    )

    segment = raw_states[
        BURN_IN:
    ]

    assert len(segment) == (
        USEFUL_TRANSITIONS
        + 2
    )

    examples = tuple(
        Example(
            prev=segment[t],
            current=segment[t + 1],
            nxt=segment[t + 2],
        )
        for t in range(
            USEFUL_TRANSITIONS
        )
    )

    useful_states = tuple(
        segment[1:]
    )

    assert len(examples) == (
        USEFUL_TRANSITIONS
    )

    assert len(useful_states) == (
        USEFUL_TRANSITIONS
        + 1
    )

    train = examples[
        :TRAIN_TRANSITIONS
    ]

    test = examples[
        TRAIN_TRANSITIONS:
    ]

    assert len(train) == (
        TRAIN_TRANSITIONS
    )

    assert len(test) == (
        TEST_TRANSITIONS
    )

    return {
        "initial_pair": (
            initial_prev,
            initial_current,
        ),
        "states": useful_states,
        "train": train,
        "test": test,
    }


# ============================================================
# GATE CONGELADO
# ============================================================

def full_seed_gate(
    hist,
    metric,
):
    p_rel = metric[
        "P_rel"
    ]

    return all(
        (
            metric["A1"] > 0.0,

            hist[
                "delta_hist"
            ] > 0.0,

            hist[
                "delta_hit"
            ],

            hist[
                "c_hist"
            ] > 0.0,

            hist[
                "c_hit"
            ],

            p_rel is not None,

            (
                p_rel > T_P
                if p_rel is not None
                else False
            ),

            metric["N"] > T_N,

            metric["U"] > T_U,
        )
    )


# ============================================================
# EVALUACION DE UNA SEMILLA
# ============================================================

def evaluate_seed(
    beta: Fraction,
    epsilon: Fraction,
    seed: int,
    generated,
):
    hist = D2.historical_metrics(
        seed,
        generated["train"],
        generated["test"],
    )

    frozen_like = {
        "delta_hist": (
            hist[
                "delta_hist"
            ]
        ),

        "c_hist": (
            hist[
                "c_hist"
            ]
        ),

        "delta_hit": (
            hist[
                "delta_hit"
            ]
        ),

        "c_hit": (
            hist[
                "c_hit"
            ]
        ),
    }

    label = (
        VERSION
        + "|"
        + point_key(
            beta,
            epsilon,
        )
    )

    metric = (
        METRICS.compute_seed_metrics(
            label,
            seed,
            generated["states"],
            frozen_like,
        )
    )

    seed_pass = full_seed_gate(
        hist,
        metric,
    )

    return {
        "seed": seed,

        "initial_pair": (
            generated[
                "initial_pair"
            ]
        ),

        "series_sha256": (
            D0.series_sha256(
                generated["states"]
            )
        ),

        "L1": hist["L1"],
        "L2": hist["L2"],

        "delta_hist": (
            hist[
                "delta_hist"
            ]
        ),

        "delta_p95": (
            hist[
                "delta_p95"
            ]
        ),

        "delta_hit": (
            hist[
                "delta_hit"
            ]
        ),

        "c_hist": (
            hist[
                "c_hist"
            ]
        ),

        "c_p95": (
            hist[
                "c_p95"
            ]
        ),

        "c_hit": (
            hist[
                "c_hit"
            ]
        ),

        "A1": metric["A1"],

        "I2_observed": (
            metric[
                "I2_observed"
            ]
        ),

        "I2_null_p95": (
            metric[
                "I2_null_p95"
            ]
        ),

        "P_rel": (
            metric[
                "P_rel"
            ]
        ),

        "D_within": (
            metric[
                "D_within"
            ]
        ),

        "D_null": (
            metric[
                "D_null"
            ]
        ),

        "N": metric["N"],
        "H3": metric["H3"],
        "D3": metric["D3"],
        "C3": metric["C3"],

        "trigram_coverage": (
            metric[
                "trigram_coverage"
            ]
        ),

        "U": metric["U"],

        "Q_period": (
            metric[
                "Q_period"
            ]
        ),

        "p_star": (
            metric[
                "p_star"
            ]
        ),

        "R_star": (
            metric[
                "R_star"
            ]
        ),

        "seed_pass": seed_pass,

        "null_delta_values": (
            hist[
                "null_delta_values"
            ]
        ),

        "null_c_values": (
            hist[
                "null_c_values"
            ]
        ),

        "I2_null_values": (
            metric[
                "I2_null_values"
            ]
        ),
    }


# ============================================================
# BASAL CONGELADO
# ============================================================

def load_frozen_baseline():
    with D2_RESULT_PATH.open(
        "r",
        encoding="utf-8",
    ) as fh:
        payload = json.load(
            fh
        )

    summary = payload[
        "summary"
    ]

    if (
        summary[
            "seed_passes"
        ] != 8
        or not summary[
            "candidate_pass"
        ]
    ):
        raise AssertionError(
            "el basal congelado "
            "no coincide con 8/8 PASS"
        )

    results = payload.get(
        "results",
        []
    )

    if len(results) != 8:
        raise AssertionError(
            "el basal debe contener "
            "ocho resultados de semilla"
        )

    if sum(
        1
        for result in results
        if result[
            "seed_pass"
        ]
    ) != 8:
        raise AssertionError(
            "las ocho semillas basales "
            "deben pasar"
        )

    return {
        "key": point_key(
            *BASELINE
        ),

        "beta": 0.0,
        "epsilon": 0.0,

        "source": (
            "frozen LAB-D2-v1 result"
        ),

        "seed_pass_count": 8,
        "point_pass": True,

        "baseline_result_file": str(
            D2_RESULT_PATH.relative_to(
                ROOT.parent
            )
        ),
    }


# ============================================================
# RESUMEN DE PUNTO
# ============================================================

def summarize_point(
    beta: Fraction,
    epsilon: Fraction,
    results,
):
    seed_pass_count = sum(
        1
        for result in results
        if result[
            "seed_pass"
        ]
    )

    p_values = [
        result[
            "P_rel"
        ]
        for result in results
        if result[
            "P_rel"
        ] is not None
    ]

    return {
        "key": point_key(
            beta,
            epsilon,
        ),

        **point_numeric(
            beta,
            epsilon,
        ),

        "source": "atlas execution",

        "seed_pass_count": (
            seed_pass_count
        ),

        "point_pass": (
            seed_pass_count >= 7
        ),

        "A1_min": min(
            result[
                "A1"
            ]
            for result in results
        ),

        "delta_hist_min": min(
            result[
                "delta_hist"
            ]
            for result in results
        ),

        "c_hist_min": min(
            result[
                "c_hist"
            ]
            for result in results
        ),

        "P_rel_min": (
            min(p_values)
            if p_values
            else None
        ),

        "N_min": min(
            result[
                "N"
            ]
            for result in results
        ),

        "U_min": min(
            result[
                "U"
            ]
            for result in results
        ),

        "results": results,
    }


# ============================================================
# COMPONENTE CONEXO BASAL
# ============================================================

def baseline_component(
    point_pass_map,
):
    beta_index = {
        beta: index
        for index, beta
        in enumerate(BETAS)
    }

    epsilon_index = {
        epsilon: index
        for index, epsilon
        in enumerate(EPSILONS)
    }

    if not point_pass_map.get(
        BASELINE,
        False,
    ):
        return tuple()

    queue = deque(
        [
            BASELINE
        ]
    )

    seen = {
        BASELINE
    }

    while queue:
        beta, epsilon = (
            queue.popleft()
        )

        i = beta_index[
            beta
        ]

        j = epsilon_index[
            epsilon
        ]

        candidates = []

        if i > 0:
            candidates.append(
                (
                    BETAS[i - 1],
                    epsilon,
                )
            )

        if i + 1 < len(BETAS):
            candidates.append(
                (
                    BETAS[i + 1],
                    epsilon,
                )
            )

        if j > 0:
            candidates.append(
                (
                    beta,
                    EPSILONS[j - 1],
                )
            )

        if j + 1 < len(EPSILONS):
            candidates.append(
                (
                    beta,
                    EPSILONS[j + 1],
                )
            )

        for candidate in candidates:
            if candidate in seen:
                continue

            if not point_pass_map.get(
                candidate,
                False,
            ):
                continue

            seen.add(
                candidate
            )

            queue.append(
                candidate
            )

    return tuple(
        sorted(
            (
                point_key(
                    beta,
                    epsilon,
                )
                for beta, epsilon
                in seen
            )
        )
    )


# ============================================================
# GATE REGIONAL
# ============================================================

def evaluate_region(
    point_pass_map,
):
    core_points = tuple(
        product(
            CORE_BETAS,
            CORE_EPSILONS,
        )
    )

    core_passes = sum(
        1
        for point
        in core_points
        if point_pass_map[
            point
        ]
    )

    all_passes = sum(
        1
        for point
        in product(
            BETAS,
            EPSILONS,
        )
        if point_pass_map[
            point
        ]
    )

    component = baseline_component(
        point_pass_map
    )

    return {
        "core_points": 9,

        "core_passes": (
            core_passes
        ),

        "local_parametric_region_pass": (
            core_passes == 9
        ),

        "full_grid_points": 20,

        "full_grid_passes": (
            all_passes
        ),

        "baseline_component_size": (
            len(component)
        ),

        "baseline_component": (
            component
        ),
    }


# ============================================================
# SALIDAS
# ============================================================

def write_outputs(
    point_records,
    all_states,
    structure,
    region,
):
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    payload = {
        "version": VERSION,

        "contract": {
            "betas": [
                float(value)
                for value in BETAS
            ],

            "epsilons": [
                float(value)
                for value in EPSILONS
            ],

            "core_betas": [
                float(value)
                for value
                in CORE_BETAS
            ],

            "core_epsilons": [
                float(value)
                for value
                in CORE_EPSILONS
            ],

            "seeds": SEEDS,

            "burn_in": BURN_IN,

            "useful_transitions": (
                USEFUL_TRANSITIONS
            ),

            "train_transitions": (
                TRAIN_TRANSITIONS
            ),

            "test_transitions": (
                TEST_TRANSITIONS
            ),

            "T_P": T_P,
            "T_N": T_N,
            "T_U": T_U,

            "required_seed_passes": 7,
            "required_core_point_passes": 9,
        },

        "trace": {
            "atlas_spec_sha256": (
                METRICS.file_sha256(
                    ATLAS_SPEC_PATH
                )
            ),

            "atlas_executable_sha256": (
                METRICS.file_sha256(
                    SELF_PATH
                )
            ),

            "d2_executable_sha256": (
                METRICS.file_sha256(
                    D2_PATH
                )
            ),

            "d2_result_sha256": (
                METRICS.file_sha256(
                    D2_RESULT_PATH
                )
            ),

            "thresholds_sha256": (
                METRICS.file_sha256(
                    THRESHOLDS_PATH
                )
            ),

            "metrics_spec_sha256": (
                METRICS.file_sha256(
                    METRICS_SPEC_PATH
                )
            ),

            "metrics_executable_sha256": (
                METRICS.file_sha256(
                    METRICS_EXEC_PATH
                )
            ),
        },

        "structure": structure,

        "points": point_records,

        "region": region,
    }

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

    with OUTPUT_SERIES.open(
        "wb"
    ) as raw:
        with gzip.GzipFile(
            fileobj=raw,
            mode="wb",
            mtime=0,
        ) as gz:
            with io.TextIOWrapper(
                gz,
                encoding="utf-8",
                newline="",
            ) as fh:
                writer = csv.writer(
                    fh
                )

                writer.writerow(
                    (
                        "version",
                        "beta",
                        "epsilon",
                        "seed",
                        "t",
                        "state",
                    )
                )

                for beta, epsilon in product(
                    BETAS,
                    EPSILONS,
                ):
                    if (
                        beta,
                        epsilon,
                    ) == BASELINE:
                        continue

                    for seed in SEEDS:
                        states = (
                            all_states[
                                (
                                    beta,
                                    epsilon,
                                )
                            ][seed]
                        )

                        for t, state in enumerate(
                            states
                        ):
                            writer.writerow(
                                (
                                    VERSION,
                                    float(beta),
                                    float(epsilon),
                                    seed,
                                    t,
                                    state,
                                )
                            )


# ============================================================
# PRESENTACION
# ============================================================

def print_structure(
    report,
):
    print(
        "LAB-D2-ATLAS-v1 "
        "— CONTROL ESTRUCTURAL"
    )

    print("=" * 116)

    print(
        "puntos de malla:             "
        f"{report['grid_points']}"
    )

    print(
        "puntos nuevos a ejecutar:    "
        f"{report['new_points_to_execute']}"
    )

    print(
        "puntos del nucleo:           "
        f"{report['core_points']}"
    )

    print(
        "contextos por punto:         "
        f"{report['contexts_per_point']}"
    )

    print(
        "distribuciones verificadas:  "
        f"{report['context_distributions_checked']}"
    )

    print(
        "probabilidad minima:         "
        f"{report['minimum_probability']:.6f}"
    )

    print(
        "probabilidad maxima:         "
        f"{report['maximum_probability']:.6f}"
    )

    print(
        "h distintos por presente:   "
        + str(
            report[
                "distinct_h_by_current"
            ]
        )
    )

    print(
        "basal exacto:                "
        f"{report['baseline_distribution_exact_match']}"
    )

    print()
    print(
        "STRUCTURE CHECK: PASS"
    )


def print_seed_result(
    result,
):
    p_rel = result[
        "P_rel"
    ]

    p_text = (
        f"{p_rel:.6f}"
        if p_rel is not None
        else "NA"
    )

    print(
        f"seed={result['seed']:3d}  "
        f"A1={result['A1']:+.6f}  "
        f"D={result['delta_hist']:+.6f}  "
        f"Dh={'Y' if result['delta_hit'] else 'N'}  "
        f"C={result['c_hist']:.6f}  "
        f"Ch={'Y' if result['c_hit'] else 'N'}  "
        f"P={p_text:>8s}  "
        f"N={result['N']:.6f}  "
        f"U={result['U']:.6f}  "
        f"PASS={'YES' if result['seed_pass'] else 'NO'}"
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
            "verifica solo la arquitectura "
            "sin generar trayectorias"
        ),
    )

    args = parser.parse_args()

    structure = verify_structure()

    print_structure(
        structure
    )

    if args.check_structure:
        return

    baseline = load_frozen_baseline()

    print()
    print(
        "PRIMERA EJECUCION "
        "LAB-D2-ATLAS-v1"
    )

    print("=" * 116)

    print(
        "basal (0,0): IMPORTADO "
        "DEL RESULTADO CONGELADO — 8/8 PASS"
    )

    point_records = []
    all_states = {}

    point_pass_map = {}

    for beta, epsilon in product(
        BETAS,
        EPSILONS,
    ):
        if (
            beta,
            epsilon,
        ) == BASELINE:
            point_records.append(
                baseline
            )

            point_pass_map[
                BASELINE
            ] = True

            continue

        key = point_key(
            beta,
            epsilon,
        )

        print()
        print(key)
        print("-" * 116)

        point_results = []

        all_states[
            (
                beta,
                epsilon,
            )
        ] = {}

        for seed in SEEDS:
            generated = generate_point(
                beta,
                epsilon,
                seed,
            )

            result = evaluate_seed(
                beta,
                epsilon,
                seed,
                generated,
            )

            all_states[
                (
                    beta,
                    epsilon,
                )
            ][seed] = (
                generated[
                    "states"
                ]
            )

            point_results.append(
                result
            )

            print_seed_result(
                result
            )

        point_record = summarize_point(
            beta,
            epsilon,
            point_results,
        )

        point_records.append(
            point_record
        )

        point_pass_map[
            (
                beta,
                epsilon,
            )
        ] = point_record[
            "point_pass"
        ]

        print(
            "POINT RESULT: "
            f"{point_record['seed_pass_count']}/8 "
            + (
                "PASS"
                if point_record[
                    "point_pass"
                ]
                else "FAIL"
            )
        )

    if len(point_pass_map) != 20:
        raise AssertionError(
            "el atlas debe clasificar "
            "exactamente 20 puntos"
        )

    region = evaluate_region(
        point_pass_map
    )

    print()
    print(
        "RESUMEN DEL ATLAS"
    )

    print("=" * 116)

    print(
        "nucleo predeclarado: "
        f"{region['core_passes']}/9"
    )

    print(
        "malla completa:      "
        f"{region['full_grid_passes']}/20"
    )

    print(
        "componente basal:    "
        f"{region['baseline_component_size']}/20"
    )

    print()

    print(
        "RESULTADO FINAL: "
        + (
            "LOCAL PARAMETRIC REGION v1 PASS"
            if region[
                "local_parametric_region_pass"
            ]
            else "LOCAL PARAMETRIC REGION v1 FAIL"
        )
    )

    write_outputs(
        point_records,
        all_states,
        structure,
        region,
    )

    print()
    print("TRAZAS")

    print("=" * 116)

    print(OUTPUT_JSON)
    print(OUTPUT_SERIES)

    if not region[
        "local_parametric_region_pass"
    ]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()