# LAB-FEN-001 — Calibración de métricas fenomenológicas v1

## Estatuto

Primera calibración de:

LAB-FEN-001-METRICS-v1

sobre los controles ya congelados:

- LAB-D0-v1;
- LAB-D1-v1.

Las definiciones métricas y su ejecutable fueron fijados en Git antes de esta ejecución.

Especificación:

`lab/LAB-FEN-001_METRICS_v1.md`

Ejecutable:

`lab/LAB-FEN-001_METRICS_v1.py`

Salida estructurada:

`lab/results/LAB-FEN-001_METRICS_v1_calibration.json`

---

## Resultado global

\[
\boxed{\mathrm{METRICS\text{-}v1\ CALIBRATION\ PASS}}
\]

Todos los criterios de calibración predeclarados fueron satisfechos.

---

## A1 — exceso histórico sobre Markov-1

LAB-D0-v1:

\[
0/8
\]

semillas con:

\[
A1>0.
\]

LAB-D1-v1:

\[
8/8
\]

semillas con:

\[
A1>0.
\]

En LAB-D0 los ocho valores fueron negativos.

En LAB-D1:

\[
I_2=1.609438
\]

en las ocho semillas, aproximadamente:

\[
\ln 5.
\]

Después de corregir por el percentil 95 del nulo Markov-1:

\[
A1\approx1.605
\]

en todas las semillas.

La separación esperada D0/D1 queda confirmada dentro del dominio del experimento.

---

## Persistencia relativa

Mediana LAB-D0:

\[
\widetilde P_0
=
0.015003630380811483.
\]

Mediana LAB-D1:

\[
\widetilde P_1
=
1.0.
\]

Se cumple:

\[
\widetilde P_1
>
\widetilde P_0.
\]

Gate de calibración:

PASS.

Umbral derivado:

\[
T_P
=
0.5075018151904057.
\]

---

## Novedad histórica

Mediana LAB-D0:

\[
\widetilde N_0
=
0.5725067711185636.
\]

Mediana LAB-D1:

\[
\widetilde N_1
=
0.2.
\]

Se cumple:

\[
\widetilde N_0
>
\widetilde N_1.
\]

Gate de calibración:

PASS.

El valor:

\[
N=0.2
\]

de LAB-D1 es coherente con:

\[
25/125,
\]

dado que su ciclo rígido utiliza 25 historias efectivas sobre los 125 trigramas posibles.

Umbral derivado:

\[
T_N
=
0.3862533855592818.
\]

---

## Aperiodicidad

Mediana LAB-D0:

\[
\widetilde U_0
=
0.9816544716915534.
\]

Mediana LAB-D1:

\[
\widetilde U_1
=
0.
\]

Se cumple:

\[
\widetilde U_0
>
\widetilde U_1.
\]

Gate de calibración:

PASS.

Para las ocho semillas de LAB-D1:

\[
U=0
\]

y:

\[
p^\*=25.
\]

Por tanto el instrumento reconoció exactamente la periodicidad estructural congelada del control rígido.

Umbral derivado:

\[
T_U
=
0.4908272358457767.
\]

---

## Umbrales derivados para LAB-D2

Quedan disponibles:

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

Estos valores se derivaron exclusivamente de LAB-D0-v1 y LAB-D1-v1 antes de diseñar o ejecutar LAB-D2-v1.

No se interpretan como constantes universales.

---

## Lectura de los controles

LAB-D0-v1 representa el extremo:

\[
\text{apertura sin historia irreductible}.
\]

Presenta:

- A1 no significativo;
- novedad relativamente alta;
- aperiodicidad alta;
- persistencia histórica relativa baja.

LAB-D1-v1 representa el extremo:

\[
\text{historia fuerte con cristalización}.
\]

Presenta:

- A1 fuerte;
- persistencia perfecta entre ventanas;
- menor diversidad histórica;
- periodicidad exacta de periodo 25.

La calibración distingue correctamente ambos extremos bajo las definiciones congeladas.

---

## Consecuencia experimental

LAB-D2 no podrá considerarse favorable sólo por producir historia.

Deberá combinar en las mismas realizaciones:

\[
A1>0,
\]

historia predictiva,

persistencia por encima del umbral,

novedad por encima del umbral,

y aperiodicidad por encima del umbral.

El objetivo es ocupar la región que ninguno de los dos controles ocupa por separado.

---

## Qué no demuestra

Esta calibración no demuestra:

- universalidad de A1;
- universalidad de P_rel;
- universalidad de N;
- universalidad de U;
- aperiodicidad matemática infinita;
- existencia de G2-PD;
- validez física externa;
- existencia de un nuevo régimen natural.

El resultado queda restringido a LAB-FEN-001-v1.

---

## Estado

CALIBRACION METRICA v1 SUPERADA — UMBRALES D2 DERIVADOS