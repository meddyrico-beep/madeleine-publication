# LAB-FEN-001 — Resultado del atlas local paramétrico LAB-D2-v1

## Estatuto

Primera ejecución de:

LAB-D2-ATLAS-v1

sobre la candidata congelada:

LAB-D2-v1.

La especificación y el ejecutable fueron congelados antes de observar resultados.

Especificación:

`lab/LAB-FEN-001_D2_ATLAS_SPEC_v1.md`

Ejecutable:

`lab/LAB-FEN-001_D2_ATLAS.py`

Resultados estructurados:

`lab/results/LAB-FEN-001_D2_ATLAS_v1_results.json`

Series completas de los puntos nuevos:

`lab/results/LAB-FEN-001_D2_ATLAS_v1_series.csv.gz`

---

# 1. Control estructural

Puntos de la malla:

20.

Puntos nuevos ejecutados:

19.

Puntos del núcleo predeclarado:

9.

Contextos por punto:

25.

Distribuciones verificadas:

500.

Dependencia estructural de h respecto al pasado:

5 valores distintos de h para cada presente.

Coincidencia analítica del basal:

PASS.

STRUCTURE CHECK:

PASS.

---

# 2. Basal

El punto:

(beta, epsilon) = (0,0)

no fue vuelto a simular.

Se importó el resultado previamente congelado de LAB-D2-v1:

8/8 seed passes.

---

# 3. Núcleo predeclarado

El núcleo estaba fijado antes de resultados como:

beta in {-0.05, 0, +0.05}

y:

epsilon in {0, 0.05, 0.10}.

Número de puntos:

9.

Resultado:

9/9 POINT PASS.

Por tanto se satisface exactamente el gate primario predeclarado.

---

# 4. Resultado primario

Resultado:

LOCAL PARAMETRIC REGION v1 PASS.

LAB-D2-v1 no se comporta como un punto aislado dentro de las perturbaciones paramétricas v1 declaradas.

Existe una región paramétrica local bajo el contrato experimental LAB-FEN-001-v1.

---

# 5. Malla completa

La malla completa contiene:

20 puntos.

Resultado:

20/20 POINT PASS.

Los 19 puntos nuevos obtuvieron 8/8 seed passes.

El basal congelado también posee 8/8.

Por tanto todos los puntos del dominio v1 satisfacen el gate completo por semilla.

---

# 6. Componente conexo del basal

La adyacencia fue definida antes de resultados mediante pasos horizontales o verticales de la malla, sin diagonales.

El componente conexo de POINT PASS que contiene al basal posee:

20/20 puntos.

Por tanto todos los puntos explorados pertenecen al mismo componente PASS conectado al basal.

---

# 7. Frontera

El atlas v1 no localizó una frontera de fallo dentro de la malla ensayada.

Esto no implica ausencia de frontera.

Implica únicamente que la ventana paramétrica:

beta in [-0.10,+0.10]

y:

epsilon in [0,0.15]

permanece íntegramente dentro de la región PASS bajo la resolución declarada.

La posición de una frontera exterior queda fuera del alcance de LAB-D2-ATLAS-v1.

---

# 8. Comportamiento descriptivo

Sin formar parte del gate primario, los resultados muestran un patrón descriptivo consistente al aumentar epsilon.

La señal histórica medida por A1, Delta_hist, C_hist y P_rel tiende a disminuir.

La diversidad histórica N tiende a aumentar.

La aperiodicidad U permanece alta dentro de toda la malla ensayada.

Estas tendencias son observaciones del atlas v1 y no se convierten aquí en leyes generales.

---

# 9. Relación con las ablaciones

Las ablaciones v1 mostraron que:

- quitar el pasado elimina la señal histórica;
- desacoplar el pasado elimina la señal histórica conjunta;
- determinizar la elección elimina la aperiodicidad.

El atlas muestra ahora que, conservando la arquitectura causal, deformaciones cuantitativas moderadas de probabilidades y fuga uniforme no destruyen la firma local.

Las dos baterías responden preguntas diferentes y complementarias.

---

# 10. Qué permite afirmar

Dentro del dominio LAB-FEN-001-v1 puede afirmarse:

LAB-D2-v1 SUPERA LA FIRMA LOCAL.

LAS ABLACIONES CAUSALES v1 SON COMPATIBLES CON LA INTERPRETACION MECANISTICA RESTRINGIDA.

EXISTE UNA REGION PARAMETRICA LOCAL v1 ALREDEDOR DEL BASAL.

EL BASAL PERTENECE A UN COMPONENTE PASS DE 20/20 PUNTOS EN LA MALLA EXPLORADA.

---

# 11. Qué todavía no permite afirmar

Este resultado no demuestra:

- universalidad;
- necesidad matemática universal;
- unicidad del mecanismo;
- robustez frente a toda perturbación;
- posición de la frontera exterior;
- G2-PD universal;
- geometría emergente;
- interpretación física;
- validación externa.

---

# 12. Relación con DMO-004

Con este resultado ya existe una región paramétrica local bajo contrato explícito.

El siguiente paso no debe ser ampliar retrospectivamente la malla sólo porque todos los puntos pasaron.

Primero debe auditarse formalmente LAB-D2-v1 frente a los criterios congelados de DMO-004:

- región paramétrica;
- acuerdo entre semillas;
- separación de nulos;
- criterio de fallo explícito;
- no reducibilidad;
- regla congelada;
- trazabilidad completa.

El atlas aporta evidencia para el primer criterio y parte de la evidencia necesaria para los restantes.

---

# 13. Hashes de artefactos

JSON SHA256:

8dab901a4aff3d5274fc74ce5233fd10e37adc2270223cce4e343b81701e7723

CSV.GZ SHA256:

f3ac6c0f91dc83dfa5aef3ad61bf072088f165e144599b12d0654d5e6a605246

---

## Estado

LOCAL PARAMETRIC REGION v1 PASS — 9/9 NUCLEO — 20/20 MALLA — COMPONENTE BASAL 20/20 — AUN NO PROMOVIDO A REGIMEN