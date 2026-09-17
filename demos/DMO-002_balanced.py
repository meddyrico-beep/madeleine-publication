from collections import defaultdict
from itertools import product
from math import log2

MAX_POS = 4
MIN_N = 1
MAX_N = 6

NS = list(range(MIN_N, MAX_N + 1))
P_N = 1.0 / len(NS)


def delta(historia):
    return sum(abs(b - a) for a, b in zip(historia, historia[1:]))


def entropy(dist):
    return -sum(
        p * log2(p)
        for p in dist.values()
        if p > 0
    )


p_n = defaultdict(float)
p_delta = defaultdict(float)
p_pair = defaultdict(float)

total_historias = 0

for n in NS:
    historias_n = 5 ** n

    # Cada valor de n recibe el mismo peso total.
    # Dentro de cada n, todas las historias reciben igual peso.
    peso_historia = P_N / historias_n

    for resto in product(range(MAX_POS + 1), repeat=n):
        h = (0,) + resto
        d = delta(h)

        p_n[n] += peso_historia
        p_delta[d] += peso_historia
        p_pair[(n, d)] += peso_historia

        total_historias += 1


H_n = entropy(p_n)
H_delta = entropy(p_delta)
H_pair = entropy(p_pair)

H_delta_given_n = H_pair - H_n
H_n_given_delta = H_pair - H_delta


print("DMO-002 — DISTRIBUCION EQUILIBRADA POR n")
print("=" * 62)
print()
print(f"Historias enumeradas: {total_historias}")
print(f"Valores de n: {len(p_n)}")
print(f"Valores de delta: {len(p_delta)}")
print(f"Pares (n, delta): {len(p_pair)}")

print()
print("PESO TOTAL POR n")
print("-" * 62)

for n in sorted(p_n):
    print(f"n={n}: {p_n[n]:.12f}")

# Debe ser uniforme.
for n in NS:
    assert abs(p_n[n] - P_N) < 1e-12


print()
print("ENTROPIAS EQUILIBRADAS")
print("-" * 62)
print(f"H(n)               = {H_n:.6f} bits")
print(f"H(delta)           = {H_delta:.6f} bits")
print(f"H(n, delta)        = {H_pair:.6f} bits")
print(f"H(delta | n)       = {H_delta_given_n:.6f} bits")
print(f"H(n | delta)       = {H_n_given_delta:.6f} bits")

assert H_delta_given_n > 0
assert H_n_given_delta > 0


print()
print("PRUEBA DE ROBUSTEZ")
print("-" * 62)

print(
    "H(delta | n) > 0: incluso equilibrando el peso de cada n, "
    "el conteo no determina la medida."
)

print(
    "H(n | delta) > 0: incluso equilibrando el peso de cada n, "
    "la medida no determina el conteo."
)

print()
print("RESULTADO")
print("-" * 62)

print(
    "La no-redundancia informacional sobrevive al eliminar "
    "el sesgo combinatorio hacia historias largas."
)

print()
print("LIMITACION")
print("-" * 62)

print(
    "La distribucion sigue siendo una eleccion operacional: "
    "n es uniforme y, condicionado a n, las historias son uniformes."
)

print(
    "El resultado prueba robustez frente al sesgo por longitud, "
    "no una irreductibilidad universal de contar y medir."
)
