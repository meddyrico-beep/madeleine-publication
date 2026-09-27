from dataclasses import dataclass, replace
from itertools import product


@dataclass(frozen=True)
class RegimeEvidence:
    """
    Evidencia mínima para que una candidata pueda cruzar
    el gate de aceptación como régimen interno.
    """

    region_parametric: bool
    seed_agreement: bool
    null_separation: bool
    explicit_failure_criterion: bool
    non_reducible: bool

    # Requisitos de procedencia / reproducibilidad.
    frozen_rule: bool
    complete_trace: bool


HARD_CRITERIA = (
    "region_parametric",
    "seed_agreement",
    "null_separation",
    "explicit_failure_criterion",
    "non_reducible",
    "frozen_rule",
    "complete_trace",
)


@dataclass(frozen=True)
class GateResult:
    accepted: bool
    failures: tuple[str, ...]


def evaluate(evidence: RegimeEvidence) -> GateResult:
    failures = tuple(
        criterion
        for criterion in HARD_CRITERIA
        if not getattr(evidence, criterion)
    )

    return GateResult(
        accepted=(len(failures) == 0),
        failures=failures,
    )


def show_case(name: str, evidence: RegimeEvidence) -> GateResult:
    result = evaluate(evidence)

    print(name)
    print("-" * 72)

    for criterion in HARD_CRITERIA:
        value = getattr(evidence, criterion)
        print(
            f"{criterion:28s} "
            f"{'PASS' if value else 'FAIL'}"
        )

    print()

    if result.accepted:
        print("GATE: ACCEPTED_AS_REGIME")
        print("fallos: NINGUNO")
    else:
        print("GATE: NOT_ACCEPTED_AS_REGIME")
        print("fallos:")
        for failure in result.failures:
            print(f"  - {failure}")

    print()

    return result


print("DMO-004 — GATE DURO DE ACEPTACION DE REGIMEN")
print("=" * 72)
print()


# ------------------------------------------------------------
# Caso base: todas las condiciones declaradas se satisfacen.
# ------------------------------------------------------------

valid = RegimeEvidence(
    region_parametric=True,
    seed_agreement=True,
    null_separation=True,
    explicit_failure_criterion=True,
    non_reducible=True,
    frozen_rule=True,
    complete_trace=True,
)

result_valid = show_case(
    "CASO 1 — CANDIDATA QUE SUPERA TODO EL GATE",
    valid,
)

assert result_valid.accepted
assert result_valid.failures == ()


# ------------------------------------------------------------
# Prueba de necesidad de cada cláusula.
#
# Se apaga una condición cada vez.
# Ninguna debe poder eliminarse sin cambiar la aceptación.
# ------------------------------------------------------------

print("PRUEBA DE NECESIDAD DE CADA CRITERIO")
print("=" * 72)
print()

for criterion in HARD_CRITERIA:
    broken = replace(
        valid,
        **{criterion: False},
    )

    result = evaluate(broken)

    assert not result.accepted
    assert criterion in result.failures

    print(
        f"apagar {criterion:28s} "
        f"-> NOT_ACCEPTED_AS_REGIME  OK"
    )


# ------------------------------------------------------------
# Barrido exhaustivo del espacio booleano.
#
# Hay 2^7 = 128 combinaciones posibles.
# Como las siete condiciones son obligatorias,
# solo una combinación puede cruzar el gate.
# ------------------------------------------------------------

print()
print("BARRIDO EXHAUSTIVO")
print("=" * 72)
print()

accepted = []
rejected = []

for values in product((False, True), repeat=len(HARD_CRITERIA)):
    evidence = RegimeEvidence(
        **dict(zip(HARD_CRITERIA, values))
    )

    result = evaluate(evidence)

    if result.accepted:
        accepted.append(evidence)
    else:
        rejected.append((evidence, result.failures))


total = len(accepted) + len(rejected)

print(f"Configuraciones totales: {total}")
print(f"Aceptadas:              {len(accepted)}")
print(f"No aceptadas:           {len(rejected)}")

assert total == 2 ** len(HARD_CRITERIA)
assert len(accepted) == 1
assert len(rejected) == total - 1
assert accepted[0] == valid


# ------------------------------------------------------------
# Casos límite explícitos.
# ------------------------------------------------------------

print()
print("CASOS LIMITE")
print("=" * 72)
print()

cases = {
    "sin_region": replace(
        valid,
        region_parametric=False,
    ),
    "dependiente_de_semilla": replace(
        valid,
        seed_agreement=False,
    ),
    "no_supera_nulos": replace(
        valid,
        null_separation=False,
    ),
    "sin_criterio_de_fallo": replace(
        valid,
        explicit_failure_criterion=False,
    ),
    "reducible_a_otro_regimen": replace(
        valid,
        non_reducible=False,
    ),
    "regla_no_congelada": replace(
        valid,
        frozen_rule=False,
    ),
    "traza_incompleta": replace(
        valid,
        complete_trace=False,
    ),
}

for name, evidence in cases.items():
    result = evaluate(evidence)

    assert not result.accepted

    print(
        f"{name:30s} "
        f"FAIL ({', '.join(result.failures)})"
    )


print()
print("RESULTADO DMO-004")
print("=" * 72)
print(
    "El gate es determinista y auditado exhaustivamente:"
)
print(
    "una candidata solo es aceptada si satisface "
    "simultaneamente todas las condiciones declaradas."
)
print()
print(
    "Ninguna clausula es redundante dentro de esta "
    "definicion: apagar una sola condicion cambia "
    "la salida de ACCEPTED a NOT_ACCEPTED."
)
print()
print(
    "Esta demo formaliza un criterio metodologico interno."
)
print(
    "No valida por si sola ningun regimen fenomenologico "
    "ni constituye evidencia fisica externa."
)