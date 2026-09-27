from __future__ import annotations

import csv
import gzip
import hashlib
import inspect
import json
import math
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from statistics import median
from typing import Iterable


VERSION = "LAB-D0-v1"

ALPHABET = (0, 1, 2, 3, 4)
N_STATES = len(ALPHABET)

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

ALPHA = 0.5
NULL_PERMUTATIONS = 64

assert TRAIN_TRANSITIONS + TEST_TRANSITIONS == USEFUL_TRANSITIONS


# ============================================================
# GENERADOR LAB-D0
# ============================================================

# offset, probability
TRANSITION_RULE = (
    (+1, 0.50),
    (0, 0.20),
    (-1, 0.15),
    (+2, 0.10),
    (-2, 0.05),
)

assert abs(sum(p for _, p in TRANSITION_RULE) - 1.0) < 1e-12


def sample_next(current: int, rng: random.Random) -> int:
    """
    LAB-D0-v1.

    El siguiente estado depende unicamente del estado presente.
    No recibe x[t-1] como argumento.
    """
    u = rng.random()
    cumulative = 0.0

    for offset, probability in TRANSITION_RULE:
        cumulative += probability
        if u < cumulative:
            return (current + offset) % N_STATES

    # Protección frente a error de redondeo.
    return (current + TRANSITION_RULE[-1][0]) % N_STATES


# Control estructural explícito:
# la interfaz generadora solo admite current + rng.
assert tuple(inspect.signature(sample_next).parameters) == (
    "current",
    "rng",
)


# ============================================================
# DATOS
# ============================================================

@dataclass(frozen=True)
class Example:
    prev: int
    current: int
    nxt: int


def generate_examples(seed: int):
    rng = random.Random(seed)

    state = rng.randrange(N_STATES)
    states = [state]

    total_steps = BURN_IN + USEFUL_TRANSITIONS

    for _ in range(total_steps):
        state = sample_next(state, rng)
        states.append(state)

    # Conservamos un estado anterior al comienzo de la
    # trayectoria útil para que la primera transición útil
    # tenga también contexto de segundo orden.
    segment = states[BURN_IN - 1 :]

    assert len(segment) == USEFUL_TRANSITIONS + 2

    examples = tuple(
        Example(
            prev=segment[t],
            current=segment[t + 1],
            nxt=segment[t + 2],
        )
        for t in range(USEFUL_TRANSITIONS)
    )

    useful_states = tuple(segment[1:])

    assert len(examples) == USEFUL_TRANSITIONS
    assert len(useful_states) == USEFUL_TRANSITIONS + 1

    train = examples[:TRAIN_TRANSITIONS]
    test = examples[TRAIN_TRANSITIONS:]

    assert len(train) == TRAIN_TRANSITIONS
    assert len(test) == TEST_TRANSITIONS

    return useful_states, train, test


# ============================================================
# MODELOS M1 Y M2
# ============================================================

def fit_m1(examples: Iterable[Example]):
    counts = [
        [ALPHA for _ in ALPHABET]
        for _ in ALPHABET
    ]

    for ex in examples:
        counts[ex.current][ex.nxt] += 1.0

    probs = []

    for current in ALPHABET:
        total = sum(counts[current])
        probs.append(
            tuple(value / total for value in counts[current])
        )

    return tuple(probs)


def fit_m2(examples: Iterable[Example]):
    counts = [
        [
            [ALPHA for _ in ALPHABET]
            for _ in ALPHABET
        ]
        for _ in ALPHABET
    ]

    for ex in examples:
        counts[ex.prev][ex.current][ex.nxt] += 1.0

    probs = []

    for prev in ALPHABET:
        by_current = []

        for current in ALPHABET:
            total = sum(counts[prev][current])

            by_current.append(
                tuple(
                    value / total
                    for value in counts[prev][current]
                )
            )

        probs.append(tuple(by_current))

    return tuple(probs)


# ============================================================
# METRICAS
# ============================================================

def mean_negative_log_likelihood_m1(model, examples):
    total = 0.0
    n = 0

    for ex in examples:
        p = model[ex.current][ex.nxt]
        total -= math.log(p)
        n += 1

    return total / n


def mean_negative_log_likelihood_m2(model, examples):
    total = 0.0
    n = 0

    for ex in examples:
        p = model[ex.prev][ex.current][ex.nxt]
        total -= math.log(p)
        n += 1

    return total / n


def total_variation(p, q):
    return 0.5 * sum(
        abs(a - b)
        for a, b in zip(p, q)
    )


def compute_c_hist(m1, m2, test):
    """
    Media ponderada por frecuencia de prueba de:

        TV(
            P_M2(. | prev,current),
            P_M1(. | current)
        )
    """
    total = 0.0

    for ex in test:
        p2 = m2[ex.prev][ex.current]
        p1 = m1[ex.current]

        total += total_variation(p2, p1)

    return total / len(test)


def evaluate(train, test):
    m1 = fit_m1(train)
    m2 = fit_m2(train)

    l1 = mean_negative_log_likelihood_m1(
        m1,
        test,
    )

    l2 = mean_negative_log_likelihood_m2(
        m2,
        test,
    )

    delta_hist = l1 - l2

    c_hist = compute_c_hist(
        m1,
        m2,
        test,
    )

    return {
        "L1": l1,
        "L2": l2,
        "delta_hist": delta_hist,
        "c_hist": c_hist,
    }


# ============================================================
# NULO HISTORICO CONDICIONADO
# ============================================================

def permute_previous_within_current(
    examples,
    rng: random.Random,
):
    examples = tuple(examples)

    indices_by_current = {
        current: []
        for current in ALPHABET
    }

    prev_by_current = {
        current: []
        for current in ALPHABET
    }

    for i, ex in enumerate(examples):
        indices_by_current[ex.current].append(i)
        prev_by_current[ex.current].append(ex.prev)

    permuted_prev = [None] * len(examples)

    for current in ALPHABET:
        values = list(prev_by_current[current])
        rng.shuffle(values)

        for index, prev in zip(
            indices_by_current[current],
            values,
        ):
            permuted_prev[index] = prev

    assert all(
        value is not None
        for value in permuted_prev
    )

    return tuple(
        Example(
            prev=permuted_prev[i],
            current=ex.current,
            nxt=ex.nxt,
        )
        for i, ex in enumerate(examples)
    )


def nearest_rank_percentile(values, q):
    values = sorted(values)

    if not values:
        raise ValueError("empty percentile input")

    rank = math.ceil(q * len(values))
    index = max(0, min(len(values) - 1, rank - 1))

    return values[index]


def build_null_distribution(
    seed: int,
    train,
    test,
):
    rng = random.Random(
        seed * 1_000_003 + 97_409
    )

    delta_values = []
    c_values = []

    for _ in range(NULL_PERMUTATIONS):
        null_train = permute_previous_within_current(
            train,
            rng,
        )

        null_test = permute_previous_within_current(
            test,
            rng,
        )

        result = evaluate(
            null_train,
            null_test,
        )

        delta_values.append(
            result["delta_hist"]
        )

        c_values.append(
            result["c_hist"]
        )

    return tuple(delta_values), tuple(c_values)


# ============================================================
# TRAZABILIDAD
# ============================================================

def series_sha256(states):
    payload = ",".join(
        str(x)
        for x in states
    ).encode("ascii")

    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class SeedResult:
    seed: int

    series_sha256: str

    L1: float
    L2: float

    delta_hist: float
    c_hist: float

    delta_null_median: float
    c_null_median: float

    delta_p95: float
    c_p95: float

    delta_hit: bool
    c_hit: bool

    delta_positive: bool
    c_above_null_median: bool

    null_delta_values: tuple[float, ...]
    null_c_values: tuple[float, ...]


# ============================================================
# EXPERIMENTO
# ============================================================

def run_seed(seed):
    states, train, test = generate_examples(seed)

    observed = evaluate(
        train,
        test,
    )

    null_delta, null_c = build_null_distribution(
        seed,
        train,
        test,
    )

    delta_p95 = nearest_rank_percentile(
        null_delta,
        0.95,
    )

    c_p95 = nearest_rank_percentile(
        null_c,
        0.95,
    )

    delta_null_median = median(null_delta)
    c_null_median = median(null_c)

    return (
        states,
        SeedResult(
            seed=seed,
            series_sha256=series_sha256(states),

            L1=observed["L1"],
            L2=observed["L2"],

            delta_hist=observed["delta_hist"],
            c_hist=observed["c_hist"],

            delta_null_median=delta_null_median,
            c_null_median=c_null_median,

            delta_p95=delta_p95,
            c_p95=c_p95,

            delta_hit=(
                observed["delta_hist"] > delta_p95
            ),

            c_hit=(
                observed["c_hist"] > c_p95
            ),

            delta_positive=(
                observed["delta_hist"] > 0.0
            ),

            c_above_null_median=(
                observed["c_hist"] > c_null_median
            ),

            null_delta_values=null_delta,
            null_c_values=null_c,
        ),
    )


def print_seed_result(r):
    print(
        f"seed={r.seed:3d}  "
        f"Delta_hist={r.delta_hist:+.6f}  "
        f"null_p95={r.delta_p95:+.6f}  "
        f"hit={'YES' if r.delta_hit else 'no ':3s}  "
        f"C_hist={r.c_hist:.6f}  "
        f"C_null_p95={r.c_p95:.6f}  "
        f"hit={'YES' if r.c_hit else 'no ':3s}"
    )


def write_outputs(all_states, results, summary):
    root = Path(__file__).resolve().parent
    output_dir = root / "results"
    output_dir.mkdir(parents=True, exist_ok=True)

    results_path = (
        output_dir
        / "LAB-FEN-001_D0_v1_results.json"
    )

    series_path = (
        output_dir
        / "LAB-FEN-001_D0_v1_series.csv.gz"
    )

    payload = {
        "version": VERSION,
        "alphabet": ALPHABET,
        "seeds": SEEDS,
        "burn_in": BURN_IN,
        "useful_transitions": USEFUL_TRANSITIONS,
        "train_transitions": TRAIN_TRANSITIONS,
        "test_transitions": TEST_TRANSITIONS,
        "alpha": ALPHA,
        "null_permutations": NULL_PERMUTATIONS,
        "percentile_method": "nearest-rank",
        "transition_rule": TRANSITION_RULE,
        "generator_uses_previous_state": False,
        "results": [
            asdict(r)
            for r in results
        ],
        "summary": summary,
    }

    with results_path.open(
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

    with gzip.open(
        series_path,
        "wt",
        encoding="utf-8",
        newline="",
    ) as fh:
        writer = csv.writer(fh)
        writer.writerow(
            ("version", "seed", "t", "state")
        )

        for seed in SEEDS:
            states = all_states[seed]

            for t, state in enumerate(states):
                writer.writerow(
                    (VERSION, seed, t, state)
                )

    return results_path, series_path


def main():
    print(
        "LAB-FEN-001 / LAB-D0-v1 — CONTROL DE PRIMER ORDEN"
    )
    print("=" * 88)

    print()
    print("PROTOCOLO CONGELADO")
    print("-" * 88)

    print(f"version:             {VERSION}")
    print(f"semillas:            {len(SEEDS)}")
    print(f"burn-in:             {BURN_IN}")
    print(
        f"transiciones utiles: {USEFUL_TRANSITIONS}"
    )
    print(
        f"train/test:          "
        f"{TRAIN_TRANSITIONS}/{TEST_TRANSITIONS}"
    )
    print(f"alpha:               {ALPHA}")
    print(
        f"permutaciones nulo:  {NULL_PERMUTATIONS}"
    )
    print(
        "generador consulta x[t-1]: NO"
    )

    print()
    print("RESULTADOS POR SEMILLA")
    print("-" * 88)

    all_states = {}
    results = []

    for seed in SEEDS:
        states, result = run_seed(seed)

        all_states[seed] = states
        results.append(result)

        print_seed_result(result)

    delta_hits = sum(
        r.delta_hit
        for r in results
    )

    c_hits = sum(
        r.c_hit
        for r in results
    )

    delta_positive_count = sum(
        r.delta_positive
        for r in results
    )

    c_above_median_count = sum(
        r.c_above_null_median
        for r in results
    )

    # Operacionalizacion pre-resultados de
    # "senal consistente entre semillas":
    #
    # con 8 semillas, 7/8 o 8/8 direcciones coincidentes
    # exceden el umbral unilateral de un sign test exacto
    # bajo p=0.5:
    #
    # P(X >= 7) = 9/256 ~= 0.0352.
    consistent_delta_signal = (
        delta_positive_count >= 7
    )

    consistent_c_signal = (
        c_above_median_count >= 7
    )

    generator_control = (
        tuple(
            inspect.signature(
                sample_next
            ).parameters
        )
        ==
        ("current", "rng")
    )

    pass_delta_hits = delta_hits <= 1
    pass_c_hits = c_hits <= 1

    pass_consistency = not (
        consistent_delta_signal
        or consistent_c_signal
    )

    passed = (
        pass_delta_hits
        and pass_c_hits
        and pass_consistency
        and generator_control
    )

    summary = {
        "delta_hits": delta_hits,
        "c_hits": c_hits,
        "delta_positive_seeds": delta_positive_count,
        "c_above_null_median_seeds": c_above_median_count,
        "consistent_delta_signal": consistent_delta_signal,
        "consistent_c_signal": consistent_c_signal,
        "generator_control": generator_control,
        "pass_delta_hits": pass_delta_hits,
        "pass_c_hits": pass_c_hits,
        "pass_consistency": pass_consistency,
        "lab_d0_v1_passed": passed,
    }

    print()
    print("RESUMEN")
    print("=" * 88)

    print(
        f"hits Delta_hist > p95 nulo: "
        f"{delta_hits}/{len(SEEDS)}"
    )

    print(
        f"hits C_hist > p95 nulo:     "
        f"{c_hits}/{len(SEEDS)}"
    )

    print(
        f"Delta_hist > 0:              "
        f"{delta_positive_count}/{len(SEEDS)}"
    )

    print(
        f"C_hist > mediana nulo:       "
        f"{c_above_median_count}/{len(SEEDS)}"
    )

    print(
        f"senal consistente Delta:     "
        f"{consistent_delta_signal}"
    )

    print(
        f"senal consistente C_hist:    "
        f"{consistent_c_signal}"
    )

    print(
        f"generador sin x[t-1]:        "
        f"{generator_control}"
    )

    print()
    print("GATE LAB-D0-v1")
    print("=" * 88)

    print(
        f"Delta hits <= 1/8:           "
        f"{'PASS' if pass_delta_hits else 'FAIL'}"
    )

    print(
        f"C_hist hits <= 1/8:          "
        f"{'PASS' if pass_c_hits else 'FAIL'}"
    )

    print(
        f"sin senal consistente:       "
        f"{'PASS' if pass_consistency else 'FAIL'}"
    )

    print(
        f"regla de primer orden:       "
        f"{'PASS' if generator_control else 'FAIL'}"
    )

    print()
    print(
        "RESULTADO FINAL: "
        + (
            "LAB-D0-v1 PASS"
            if passed
            else "LAB-D0-v1 FAIL"
        )
    )

    results_path, series_path = write_outputs(
        all_states,
        results,
        summary,
    )

    print()
    print("TRAZAS")
    print("=" * 88)
    print(results_path)
    print(series_path)

    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()