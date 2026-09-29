# LAB-FEN-001 — Gate operativo de ablaciones D2 v1

## Estatuto

Este documento resuelve antes de resultados dos detalles operativos de:

`LAB-FEN-001_D2_ABLATIONS_SPEC_v1.md`

No modifica ninguna ablación, métrica, semilla, longitud ni umbral.

Versión:

LAB-D2-ABLATIONS-GATE-v1

---

# 1. Regla de precedencia

Cuando el protocolo contiene una condición específica por ablación y posteriormente una formulación resumida más débil, se aplicará la condición específica más estricta.

No se elegirá retrospectivamente la versión que favorezca los resultados.

---

# 2. NO_PAST

Para que NO_PAST sea compatible con la falsación esperada deberán cumplirse simultáneamente:

\[
\#(A1>0)\le1,
\]

\[
\#(\text{Delta hit})\le1,
\]

\[
\#(\text{C hit})\le1,
\]

\[
\#(\text{seed pass})\le1.
\]

También se registrará:

\[
H_s
=
(A1>0)
\land
\text{Delta hit}
\land
\text{C hit}.
\]

Pero H_s no sustituye los cuatro criterios anteriores.

---

# 3. RANDOMIZED_PAST

Para que RANDOMIZED_PAST sea compatible con la falsación esperada deberán cumplirse simultáneamente:

\[
\#(A1>0)\le1,
\]

\[
\#(\text{Delta hit})\le1,
\]

\[
\#(\text{C hit})\le1,
\]

\[
\#(\text{seed pass})\le1.
\]

También se registrará H_s como diagnóstico conjunto.

---

# 4. DETERMINISTIC_CHOICE

La predicción primaria permanece:

\[
\#(U\le T_U)\ge7
\]

y:

\[
\#(\text{seed pass})<7.
\]

No se exige de antemano supervivencia de A1, Delta_hist o C_hist.

---

# 5. DELAYED_PAST

DELAYED_PAST continúa siendo únicamente diagnóstico.

No contribuye al PASS/FAIL primario de la batería.

Se registrarán todas las métricas sin imponer una dirección retrospectiva.

---

# 6. Inicialización de NO_PAST

Se utilizará:

`random.Random(seed)`

y se extraerán uniformemente, en este orden:

1. x[-1];
2. x[0].

Después actúa la regla NO_PAST.

---

# 7. Inicialización de RANDOMIZED_PAST

Generador principal:

`random.Random(seed)`

Extrae, en este orden:

1. x[-1];
2. x[0].

El mismo generador principal elige posteriormente dentro de cada familia.

Generador auxiliar:

`random.Random(seed + 1000003)`

produce únicamente el pasado desacoplado:

\[
\tilde a_t.
\]

---

# 8. Inicialización de DETERMINISTIC_CHOICE

Se utilizará:

`random.Random(seed)`

para extraer uniformemente:

1. x[-1];
2. x[0].

Después de esos dos estados la evolución es completamente determinista.

---

# 9. Inicialización de DELAYED_PAST

DELAYED_PAST necesita tres estados iniciales.

Se utilizará:

`random.Random(seed)`

para extraer uniformemente, en este orden:

1. x[-2];
2. x[-1];
3. x[0].

A partir de ahí:

\[
x_{t+1}
\]

utiliza:

\[
(x_{t-2},x_t)
\]

para construir su familia de sucesores.

La elección dentro de la familia continúa siendo uniforme mediante el mismo generador.

---

# 10. Longitudes

En las cuatro ablaciones se conservarán exactamente:

- burn-in = 1000;
- transiciones útiles = 30000;
- train = 18000;
- test = 12000.

La serie útil entregada a las métricas tendrá exactamente:

\[
30001
\]

estados.

---

# 11. PASS primario de la batería

La batería primaria pasa únicamente si:

NO_PAST cumple sus cuatro condiciones estrictas;

AND

RANDOMIZED_PAST cumple sus cuatro condiciones estrictas;

AND

DETERMINISTIC_CHOICE cumple sus dos condiciones primarias.

DELAYED_PAST no interviene en este booleano.

---

# 12. Regla anti-ajuste

Después de la primera ejecución no podrán modificarse bajo v1:

- esta precedencia;
- los conteos 1/8;
- el criterio 7/8 de DETERMINISTIC_CHOICE;
- las inicializaciones;
- las fuentes pseudoaleatorias;
- el papel exclusivamente diagnóstico de DELAYED_PAST.

Cualquier modificación requerirá una nueva versión.

---

## Estado

GATE OPERATIVO DE ABLACIONES v1 CONGELABLE ANTES DE RESULTADOS