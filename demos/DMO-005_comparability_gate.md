# DMO-005 — Gate de comparabilidad entre lecturas

## Claim asociado

C026 — Dos lecturas solo son comparables si comparten criterios mínimos de régimen, escala de lectura y trazabilidad.

---

## Propósito

Formalizar cuándo dos lecturas pueden compararse componente a componente sin mezclar contratos de observación distintos.

La demo no decide si dos sistemas físicos son equivalentes.

Tampoco establece que las métricas usadas sean universales.

Su función es impedir comparaciones numéricas directas cuando las lecturas fueron construidas bajo condiciones incompatibles.

---

## Contrato de lectura

Para una lectura válida L definimos:

\[
K(L)
=
(
M,
W,
k,
G,
T
),
\]

donde:

- M es el esquema de métricas;
- W es el tamaño de ventana;
- k es la profundidad histórica;
- G es la versión del criterio de régimen;
- T es el esquema de trazabilidad.

Dos lecturas se consideran directamente comparables si:

\[
L_1 \sim L_2
\]

si y solo si:

\[
K(L_1)=K(L_2).
\]

---

## Firma utilizada en la demo

La implementación utiliza como ejemplo:

\[
M=
(A0,A1,P_{\mathrm{rel}},N,U).
\]

Los valores concretos son datos sintéticos de prueba.

No representan resultados fenomenológicos reales.

---

## Implementación

Script:

`demos/DMO-005_comparability_gate.py`

La función de comparación verifica:

1. validez interna de cada lectura;
2. mismo esquema de métricas;
3. mismo tamaño de ventana;
4. misma profundidad histórica;
5. mismo criterio de régimen;
6. mismo esquema de trazabilidad.

Solo cuando todas estas condiciones coinciden se calcula:

\[
\Delta M=M_B-M_A.
\]

---

## Caso comparable

Dos lecturas con el mismo contrato produjeron:

    COMPARABLE: SI

y se habilitó la diferencia componente a componente:

    A0       -0.080
    A1       +0.180
    P_rel    -0.070
    N        +0.230
    U        +0.260

Estos números son únicamente valores sintéticos para comprobar el protocolo.

---

## Casos rechazados

La comparación directa fue rechazada cuando se modificó individualmente:

- el tamaño de ventana;
- el esquema de métricas;
- el esquema de trazabilidad;
- el criterio de régimen;
- la profundidad histórica.

También se rechazó una lectura cuya dimensión de valores no coincidía con su esquema de métricas.

---

## Relación de comparabilidad

Sobre lecturas internamente válidas definimos:

\[
L_1\sim L_2
\iff
K(L_1)=K(L_2).
\]

### Reflexividad

Para toda lectura válida:

\[
K(L)=K(L).
\]

Por tanto:

\[
L\sim L.
\]

### Simetría

Si:

\[
K(L_1)=K(L_2),
\]

entonces:

\[
K(L_2)=K(L_1).
\]

Por tanto:

\[
L_1\sim L_2
\Rightarrow
L_2\sim L_1.
\]

### Transitividad

Si:

\[
K(L_1)=K(L_2)
\]

y:

\[
K(L_2)=K(L_3),
\]

entonces:

\[
K(L_1)=K(L_3).
\]

Por tanto:

\[
L_1\sim L_2
\land
L_2\sim L_3
\Rightarrow
L_1\sim L_3.
\]

Así, compartir exactamente el mismo contrato de lectura define una relación de equivalencia sobre el conjunto de lecturas válidas.

---

## Clases de comparabilidad

La relación anterior particiona las lecturas válidas en clases:

\[
[L]
=
\{
L' : K(L')=K(L)
\}.
\]

La diferencia numérica directa:

\[
\Delta M=M_B-M_A
\]

solo se habilita cuando:

\[
L_A,L_B\in[L].
\]

Esto evita producir diferencias aparentemente precisas entre firmas construidas bajo contratos distintos.

---

## Antisimetría de la diferencia

Para dos lecturas comparables:

\[
\Delta M_{B-A}=M_B-M_A.
\]

Al invertir el orden:

\[
\Delta M_{A-B}=M_A-M_B.
\]

Por tanto:

\[
\Delta M_{B-A}
=
-\Delta M_{A-B}.
\]

La implementación verifica esta propiedad componente a componente.

---

## Qué demuestra

DMO-005 demuestra que el criterio declarado de comparabilidad puede convertirse en un protocolo determinista y ejecutable.

Dentro de esta definición:

- las lecturas quedan agrupadas en clases de comparabilidad;
- una comparación numérica directa solo se permite dentro de la misma clase;
- diferencias de escala, firma, criterio de régimen o trazabilidad bloquean la comparación directa.

---

## Qué no demuestra

DMO-005 no demuestra:

- que las métricas A0, A1, P_rel, N o U sean universales;
- que dos lecturas dentro de la misma clase describan el mismo fenómeno;
- que una diferencia grande sea científicamente significativa;
- que una diferencia pequeña implique equivalencia física;
- que contratos diferentes nunca puedan traducirse entre sí.

Ese último problema pertenece a una etapa posterior de traducción entre niveles o contratos.

---

## Relación con el laboratorio fenomenológico

El laboratorio utiliza firmas vectoriales precisamente para evitar que mecanismos diferentes queden ocultos dentro de un único índice.

DMO-005 no valida esas firmas.

Solo fija cuándo dos firmas pueden compararse directamente sin cambiar simultáneamente la escala o el protocolo que las produjo.

---

## Estado

CONSTRUIDA — INTERNA — REPRODUCIBLE — RELACIÓN DE COMPARABILIDAD FORMALIZADA