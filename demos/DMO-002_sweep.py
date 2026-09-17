from collections import Counter, defaultdict
from itertools import product
from math import log2


MAX_POS = 4
MIN_N = 1
MAX_N = 6


def delta(historia):
    return sum(abs(b - a) for a, b in zip(historia, historia[1:]))


def entropy(counter):
    total = sum(counter.values())
    h = 0.0

    for count in counter.values():
        p = count / total
        h -= p * log2(p)

    return h


historias = []

for n in range(MIN_N, MAX_N + 1):
    for resto in product(range(MAX_POS + 1), repeat=n):
        h = (0,) + resto
        d = delta(h)
        historias.append((h, n, d))


N = len(historias)

count_n = Counter(n for _, n, _ in historias)
count_delta = Counter(d for _, _, d in historias)
count_pair = Counter((n, d) for _, n, d in historias)

deltas_por_n = defaultdict(set)
ns_por_delta = defaultdict(set)

for _, n, d in historias:
    deltas_por_n[n].add(d)
    ns_por_delta[d].add(n)


# Entropías bajo distribución uniforme sobre las historias enumeradas.
H_n = entropy(count_n)
H_delta = entropy(count_delta)
H_pair = entropy(count_pair)

H_delta_given_n = H_pair - H_n
H_n_given_delta = H_pair - H_delta


print("DMO-002 — BARRIDO EXHAUSTIVO")
print("=" * 60)
print()
print(f"Dominio de posiciones: 0..{MAX_POS}")
print(f"Transiciones n: {MIN_N}..{MAX_N}")
print(f"Historias totales: {N}")
print()

print("CARDINALIDADES OBSERVADAS")
print("-" * 60)
print(f"Valores distintos de n:             {len(count_n)}")
print(f"Valores distintos de delta:         {len(count_delta)}")
print(f"Pares distintos (n, delta):         {len(count_pair)}")
print()

print("DELTA POSIBLES PARA CADA n")
print("-" * 60)

for n in sorted(deltas_por_n):
    valores = sorted(deltas_por_n[n])
    print(
        f"n={n}: {len(valores):>3} valores distintos de delta "
        f"[{min(valores)}, {max(valores)}]"
    )

print()
print("n POSIBLES PARA CADA delta")
print("-" * 60)

multi_n = {
    d: sorted(ns)
    for d, ns in ns_por_delta.items()
    if len(ns) > 1
}

for d in sorted(multi_n):
    print(f"delta={d:>2}: n={multi_n[d]}")

print()
print("PRUEBAS DE NO DETERMINACION")
print("-" * 60)

violacion_n_a_delta = any(
    len(ds) > 1
    for ds in deltas_por_n.values()
)

violacion_delta_a_n = any(
    len(ns) > 1
    for ns in ns_por_delta.values()
)

assert violacion_n_a_delta
assert violacion_delta_a_n

print(
    "n -> delta: FALSA como determinacion funcional "
    "en el dominio."
)
print(
    "delta -> n: FALSA como determinacion funcional "
    "en el dominio."
)

print()
print("ENTROPIAS")
print("-" * 60)
print(f"H(n)               = {H_n:.6f} bits")
print(f"H(delta)           = {H_delta:.6f} bits")
print(f"H(n, delta)        = {H_pair:.6f} bits")
print(f"H(delta | n)       = {H_delta_given_n:.6f} bits")
print(f"H(n | delta)       = {H_n_given_delta:.6f} bits")

assert H_delta_given_n > 0
assert H_n_given_delta > 0

print()
print("LECTURA")
print("-" * 60)
print(
    "H(delta | n) > 0: conocer el conteo no elimina "
    "la incertidumbre sobre la medida."
)
print(
    "H(n | delta) > 0: conocer la medida no elimina "
    "la incertidumbre sobre el conteo."
)

print()
print("PODER DISCRIMINANTE")
print("-" * 60)
print(f"Clases usando solo n:             {len(count_n)}")
print(f"Clases usando solo delta:         {len(count_delta)}")
print(f"Clases usando el par (n, delta):  {len(count_pair)}")

assert len(count_pair) > len(count_n)
assert len(count_pair) > len(count_delta)

print()
print(
    "El par (n, delta) separa más clases de historias "
    "que cualquiera de las dos coordenadas aisladas."
)

print()
print("LIMITACION")
print("-" * 60)
print(
    "El resultado es exhaustivo para este dominio finito, "
    "no universal para toda nocion posible de contar o medir."
)
print(
    "Tampoco afirma que (n, delta) identifique completamente "
    "cada historia: distintas historias pueden compartir el mismo par."
)
