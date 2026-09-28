# LAB-FEN-001 — Umbrales congelados para LAB-D2-v1

## Estatuto

Este documento congela los criterios de decisión de LAB-D2-v1 antes de diseñar o ejecutar su dinámica.

Versión:

LAB-FEN-001-THRESHOLDS-v1

Los umbrales proceden exclusivamente de la calibración congelada sobre:

- LAB-D0-v1;
- LAB-D1-v1.

Fuente de calibración:

`lab/results/LAB-FEN-001_METRICS_v1_calibration.json`

Resultado documentado:

`lab/LAB-FEN-001_METRICS_RESULT_v1.md`

Commit de calibración:

`b635da0`

Estos valores son umbrales internos de LAB-FEN-001-v1.

No son constantes universales ni parámetros canónicos de MADELEINE.

---

# 1. Firma evaluada

Cada semilla de LAB-D2-v1 deberá producir:

\[
M_{G2}^{v1}
=
(
A1,
\Delta_{\mathrm{hist}},
C_{\mathrm{hist}},
P_{\mathrm{rel}},
N,
U
).
\]

Las coordenadas se conservarán por separado.

No se construirá un score escalar compensatorio.

---

# 2. Umbrales derivados

De la calibración D0/D1 quedan congelados:

\[
T_P
=
0.5075018151904057,
\]

\[
T_N
=
0.3862533855592818,
\]

\[
T_U
=
0.4908272358457767.
\]

No podrán modificarse después de observar LAB-D2-v1.

---

# 3. Gate A1

Para una semilla:

\[
A1>0.
\]

A1 se define según:

`LAB-FEN-001-METRICS-v1`

como exceso de información histórica condicional respecto al percentil 95 del nulo Markov-1.

---

# 4. Gate Delta_hist

Para una semilla deberán cumplirse simultáneamente:

\[
\Delta_{\mathrm{hist}}>0
\]

y:

\[
\Delta_{\mathrm{hist}}
>
Q_{0.95}^{null}.
\]

Operativamente:

- `delta_hist > 0`;
- `delta_hit == True`.

Un valor positivo que no supere el nulo no pasa.

---

# 5. Gate C_hist

Para una semilla deberán cumplirse:

\[
C_{\mathrm{hist}}>0
\]

y:

\[
C_{\mathrm{hist}}
>
Q_{0.95}^{null}.
\]

Operativamente:

- `c_hist > 0`;
- `c_hit == True`.

---

# 6. Gate P_rel

Para una semilla:

\[
P_{\mathrm{rel}}
>
0.5075018151904057.
\]

---

# 7. Gate N

Para una semilla:

\[
N
>
0.3862533855592818.
\]

---

# 8. Gate U

Para una semilla:

\[
U
>
0.4908272358457767.
\]

---

# 9. Gate conjunto por semilla

Una semilla sólo se considera:

D2-SEED-PASS

si las seis coordenadas satisfacen simultáneamente sus condiciones.

Formalmente:

\[
G_s
=
G_{A1}
\land
G_{\Delta}
\land
G_C
\land
G_P
\land
G_N
\land
G_U.
\]

No basta con que diferentes subconjuntos de semillas satisfagan coordenadas distintas.

---

# 10. Consistencia entre semillas

Se mantienen exactamente ocho semillas:

11
23
37
51
79
101
131
173

Para que LAB-D2-v1 pase como primera candidata deberán existir al menos:

\[
7/8
\]

semillas con:

\[
G_s=True.
\]

---

# 11. Regla contra compensación

No se permitirá compensar una coordenada fallida mediante otra más fuerte.

La firma es conjuntiva.

---

# 12. Gate programático congelado

Para cada semilla deberá implementarse literalmente:

seed_pass =
    (A1 > 0)
    AND
    (delta_hist > 0)
    AND
    delta_hit
    AND
    (c_hist > 0)
    AND
    c_hit
    AND
    (P_rel > 0.5075018151904057)
    AND
    (N > 0.3862533855592818)
    AND
    (U > 0.4908272358457767)

Y para la candidata:

candidate_pass =
    number_of_seed_passes >= 7

No se alterará esta lógica después de observar resultados.

---

# 13. Condición mínima de candidata

Si:

\[
\#\{s:G_s=True\}
\ge7,
\]

LAB-D2-v1 podrá etiquetarse únicamente como:

CANDIDATA INTERNA QUE SUPERA LA FIRMA LOCAL.

Esto todavía no equivale a:

REGIMEN G2-PD ROBUSTO.

---

# 14. Condición posterior de régimen

Después del éxito local deberán verificarse separadamente los criterios de DMO-004:

1. región paramétrica;
2. acuerdo entre semillas;
3. separación frente a nulos;
4. criterio explícito de fallo;
5. no reducibilidad;
6. regla congelada;
7. trazabilidad completa.

---

# 15. Regla de versión

Después de la primera ejecución de LAB-D2-v1 no podrán modificarse bajo esta versión:

- T_P;
- T_N;
- T_U;
- regla A1;
- gate Delta_hist;
- gate C_hist;
- regla conjunta por semilla;
- requisito 7/8.

Cualquier modificación exige una nueva versión documentada.

---

## Estado

UMBRALES LAB-D2-v1 CONGELADOS ANTES DEL DISEÑO DE D2