# LAB-FEN-001 — Resultado LAB-D0-v1

## Estatuto

Primera ejecución del control negativo LAB-D0-v1.

El protocolo y el ejecutable fueron congelados en Git antes de observar resultados.

Especificación:

`lab/LAB-FEN-001_D0_SPEC_v1.md`

Ejecutable:

`lab/LAB-FEN-001_D0.py`

---

## Hipótesis estructural

LAB-D0 es un proceso de primer orden:

\[
P(x_{t+1}\mid x_t,x_{t-1})
=
P(x_{t+1}\mid x_t).
\]

Por construcción, el estado anterior no interviene en la ley generadora una vez conocido el presente.

---

## Configuración

Semillas:

\[
8
\]

Burn-in:

\[
1000
\]

Transiciones útiles por semilla:

\[
30000
\]

Partición:

\[
18000\ \mathrm{train}
+
12000\ \mathrm{test}
\]

Suavizado:

\[
\alpha=0.5
\]

Nulos históricos condicionados:

\[
64
\]

por semilla.

---

## Resultado por semilla

| seed | Delta_hist | p95 nulo Delta | hit Delta | C_hist | p95 nulo C | hit C |
|---:|---:|---:|:---:|---:|---:|:---:|
| 11  | -0.002145 | -0.001231 | no | 0.021269 | 0.024306 | no |
| 23  | -0.002339 | -0.000820 | no | 0.019230 | 0.025058 | no |
| 37  | -0.002034 | -0.000936 | no | 0.019508 | 0.025031 | no |
| 51  | -0.002724 | -0.001261 | no | 0.022837 | 0.023802 | no |
| 79  | -0.002239 | -0.001055 | no | 0.019548 | 0.024035 | no |
| 101 | -0.001426 | -0.001045 | no | 0.018599 | 0.024198 | no |
| 131 | -0.001809 | -0.000810 | no | 0.020187 | 0.024525 | no |
| 173 | -0.002167 | -0.001222 | no | 0.019248 | 0.024192 | no |

---

## Resumen

Hits de Delta_hist por encima del p95 nulo:

\[
0/8.
\]

Hits de C_hist por encima del p95 nulo:

\[
0/8.
\]

Semillas con:

\[
\Delta_{\mathrm{hist}}>0:
\]

\[
0/8.
\]

Semillas con C_hist por encima de la mediana de su nulo:

\[
2/8.
\]

Señal consistente entre semillas para Delta_hist:

NO.

Señal consistente entre semillas para C_hist:

NO.

Control estructural del generador:

\[
x_{t-1}\ \text{no es consultado}.
\]

---

## Gate congelado

Delta hits <= 1/8:

PASS.

C_hist hits <= 1/8:

PASS.

Ausencia de señal histórica consistente:

PASS.

Regla generadora de primer orden:

PASS.

Resultado:

\[
\boxed{\mathrm{LAB\text{-}D0\text{-}v1\ PASS}}
\]

---

## Lectura metodológica

Delta_hist fue negativo en las ocho semillas.

Por tanto, añadir contexto de segundo orden no mejoró la predicción fuera de muestra y, en esta realización, introdujo una pequeña penalización compatible con un modelo más parametrizado sin información histórica adicional útil.

C_hist fue positivo pero pequeño.

Esto no se interpreta como dependencia causal histórica, porque una estimación finita no tiene por qué producir exactamente cero y los ocho valores observados permanecieron por debajo del percentil 95 de sus respectivos nulos condicionados.

Este resultado confirma la necesidad de comparar C_hist con un nulo en lugar de interpretar cualquier valor positivo como historia.

---

## Qué permite afirmar

Bajo LAB-D0-v1, el bloque de detección histórica no produjo una señal robusta falsa en un proceso construido explícitamente como Markov de primer orden.

El control negativo sobrevivió los criterios congelados antes de resultados.

---

## Qué no permite afirmar

Este experimento no demuestra que:

- Delta_hist o C_hist sean estimadores universalmente válidos;
- el mismo comportamiento se mantenga para cualquier proceso de primer orden;
- LAB-D1 o LAB-D2 vayan a producir historia causal;
- una futura señal positiva implique automáticamente causalidad;
- exista todavía un régimen G2-PD.

LAB-D0-v1 es una calibración negativa del instrumento, no una validación del objetivo fenomenológico.

---

## Trazas

Resultados estructurados:

`lab/results/LAB-FEN-001_D0_v1_results.json`

Serie completa comprimida:

`lab/results/LAB-FEN-001_D0_v1_series.csv.gz`

Cada semilla conserva además en el JSON el SHA-256 lógico de su serie.

---

## Estado

CONTROL NEGATIVO SUPERADO — RESULTADO CONGELABLE