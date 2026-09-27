from dataclasses import dataclass
from collections import defaultdict
from typing import Callable, Hashable, Iterable, Tuple


@dataclass(frozen=True)
class TranslationReport:
    source_size: int
    target_size: int
    image_size: int

    injective: bool
    surjective: bool
    bijective: bool

    collapsed_excess: int
    indistinguishable_pairs: int
    unreachable_targets: int

    fiber_sizes: Tuple[Tuple[Hashable, int], ...]


def analyse_translation(
    source: Iterable[Hashable],
    target: Iterable[Hashable],
    mapping: Callable[[Hashable], Hashable],
) -> TranslationReport:

    X = tuple(source)
    Y = tuple(target)

    if len(set(X)) != len(X):
        raise ValueError("source domain contains duplicates")

    if len(set(Y)) != len(Y):
        raise ValueError("target domain contains duplicates")

    Y_set = set(Y)

    fibers = defaultdict(list)

    for x in X:
        y = mapping(x)

        if y not in Y_set:
            raise ValueError(
                f"mapping sends {x!r} outside target domain: {y!r}"
            )

        fibers[y].append(x)

    image = set(fibers)

    injective = all(
        len(preimages) == 1
        for preimages in fibers.values()
    )

    surjective = (image == Y_set)
    bijective = injective and surjective

    # Cada elemento adicional dentro de una fibra representa
    # una distinción del dominio fuente que el destino ya no
    # puede recuperar únicamente a partir de T(x).
    collapsed_excess = sum(
        len(preimages) - 1
        for preimages in fibers.values()
    )

    indistinguishable_pairs = sum(
        len(preimages) * (len(preimages) - 1) // 2
        for preimages in fibers.values()
    )

    unreachable_targets = len(Y_set - image)

    fiber_sizes = tuple(
        sorted(
            (
                (y, len(fibers.get(y, ())))
                for y in Y
            ),
            key=lambda item: repr(item[0]),
        )
    )

    return TranslationReport(
        source_size=len(X),
        target_size=len(Y),
        image_size=len(image),
        injective=injective,
        surjective=surjective,
        bijective=bijective,
        collapsed_excess=collapsed_excess,
        indistinguishable_pairs=indistinguishable_pairs,
        unreachable_targets=unreachable_targets,
        fiber_sizes=fiber_sizes,
    )


def show(title, report):
    print(title)
    print("-" * 76)

    print(f"|X|:                  {report.source_size}")
    print(f"|Y|:                  {report.target_size}")
    print(f"|T(X)|:               {report.image_size}")

    print(f"inyectiva:            {report.injective}")
    print(f"sobreyectiva:         {report.surjective}")
    print(f"biyectiva:            {report.bijective}")

    print(
        f"exceso colapsado:      {report.collapsed_excess}"
    )
    print(
        f"pares indistinguibles: {report.indistinguishable_pairs}"
    )
    print(
        f"destinos no alcanzados:{report.unreachable_targets:2d}"
    )

    print("fibras:")
    for y, size in report.fiber_sizes:
        print(f"  {y!r}: {size}")

    print()


print("DMO-006 — CONTABILIDAD DE TRADUCCION ENTRE LECTURAS")
print("=" * 76)
print()


# ============================================================
# CASO 1
# Cambio de lectura biyectivo.
#
# Mismo número de estados y correspondencia uno-a-uno.
# No se pierde ninguna distinción y todo destino es alcanzable.
# ============================================================

X1 = (0, 1, 2, 3)
Y1 = ("a", "b", "c", "d")

table1 = {
    0: "d",
    1: "c",
    2: "b",
    3: "a",
}

r1 = analyse_translation(
    X1,
    Y1,
    lambda x: table1[x],
)

show(
    "CASO 1 — RELABELING BIYECTIVO",
    r1,
)

assert r1.injective
assert r1.surjective
assert r1.bijective
assert r1.collapsed_excess == 0
assert r1.unreachable_targets == 0


# ============================================================
# CASO 2
# Coarse-graining.
#
# Cuatro estados fuente se traducen a dos clases.
# Diferentes estados fuente quedan identificados.
# ============================================================

X2 = (0, 1, 2, 3)
Y2 = ("par", "impar")

r2 = analyse_translation(
    X2,
    Y2,
    lambda x: "par" if x % 2 == 0 else "impar",
)

show(
    "CASO 2 — TRADUCCION CON PERDIDA",
    r2,
)

assert not r2.injective
assert r2.surjective
assert not r2.bijective

assert r2.image_size == 2
assert r2.collapsed_excess == 2
assert r2.unreachable_targets == 0


# ============================================================
# CASO 3
# Enriquecimiento representacional derivado.
#
# Se añade una segunda coordenada, pero dicha coordenada
# está completamente determinada por x.
#
# No aparece información independiente nueva.
# ============================================================

X3 = (0, 1, 2, 3)

Y3 = tuple(
    (x, parity)
    for x in X3
    for parity in (0, 1)
)

r3 = analyse_translation(
    X3,
    Y3,
    lambda x: (x, x % 2),
)

show(
    "CASO 3 — GANANCIA DE REPRESENTACION DERIVADA",
    r3,
)

assert r3.injective
assert not r3.surjective
assert not r3.bijective

assert r3.collapsed_excess == 0
assert r3.unreachable_targets == 4


# ============================================================
# CASO 4
# Proyección de canales opuestos.
#
# Versión mínima 1D de la estructura usada en DMO-003:
#
#     T(a,b) = a-b
#
# Con coexistencia de canales opuestos aparecen colisiones.
# ============================================================

X4 = tuple(
    (a, b)
    for a in (0, 1)
    for b in (0, 1)
)

Y4 = (-1, 0, 1)

r4 = analyse_translation(
    X4,
    Y4,
    lambda pair: pair[0] - pair[1],
)

show(
    "CASO 4 — PROYECCION DE CANALES OPUESTOS",
    r4,
)

assert not r4.injective
assert r4.surjective
assert not r4.bijective

assert r4.source_size == 4
assert r4.image_size == 3
assert r4.collapsed_excess == 1


# ============================================================
# CASO 5
# Misma proyección, restringida a exclusividad.
#
# Cada valor neto tiene representación única.
# ============================================================

X5 = (
    (0, 0),
    (1, 0),
    (0, 1),
)

Y5 = (-1, 0, 1)

r5 = analyse_translation(
    X5,
    Y5,
    lambda pair: pair[0] - pair[1],
)

show(
    "CASO 5 — CANALES BAJO EXCLUSIVIDAD",
    r5,
)

assert r5.injective
assert r5.surjective
assert r5.bijective

assert r5.collapsed_excess == 0
assert r5.unreachable_targets == 0


# ============================================================
# CASO 6
# Fibra de tamaño 3.
#
# Permite distinguir:
#
#   exceso colapsado = 3 - 1 = 2
#
# de:
#
#   pares indistinguibles = C(3,2) = 3
#
# ============================================================

X6 = (0, 1, 2)
Y6 = ("unica_clase",)

r6 = analyse_translation(
    X6,
    Y6,
    lambda x: "unica_clase",
)

show(
    "CASO 6 — FIBRA DE TAMANO TRES",
    r6,
)

assert not r6.injective
assert r6.surjective
assert not r6.bijective

assert r6.image_size == 1
assert r6.collapsed_excess == 2
assert r6.indistinguishable_pairs == 3
assert r6.unreachable_targets == 0


# ============================================================
# IDENTIDADES FINITAS
# ============================================================

print("IDENTIDADES DE CONTROL")
print("=" * 76)

for name, r in (
    ("R1", r1),
    ("R2", r2),
    ("R3", r3),
    ("R4", r4),
    ("R5", r5),
    ("R6", r6),
):
    # En un mapa finito:
    #
    # exceso colapsado = |X| - |imagen|
    #
    # porque cada fibra de tamaño n aporta n-1 colisiones.
    assert (
        r.collapsed_excess
        ==
        r.source_size - r.image_size
    )

    assert (
        r.unreachable_targets
        ==
        r.target_size - r.image_size
    )

    assert (
        r.bijective
        ==
        (
            r.collapsed_excess == 0
            and r.unreachable_targets == 0
        )
    )

    print(
        f"{name}: "
        "|X|-|imagen| = exceso colapsado, "
        "|Y|-|imagen| = no alcanzados   OK"
    )


print()
print("CLASIFICACION")
print("=" * 76)

print(
    "Caso 1: equivalencia exacta por biyeccion."
)

print(
    "Caso 2: traduccion con perdida de distinciones."
)

print(
    "Caso 3: embedding fiel con nueva coordenada derivada; "
    "no hay informacion independiente creada."
)

print(
    "Caso 4: proyeccion no inyectiva; estados fuente distintos "
    "se vuelven indistinguibles."
)

print(
    "Caso 5: la restriccion de dominio elimina la perdida y "
    "restaura una biyeccion."
)


print(
    "Caso 6: una fibra de tamano tres separa exceso colapsado "
    "de numero de pares indistinguibles."
)

print()
print("RESULTADO DMO-006")
print("=" * 76)

print(
    "Una traduccion no debe identificarse automaticamente "
    "con una equivalencia."
)

print(
    "En dominios finitos, la perdida de distinciones queda "
    "detectada por la no inyectividad y los estados destino "
    "no alcanzados por la no sobreyectividad."
)

print(
    "La equivalencia exacta como conjuntos entre los dominios declarados requiere biyeccion."
)

print(
    "Una representacion puede añadir descriptores derivados "
    "sin añadir informacion independiente."
)

print()
print(
    "La demo es metodologica e interna. "
    "No establece equivalencia fisica entre niveles."
)