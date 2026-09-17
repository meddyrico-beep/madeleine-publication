from itertools import product


def delta(historia):
    return sum(abs(b - a) for a, b in zip(historia, historia[1:]))


def medidas_observadas(m, n):
    valores = set()

    for resto in product(range(m + 1), repeat=n):
        h = (0,) + resto
        valores.add(delta(h))

    return valores


print("DMO-002 — verificacion de la formula |Delta_n| = m*n + 1")
print("=" * 68)

for m in range(1, 6):
    for n in range(1, 6):
        observadas = medidas_observadas(m, n)
        esperadas = set(range(m * n + 1))

        assert observadas == esperadas
        assert len(observadas) == m * n + 1

        print(
            f"m={m}, n={n}: "
            f"|Delta|={len(observadas):>3} "
            f"esperado={m*n+1:>3}  OK"
        )

print()
print("TODAS LAS COMPROBACIONES PASARON.")
