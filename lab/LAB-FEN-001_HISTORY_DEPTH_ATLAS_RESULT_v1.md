# LAB-FEN-001 — Resultado HISTORY-DEPTH-ATLAS-v1

## Estatuto

Primera ejecución de:

HISTORY-DEPTH-ATLAS-v1.

Protocolo congelado:

`lab/LAB-FEN-001_HISTORY_DEPTH_ATLAS_SPEC_v1.md`

Ejecutable congelado:

`lab/LAB-FEN-001_HISTORY_DEPTH_ATLAS.py`

Resultado estructurado:

`lab/results/LAB-FEN-001_HISTORY_DEPTH_ATLAS_v1_results.json`

Resumen tabular:

`lab/results/LAB-FEN-001_HISTORY_DEPTH_ATLAS_v1_summary.csv`

No se regeneraron trayectorias.

No se recalibró HISTORY-DEPTH-v1.

El punto basal se reutilizó desde el resultado congelado de HISTORY-DEPTH-v1.

Los otros 19 puntos consumieron exclusivamente series previamente congeladas de ATLAS-v1.

---

# 1. Pregunta

Se evaluó si la profundidad histórica operativa:

k*=2

observada en LAB-D2-v1 permanece estable dentro de la región paramétrica previamente admitida.

---

# 2. Instrumento

Se reutilizó sin modificaciones:

HISTORY-DEPTH-v1.

Se conservaron:

- M1, M2, M3 y M4;
- G2, G3 y G4;
- alpha = 0.5;
- 64 permutaciones;
- Q0.95 nearest-rank;
- definición de DEPTH_HIT;
- clasificación k*;
- semillas;
- train/test;
- contabilidad de borde.

---

# 3. Núcleo formal

Núcleo predeclarado:

beta = {-0.05, 0.00, +0.05}

epsilon = {0.00, 0.05, 0.10}

Total:

9 puntos.

Gate por punto:

al menos 7/8 semillas clasificadas como k*=2.

Gate regional:

9/9 DEPTH POINT PASS.

---

# 4. Resultado del núcleo

Resultado observado:

9/9 DEPTH POINT PASS.

Cada uno de los nueve puntos obtuvo:

8/8 semillas clasificadas como k*=2.

Resultado formal:

HISTORY-DEPTH-ATLAS-v1 PASS.

---

# 5. Malla completa

La malla completa contiene:

20 puntos.

Resultado descriptivo:

20/20 DEPTH POINT PASS.

Total de clasificaciones punto-semilla:

160.

Clasificaciones k*=2:

160/160.

No aparecieron clasificaciones:

k*=1,

k*=3,

k*=4,

ni:

DEPTH COMPLEX.

La malla completa es descriptiva y no redefine retrospectivamente el núcleo formal.

---

# 6. Punto basal

El punto:

beta=0,
epsilon=0

se importó desde HISTORY-DEPTH-v1.

Resultado basal:

8/8 semillas con k*=2.

No se regeneró ni recalibró.

---

# 7. Patrón observado

En todos los puntos evaluados se observa el mismo patrón cualitativo:

G2 positivo con DEPTH_HIT_2.

G3 sin hit.

G4 sin hit.

Por tanto, dentro de la malla ensayada, no se observa desplazamiento de profundidad operativa desde k*=2 hacia profundidades superiores o inferiores.

---

# 8. Resultado formal permitido

Puede afirmarse:

LA PROFUNDIDAD HISTORICA OPERATIVA k*=2 ES ESTABLE EN EL NUCLEO PARAMETRICO PREDECLARADO DE LAB-D2 BAJO HISTORY-DEPTH-v1.

También puede afirmarse:

k*=2 NO ES EXCLUSIVO DEL PUNTO BASAL DENTRO DEL NUCLEO ENSAYADO.

---

# 9. Observación descriptiva adicional

En la malla completa v1:

20/20 puntos

y:

160/160 clasificaciones punto-semilla

mantuvieron:

k*=2.

Este resultado no amplía retrospectivamente el dominio formal del gate.

---

# 10. Relación con resultados anteriores

HISTORY-DEPTH-v1 había establecido dentro de los controles construidos:

D0 -> k*=1

D1 -> k*=2

D2 -> k*=2

DELAYED -> k*=3.

HISTORY-DEPTH-ATLAS-v1 añade que el k*=2 de D2 persiste en la región paramétrica local ensayada.

---

# 11. Lo que no demuestra

Este resultado no demuestra:

- que k*=2 sea universal;
- que toda familia causal tipo D2 tenga k*=2;
- que k*=2 persista fuera de la malla ensayada;
- que no exista una frontera de profundidad histórica;
- que k*=2 sea una constante física;
- que k*=2 sea una geometría;
- memoria física externa;
- causalidad física externa.

---

# 12. Consecuencia metodológica

Dentro del dominio estudiado, la profundidad histórica operativa no aparece como una propiedad accidental de un único punto paramétrico.

Se comporta como una propiedad estable del régimen local ensayado.

Esta afirmación permanece restringida al laboratorio y al instrumento congelado.

---

# 13. Cierre experimental

Con este resultado se cierra la expansión experimental de LAB-FEN-001 para la presente fase de publicación.

No se abrirán nuevas baterías antes del Publication Gap Audit.

Los resultados existentes se preservan como base congelada para integración editorial y auditoría de publicación.

---

# 14. Hashes

JSON SHA256:

88eef99a1595709f8a5ae412dc9f66cf99a7e34cfd7445f37df8cf3871807bc3

CSV SHA256:

d27a60284ec55f29f013880481ed17692f6819de211cf601874b907d0de40025

---

## Estado

HISTORY-DEPTH-ATLAS-v1 PASS — NUCLEO 9/9 — MALLA 20/20 — 160/160 k*=2 — CIERRE EXPERIMENTAL DE LA FASE — SIN CLAIM FISICO EXTERNO