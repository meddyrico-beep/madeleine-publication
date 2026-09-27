from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Reading:
    name: str

    # Criterios con los que se construye la firma.
    metric_schema: Tuple[str, ...]

    # Escala declarada de lectura.
    window_size: int
    history_depth: int

    # Protocolo usado para decidir régimen.
    regime_gate_version: str

    # Campos mínimos de trazabilidad.
    trace_schema: Tuple[str, ...]

    # Valores de la firma.
    values: Tuple[float, ...]


@dataclass(frozen=True)
class ComparisonResult:
    comparable: bool
    failures: Tuple[str, ...]
    differences: Tuple[Tuple[str, float], ...]


def validate_reading(r: Reading):
    failures = []

    if len(r.metric_schema) == 0:
        failures.append("metric_schema_empty")

    if len(r.metric_schema) != len(r.values):
        failures.append("metric_value_dimension_mismatch")

    if r.window_size <= 0:
        failures.append("invalid_window_size")

    if r.history_depth < 0:
        failures.append("invalid_history_depth")

    if not r.regime_gate_version.strip():
        failures.append("missing_regime_gate")

    if len(r.trace_schema) == 0:
        failures.append("missing_trace_schema")

    return tuple(failures)


def compare(a: Reading, b: Reading) -> ComparisonResult:
    failures = []

    failures.extend(
        f"A:{x}"
        for x in validate_reading(a)
    )

    failures.extend(
        f"B:{x}"
        for x in validate_reading(b)
    )

    # 1. Criterios comunes.
    if a.metric_schema != b.metric_schema:
        failures.append("different_metric_schema")

    # 2. Misma escala de lectura.
    if a.window_size != b.window_size:
        failures.append("different_window_size")

    if a.history_depth != b.history_depth:
        failures.append("different_history_depth")

    # 3. Mismo criterio de régimen.
    if a.regime_gate_version != b.regime_gate_version:
        failures.append("different_regime_gate")

    # 4. Trazabilidad comparable.
    if a.trace_schema != b.trace_schema:
        failures.append("different_trace_schema")

    comparable = (len(failures) == 0)

    differences = ()

    if comparable:
        differences = tuple(
            (metric, vb - va)
            for metric, va, vb
            in zip(a.metric_schema, a.values, b.values)
        )

    return ComparisonResult(
        comparable=comparable,
        failures=tuple(failures),
        differences=differences,
    )


def report(title, a, b):
    result = compare(a, b)

    print(title)
    print("-" * 74)

    print(f"A: {a.name}")
    print(f"B: {b.name}")

    if result.comparable:
        print("COMPARABLE: SI")
        print("Diferencias B - A:")

        for metric, delta in result.differences:
            print(f"  {metric:10s} {delta:+.3f}")
    else:
        print("COMPARABLE: NO")
        print("Razones:")

        for failure in result.failures:
            print(f"  - {failure}")

    print()

    return result


METRICS = (
    "A0",
    "A1",
    "P_rel",
    "N",
    "U",
)

TRACE = (
    "rule_version",
    "seed",
    "parameters",
    "window",
    "series_hash",
)


base = Reading(
    name="lectura_A",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.70, 0.10, 0.82, 0.35, 0.18),
)


same_contract = Reading(
    name="lectura_B",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.62, 0.28, 0.75, 0.58, 0.44),
)


different_scale = Reading(
    name="lectura_C_escala_distinta",
    metric_schema=METRICS,
    window_size=512,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.62, 0.28, 0.75, 0.58, 0.44),
)


different_metrics = Reading(
    name="lectura_D_firma_distinta",
    metric_schema=("A0", "P_rel", "N", "U"),
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.62, 0.75, 0.58, 0.44),
)


different_trace = Reading(
    name="lectura_E_traza_distinta",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=(
        "rule_version",
        "seed",
        "parameters",
    ),
    values=(0.62, 0.28, 0.75, 0.58, 0.44),
)


different_gate = Reading(
    name="lectura_F_gate_distinto",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="otro-gate",
    trace_schema=TRACE,
    values=(0.62, 0.28, 0.75, 0.58, 0.44),
)


print("DMO-005 — GATE DE COMPARABILIDAD ENTRE LECTURAS")
print("=" * 74)
print()


r1 = report(
    "CASO 1 — MISMO CONTRATO DE LECTURA",
    base,
    same_contract,
)

assert r1.comparable
assert len(r1.failures) == 0
assert len(r1.differences) == len(METRICS)


r2 = report(
    "CASO 2 — ESCALA DISTINTA",
    base,
    different_scale,
)

assert not r2.comparable
assert "different_window_size" in r2.failures


r3 = report(
    "CASO 3 — FIRMA DISTINTA",
    base,
    different_metrics,
)

assert not r3.comparable
assert "different_metric_schema" in r3.failures


r4 = report(
    "CASO 4 — TRAZABILIDAD DISTINTA",
    base,
    different_trace,
)

assert not r4.comparable
assert "different_trace_schema" in r4.failures


r5 = report(
    "CASO 5 — CRITERIO DE REGIMEN DISTINTO",
    base,
    different_gate,
)

assert not r5.comparable
assert "different_regime_gate" in r5.failures


print("PRUEBA DE SIMETRIA")
print("=" * 74)

ab = compare(base, same_contract)
ba = compare(same_contract, base)

assert ab.comparable == ba.comparable

for (_, dab), (_, dba) in zip(
    ab.differences,
    ba.differences,
):
    assert abs(dab + dba) < 1e-12

print("comparabilidad(A,B) = comparabilidad(B,A)  OK")
print("delta(B-A) = -delta(A-B)                  OK")


print()
print("RESULTADO DMO-005")
print("=" * 74)

print(
    "Dos firmas solo se comparan componente a componente "
    "cuando comparten esquema, escala, criterio de regimen "
    "y trazabilidad."
)

print(
    "Si una de esas condiciones cambia, la demo rechaza "
    "la comparacion directa en lugar de producir una "
    "diferencia numerica engañosa."
)

print()
print(
    "La demo formaliza comparabilidad metodologica interna."
)
print(
    "No demuestra que las metricas elegidas sean universales "
    "ni que dos sistemas fisicos sean equivalentes."
)

print()
print("PRUEBAS FORMALES DE LA RELACION DE COMPARABILIDAD")
print("=" * 74)


# Reflexividad
aa = compare(base, base)

assert aa.comparable

print("reflexividad: comparabilidad(A,A) = True       OK")


# Simetría ya comprobada arriba, se reafirma aquí.
ab = compare(base, same_contract)
ba = compare(same_contract, base)

assert ab.comparable == ba.comparable

print("simetria: comparabilidad(A,B) = comparabilidad(B,A)  OK")


# Tercer elemento con exactamente el mismo contrato.
third_same_contract = Reading(
    name="lectura_G",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.80, 0.15, 0.69, 0.41, 0.52),
)

bc = compare(same_contract, third_same_contract)
ac = compare(base, third_same_contract)

assert ab.comparable
assert bc.comparable
assert ac.comparable

print(
    "transitividad: A~B y B~C implica A~C             OK"
)


# Profundidad histórica como parte de la escala.
different_history_depth = Reading(
    name="lectura_H_profundidad_distinta",
    metric_schema=METRICS,
    window_size=256,
    history_depth=3,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.62, 0.28, 0.75, 0.58, 0.44),
)

rh = compare(base, different_history_depth)

assert not rh.comparable
assert "different_history_depth" in rh.failures

print(
    "history_depth distinto bloquea comparacion directa  OK"
)


# Una lectura internamente mal formada tampoco es comparable.
invalid_dimension = Reading(
    name="lectura_I_dimension_invalida",
    metric_schema=METRICS,
    window_size=256,
    history_depth=2,
    regime_gate_version="DMO-004-v1",
    trace_schema=TRACE,
    values=(0.62, 0.28),
)

ri = compare(base, invalid_dimension)

assert not ri.comparable
assert "B:metric_value_dimension_mismatch" in ri.failures

print(
    "firma internamente inconsistente es rechazada       OK"
)


print()
print("CONCLUSION FORMAL")
print("=" * 74)
print(
    "Sobre lecturas validas, compartir exactamente el mismo "
    "contrato de lectura define una relacion reflexiva, "
    "simetrica y transitiva."
)
print(
    "La comparacion numerica de las firmas solo se habilita "
    "dentro de una misma clase de comparabilidad."
)