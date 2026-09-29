from __future__ import annotations

import argparse
import csv
import gzip
import importlib.util
import io
import json
import random
import sys

from collections import Counter
from itertools import product
from pathlib import Path


VERSION = "LAB-D2-ABLATIONS-v1"

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"

D2_PATH = ROOT / "LAB-FEN-001_D2.py"

ABLATIONS_SPEC_PATH = (
    ROOT
    / "LAB-FEN-001_D2_ABLATIONS_SPEC_v1.md"
)

ABLATIONS_GATE_PATH = (
    ROOT
    / "LAB-FEN-001_D2_ABLATIONS_GATE_v1.md"
)

D2_RESULT_PATH = (
    ROOT
    / "results"
    / "LAB-FEN-001_D2_v1_results.json"
)

OUTPUT_JSON = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_ABLATIONS_v1_results.json"
)

OUTPUT_SERIES = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_ABLATIONS_v1_series.csv.gz"
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
    "lab_d2_v1_frozen_for_ablations",
    D2_PATH,
)

D0 = D2.D0
METRICS = D2.METRICS


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

AUX_PAST_OFFSET = 1_000_003

Example = D0.Example


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

assert T_P == 0.5075018151904057
assert T_N == 0.3862533855592818
assert T_U == 0.4908272358457767


ABL_NO_PAST = "ABL-NO-PAST-v1"
ABL_RANDOMIZED = "ABL-RANDOMIZED-PAST-v1"
ABL_DETERMINISTIC = "ABL-DETERMINISTIC-v1"
ABL_DELAYED = "ABL-DELAYED-PAST-v1"

ABLATIONS = (
    ABL_NO_PAST,
    ABL_RANDOMIZED,
    ABL_DETERMINISTIC,
    ABL_DELAYED,
)


# ============================================================
# UTILIDADES
# ============================================================

def choose_uniform(
    family,
    rng: random.Random,
):
    return family[
        rng.randrange(
            len(family)
        )
    ]


def no_past_family(
    current: int,
):
    return tuple(
        (
            current + offset
        )
        % N_STATES
        for offset in range(3)
    )


def finalize_two_state(
    raw_states,
    metadata,
):
    expected_raw = (
        BURN_IN
        + USEFUL_TRANSITIONS
        + 2
    )

    assert len(raw_states) == (
        expected_raw
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

    assert len(useful_states) == (
        USEFUL_TRANSITIONS
        + 1
    )

    assert len(examples) == (
        USEFUL_TRANSITIONS
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
        "states": useful_states,
        "train": train,
        "test": test,
        "metadata": metadata,
    }


def finalize_three_state(
    raw_states,
    metadata,
):
    expected_raw = (
        BURN_IN
        + USEFUL_TRANSITIONS
        + 3
    )

    assert len(raw_states) == (
        expected_raw
    )

    # raw:
    # x[-2], x[-1], x[0], x[1], ...
    #
    # Tras burn-in queremos, como en D2:
    # contexto previo + 30001 estados útiles.
    segment = raw_states[
        BURN_IN + 1:
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
        "states": useful_states,
        "train": train,
        "test": test,
        "metadata": metadata,
    }


# ============================================================
# ABLACION A — NO_PAST
# ============================================================

def generate_no_past(
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
        family = no_past_family(
            current
        )

        nxt = choose_uniform(
            family,
            rng,
        )

        raw_states.append(
            nxt
        )

        prev, current = (
            current,
            nxt,
        )

    return finalize_two_state(
        raw_states,
        {
            "initial_pair": (
                initial_prev,
                initial_current,
            ),
        },
    )


# ============================================================
# ABLACION B — RANDOMIZED_PAST
# ============================================================

def generate_randomized_past(
    seed: int,
):
    rng = random.Random(
        seed
    )

    past_rng = random.Random(
        seed
        + AUX_PAST_OFFSET
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

    fake_past_counts = Counter()

    for _ in range(
        BURN_IN
        + USEFUL_TRANSITIONS
    ):
        fake_prev = past_rng.choice(
            ALPHABET
        )

        fake_past_counts[
            fake_prev
        ] += 1

        family = D2.allowed_successors(
            fake_prev,
            current,
        )

        nxt = choose_uniform(
            family,
            rng,
        )

        raw_states.append(
            nxt
        )

        prev, current = (
            current,
            nxt,
        )

    return finalize_two_state(
        raw_states,
        {
            "initial_pair": (
                initial_prev,
                initial_current,
            ),

            "aux_seed": (
                seed
                + AUX_PAST_OFFSET
            ),

            "fake_past_counts": {
                str(state): (
                    fake_past_counts[
                        state
                    ]
                )
                for state
                in ALPHABET
            },
        },
    )


# ============================================================
# ABLACION C — DETERMINISTIC_CHOICE
# ============================================================

def generate_deterministic(
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
        nxt = D2.family_base(
            prev,
            current,
        )

        raw_states.append(
            nxt
        )

        prev, current = (
            current,
            nxt,
        )

    return finalize_two_state(
        raw_states,
        {
            "initial_pair": (
                initial_prev,
                initial_current,
            ),
        },
    )


# ============================================================
# ABLACION D — DELAYED_PAST
# ============================================================

def generate_delayed_past(
    seed: int,
):
    rng = random.Random(
        seed
    )

    initial_m2 = rng.choice(
        ALPHABET
    )

    initial_m1 = rng.choice(
        ALPHABET
    )

    initial_0 = rng.choice(
        ALPHABET
    )

    raw_states = [
        initial_m2,
        initial_m1,
        initial_0,
    ]

    for _ in range(
        BURN_IN
        + USEFUL_TRANSITIONS
    ):
        delayed_prev = (
            raw_states[-3]
        )

        current = (
            raw_states[-1]
        )

        family = D2.allowed_successors(
            delayed_prev,
            current,
        )

        nxt = choose_uniform(
            family,
            rng,
        )

        raw_states.append(
            nxt
        )

    return finalize_three_state(
        raw_states,
        {
            "initial_triple": (
                initial_m2,
                initial_m1,
                initial_0,
            ),
        },
    )


GENERATORS = {
    ABL_NO_PAST: (
        generate_no_past
    ),

    ABL_RANDOMIZED: (
        generate_randomized_past
    ),

    ABL_DETERMINISTIC: (
        generate_deterministic
    ),

    ABL_DELAYED: (
        generate_delayed_past
    ),
}


# ============================================================
# VERIFICACIONES ESTRUCTURALES
# ============================================================

def deterministic_edges():
    edges = set()

    for prev, current in product(
        ALPHABET,
        repeat=2,
    ):
        nxt = D2.family_base(
            prev,
            current,
        )

        edges.add(
            (
                (prev, current),
                (current, nxt),
            )
        )

    return edges


def delayed_edges():
    edges = set()

    for a, b, c in product(
        ALPHABET,
        repeat=3,
    ):
        for nxt in (
            D2.allowed_successors(
                a,
                c,
            )
        ):
            edges.add(
                (
                    (a, b, c),
                    (b, c, nxt),
                )
            )

    return edges


def verify_structure():
    baseline = (
        D2.verify_structure()
    )

    if baseline["nodes"] != 25:
        raise AssertionError(
            "baseline D2 invalida"
        )

    no_past_distinct = {}

    for current in ALPHABET:
        families = {
            no_past_family(
                current
            )
            for _prev
            in ALPHABET
        }

        no_past_distinct[
            str(current)
        ] = len(families)

    if any(
        value != 1
        for value
        in no_past_distinct.values()
    ):
        raise AssertionError(
            "NO_PAST depende del pasado"
        )

    no_past_sizes = {
        len(
            no_past_family(
                current
            )
        )
        for current
        in ALPHABET
    }

    if no_past_sizes != {
        3
    }:
        raise AssertionError(
            "NO_PAST no conserva "
            "familia de tamaño 3"
        )

    det_edges = (
        deterministic_edges()
    )

    if len(det_edges) != 25:
        raise AssertionError(
            "DETERMINISTIC debe "
            "tener 25 aristas"
        )

    det_out_degree = Counter(
        source
        for source, _target
        in det_edges
    )

    if any(
        det_out_degree[node] != 1
        for node in product(
            ALPHABET,
            repeat=2,
        )
    ):
        raise AssertionError(
            "DETERMINISTIC debe "
            "tener out-degree 1"
        )

    delayed = delayed_edges()

    if len(delayed) != 375:
        raise AssertionError(
            "DELAYED debe tener "
            "125*3 aristas"
        )

    delayed_out_degree = Counter(
        source
        for source, _target
        in delayed
    )

    if any(
        delayed_out_degree[node]
        != 3
        for node in product(
            ALPHABET,
            repeat=3,
        )
    ):
        raise AssertionError(
            "DELAYED debe tener "
            "out-degree 3"
        )

    return {
        "baseline_nodes": 25,
        "baseline_edges": 75,

        "no_past_distinct_families_by_current": (
            no_past_distinct
        ),

        "no_past_family_size": 3,

        "randomized_past_aux_seed_offset": (
            AUX_PAST_OFFSET
        ),

        "deterministic_nodes": 25,
        "deterministic_edges": 25,
        "deterministic_out_degree": 1,

        "delayed_nodes": 125,
        "delayed_edges": 375,
        "delayed_out_degree": 3,
    }


# ============================================================
# GATE COMPLETO D2 CONGELADO
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
                if p_rel
                is not None
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
    ablation,
    seed,
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

    metric = (
        METRICS.compute_seed_metrics(
            ablation,
            seed,
            generated["states"],
            frozen_like,
        )
    )

    seed_pass = full_seed_gate(
        hist,
        metric,
    )

    historical_joint = all(
        (
            metric["A1"] > 0.0,
            hist["delta_hit"],
            hist["c_hit"],
        )
    )

    return {
        "ablation": ablation,
        "seed": seed,

        "metadata": (
            generated[
                "metadata"
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

        "A1_positive": (
            metric["A1"] > 0.0
        ),

        "historical_joint": (
            historical_joint
        ),

        "U_le_T_U": (
            metric["U"] <= T_U
        ),

        "seed_pass": (
            seed_pass
        ),

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
# RESUMEN POR ABLACION
# ============================================================

def summarize(
    results,
):
    return {
        "A1_positive_count": sum(
            1
            for r in results
            if r[
                "A1_positive"
            ]
        ),

        "delta_hit_count": sum(
            1
            for r in results
            if r[
                "delta_hit"
            ]
        ),

        "c_hit_count": sum(
            1
            for r in results
            if r[
                "c_hit"
            ]
        ),

        "historical_joint_count": sum(
            1
            for r in results
            if r[
                "historical_joint"
            ]
        ),

        "U_le_T_U_count": sum(
            1
            for r in results
            if r[
                "U_le_T_U"
            ]
        ),

        "seed_pass_count": sum(
            1
            for r in results
            if r[
                "seed_pass"
            ]
        ),
    }


def evaluate_battery(
    summaries,
):
    no_past = summaries[
        ABL_NO_PAST
    ]

    randomized = summaries[
        ABL_RANDOMIZED
    ]

    deterministic = summaries[
        ABL_DETERMINISTIC
    ]

    no_past_pass = all(
        (
            no_past[
                "A1_positive_count"
            ] <= 1,

            no_past[
                "delta_hit_count"
            ] <= 1,

            no_past[
                "c_hit_count"
            ] <= 1,

            no_past[
                "seed_pass_count"
            ] <= 1,
        )
    )

    randomized_pass = all(
        (
            randomized[
                "A1_positive_count"
            ] <= 1,

            randomized[
                "delta_hit_count"
            ] <= 1,

            randomized[
                "c_hit_count"
            ] <= 1,

            randomized[
                "seed_pass_count"
            ] <= 1,
        )
    )

    deterministic_pass = all(
        (
            deterministic[
                "U_le_T_U_count"
            ] >= 7,

            deterministic[
                "seed_pass_count"
            ] < 7,
        )
    )

    battery_pass = all(
        (
            no_past_pass,
            randomized_pass,
            deterministic_pass,
        )
    )

    return {
        "NO_PAST_primary_pass": (
            no_past_pass
        ),

        "RANDOMIZED_PAST_primary_pass": (
            randomized_pass
        ),

        "DETERMINISTIC_CHOICE_primary_pass": (
            deterministic_pass
        ),

        "DELAYED_PAST_role": (
            "diagnostic-only"
        ),

        "battery_primary_pass": (
            battery_pass
        ),
    }


# ============================================================
# TRAZAS
# ============================================================

def load_baseline_summary():
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
            "baseline D2 congelado "
            "no coincide con 8/8 PASS"
        )

    return {
        "seed_passes": (
            summary[
                "seed_passes"
            ]
        ),

        "candidate_pass": (
            summary[
                "candidate_pass"
            ]
        ),
    }


def write_outputs(
    all_states,
    results_by_ablation,
    summaries,
    structure,
    battery,
):
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    payload = {
        "version": VERSION,

        "baseline_D2": (
            load_baseline_summary()
        ),

        "contract": {
            "alphabet": ALPHABET,
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

            "aux_past_seed_offset": (
                AUX_PAST_OFFSET
            ),
        },

        "trace": {
            "ablation_spec_sha256": (
                METRICS.file_sha256(
                    ABLATIONS_SPEC_PATH
                )
            ),

            "ablation_gate_sha256": (
                METRICS.file_sha256(
                    ABLATIONS_GATE_PATH
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
        },

        "structure": structure,

        "results": (
            results_by_ablation
        ),

        "summaries": summaries,

        "battery": battery,
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
                        "ablation",
                        "seed",
                        "t",
                        "state",
                    )
                )

                for ablation in ABLATIONS:
                    for seed in SEEDS:
                        states = (
                            all_states[
                                ablation
                            ][seed]
                        )

                        for t, state in enumerate(
                            states
                        ):
                            writer.writerow(
                                (
                                    VERSION,
                                    ablation,
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
        "LAB-D2-ABLATIONS-v1 "
        "— CONTROL ESTRUCTURAL"
    )

    print("=" * 116)

    print(
        "NO_PAST familias distintas "
        "por presente: "
        + str(
            report[
                "no_past_distinct_families_by_current"
            ]
        )
    )

    print(
        "NO_PAST family size:        "
        f"{report['no_past_family_size']}"
    )

    print(
        "RANDOMIZED aux offset:      "
        f"{report['randomized_past_aux_seed_offset']}"
    )

    print(
        "DETERMINISTIC nodes/edges:  "
        f"{report['deterministic_nodes']}/"
        f"{report['deterministic_edges']}"
    )

    print(
        "DETERMINISTIC out-degree:   "
        f"{report['deterministic_out_degree']}"
    )

    print(
        "DELAYED nodes/edges:        "
        f"{report['delayed_nodes']}/"
        f"{report['delayed_edges']}"
    )

    print(
        "DELAYED out-degree:         "
        f"{report['delayed_out_degree']}"
    )

    print()
    print(
        "STRUCTURE CHECK: PASS"
    )


def print_seed(
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
        f"H={'Y' if result['historical_joint'] else 'N'}  "
        f"PASS={'YES' if result['seed_pass'] else 'NO'}"
    )


def print_summary(
    ablation,
    summary,
):
    print()
    print(
        f"RESUMEN {ablation}"
    )

    print("-" * 116)

    print(
        "A1 positivos:       "
        f"{summary['A1_positive_count']}/8"
    )

    print(
        "Delta hits:         "
        f"{summary['delta_hit_count']}/8"
    )

    print(
        "C hits:             "
        f"{summary['c_hit_count']}/8"
    )

    print(
        "H conjunto:         "
        f"{summary['historical_joint_count']}/8"
    )

    print(
        "U <= T_U:           "
        f"{summary['U_le_T_U_count']}/8"
    )

    print(
        "seed passes:        "
        f"{summary['seed_pass_count']}/8"
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

    print()
    print(
        "PRIMERA EJECUCION DE "
        "ABLACIONES CAUSALES v1"
    )

    print("=" * 116)

    baseline = load_baseline_summary()

    print(
        "baseline D2 congelado: "
        f"{baseline['seed_passes']}/8 PASS"
    )

    all_states = {
        ablation: {}
        for ablation
        in ABLATIONS
    }

    results_by_ablation = {}
    summaries = {}

    for ablation in ABLATIONS:
        print()
        print(ablation)

        print("=" * 116)

        generator = GENERATORS[
            ablation
        ]

        condition_results = []

        for seed in SEEDS:
            generated = generator(
                seed
            )

            result = evaluate_seed(
                ablation,
                seed,
                generated,
            )

            all_states[
                ablation
            ][seed] = (
                generated[
                    "states"
                ]
            )

            condition_results.append(
                result
            )

            print_seed(
                result
            )

        results_by_ablation[
            ablation
        ] = condition_results

        summary = summarize(
            condition_results
        )

        summaries[
            ablation
        ] = summary

        print_summary(
            ablation,
            summary,
        )

    battery = evaluate_battery(
        summaries
    )

    print()
    print(
        "GATE PRIMARIO DE LA BATERIA"
    )

    print("=" * 116)

    print(
        "NO_PAST:             "
        + (
            "PASS"
            if battery[
                "NO_PAST_primary_pass"
            ]
            else "FAIL"
        )
    )

    print(
        "RANDOMIZED_PAST:     "
        + (
            "PASS"
            if battery[
                "RANDOMIZED_PAST_primary_pass"
            ]
            else "FAIL"
        )
    )

    print(
        "DETERMINISTIC:       "
        + (
            "PASS"
            if battery[
                "DETERMINISTIC_CHOICE_primary_pass"
            ]
            else "FAIL"
        )
    )

    print(
        "DELAYED_PAST:        "
        "DIAGNOSTIC ONLY"
    )

    print()

    print(
        "RESULTADO FINAL: "
        + (
            "ABLATION BATTERY v1 PASS"
            if battery[
                "battery_primary_pass"
            ]
            else "ABLATION BATTERY v1 FAIL"
        )
    )

    write_outputs(
        all_states,
        results_by_ablation,
        summaries,
        structure,
        battery,
    )

    print()
    print("TRAZAS")

    print("=" * 116)

    print(OUTPUT_JSON)
    print(OUTPUT_SERIES)

    if not battery[
        "battery_primary_pass"
    ]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()