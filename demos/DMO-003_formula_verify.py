from itertools import product


def proyectar(c):
    xp, xm, yp, ym, zp, zm = c
    return xp - xm, yp - ym, zp - zm


def exclusivo(c):
    xp, xm, yp, ym, zp, zm = c
    return (
        xp * xm == 0
        and yp * ym == 0
        and zp * zm == 0
    )


for m in range(1, 5):

    estados = list(
        product(range(m + 1), repeat=6)
    )

    fibras = {}

    for c in estados:
        v = proyectar(c)
        fibras.setdefault(v, []).append(c)

    assert len(estados) == (m + 1) ** 6
    assert len(fibras) == (2 * m + 1) ** 3

    # Fórmula exacta de las fibras.
    for (dx, dy, dz), preimagenes in fibras.items():

        esperado = (
            (m + 1 - abs(dx))
            * (m + 1 - abs(dy))
            * (m + 1 - abs(dz))
        )

        assert len(preimagenes) == esperado

    multiples = sum(
        len(preimagenes) > 1
        for preimagenes in fibras.values()
    )

    assert multiples == (2 * m + 1) ** 3 - 8

    exclusivos = [
        c for c in estados
        if exclusivo(c)
    ]

    fibras_exc = {}

    for c in exclusivos:
        v = proyectar(c)
        fibras_exc.setdefault(v, []).append(c)

    assert len(exclusivos) == (2 * m + 1) ** 3
    assert len(fibras_exc) == (2 * m + 1) ** 3

    assert all(
        len(preimagenes) == 1
        for preimagenes in fibras_exc.values()
    )

    print(
        f"m={m}: "
        f"estados={(m+1)**6}, "
        f"imagen={(2*m+1)**3}, "
        f"vectores_con_colision={multiples}, "
        f"exclusivos={len(exclusivos)}  OK"
    )


print()
print("TODAS LAS COMPROBACIONES DMO-003 PASARON.")
