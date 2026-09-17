from itertools import product


def proyectar(c):
    xp, xm, yp, ym, zp, zm = c
    return (
        xp - xm,
        yp - ym,
        zp - zm,
    )


def exclusivo(c):
    xp, xm, yp, ym, zp, zm = c
    return (
        xp * xm == 0
        and yp * ym == 0
        and zp * zm == 0
    )


MAX_CANAL = 2

estados = list(
    product(range(MAX_CANAL + 1), repeat=6)
)

grupos = {}

for c in estados:
    v = proyectar(c)
    grupos.setdefault(v, []).append(c)


colisiones = {
    v: cs
    for v, cs in grupos.items()
    if len(cs) > 1
}


print("DMO-003 — plano carlesino vs proyeccion cartesiana")
print("=" * 66)
print()
print(f"Estados carlesinos enumerados: {len(estados)}")
print(f"Vectores cartesianos obtenidos: {len(grupos)}")
print(f"Vectores con multiples preimagenes: {len(colisiones)}")

print()
print("EJEMPLO DE PERDIDA DE INFORMACION")
print("-" * 66)

a = (1, 0, 0, 0, 0, 0)
b = (2, 1, 0, 0, 0, 0)

assert a != b
assert proyectar(a) == proyectar(b)

print(f"a = {a}")
print(f"b = {b}")
print(f"P(a) = P(b) = {proyectar(a)}")
print()
print(
    "Dos estados distintos de seis canales producen "
    "la misma lectura cartesiana."
)


# Ahora restringimos a estados de canales opuestos exclusivos.
estados_exclusivos = [
    c for c in estados
    if exclusivo(c)
]

grupos_exclusivos = {}

for c in estados_exclusivos:
    v = proyectar(c)
    grupos_exclusivos.setdefault(v, []).append(c)


colisiones_exclusivas = {
    v: cs
    for v, cs in grupos_exclusivos.items()
    if len(cs) > 1
}


print()
print("REGIMEN DE EXCLUSIVIDAD")
print("-" * 66)
print(f"Estados exclusivos: {len(estados_exclusivos)}")
print(
    "Colisiones entre estados exclusivos: "
    f"{len(colisiones_exclusivas)}"
)

assert len(colisiones_exclusivas) == 0


print()
print("RESULTADO")
print("-" * 66)
print(
    "Sin exclusividad de canales opuestos, "
    "la proyeccion cartesiana no es inyectiva."
)
print(
    "Por tanto, una representacion de seis canales puede "
    "conservar informacion que (x,y,z) pierde."
)

print()
print(
    "Con exclusividad de canales opuestos, "
    "la proyeccion es inyectiva en el dominio enumerado."
)
print(
    "En ese regimen, los seis canales funcionan como "
    "una codificacion signo-magnitud del vector cartesiano."
)

print()
print("LIMITACION")
print("-" * 66)
print(
    "La demo no demuestra por si sola una geometria nueva."
)
print(
    "Demuestra exactamente que la no-equivalencia depende "
    "de que el estado de canales contenga estructura adicional "
    "que no sea eliminada por restricciones de exclusividad."
)
