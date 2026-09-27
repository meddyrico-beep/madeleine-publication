from __future__ import annotations

import csv
import gzip
import hashlib
import json
import math
import random

from collections import Counter
from pathlib import Path
from statistics import median


VERSION = "LAB-FEN-001-METRICS-v1"

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

TRAIN_TRANSITIONS = 18_000
TEST_TRANSITIONS = 12_000

WINDOW_TRANSITIONS = 1_500
N_WINDOWS = 8

ALPHA = 0.5
NULL_REPLICATES = 64

MAX_LAG = 1_500

assert N_WINDOWS * WINDOW_TRANSITIONS == TEST_TRANSITIONS


ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"

METRICS_SPEC = ROOT / "LAB-FEN-001_METRICS_v1.md"

D0_JSON = RESULTS_DIR / "LAB-FEN-001_D0_v1_results.json"
D0_SERIES = RESULTS_DIR / "LAB-FEN-001_D0_v1_series.csv.gz"

D1_JSON = RESULTS_DIR / "LAB-FEN-001_D1_v1_results.json"
D1_SERIES = RESULTS_DIR / "LAB-FEN-001_D1_v1_series.csv.gz"

OUTPUT_JSON = (
    RESULTS_DIR
    / "LAB-FEN-001_METRICS_v1_calibration.json"
)


# ============================================================
# UTILIDADES DE TRAZABILIDAD
# ============================================================

def file_sha256(path: Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as fh:
        for block in iter(
            lambda: fh.read(1024 * 1024),
            b"",
        ):
            h.update(block)

    return h.hexdigest()


def logical_series_sha256(states) -> str:
    payload = ",".join(
        str(x)
        for x in states
    ).encode("ascii")

    return hashlib.sha256(payload).hexdigest()


def load_json(path: Path):
    with path.open(
        "r",
        encoding="utf-8",
    ) as fh:
        return json.load(fh)


def load_series(path: Path):
    by_seed = {
        seed: []
        for seed in SEEDS
    }

    expected_t = {
        seed: 0
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

        if set(reader.fieldnames or ()) != required:
            raise AssertionError(
                f"cabecera inesperada en {path.name}: "
                f"{reader.fieldnames}"
            )

        for row in reader:
            seed = int(row["seed"])
            t = int(row["t"])
            state = int(row["state"])

            if seed not in by_seed:
                raise AssertionError(
                    f"semilla inesperada: {seed}"
                )

            if state not in ALPHABET:
                raise AssertionError(
                    f"estado fuera de alfabeto: {state}"
                )

            if t != expected_t[seed]:
                raise AssertionError(
                    f"indice discontinuo seed={seed}: "
                    f"esperado {expected_t[seed]}, obtenido {t}"
                )

            by_seed[seed].append(state)
            expected_t[seed] += 1

    result = {
        seed: tuple(values)
        for seed, values in by_seed.items()
    }

    for seed in SEEDS:
        if len(result[seed]) != 30_001:
            raise AssertionError(
                f"longitud inesperada seed={seed}: "
                f"{len(result[seed])}"
            )

    return result


def result_index(payload):
    return {
        int(item["seed"]): item
        for item in payload["results"]
    }


def verify_frozen_dataset(
    label,
    payload,
    series,
):
    index = result_index(payload)

    if tuple(int(x) for x in payload["seeds"]) != SEEDS:
        raise AssertionError(
            f"{label}: semillas no coinciden"
        )

    for seed in SEEDS:
        expected = index[seed]["series_sha256"]
        actual = logical_series_sha256(
            series[seed]
        )

        if actual != expected:
            raise AssertionError(
                f"{label}: SHA logico incorrecto "
                f"para seed={seed}"
            )


# ============================================================
# CORTE TRAIN / TEST
# ============================================================

def split_frozen_series(states):
    """
    La serie guardada contiene 30001 estados:

        s1 ... s30001

    que representan 30000 transiciones predictivas.

    Train:
        s1 -> ... -> s18001
        18000 transiciones.

    Test path:
        s18001 -> ... -> s30001
        12000 transiciones.

    Para los 12000 trigramas de test necesitamos además:

        s18000

    como contexto previo.
    """

    train_path = states[
        : TRAIN_TRANSITIONS + 1
    ]

    test_history = states[
        TRAIN_TRANSITIONS - 1 :
    ]

    test_path = states[
        TRAIN_TRANSITIONS :
    ]

    assert len(train_path) == 18_001
    assert len(test_history) == 12_002
    assert len(test_path) == 12_001

    return (
        train_path,
        test_history,
        test_path,
    )


# ============================================================
# MODELO MARKOV-1
# ============================================================

def fit_m1(train_path):
    counts = [
        [
            ALPHA
            for _ in ALPHABET
        ]
        for _ in ALPHABET
    ]

    for current, nxt in zip(
        train_path[:-1],
        train_path[1:],
    ):
        counts[current][nxt] += 1.0

    probs = []

    for current in ALPHABET:
        total = sum(
            counts[current]
        )

        probs.append(
            tuple(
                value / total
                for value in counts[current]
            )
        )

    return tuple(probs)


def sample_categorical(
    probs,
    rng: random.Random,
):
    u = rng.random()
    cumulative = 0.0

    for state, p in enumerate(probs):
        cumulative += p

        if u < cumulative:
            return state

    return len(probs) - 1


def surrogate_rng(
    seed: int,
    replicate: int,
):
    """
    Fórmula congelada antes de resultados.

    No usa hash() de Python para evitar
    aleatoriedad entre procesos.
    """
    derived = (
        seed * 10_000_019
        + (replicate + 1) * 104_729
        + 4_241
    )

    return random.Random(derived)


def generate_markov1_surrogate(
    m1,
    observed_test_history,
    seed,
    replicate,
):
    """
    Produce exactamente 12000 trigramas evaluables.

    Los dos primeros estados se fijan al contexto
    de frontera observado:

        predecessor,
        first test current.

    A partir de ahí sólo actúa M1.

    El primer estado es contexto de frontera;
    la regla generadora nunca consulta ese pasado.
    """

    rng = surrogate_rng(
        seed,
        replicate,
    )

    history = [
        observed_test_history[0],
        observed_test_history[1],
    ]

    current = history[-1]

    for _ in range(TEST_TRANSITIONS):
        nxt = sample_categorical(
            m1[current],
            rng,
        )

        history.append(nxt)
        current = nxt

    assert len(history) == 12_002

    return tuple(history)


# ============================================================
# TRIGRAMAS
# ============================================================

def trigram_counter(history):
    assert len(history) >= 3

    return Counter(
        zip(
            history[:-2],
            history[1:-1],
            history[2:],
        )
    )


def trigram_distribution(history):
    counts = trigram_counter(
        history
    )

    total = sum(counts.values())

    expected = len(history) - 2

    assert total == expected

    vector = []

    for a in ALPHABET:
        for b in ALPHABET:
            for c in ALPHABET:
                vector.append(
                    counts.get(
                        (a, b, c),
                        0,
                    )
                    / total
                )

    assert len(vector) == 125

    return tuple(vector)


def window_distributions(test_history):
    distributions = []

    for w in range(N_WINDOWS):
        start = (
            w
            * WINDOW_TRANSITIONS
        )

        end = (
            start
            + WINDOW_TRANSITIONS
            + 2
        )

        segment = test_history[
            start:end
        ]

        assert len(segment) == 1_502

        q = trigram_distribution(
            segment
        )

        distributions.append(q)

    assert len(distributions) == 8

    return tuple(distributions)


# ============================================================
# A1 — CMI DE SEGUNDO ORDEN
# ============================================================

def conditional_mutual_information(
    history,
):
    """
    I(X[t-1]; X[t+1] | X[t])

    Estimador empirico plugin sin suavizado.
    Logaritmos naturales.
    """

    abc = trigram_counter(
        history
    )

    n = sum(abc.values())

    if n <= 0:
        raise ValueError(
            "trayectoria sin trigramas"
        )

    ab = Counter()
    bc = Counter()
    b_count = Counter()

    for (
        a,
        b,
        c,
    ), count in abc.items():
        ab[(a, b)] += count
        bc[(b, c)] += count
        b_count[b] += count

    value = 0.0

    for (
        a,
        b,
        c,
    ), count in abc.items():
        numerator = (
            count
            * b_count[b]
        )

        denominator = (
            ab[(a, b)]
            * bc[(b, c)]
        )

        if (
            numerator <= 0
            or denominator <= 0
        ):
            continue

        p_abc = count / n

        value += (
            p_abc
            * math.log(
                numerator
                / denominator
            )
        )

    # Protección únicamente frente a ruido flotante.
    if value < 0.0 and abs(value) < 1e-15:
        value = 0.0

    return value


def nearest_rank_percentile(
    values,
    q,
):
    values = sorted(values)

    if not values:
        raise ValueError(
            "percentile input vacio"
        )

    rank = math.ceil(
        q
        * len(values)
    )

    index = max(
        0,
        min(
            len(values) - 1,
            rank - 1,
        ),
    )

    return values[index]


# ============================================================
# JENSEN-SHANNON
# ============================================================

def kl_divergence(
    p,
    q,
):
    total = 0.0

    for a, b in zip(p, q):
        if a <= 0.0:
            continue

        if b <= 0.0:
            raise AssertionError(
                "KL con q=0 y p>0"
            )

        total += (
            a
            * math.log(a / b)
        )

    return total


def js_divergence(
    p,
    q,
):
    m = tuple(
        (a + b) / 2.0
        for a, b in zip(p, q)
    )

    return 0.5 * (
        kl_divergence(p, m)
        + kl_divergence(q, m)
    )


def compute_p_rel(
    observed_windows,
    surrogate_windows,
):
    within = []

    for i in range(N_WINDOWS):
        for j in range(
            i + 1,
            N_WINDOWS,
        ):
            within.append(
                js_divergence(
                    observed_windows[i],
                    observed_windows[j],
                )
            )

    d_within = median(
        within
    )

    null_distances = []

    for replicate_windows in surrogate_windows:
        assert len(
            replicate_windows
        ) == N_WINDOWS

        for w in range(
            N_WINDOWS
        ):
            null_distances.append(
                js_divergence(
                    observed_windows[w],
                    replicate_windows[w],
                )
            )

    d_null = median(
        null_distances
    )

    if d_null == 0.0:
        return {
            "p_rel": None,
            "d_within": d_within,
            "d_null": d_null,
            "evaluable": False,
        }

    p_rel = (
        1.0
        - d_within
        / d_null
    )

    return {
        "p_rel": p_rel,
        "d_within": d_within,
        "d_null": d_null,
        "evaluable": True,
    }


# ============================================================
# N — DIVERSIDAD HISTORICA
# ============================================================

def novelty_metrics(
    test_history,
):
    q = trigram_distribution(
        test_history
    )

    entropy = -sum(
        p * math.log(p)
        for p in q
        if p > 0.0
    )

    effective = math.exp(
        entropy
    )

    n_value = (
        effective
        / 125.0
    )

    coverage_count = sum(
        1
        for p in q
        if p > 0.0
    )

    c3 = (
        coverage_count
        / 125.0
    )

    return {
        "H3": entropy,
        "D3": effective,
        "N": n_value,
        "coverage_count": coverage_count,
        "C3": c3,
    }


# ============================================================
# U — APERIODICIDAD FINITA
# ============================================================

def aperiodicity_metrics(
    test_path,
):
    n = len(test_path)

    frequencies = Counter(
        test_path
    )

    marginal = {
        state: (
            frequencies.get(
                state,
                0,
            )
            / n
        )
        for state in ALPHABET
    }

    baseline = sum(
        p * p
        for p in marginal.values()
    )

    if baseline >= 1.0:
        return {
            "U": 0.0,
            "Q_period": 1.0,
            "p_star": 1,
            "baseline_B": baseline,
            "R_star": 1.0,
        }

    best_excess = -1.0
    best_lag = None
    best_recurrence = None

    upper = min(
        MAX_LAG,
        n - 1,
    )

    for p in range(
        1,
        upper + 1,
    ):
        comparisons = (
            n - p
        )

        matches = sum(
            1
            for t in range(
                p,
                n,
            )
            if test_path[t]
            == test_path[t - p]
        )

        recurrence = (
            matches
            / comparisons
        )

        excess = max(
            0.0,
            (
                recurrence
                - baseline
            )
            / (
                1.0
                - baseline
            ),
        )

        if excess > best_excess:
            best_excess = excess
            best_lag = p
            best_recurrence = (
                recurrence
            )

    q_period = best_excess

    u_value = (
        1.0
        - q_period
    )

    if abs(u_value) < 1e-15:
        u_value = 0.0

    return {
        "U": u_value,
        "Q_period": q_period,
        "p_star": best_lag,
        "baseline_B": baseline,
        "R_star": best_recurrence,
    }


# ============================================================
# METRICAS POR SEMILLA
# ============================================================

def compute_seed_metrics(
    label,
    seed,
    states,
    frozen_result,
):
    (
        train_path,
        test_history,
        test_path,
    ) = split_frozen_series(
        states
    )

    m1 = fit_m1(
        train_path
    )

    observed_i2 = (
        conditional_mutual_information(
            test_history
        )
    )

    observed_windows = (
        window_distributions(
            test_history
        )
    )

    null_i2 = []
    null_windows = []

    for replicate in range(
        NULL_REPLICATES
    ):
        surrogate = (
            generate_markov1_surrogate(
                m1,
                test_history,
                seed,
                replicate,
            )
        )

        null_i2.append(
            conditional_mutual_information(
                surrogate
            )
        )

        null_windows.append(
            window_distributions(
                surrogate
            )
        )

    i2_p95 = (
        nearest_rank_percentile(
            null_i2,
            0.95,
        )
    )

    a1 = (
        observed_i2
        - i2_p95
    )

    p_result = compute_p_rel(
        observed_windows,
        null_windows,
    )

    n_result = novelty_metrics(
        test_history
    )

    u_result = (
        aperiodicity_metrics(
            test_path
        )
    )

    result = {
        "label": label,
        "seed": seed,

        "series_sha256": (
            logical_series_sha256(
                states
            )
        ),

        "I2_observed": (
            observed_i2
        ),

        "I2_null_median": (
            median(null_i2)
        ),

        "I2_null_p95": (
            i2_p95
        ),

        "A1": a1,

        "A1_positive": (
            a1 > 0.0
        ),

        "P_rel": (
            p_result["p_rel"]
        ),

        "D_within": (
            p_result["d_within"]
        ),

        "D_null": (
            p_result["d_null"]
        ),

        "P_rel_evaluable": (
            p_result["evaluable"]
        ),

        "H3": (
            n_result["H3"]
        ),

        "D3": (
            n_result["D3"]
        ),

        "N": (
            n_result["N"]
        ),

        "C3": (
            n_result["C3"]
        ),

        "trigram_coverage": (
            n_result[
                "coverage_count"
            ]
        ),

        "U": (
            u_result["U"]
        ),

        "Q_period": (
            u_result[
                "Q_period"
            ]
        ),

        "p_star": (
            u_result["p_star"]
        ),

        "baseline_B": (
            u_result[
                "baseline_B"
            ]
        ),

        "R_star": (
            u_result["R_star"]
        ),

        # Se preservan, no se recalculan.
        "delta_hist_frozen": (
            frozen_result[
                "delta_hist"
            ]
        ),

        "c_hist_frozen": (
            frozen_result[
                "c_hist"
            ]
        ),

        "delta_hit_frozen": (
            frozen_result[
                "delta_hit"
            ]
        ),

        "c_hit_frozen": (
            frozen_result[
                "c_hit"
            ]
        ),

        # El nulo completo se conserva
        # para auditoría.
        "I2_null_values": tuple(
            null_i2
        ),
    }

    return result


# ============================================================
# RESUMEN / CALIBRACION
# ============================================================

def median_metric(
    results,
    name,
):
    values = [
        item[name]
        for item in results
    ]

    if any(
        value is None
        for value in values
    ):
        return None

    return median(values)


def summarize_condition(
    results,
):
    return {
        "A1_median": (
            median_metric(
                results,
                "A1",
            )
        ),

        "A1_positive_count": sum(
            1
            for item in results
            if item[
                "A1_positive"
            ]
        ),

        "P_rel_median": (
            median_metric(
                results,
                "P_rel",
            )
        ),

        "N_median": (
            median_metric(
                results,
                "N",
            )
        ),

        "U_median": (
            median_metric(
                results,
                "U",
            )
        ),

        "p_star_values": [
            item["p_star"]
            for item in results
        ],
    }


def calibration(
    d0_results,
    d1_results,
):
    d0 = summarize_condition(
        d0_results
    )

    d1 = summarize_condition(
        d1_results
    )

    if (
        d0["P_rel_median"] is None
        or d1["P_rel_median"] is None
    ):
        p_order = False
        t_p = None
    else:
        p_order = (
            d1["P_rel_median"]
            >
            d0["P_rel_median"]
        )

        t_p = (
            (
                d0["P_rel_median"]
                + d1["P_rel_median"]
            )
            / 2.0
            if p_order
            else None
        )

    n_order = (
        d0["N_median"]
        >
        d1["N_median"]
    )

    t_n = (
        (
            d0["N_median"]
            + d1["N_median"]
        )
        / 2.0
        if n_order
        else None
    )

    u_order = (
        d0["U_median"]
        >
        d1["U_median"]
    )

    t_u = (
        (
            d0["U_median"]
            + d1["U_median"]
        )
        / 2.0
        if u_order
        else None
    )

    # "sistematicamente" se interpreta
    # usando la regla congelada 7/8.
    d0_a1_systematic = (
        d0["A1_positive_count"]
        >= 7
    )

    d1_a1_pass = (
        d1["A1_positive_count"]
        >= 7
    )

    # D1 debe ser reconocido como
    # periodicidad exacta de periodo 25.
    d1_period_pass = all(
        item["U"] <= 1e-12
        and item["p_star"] == 25
        for item in d1_results
    )

    metrics_calibration_passed = all(
        (
            not d0_a1_systematic,
            d1_a1_pass,
            p_order,
            n_order,
            u_order,
            d1_period_pass,
        )
    )

    return {
        "D0": d0,
        "D1": d1,

        "D0_A1_systematic": (
            d0_a1_systematic
        ),

        "D1_A1_7of8": (
            d1_a1_pass
        ),

        "P_rel_order_pass": (
            p_order
        ),

        "N_order_pass": (
            n_order
        ),

        "U_order_pass": (
            u_order
        ),

        "D1_period25_pass": (
            d1_period_pass
        ),

        "T_P": t_p,
        "T_N": t_n,
        "T_U": t_u,

        "metrics_v1_calibration_passed": (
            metrics_calibration_passed
        ),
    }


# ============================================================
# IMPRESION
# ============================================================

def print_condition(
    label,
    results,
):
    print()
    print(label)
    print("-" * 108)

    for r in results:
        p_rel_text = (
            f"{r['P_rel']:+.6f}"
            if r["P_rel"] is not None
            else "NA"
        )

        print(
            f"seed={r['seed']:3d}  "
            f"A1={r['A1']:+.6f}  "
            f"I2={r['I2_observed']:.6f}  "
            f"I2_p95={r['I2_null_p95']:.6f}  "
            f"P_rel={p_rel_text:>9s}  "
            f"N={r['N']:.6f}  "
            f"U={r['U']:.6f}  "
            f"p*={r['p_star']}"
        )


def print_calibration(c):
    print()
    print("CALIBRACION D0 / D1")
    print("=" * 108)

    print(
        f"D0 A1 positivos:     "
        f"{c['D0']['A1_positive_count']}/8"
    )

    print(
        f"D1 A1 positivos:     "
        f"{c['D1']['A1_positive_count']}/8"
    )

    print()

    print(
        f"median P_rel D0:      "
        f"{c['D0']['P_rel_median']}"
    )

    print(
        f"median P_rel D1:      "
        f"{c['D1']['P_rel_median']}"
    )

    print(
        f"orden P_rel D1>D0:    "
        f"{'PASS' if c['P_rel_order_pass'] else 'FAIL'}"
    )

    print()

    print(
        f"median N D0:          "
        f"{c['D0']['N_median']:.6f}"
    )

    print(
        f"median N D1:          "
        f"{c['D1']['N_median']:.6f}"
    )

    print(
        f"orden N D0>D1:        "
        f"{'PASS' if c['N_order_pass'] else 'FAIL'}"
    )

    print()

    print(
        f"median U D0:          "
        f"{c['D0']['U_median']:.6f}"
    )

    print(
        f"median U D1:          "
        f"{c['D1']['U_median']:.6f}"
    )

    print(
        f"orden U D0>D1:        "
        f"{'PASS' if c['U_order_pass'] else 'FAIL'}"
    )

    print(
        f"D1 periodo 25:        "
        f"{'PASS' if c['D1_period25_pass'] else 'FAIL'}"
    )

    print()
    print("UMBRALES PARA D2")
    print("-" * 108)

    print(
        f"T_P = {c['T_P']}"
    )

    print(
        f"T_N = {c['T_N']}"
    )

    print(
        f"T_U = {c['T_U']}"
    )

    print()
    print(
        "RESULTADO FINAL: "
        + (
            "METRICS-v1 CALIBRATION PASS"
            if c[
                "metrics_v1_calibration_passed"
            ]
            else "METRICS-v1 CALIBRATION FAIL"
        )
    )


# ============================================================
# MAIN
# ============================================================

def main():
    print(
        "LAB-FEN-001 — CALIBRACION "
        "DE METRICAS FENOMENOLOGICAS v1"
    )

    print("=" * 108)

    required = (
        METRICS_SPEC,
        D0_JSON,
        D0_SERIES,
        D1_JSON,
        D1_SERIES,
    )

    for path in required:
        if not path.exists():
            raise FileNotFoundError(
                path
            )

    d0_payload = load_json(
        D0_JSON
    )

    d1_payload = load_json(
        D1_JSON
    )

    d0_series = load_series(
        D0_SERIES
    )

    d1_series = load_series(
        D1_SERIES
    )

    verify_frozen_dataset(
        "LAB-D0-v1",
        d0_payload,
        d0_series,
    )

    verify_frozen_dataset(
        "LAB-D1-v1",
        d1_payload,
        d1_series,
    )

    print()
    print("TRAZABILIDAD")
    print("-" * 108)

    print(
        f"metrics spec SHA256: "
        f"{file_sha256(METRICS_SPEC)}"
    )

    print(
        f"D0 results SHA256:   "
        f"{file_sha256(D0_JSON)}"
    )

    print(
        f"D0 series SHA256:    "
        f"{file_sha256(D0_SERIES)}"
    )

    print(
        f"D1 results SHA256:   "
        f"{file_sha256(D1_JSON)}"
    )

    print(
        f"D1 series SHA256:    "
        f"{file_sha256(D1_SERIES)}"
    )

    print()
    print(
        "SHA logico por semilla: PASS"
    )

    d0_index = result_index(
        d0_payload
    )

    d1_index = result_index(
        d1_payload
    )

    d0_results = []

    d1_results = []

    print()
    print(
        "Calculando 64 nulos Markov-1 "
        "por semilla y condicion..."
    )

    for seed in SEEDS:
        d0_results.append(
            compute_seed_metrics(
                "LAB-D0-v1",
                seed,
                d0_series[seed],
                d0_index[seed],
            )
        )

    for seed in SEEDS:
        d1_results.append(
            compute_seed_metrics(
                "LAB-D1-v1",
                seed,
                d1_series[seed],
                d1_index[seed],
            )
        )

    print_condition(
        "LAB-D0-v1",
        d0_results,
    )

    print_condition(
        "LAB-D1-v1",
        d1_results,
    )

    cal = calibration(
        d0_results,
        d1_results,
    )

    print_calibration(
        cal
    )

    output = {
        "version": VERSION,

        "contract": {
            "alphabet": ALPHABET,
            "seeds": SEEDS,
            "train_transitions": (
                TRAIN_TRANSITIONS
            ),
            "test_transitions": (
                TEST_TRANSITIONS
            ),
            "window_transitions": (
                WINDOW_TRANSITIONS
            ),
            "n_windows": N_WINDOWS,
            "alpha": ALPHA,
            "null_replicates": (
                NULL_REPLICATES
            ),
            "max_lag": MAX_LAG,
            "log_base": "e",
            "percentile_method": (
                "nearest-rank"
            ),
        },

        "trace": {
            "metrics_spec_sha256": (
                file_sha256(
                    METRICS_SPEC
                )
            ),

            "d0_results_sha256": (
                file_sha256(
                    D0_JSON
                )
            ),

            "d0_series_file_sha256": (
                file_sha256(
                    D0_SERIES
                )
            ),

            "d1_results_sha256": (
                file_sha256(
                    D1_JSON
                )
            ),

            "d1_series_file_sha256": (
                file_sha256(
                    D1_SERIES
                )
            ),
        },

        "D0_results": d0_results,
        "D1_results": d1_results,

        "calibration": cal,
    }

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_JSON.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as fh:
        json.dump(
            output,
            fh,
            ensure_ascii=False,
            indent=2,
        )
        fh.write("\n")

    print()
    print("SALIDA")
    print("=" * 108)

    print(OUTPUT_JSON)

    if not cal[
        "metrics_v1_calibration_passed"
    ]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()