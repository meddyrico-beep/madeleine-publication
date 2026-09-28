# LAB-FEN-001 — Resultado LAB-D2-v1

## Estatuto

Primera evaluación de LAB-D2-v1 bajo especificación, métricas y umbrales congelados previamente.

Especificación:

`lab/LAB-FEN-001_D2_SPEC_v1.md`

Umbrales:

`lab/LAB-FEN-001_THRESHOLDS_v1.md`

Ejecutable:

`lab/LAB-FEN-001_D2.py`

Resultados:

`lab/results/LAB-FEN-001_D2_v1_results.json`

Serie:

`lab/results/LAB-FEN-001_D2_v1_series.csv.gz`

---

## Proveniencia experimental

La especificación de LAB-D2-v1 fue congelada antes de producir trayectorias.

El ejecutable fue congelado antes de la primera ejecución completa.

La primera ejecución calculó correctamente las métricas y produjo:

8/8 seed passes,

pero falló después al serializar el bloque estructural del JSON porque contenía claves Python de tipo tuple.

La corrección posterior modificó exclusivamente la representación serializable de esas claves.

No se modificaron:

- regla generadora;
- familias de sucesores;
- semillas;
- longitudes;
- métricas;
- nulos;
- umbrales;
- gates;
- criterio 7/8.

La ejecución posterior reprodujo exactamente los mismos valores numéricos observados en la primera ejecución y completó las trazas.

---

# 1. Arquitectura

Alfabeto:

\[
S=\{0,1,2,3,4\}.
\]

Regla base:

\[
h(a,b)
=
(b+2a)\bmod5.
\]

Familia causal:

\[
\mathcal S(a,b)
=
\{
h(a,b),
h(a,b)+1,
h(a,b)+2
\}
\bmod5.
\]

Elección:

uniforme dentro de la familia.

---

# 2. Verificación estructural

Nodos de segundo orden:

\[
25.
\]

Aristas:

\[
75.
\]

Trigramas permitidos:

\[
75.
\]

Conectividad fuerte:

PASS.

Familias distintas por presente:

\[
5/5
\]

para cada estado presente.

Auto-bucles:

\[
(0,0),
(2,2),
(4,4).
\]

STRUCTURE CHECK:

PASS.

---

# 3. Resultados por semilla

| seed | A1 | Delta_hist | Delta hit | C_hist | C hit | P_rel | N | U | seed pass |
|---:|---:|---:|:---:|---:|:---:|---:|---:|---:|:---:|
| 11 | +0.507297 | +0.509742 | sí | 0.398824 | sí | 0.920374 | 0.598333 | 0.983432 | sí |
| 23 | +0.508101 | +0.508704 | sí | 0.398481 | sí | 0.934840 | 0.597898 | 0.983355 | sí |
| 37 | +0.507798 | +0.509093 | sí | 0.398656 | sí | 0.921320 | 0.597945 | 0.985174 | sí |
| 51 | +0.507510 | +0.508788 | sí | 0.398689 | sí | 0.940535 | 0.597829 | 0.986333 | sí |
| 79 | +0.508893 | +0.508414 | sí | 0.398537 | sí | 0.935760 | 0.598090 | 0.985446 | sí |
| 101 | +0.508195 | +0.507978 | sí | 0.398634 | sí | 0.931108 | 0.598043 | 0.982682 | sí |
| 131 | +0.507445 | +0.508873 | sí | 0.398642 | sí | 0.914476 | 0.598463 | 0.983735 | sí |
| 173 | +0.507842 | +0.508218 | sí | 0.398548 | sí | 0.929517 | 0.598490 | 0.982922 | sí |

---

# 4. Gate histórico

Para las ocho semillas:

\[
A1>0.
\]

Para las ocho semillas:

\[
\Delta_{\mathrm{hist}}>0
\]

y:

Delta hit = True.

Para las ocho semillas:

\[
C_{\mathrm{hist}}>0
\]

y:

C hit = True.

Resultado histórico:

\[
8/8.
\]

---

# 5. Persistencia

Umbral congelado:

\[
T_P
=
0.5075018151904057.
\]

Mínimo observado:

\[
P_{\mathrm{rel,min}}
=
0.914476.
\]

Por tanto:

\[
P_{\mathrm{rel}}>T_P
\]

en:

\[
8/8
\]

semillas.

---

# 6. Novedad histórica

Umbral congelado:

\[
T_N
=
0.3862533855592818.
\]

Mínimo observado:

\[
N_{\min}
=
0.597829.
\]

Por tanto:

\[
N>T_N
\]

en:

\[
8/8
\]

semillas.

---

# 7. Aperiodicidad

Umbral congelado:

\[
T_U
=
0.4908272358457767.
\]

Mínimo observado:

\[
U_{\min}
=
0.982682.
\]

Por tanto:

\[
U>T_U
\]

en:

\[
8/8
\]

semillas.

---

# 8. Gate conjunto

Una semilla sólo podía pasar si satisfacía simultáneamente:

\[
A1>0,
\]

\[
\Delta_{\mathrm{hist}}>0
\]

con hit frente al nulo,

\[
C_{\mathrm{hist}}>0
\]

con hit frente al nulo,

\[
P_{\mathrm{rel}}>T_P,
\]

\[
N>T_N,
\]

\[
U>T_U.
\]

Resultado:

\[
8/8
\]

semillas satisfacen conjuntamente la firma.

---

# 9. Resultado formal del laboratorio

Según el contrato previamente congelado:

\[
\boxed{
\mathrm{LAB\text{-}D2\text{-}v1\
LOCAL\ CANDIDATE\ PASS}
}
\]

Estado permitido:

CANDIDATA INTERNA QUE SUPERA LA FIRMA LOCAL LAB-FEN-001-v1.

---

# 10. Comparación conceptual D0 / D1 / D2

LAB-D0-v1:

apertura y aperiodicidad altas sin dependencia histórica robusta.

LAB-D1-v1:

dependencia histórica fuerte y persistencia alta con periodicidad rígida.

LAB-D2-v1:

dependencia histórica fuerte, persistencia alta, diversidad histórica alta y ausencia de periodicidad dominante bajo las métricas congeladas.

Esta separación es válida dentro del dominio experimental LAB-FEN-001-v1.

---

# 11. Qué permite afirmar

El experimento muestra que la arquitectura causal flexible de LAB-D2-v1 puede, en esta construcción concreta, satisfacer simultáneamente los seis componentes de la firma local predeclarada.

El resultado no fue obtenido ajustando los umbrales después de observar D2.

La primera repetición después de la corrección puramente serializadora reprodujo los valores numéricos de la primera ejecución.

---

# 12. Qué todavía no permite afirmar

LAB-D2-v1 no establece todavía:

- una región paramétrica;
- robustez frente a variaciones de arquitectura;
- supervivencia a ablaciones;
- no reducibilidad completa;
- régimen G2-PD robusto;
- entrada al atlas;
- interpretación geométrica;
- interpretación física;
- validación externa.

Un único mecanismo congelado que supera la firma local sigue siendo una candidata.

---

# 13. Próxima falsación

Antes de ampliar la interpretación deberán estudiarse:

- eliminación del pasado;
- permutación del pasado;
- retraso del pasado;
- determinización de la elección;
- reducción de la familia causal a dependencia sólo del presente;
- vecindad de arquitecturas alrededor de LAB-D2-v1.

Sólo después podrá evaluarse el gate completo de DMO-004.

---

## Estado

CANDIDATA LOCAL LAB-D2-v1 SUPERADA — 8/8 — AUN NO REGIMEN G2-PD ROBUSTO