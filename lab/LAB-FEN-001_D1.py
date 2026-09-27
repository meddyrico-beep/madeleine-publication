from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.util
import inspect
import io
import json
import random
import sys

from dataclasses import asdict, dataclass
from itertools import product
from pathlib import Path
from statistics import median


VERSION = "LAB-D1-v1"


# ============================================================
# CARGA DEL BLOQUE INSTRUMENTAL CONGELADO DE LAB-D0
# ============================================================

D0_PATH = Path(__file__).resolve().with_name(
    "LAB-FEN-001_D0.py"
)

spec = importlib.util.spec_from_file_location(
    "lab_d0_v1_frozen",
    D0_PATH,
)

if spec is None or spec.loader is None:
    raise RuntimeError(
        "No se pudo cargar LAB-FEN-001_D0.py"
    )

D0 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = D0
spec.loader.exec_module(D0)


ALPHABET = D0.ALPHABET
N_STATES = D0.N_STATES

SEEDS = D0.SEEDS

BURN_IN = D0.BURN_IN
USEFUL_TRANSITIONS = D0.USEFUL_TRANSITIONS
TRAIN_TRANSITIONS = D0.TRAIN_TRANSITIONS
TEST_TRANSITIONS = D0.TEST_TRANSITIONS

ALPHA = D0.ALPHA
NULL_PERMUTATIONS = D0.NULL_PERMUTATIONS

Example = D0.Example


# Contrato heredado de D0.
assert ALPHABET == (0, 1, 2, 3, 4)

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

assert ALPHA == 0.5
assert NULL_PERMUTATIONS == 64


# ============================================================
# CICLO DE DE BRUIJN CONGELADO
# ============================================================

B = (
    0, 0, 1, 0, 2, 0, 3, 0, 4,
    1, 1, 2, 1, 3, 1, 4,
    2, 2, 3, 2, 4,
    3, 3, 4, 4,
)

PERIOD = len(B)

assert PERIOD == 25


def cyclic_pairs(sequence):
    n = len(sequence)

    return tuple(
        (
            sequence[i],
            sequence[(i + 1) % n],
        )
        for i in range(n)
    )


CONTEXT_CYCLE = cyclic_pairs(B)

assert len(CONTEXT_CYCLE) == 25
assert len(set(CONTEXT_CYCLE)) == 25

EXPECTED_CONTEXTS = set(
    product(ALPHABET, repeat=2)
)

assert set(CONTEXT_CYCLE) == EXPECTED_CONTEXTS


# ============================================================
# TABLA F(a,b)
# ============================================================

def build_transition_table():
    table = {}

    for i in range(PERIOD):
        prev = B[i]
        current = B[(i + 1) % PERIOD]
        nxt = B[(i + 2) % PERIOD]

        key = (prev, current)

        if key in table:
            raise AssertionError(
                f"contexto repetido: {key}"
            )

        table[key] = nxt

    return table


F = build_transition_table()

assert len(F) == 25
assert set(F) == EXPECTED_CONTEXTS


# ============================================================
# PROPIEDADES ESTRUCTURALES
# ============================================================

def successors_for_current(current):
    return {
        F[(prev, current)]
        for prev in ALPHABET
    }


SUCCESSOR_SETS = {
    current: successors_for_current(current)
    for current in ALPHABET
}


# Para cada presente, diferentes pasados producen
# múltiples futuros.
HISTORY_DEPENDENCY_ALL_CURRENT = all(
    len(SUCCESSOR_SETS[current]) > 1
    for current in ALPHABET
)


# Esta construcción es incluso más fuerte:
# los cinco pasados producen cinco sucesores distintos
# para cada estado presente.
HISTORY_FULL_SEPARATION = all(
    len(SUCCESSOR_SETS[current]) == N_STATES
    for current in ALPHABET
)

assert HISTORY_DEPENDENCY_ALL_CURRENT
assert HISTORY_FULL_SEPARATION


# Una tabla completa de pares -> sucesor es determinista
# si cada contexto tiene exactamente una salida.
DETERMINISTIC_RULE = (
    len(F) == len(EXPECTED_CONTEXTS)
)

assert DETERMINISTIC_RULE


def minimal_period(sequence):
    n = len(sequence)

    for p in range(1, n + 1):
        if n % p != 0:
            continue

        if all(
            sequence[i] == sequence[i % p]
            for i in range(n)
        ):
            return p

    raise AssertionError(
        "no se pudo determinar periodo"
    )


CONTEXT_PERIOD = minimal_period(
    CONTEXT_CYCLE
)

assert CONTEXT_PERIOD == 25


# ============================================================
# GENERADOR LAB-D1
# ============================================================

def sample_next(prev: int, current: int) -> int:
    """
    LAB-D1-v1.

    El futuro depende del par:
        (x[t-1], x[t])

    y es determinista.
    """
    return F[(prev, current)]


assert tuple(
    inspect.signature(
        sample_next
    ).parameters
) == (
    "prev",
    "current",
)


# ============================================================
# GENERACION DE DATOS
# ============================================================

def generate_examples(seed: int):
    rng = random.Random(seed)

    # La semilla solo selecciona fase.
    phase = rng.randrange(PERIOD)

    prev = B[phase]
    current = B[(phase + 1) % PERIOD]

    states = [
        prev,
        current,
    ]

    total_generated = (
        BURN_IN
        + USEFUL_TRANSITIONS
    )

    for _ in range(total_generated):
        nxt = sample_next(
            prev,
            current,
        )

        states.append(nxt)

        prev, current = (
            current,
            nxt,
        )

    # 2 + burn-in + transiciones útiles
    assert len(states) == (
        BURN_IN
        + USEFUL_TRANSITIONS
        + 2
    )

    # Tras descartar burn-in quedan exactamente
    # 30002 estados -> 30000 triples.
    segment = states[BURN_IN:]

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
        USEFUL_TRANSITIONS + 1
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

    # Ambos cortes contienen ciclos completos.
    assert len(train) % PERIOD == 0
    assert len(test) % PERIOD == 0

    return (
        phase,
        useful_states,
        train,
        test,
    )


# ============================================================
# INSTRUMENTOS HEREDADOS SIN MODIFICACION
# ============================================================

def evaluate(train, test):
    return D0.evaluate(
        train,
        test,
    )


def build_null_distribution(
    seed,
    train,
    test,
):
    return D0.build_null_distribution(
        seed,
        train,
        test,
    )


def nearest_rank_percentile(
    values,
    q,
):
    return D0.nearest_rank_percentile(
        values,
        q,
    )


def series_sha256(states):
    return D0.series_sha256(
        states
    )


# ============================================================
# RESULTADO POR SEMILLA
# ============================================================

@dataclass(frozen=True)
class SeedResult:
    seed: int
    phase: int

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

    null_delta_values: tuple[float, ...]
    null_c_values: tuple[float, ...]


def run_seed(seed):
    (
        phase,
        states,
        train,
        test,
    ) = generate_examples(seed)

    observed = evaluate(
        train,
        test,
    )

    (
        null_delta,
        null_c,
    ) = build_null_distribution(
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

    result = SeedResult(
        seed=seed,
        phase=phase,

        series_sha256=series_sha256(
            states
        ),

        L1=observed["L1"],
        L2=observed["L2"],

        delta_hist=observed[
            "delta_hist"
        ],

        c_hist=observed[
            "c_hist"
        ],

        delta_null_median=median(
            null_delta
        ),

        c_null_median=median(
            null_c
        ),

        delta_p95=delta_p95,
        c_p95=c_p95,

        delta_hit=(
            observed["delta_hist"]
            > delta_p95
        ),

        c_hit=(
            observed["c_hist"]
            > c_p95
        ),

        delta_positive=(
            observed["delta_hist"]
            > 0.0
        ),

        null_delta_values=null_delta,
        null_c_values=null_c,
    )

    return states, result


# ============================================================
# SALIDA
# ============================================================

def print_seed_result(r):
    print(
        f"seed={r.seed:3d}  "
        f"phase={r.phase:2d}  "
        f"Delta_hist={r.delta_hist:+.6f}  "
        f"null_p95={r.delta_p95:+.6f}  "
        f"hit={'YES' if r.delta_hit else 'no ':3s}  "
        f"C_hist={r.c_hist:.6f}  "
        f"C_null_p95={r.c_p95:.6f}  "
        f"hit={'YES' if r.c_hit else 'no ':3s}"
    )


def write_outputs(
    all_states,
    results,
    summary,
):
    root = Path(__file__).resolve().parent

    output_dir = (
        root
        / "results"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    results_path = (
        output_dir
        / "LAB-FEN-001_D1_v1_results.json"
    )

    series_path = (
        output_dir
        / "LAB-FEN-001_D1_v1_series.csv.gz"
    )

    transition_table = [
        {
            "prev": prev,
            "current": current,
            "next": F[(prev, current)],
        }
        for prev, current
        in sorted(F)
    ]

    payload = {
        "version": VERSION,

        "source_instrument": (
            "LAB-FEN-001_D0.py"
        ),

        "alphabet": ALPHABET,
        "cycle_B": B,
        "period": PERIOD,

        "transition_table": (
            transition_table
        ),

        "history_dependency_all_current": (
            HISTORY_DEPENDENCY_ALL_CURRENT
        ),

        "history_full_separation": (
            HISTORY_FULL_SEPARATION
        ),

        "deterministic_rule": (
            DETERMINISTIC_RULE
        ),

        "context_period": (
            CONTEXT_PERIOD
        ),

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

        "alpha": ALPHA,

        "null_permutations": (
            NULL_PERMUTATIONS
        ),

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

    # gzip reproducible:
    # mtime=0 evita una marca temporal variable
    # en la cabecera.
    with series_path.open(
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
                writer = csv.writer(fh)

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

    return (
        results_path,
        series_path,
    )


# ============================================================
# MAIN
# ============================================================

def main():
    print(
        "LAB-FEN-001 / LAB-D1-v1 — "
        "CONTROL POSITIVO DE SEGUNDO ORDEN"
    )

    print("=" * 94)

    print()
    print("PROTOCOLO CONGELADO")
    print("-" * 94)

    print(
        f"version:                  "
        f"{VERSION}"
    )

    print(
        f"periodo contexto:         "
        f"{CONTEXT_PERIOD}"
    )

    print(
        f"contextos cubiertos:       "
        f"{len(F)}/25"
    )

    print(
        f"dependencia historica:    "
        f"{HISTORY_DEPENDENCY_ALL_CURRENT}"
    )

    print(
        f"separacion completa:      "
        f"{HISTORY_FULL_SEPARATION}"
    )

    print(
        f"regla determinista:       "
        f"{DETERMINISTIC_RULE}"
    )

    print(
        f"semillas:                 "
        f"{len(SEEDS)}"
    )

    print(
        f"train/test:               "
        f"{TRAIN_TRANSITIONS}/"
        f"{TEST_TRANSITIONS}"
    )

    print(
        f"alpha:                    "
        f"{ALPHA}"
    )

    print(
        f"permutaciones nulo:       "
        f"{NULL_PERMUTATIONS}"
    )

    print()
    print("SUCESORES POR ESTADO PRESENTE")
    print("-" * 94)

    for current in ALPHABET:
        print(
            f"x[t]={current}: "
            f"{sorted(SUCCESSOR_SETS[current])}"
        )

    print()
    print("RESULTADOS POR SEMILLA")
    print("-" * 94)

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

    pass_delta_hits = (
        delta_hits >= 7
    )

    pass_c_hits = (
        c_hits >= 7
    )

    pass_delta_positive = (
        delta_positive_count >= 7
    )

    pass_context_coverage = (
        len(F) == 25
        and set(F) == EXPECTED_CONTEXTS
    )

    pass_history_dependency = (
        HISTORY_DEPENDENCY_ALL_CURRENT
    )

    pass_deterministic = (
        DETERMINISTIC_RULE
    )

    pass_period = (
        CONTEXT_PERIOD == 25
    )

    passed = all(
        (
            pass_delta_hits,
            pass_c_hits,
            pass_delta_positive,
            pass_context_coverage,
            pass_history_dependency,
            pass_deterministic,
            pass_period,
        )
    )

    summary = {
        "delta_hits": delta_hits,
        "c_hits": c_hits,

        "delta_positive_seeds": (
            delta_positive_count
        ),

        "pass_delta_hits": (
            pass_delta_hits
        ),

        "pass_c_hits": (
            pass_c_hits
        ),

        "pass_delta_positive": (
            pass_delta_positive
        ),

        "pass_context_coverage": (
            pass_context_coverage
        ),

        "pass_history_dependency": (
            pass_history_dependency
        ),

        "pass_deterministic": (
            pass_deterministic
        ),

        "pass_period": (
            pass_period
        ),

        "lab_d1_v1_passed": (
            passed
        ),
    }

    print()
    print("RESUMEN")
    print("=" * 94)

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
        f"{delta_positive_count}/"
        f"{len(SEEDS)}"
    )

    print()
    print("GATE LAB-D1-v1")
    print("=" * 94)

    print(
        f"Delta hits >= 7/8:           "
        f"{'PASS' if pass_delta_hits else 'FAIL'}"
    )

    print(
        f"C_hist hits >= 7/8:          "
        f"{'PASS' if pass_c_hits else 'FAIL'}"
    )

    print(
        f"Delta positivo >= 7/8:       "
        f"{'PASS' if pass_delta_positive else 'FAIL'}"
    )

    print(
        f"cobertura 25/25:             "
        f"{'PASS' if pass_context_coverage else 'FAIL'}"
    )

    print(
        f"historia cambia sucesor:      "
        f"{'PASS' if pass_history_dependency else 'FAIL'}"
    )

    print(
        f"regla determinista:           "
        f"{'PASS' if pass_deterministic else 'FAIL'}"
    )

    print(
        f"periodo estructural = 25:     "
        f"{'PASS' if pass_period else 'FAIL'}"
    )

    print()
    print(
        "RESULTADO FINAL: "
        + (
            "LAB-D1-v1 PASS"
            if passed
            else "LAB-D1-v1 FAIL"
        )
    )

    results_path, series_path = (
        write_outputs(
            all_states,
            results,
            summary,
        )
    )

    print()
    print("TRAZAS")
    print("=" * 94)

    print(results_path)
    print(series_path)

    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()