from __future__ import annotations

import argparse
import csv
import gzip
import importlib.util
import inspect
import io
import json
import random
import sys

from itertools import product
from pathlib import Path
from statistics import median


VERSION = "LAB-D2-v1"

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"

D0_PATH = ROOT / "LAB-FEN-001_D0.py"
METRICS_PATH = ROOT / "LAB-FEN-001_METRICS_v1.py"

D2_SPEC_PATH = ROOT / "LAB-FEN-001_D2_SPEC_v1.md"
THRESHOLDS_PATH = ROOT / "LAB-FEN-001_THRESHOLDS_v1.md"
METRICS_SPEC_PATH = ROOT / "LAB-FEN-001_METRICS_v1.md"

OUTPUT_JSON = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_v1_results.json"
)

OUTPUT_SERIES = (
    RESULTS_DIR
    / "LAB-FEN-001_D2_v1_series.csv.gz"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(
        name,
        path,
    )

    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"No se pudo cargar {path}"
        )

    module = importlib.util.module_from_spec(spec)

    sys.modules[name] = module
    spec.loader.exec_module(module)

    return module


D0 = load_module(
    "lab_d0_v1_frozen_for_d2",
    D0_PATH,
)

METRICS = load_module(
    "lab_metrics_v1_frozen_for_d2",
    METRICS_PATH,
)


ALPHABET = (0, 1, 2, 3, 4)
N_STATES = 5

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

BURN_IN = 1_000
USEFUL_TRANSITIONS = 30_000
TRAIN_TRANSITIONS = 18_000
TEST_TRANSITIONS = 12_000

T_P = 0.5075018151904057
T_N = 0.3862533855592818
T_U = 0.4908272358457767


assert tuple(D0.ALPHABET) == ALPHABET
assert D0.N_STATES == N_STATES
assert tuple(D0.SEEDS) == SEEDS

assert D0.BURN_IN == BURN_IN
assert D0.USEFUL_TRANSITIONS == USEFUL_TRANSITIONS
assert D0.TRAIN_TRANSITIONS == TRAIN_TRANSITIONS
assert D0.TEST_TRANSITIONS == TEST_TRANSITIONS

assert METRICS.TRAIN_TRANSITIONS == TRAIN_TRANSITIONS
assert METRICS.TEST_TRANSITIONS == TEST_TRANSITIONS
assert tuple(METRICS.SEEDS) == SEEDS


Example = D0.Example


# ============================================================
# REGLA GENERADORA CONGELADA
# ============================================================

def family_base(
    prev: int,
    current: int,
) -> int:
    return (
        current
        + 2 * prev
    ) % N_STATES


def allowed_successors(
    prev: int,
    current: int,
):
    base = family_base(
        prev,
        current,
    )

    return tuple(
        (
            base + offset
        )
        % N_STATES
        for offset in range(3)
    )


def sample_next(
    prev: int,
    current: int,
    rng: random.Random,
) -> int:
    family = allowed_successors(
        prev,
        current,
    )

    return family[
        rng.randrange(3)
    ]


assert tuple(
    inspect.signature(
        sample_next
    ).parameters
) == (
    "prev",
    "current",
    "rng",
)


# ============================================================
# ESTRUCTURA CAUSAL
# ============================================================

NODES = tuple(
    product(
        ALPHABET,
        repeat=2,
    )
)


def build_edges():
    edges = set()

    for prev, current in NODES:
        family = allowed_successors(
            prev,
            current,
        )

        for nxt in family:
            edges.add(
                (
                    (prev, current),
                    (current, nxt),
                )
            )

    return frozenset(edges)


EDGES = build_edges()


def build_graphs():
    forward = {
        node: set()
        for node in NODES
    }

    reverse = {
        node: set()
        for node in NODES
    }

    for source, target in EDGES:
        forward[source].add(
            target
        )

        reverse[target].add(
            source
        )

    return forward, reverse


FORWARD_GRAPH, REVERSE_GRAPH = (
    build_graphs()
)


def reachable(
    start,
    graph,
):
    seen = {
        start
    }

    stack = [
        start
    ]

    while stack:
        node = stack.pop()

        for nxt in graph[node]:
            if nxt in seen:
                continue

            seen.add(nxt)
            stack.append(nxt)

    return seen


def structural_report():
    family_sizes = {
        node: len(
            set(
                allowed_successors(
                    *node
                )
            )
        )
        for node in NODES
    }

    distinct_families_by_current = {}

    for current in ALPHABET:
        families = {
            allowed_successors(
                prev,
                current,
            )
            for prev in ALPHABET
        }

        distinct_families_by_current[
            current
        ] = len(families)

    out_degrees = {
        node: len(
            FORWARD_GRAPH[node]
        )
        for node in NODES
    }

    self_loops = tuple(
        sorted(
            source
            for source, target
            in EDGES
            if source == target
        )
    )

    start = NODES[0]

    forward_reachable = reachable(
        start,
        FORWARD_GRAPH,
    )

    reverse_reachable = reachable(
        start,
        REVERSE_GRAPH,
    )

    strongly_connected = (
        len(forward_reachable)
        == len(NODES)
        and
        len(reverse_reachable)
        == len(NODES)
    )

    triple_support = {
        (
            prev,
            current,
            nxt,
        )
        for prev, current
        in NODES
        for nxt
        in allowed_successors(
            prev,
            current,
        )
    }

    return {
        "nodes": len(NODES),
        "edges": len(EDGES),

        "family_sizes": (
            family_sizes
        ),

        "distinct_families_by_current": (
            distinct_families_by_current
        ),

        "out_degrees": (
            out_degrees
        ),

        "self_loops": (
            self_loops
        ),

        "strongly_connected": (
            strongly_connected
        ),

        "triple_support": len(
            triple_support
        ),
    }


def verify_structure():
    report = structural_report()

    if report["nodes"] != 25:
        raise AssertionError(
            "LAB-D2 debe tener 25 nodos"
        )

    if report["edges"] != 75:
        raise AssertionError(
            "LAB-D2 debe tener 75 aristas"
        )

    if report[
        "triple_support"
    ] != 75:
        raise AssertionError(
            "LAB-D2 debe admitir "
            "75 trigramas"
        )

    if any(
        size != 3
        for size
        in report[
            "family_sizes"
        ].values()
    ):
        raise AssertionError(
            "cada contexto debe "
            "tener familia de tamaño 3"
        )

    if any(
        degree != 3
        for degree
        in report[
            "out_degrees"
        ].values()
    ):
        raise AssertionError(
            "cada nodo debe tener "
            "out-degree 3"
        )

    if any(
        count != 5
        for count
        in report[
            "distinct_families_by_current"
        ].values()
    ):
        raise AssertionError(
            "cada presente debe recibir "
            "5 familias historicas distintas"
        )

    expected_loops = (
        (0, 0),
        (2, 2),
        (4, 4),
    )

    if (
        report["self_loops"]
        != expected_loops
    ):
        raise AssertionError(
            "auto-bucles inesperados: "
            f"{report['self_loops']}"
        )

    if not report[
        "strongly_connected"
    ]:
        raise AssertionError(
            "el grafo causal "
            "no es fuertemente conexo"
        )

    return report


# ============================================================
# GENERACION DE TRAYECTORIA
# ============================================================

def generate_seed(seed: int):
    rng = random.Random(seed)

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

    total_generated = (
        BURN_IN
        + USEFUL_TRANSITIONS
    )

    for _ in range(
        total_generated
    ):
        nxt = sample_next(
            prev,
            current,
            rng,
        )

        raw_states.append(
            nxt
        )

        prev, current = (
            current,
            nxt,
        )

    assert len(
        raw_states
    ) == (
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

    assert len(
        useful_states
    ) == (
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

        "states": (
            useful_states
        ),

        "train": train,
        "test": test,
    }


# ============================================================
# BLOQUE HISTORICO CONGELADO
# ============================================================

def historical_metrics(
    seed,
    train,
    test,
):
    observed = D0.evaluate(
        train,
        test,
    )

    (
        null_delta,
        null_c,
    ) = D0.build_null_distribution(
        seed,
        train,
        test,
    )

    delta_p95 = (
        D0.nearest_rank_percentile(
            null_delta,
            0.95,
        )
    )

    c_p95 = (
        D0.nearest_rank_percentile(
            null_c,
            0.95,
        )
    )

    delta_hist = observed[
        "delta_hist"
    ]

    c_hist = observed[
        "c_hist"
    ]

    delta_hit = (
        delta_hist
        > delta_p95
    )

    c_hit = (
        c_hist
        > c_p95
    )

    return {
        "L1": observed["L1"],
        "L2": observed["L2"],

        "delta_hist": (
            delta_hist
        ),

        "c_hist": (
            c_hist
        ),

        "delta_null_median": (
            median(null_delta)
        ),

        "c_null_median": (
            median(null_c)
        ),

        "delta_p95": (
            delta_p95
        ),

        "c_p95": (
            c_p95
        ),

        "delta_hit": (
            delta_hit
        ),

        "c_hit": (
            c_hit
        ),

        "null_delta_values": tuple(
            null_delta
        ),

        "null_c_values": tuple(
            null_c
        ),
    }


# ============================================================
# FIRMA COMPLETA
# ============================================================

def run_seed(seed: int):
    generated = generate_seed(
        seed
    )

    hist = historical_metrics(
        seed,
        generated["train"],
        generated["test"],
    )

    frozen_like_result = {
        "delta_hist": (
            hist["delta_hist"]
        ),

        "c_hist": (
            hist["c_hist"]
        ),

        "delta_hit": (
            hist["delta_hit"]
        ),

        "c_hit": (
            hist["c_hit"]
        ),
    }

    metric = (
        METRICS.compute_seed_metrics(
            VERSION,
            seed,
            generated["states"],
            frozen_like_result,
        )
    )

    p_rel = metric[
        "P_rel"
    ]

    seed_pass = all(
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

    result = {
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
            hist["delta_hist"]
        ),

        "c_hist": (
            hist["c_hist"]
        ),

        "delta_null_median": (
            hist[
                "delta_null_median"
            ]
        ),

        "c_null_median": (
            hist[
                "c_null_median"
            ]
        ),

        "delta_p95": (
            hist["delta_p95"]
        ),

        "c_p95": (
            hist["c_p95"]
        ),

        "delta_hit": (
            hist["delta_hit"]
        ),

        "c_hit": (
            hist["c_hit"]
        ),

        "A1": metric["A1"],

        "I2_observed": (
            metric[
                "I2_observed"
            ]
        ),

        "I2_null_median": (
            metric[
                "I2_null_median"
            ]
        ),

        "I2_null_p95": (
            metric[
                "I2_null_p95"
            ]
        ),

        "P_rel": (
            metric["P_rel"]
        ),

        "D_within": (
            metric["D_within"]
        ),

        "D_null": (
            metric["D_null"]
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
            metric["Q_period"]
        ),

        "p_star": (
            metric["p_star"]
        ),

        "baseline_B": (
            metric[
                "baseline_B"
            ]
        ),

        "R_star": (
            metric["R_star"]
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

    return (
        generated["states"],
        result,
    )


# ============================================================
# SALIDAS
# ============================================================

def write_outputs(
    all_states,
    results,
    structure,
    candidate_pass,
):
    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    trace = {
        "d2_spec_sha256": (
            METRICS.file_sha256(
                D2_SPEC_PATH
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

        "d0_instrument_sha256": (
            METRICS.file_sha256(
                D0_PATH
            )
        ),

        "metrics_executable_sha256": (
            METRICS.file_sha256(
                METRICS_PATH
            )
        ),
    }

    structure_json = dict(
        structure
    )

    structure_json["family_sizes"] = {
        f"{a},{b}": value
        for (a, b), value
        in structure["family_sizes"].items()
    }

    structure_json["out_degrees"] = {
        f"{a},{b}": value
        for (a, b), value
        in structure["out_degrees"].items()
    }

    payload = {
        "version": VERSION,

        "rule": {
            "alphabet": ALPHABET,

            "family_base": (
                "(current + 2*prev) mod 5"
            ),

            "family_offsets": (
                0,
                1,
                2,
            ),

            "family_size": 3,

            "choice": (
                "uniform"
            ),
        },

        "contract": {
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

            "required_seed_passes": (
                7
            ),
        },

        "structure": structure_json,

        "trace": trace,

        "results": results,

        "summary": {
            "seed_passes": sum(
                1
                for r in results
                if r["seed_pass"]
            ),

            "candidate_pass": (
                candidate_pass
            ),
        },
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
                        "seed",
                        "t",
                        "state",
                    )
                )

                for seed in SEEDS:
                    states = all_states[
                        seed
                    ]

                    for t, state in enumerate(
                        states
                    ):
                        writer.writerow(
                            (
                                VERSION,
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
        "LAB-FEN-001 / LAB-D2-v1 "
        "— CONTROL ESTRUCTURAL"
    )

    print("=" * 112)

    print(
        f"nodos:                     "
        f"{report['nodes']}"
    )

    print(
        f"aristas:                   "
        f"{report['edges']}"
    )

    print(
        f"trigramas permitidos:       "
        f"{report['triple_support']}"
    )

    print(
        f"conectividad fuerte:        "
        f"{report['strongly_connected']}"
    )

    print(
        f"auto-bucles:                "
        f"{report['self_loops']}"
    )

    print(
        "familias por presente:      "
        + str(
            report[
                "distinct_families_by_current"
            ]
        )
    )

    print()
    print(
        "STRUCTURE CHECK: PASS"
    )


def print_seed_result(r):
    p_rel = (
        f"{r['P_rel']:.6f}"
        if r["P_rel"] is not None
        else "NA"
    )

    print(
        f"seed={r['seed']:3d}  "
        f"A1={r['A1']:+.6f}  "
        f"Delta={r['delta_hist']:+.6f}  "
        f"Dhit={'Y' if r['delta_hit'] else 'N'}  "
        f"C={r['c_hist']:.6f}  "
        f"Chit={'Y' if r['c_hit'] else 'N'}  "
        f"P={p_rel:>8s}  "
        f"N={r['N']:.6f}  "
        f"U={r['U']:.6f}  "
        f"PASS={'YES' if r['seed_pass'] else 'NO'}"
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
        "PRIMERA EJECUCION LAB-D2-v1"
    )

    print("=" * 112)

    print(
        "Los gates y la regla generadora "
        "ya deben estar congelados en Git."
    )

    all_states = {}
    results = []

    for seed in SEEDS:
        states, result = run_seed(
            seed
        )

        all_states[seed] = states
        results.append(result)

        print_seed_result(
            result
        )

    seed_passes = sum(
        1
        for result in results
        if result["seed_pass"]
    )

    candidate_pass = (
        seed_passes >= 7
    )

    print()
    print("RESUMEN")
    print("=" * 112)

    print(
        f"seed passes conjuntos: "
        f"{seed_passes}/8"
    )

    print(
        "RESULTADO FINAL: "
        + (
            "LAB-D2-v1 LOCAL CANDIDATE PASS"
            if candidate_pass
            else "LAB-D2-v1 FAIL"
        )
    )

    write_outputs(
        all_states,
        results,
        structure,
        candidate_pass,
    )

    print()
    print("TRAZAS")
    print("=" * 112)

    print(OUTPUT_JSON)
    print(OUTPUT_SERIES)

    if not candidate_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()