# LAB-FEN-001 — Auditoría DMO-004 de LAB-D2-v1

## Estatuto

Este documento fija cómo se evaluará LAB-D2-v1 frente al gate interno DMO-004.

No se generan nuevos datos experimentales.

No se modifican métricas, umbrales, semillas, reglas ni resultados previos.

Versión:

LAB-D2-DMO004-AUDIT-v1

---

# 1. Gate DMO-004

DMO-004 exige conjuntamente siete condiciones:

1. region_parametric
2. seed_agreement
3. null_separation
4. explicit_failure_criterion
5. non_reducible
6. frozen_rule
7. complete_trace

El gate global pasa únicamente si:

7/7 criterios = PASS.

No existe compensación entre criterios.

---

# 2. REGION_PARAMETRIC

PASS requiere una región predeclarada y no un punto aislado.

Evidencia admisible:

`LAB-FEN-001_D2_ATLAS_SPEC_v1.md`

y:

`LAB-FEN-001_D2_ATLAS_RESULT_v1.md`

Criterio operativo:

- núcleo predeclarado = 9 puntos;
- 9/9 POINT PASS;
- basal incluido en la región;
- reglas del núcleo congeladas antes de resultados.

No se utilizará el 20/20 extendido para redefinir retrospectivamente el núcleo.

---

# 3. SEED_AGREEMENT

PASS requiere acuerdo entre semillas dentro de la región declarada.

Criterio operativo:

cada uno de los nueve puntos del núcleo debe tener:

seed_pass_count >= 7/8.

Se registrará adicionalmente el resultado observado de 8/8 cuando corresponda.

---

# 4. NULL_SEPARATION

PASS requiere separación explícita respecto de los nulos históricos congelados.

Para cada semilla que contribuya al POINT PASS deberán cumplirse:

Delta hit = True

y:

C hit = True.

Además:

A1 > 0

bajo la corrección respecto del nulo Markov-1 definida en METRICS-v1.

No se introducirán nuevos nulos durante esta auditoría.

---

# 5. EXPLICIT_FAILURE_CRITERION

PASS requiere que los criterios de fallo hayan sido definidos antes de observar los resultados relevantes.

Evidencia admisible:

- protocolo LAB-FEN-001;
- umbrales LAB-D2-v1;
- especificación de LAB-D2-v1;
- protocolo de ablaciones;
- gate de ablaciones;
- especificación del atlas.

Debe poder demostrarse que existían condiciones explícitas capaces de producir FAIL antes de la ejecución.

---

# 6. NON_REDUCIBLE

Este criterio se interpreta de manera restringida al laboratorio LAB-FEN-001-v1.

No significa irreducibilidad universal.

PASS requiere evidencia de que la firma completa de LAB-D2-v1 no se reduce, dentro de los controles ensayados, a ninguno de estos límites:

A. dinámica sin dependencia histórica inmediata;

B. señal histórica desacoplada del pasado real;

C. dinámica histórica rígidamente determinista y periódica;

D. control LAB-D0 de primer orden;

E. control LAB-D1 rígido de segundo orden.

Evidencia requerida:

NO_PAST:

seed passes completos <= 1/8.

RANDOMIZED_PAST:

seed passes completos <= 1/8.

DETERMINISTIC_CHOICE:

seed passes completos < 7/8

y:

U <= T_U en al menos 7/8.

Además deberán conservarse las diferencias previamente registradas entre LAB-D0, LAB-D1 y LAB-D2.

Este PASS, si se obtiene, sólo autoriza la frase:

NO REDUCIBLE A LOS LIMITES INTERNOS ENSAYADOS EN LAB-FEN-001-v1.

No autoriza:

IRREDUCIBLE UNIVERSAL.

---

# 7. FROZEN_RULE

PASS requiere trazabilidad temporal inequívoca:

- especificación D2 antes de resultados;
- umbrales antes de resultados D2;
- ejecutable D2 antes de ejecución completa;
- protocolo de ablaciones antes de ablaciones;
- ejecutable de ablaciones antes de resultados;
- especificación del atlas antes del atlas;
- ejecutable del atlas antes de resultados.

Los commits Git constituyen la evidencia de orden.

---

# 8. COMPLETE_TRACE

PASS requiere que existan artefactos suficientes para reproducir y auditar el recorrido experimental.

Como mínimo:

- especificaciones;
- ejecutables;
- seeds;
- longitudes;
- métricas;
- thresholds;
- JSON de resultados;
- series;
- hashes de artefactos;
- commits asociados.

No se exige que toda la publicación externa contenga estas trazas.

Se exige que estén preservadas en el laboratorio/repo.

---

# 9. Regla de evaluación

Cada criterio recibirá exactamente uno de:

PASS

FAIL

INSUFFICIENT EVIDENCE

El gate global sólo puede ser:

DMO-004 PASS

si los siete criterios son PASS.

Cualquier FAIL produce:

DMO-004 FAIL.

Cualquier INSUFFICIENT EVIDENCE impide declarar PASS.

---

# 10. Regla anti-promoción

Incluso si DMO-004 resulta PASS, la promoción permitida queda restringida a:

REGIMEN INTERNO ADMITIDO BAJO LAB-FEN-001-v1 Y DMO-004.

No implica:

- teoría física validada;
- universalidad;
- geometría física;
- nueva ley natural;
- sustitución de marcos clásicos;
- validación externa.

---

# 11. Orden de auditoría

1. congelar este contrato;
2. construir auditor reproducible;
3. verificar que sólo consume artefactos congelados;
4. congelar auditor;
5. ejecutar auditor;
6. registrar criterio por criterio;
7. emitir veredicto conjunto;
8. congelar resultado.

---

## Estado

CONTRATO DE AUDITORIA DMO-004 v1 DEFINIDO — AUN NO EVALUADO