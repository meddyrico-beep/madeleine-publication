# LAB-FEN-001 — Resultado LAB-D1-v1

## Estatuto

Primera ejecución del control positivo LAB-D1-v1.

La especificación y el ejecutable fueron congelados en Git antes de observar resultados.

Especificación:

`lab/LAB-FEN-001_D1_SPEC_v1.md`

Ejecutable:

`lab/LAB-FEN-001_D1.py`

---

## Construcción

LAB-D1 es una dinámica determinista de segundo orden:

\[
x_{t+1}=F(x_{t-1},x_t).
\]

La construcción utiliza un ciclo de 25 contextos que cubre exactamente:

\[
S^2,
\qquad
S=\{0,1,2,3,4\}.
\]

Número de contextos:

\[
25/25.
\]

Periodo estructural:

\[
25.
\]

Para cada estado presente:

\[
x_t\in S,
\]

los cinco valores posibles de:

\[
x_{t-1}
\]

producen los cinco sucesores posibles.

Por tanto el presente aislado no determina el futuro.

---

## Contrato instrumental

Se mantuvieron respecto a LAB-D0-v1:

- mismo alfabeto;
- mismas ocho semillas;
- mismo burn-in;
- misma longitud;
- misma partición train/test;
- mismo suavizado;
- mismas 64 permutaciones nulas;
- misma definición de Delta_hist;
- misma definición de C_hist;
- mismo procedimiento de nulo condicionado;
- mismo percentil 95.

---

## Resultados

| seed | phase | Delta_hist | p95 nulo Delta | hit Delta | C_hist | p95 nulo C | hit C |
|---:|---:|---:|---:|:---:|---:|---:|:---:|
| 11  | 14 | +1.606666 | -0.000821 | sí | 0.797232 | 0.030893 | sí |
| 23  | 24 | +1.606666 | -0.001477 | sí | 0.797232 | 0.029398 | sí |
| 37  | 21 | +1.606666 | -0.001283 | sí | 0.797232 | 0.029619 | sí |
| 51  | 7  | +1.606666 | -0.001316 | sí | 0.797232 | 0.031668 | sí |
| 79  | 4  | +1.606666 | -0.001444 | sí | 0.797232 | 0.029287 | sí |
| 101 | 18 | +1.606666 | -0.000842 | sí | 0.797232 | 0.029841 | sí |
| 131 | 10 | +1.606666 | -0.001101 | sí | 0.797232 | 0.029730 | sí |
| 173 | 10 | +1.606666 | -0.000963 | sí | 0.797232 | 0.029509 | sí |

---

## Resumen

Hits de Delta_hist por encima del p95 nulo:

\[
8/8.
\]

Hits de C_hist por encima del p95 nulo:

\[
8/8.
\]

Semillas con:

\[
\Delta_{\mathrm{hist}}>0:
\]

\[
8/8.
\]

Cobertura de contextos:

\[
25/25.
\]

Historia cambia el sucesor:

PASS.

Regla determinista:

PASS.

Periodo estructural:

\[
25.
\]

Resultado:

\[
\boxed{\mathrm{LAB\text{-}D1\text{-}v1\ PASS}}
\]

---

## Contraste con LAB-D0-v1

LAB-D0-v1:

\[
0/8
\]

hits de Delta_hist.

LAB-D1-v1:

\[
8/8
\]

hits de Delta_hist.

LAB-D0-v1:

\[
0/8
\]

hits de C_hist.

LAB-D1-v1:

\[
8/8
\]

hits de C_hist.

Bajo el mismo contrato instrumental, el bloque histórico distingue el control construido sin dependencia de segundo orden del control construido con dependencia explícita de segundo orden.

---

## Lectura metodológica

LAB-D1-v1 demuestra dentro del dominio declarado que el instrumento es capaz de detectar una dependencia histórica fuerte cuando ésta ha sido introducida explícitamente en la regla generadora.

La separación respecto al nulo es amplia en las ocho semillas.

El resultado complementa LAB-D0-v1:

- LAB-D0 controla falsos positivos históricos;
- LAB-D1 controla falsos negativos frente a una dependencia histórica fuerte.

La combinación constituye una calibración bidireccional del bloque histórico del laboratorio.

---

## Rigidez

LAB-D1-v1 es deliberadamente periódico.

Su periodo estructural es:

\[
25.
\]

Por tanto este resultado muestra también que:

\[
\text{dependencia histórica}
\not\Rightarrow
\text{aperiodicidad}.
\]

Una dinámica puede poseer historia causal muy fuerte y, al mismo tiempo, estar completamente cristalizada en un ciclo.

---

## Qué permite afirmar

Dentro del contrato LAB-FEN-001-v1:

1. el control de primer orden LAB-D0 no generó señal histórica robusta;
2. el control determinista de segundo orden LAB-D1 sí generó señal histórica robusta;
3. Delta_hist y C_hist distinguen correctamente estos dos controles construidos;
4. el nulo condicionado destruye la señal adicional de segundo orden sin destruir la estructura de primer orden.

---

## Qué no permite afirmar

Este resultado no demuestra que:

- Delta_hist sea universal;
- C_hist sea universal;
- cualquier señal positiva implique causalidad;
- cualquier segundo orden sea detectable con estas longitudes;
- LAB-D2 vaya a sobrevivir;
- exista G2-PD;
- exista todavía un nuevo régimen fenomenológico.

LAB-D1-v1 es un control positivo calibrado, no el fenómeno objetivo.

---

## Trazas

Resultados estructurados:

`lab/results/LAB-FEN-001_D1_v1_results.json`

Serie completa comprimida:

`lab/results/LAB-FEN-001_D1_v1_series.csv.gz`

---

## Estado

CONTROL POSITIVO SUPERADO — RESULTADO CONGELABLE