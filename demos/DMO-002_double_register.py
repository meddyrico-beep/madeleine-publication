from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Registro:
    nombre: str
    historia: tuple[float, ...]
    n: int
    delta: float


def medir(nombre: str, historia: Sequence[float]) -> Registro:
    """
    Operacionalización mínima para DMO-002.

    n:
        número de transiciones entre marcas sucesivas.

    delta:
        medida acumulada de trayectoria:
        suma de |x[i+1] - x[i]|.
    """
    h = tuple(float(x) for x in historia)

    if len(h) < 2:
        raise ValueError("Una historia necesita al menos dos marcas.")

    n = len(h) - 1
    delta = sum(abs(b - a) for a, b in zip(h, h[1:]))

    return Registro(nombre, h, n, delta)


casos = [
    # Mismo conteo, distinta medida.
    medir("A", [0, 1, 2]),       # (n=2, delta=2)
    medir("B", [0, 2, 0]),       # (n=2, delta=4)

    # Misma medida, distinto conteo.
    medir("C", [0, 4]),          # (n=1, delta=4)
    medir("D", [0, 1, 2, 3, 4]) # (n=4, delta=4)
]


print("DMO-002 — doble registro conteo/medida")
print()
print(f"{'Caso':<6} {'Historia':<28} {'n':>4} {'delta':>10}")
print("-" * 54)

for r in casos:
    print(f"{r.nombre:<6} {str(r.historia):<28} {r.n:>4} {r.delta:>10.3f}")


A, B, C, D = casos

# Prueba 1:
# n no determina delta.
assert A.n == B.n
assert A.delta != B.delta

# Prueba 2:
# delta no determina n.
assert C.delta == D.delta
assert C.n != D.n


print()
print("PRUEBA 1")
print(
    f"A y B tienen el mismo conteo n={A.n}, "
    f"pero medidas distintas: {A.delta} != {B.delta}."
)
print("Resultado: n no determina delta en este dominio.")

print()
print("PRUEBA 2")
print(
    f"C y D tienen la misma medida delta={C.delta}, "
    f"pero conteos distintos: {C.n} != {D.n}."
)
print("Resultado: delta no determina n en este dominio.")

print()
print("RESULTADO DMO-002")
print(
    "Dentro de esta operacionalizacion minima, "
    "los dos registros son no redundantes."
)
print(
    "Eliminar cualquiera de ellos identifica historias "
    "que el par (n, delta) mantiene distintas."
)

print()
print("LIMITACION")
print(
    "Esto no demuestra una irreductibilidad universal de contar y medir, "
    "ni impide codificar el par mediante otra representacion inyectiva. "
    "Demuestra solamente que, bajo estas definiciones y este dominio, "
    "ninguna de las dos coordenadas determina por si sola a la otra."
)
