# LAB-FEN-001 — Resultado de ablaciones causales LAB-D2-v1

## Estatuto

Primera ejecución de:

LAB-D2-ABLATIONS-v1

sobre la candidata congelada:

LAB-D2-v1.

La especificación, el gate de decisión y el ejecutable fueron congelados antes de observar resultados.

Protocolo:

`lab/LAB-FEN-001_D2_ABLATIONS_SPEC_v1.md`

Gate:

`lab/LAB-FEN-001_D2_ABLATIONS_GATE_v1.md`

Ejecutable:

`lab/LAB-FEN-001_D2_ABLATIONS.py`

Resultados estructurados:

`lab/results/LAB-FEN-001_D2_ABLATIONS_v1_results.json`

Series completas:

`lab/results/LAB-FEN-001_D2_ABLATIONS_v1_series.csv.gz`

---

# 1. Validación de artefactos

El JSON fue parseado correctamente y reproduce los gates registrados por el ejecutable.

Resultado primario:

ABLATION BATTERY v1 PASS.

El CSV gzip fue leído completamente.

Número de condiciones:

4.

Número de semillas por condición:

8.

Número de combinaciones condición/semilla:

32.

Estados registrados por combinación:

30001.

Número total de filas de datos:

960032.

---

# 2. Basal congelado

LAB-D2-v1 había producido:

8/8

seed passes conjuntos bajo la firma local congelada.

Las ablaciones se evaluaron sin recalibrar métricas ni umbrales.

---

# 3. NO_PAST

Se eliminó completamente la dependencia generativa del pasado inmediato.

Resultado:

A1 positivos:

0/8.

Delta hits:

0/8.

C hits:

0/8.

Señal histórica conjunta H:

0/8.

Seed passes completos:

0/8.

La eliminación del pasado destruye la señal histórica que estaba presente en LAB-D2-v1.

Resultado primario:

PASS.

---

# 4. RANDOMIZED_PAST

El pasado real fue sustituido por una señal uniforme independiente.

Resultado:

A1 positivos:

1/8.

Delta hits:

1/8.

C hits:

1/8.

Las apariciones individuales no coinciden conjuntamente:

H conjunto:

0/8.

Seed passes completos:

0/8.

La ablación mantiene diversidad y aperiodicidad muy altas, aproximadamente:

N ~ 0.995

y:

U ~ 0.985,

pero pierde la señal histórica alineada.

Resultado primario:

PASS.

---

# 5. DETERMINISTIC_CHOICE

Se conservó la dependencia histórica de la regla base, pero se eliminó la elección flexible dentro de la familia.

Resultado:

A1 positivos:

5/8.

Delta hits:

5/8.

C hits:

5/8.

H conjunto:

5/8.

Sin embargo:

U <= T_U:

8/8.

En las ocho semillas:

U = 0.

La diversidad histórica observada queda en:

N = 0.016

o:

N = 0.032.

Seed passes completos:

0/8.

La historia puede sobrevivir parcialmente, pero la eliminación de la elección flexible produce cristalización bajo U-v1.

Resultado primario:

PASS.

---

# 6. DELAYED_PAST

El generador utilizó x[t-2] en lugar de x[t-1].

Esta condición estaba congelada como diagnóstico y no formaba parte del booleano primario.

Resultado bajo el detector histórico inmediato:

A1 positivos:

0/8.

Delta hits:

0/8.

C hits:

0/8.

H conjunto:

0/8.

Seed passes:

0/8.

Al mismo tiempo conserva aproximadamente:

N ~ 0.995

y:

U ~ 0.98.

Este resultado no demuestra ausencia de dependencia histórica porque el mecanismo generador depende de un retardo diferente del evaluado directamente por el bloque inmediato.

Queda como motivación para un futuro protocolo específico de profundidad histórica.

---

# 7. Gate primario de la batería

NO_PAST:

PASS.

RANDOMIZED_PAST:

PASS.

DETERMINISTIC_CHOICE:

PASS.

DELAYED_PAST:

DIAGNOSTIC ONLY.

Resultado final:

ABLATION BATTERY v1 PASS.

---

# 8. Lectura mecanística restringida

Dentro del experimento declarado se observa una separación selectiva.

Cuando se elimina el pasado real:

desaparece la señal histórica.

Cuando el pasado real se sustituye por una señal independiente:

persisten apertura, diversidad y aperiodicidad, pero desaparece la señal histórica conjunta.

Cuando se conserva la dependencia histórica y se elimina la elección flexible:

puede sobrevivir parte de la señal histórica, pero la dinámica colapsa en periodicidad.

El patrón es compatible con que la firma completa observada en LAB-D2-v1 dependa conjuntamente de:

historia alineada

+

elección flexible.

Esta lectura es mecanística dentro del modelo construido y no constituye una demostración causal universal.

---

# 9. Qué fortalece

Las ablaciones debilitan dentro de LAB-FEN-001-v1 tres explicaciones triviales:

1. que la firma histórica sobreviva aunque el generador ignore el pasado;
2. que cualquier señal presentada como pasado produzca el mismo resultado;
3. que la dependencia histórica por sí sola baste para conservar diversidad y aperiodicidad.

---

# 10. Qué no demuestra

La batería no demuestra:

- necesidad universal de esta arquitectura;
- unicidad del mecanismo;
- causalidad física;
- región paramétrica;
- robustez de una familia alrededor del punto;
- G2-PD robusta;
- entrada al atlas;
- interpretación geométrica;
- interpretación física;
- validación externa.

LAB-D2-v1 continúa siendo una candidata interna.

---

# 11. Siguiente cuello de botella

Después de:

- calibración D0/D1;
- firma local D2 8/8;
- ablaciones causales primarias superadas;

el requisito todavía ausente es demostrar que el resultado ocupa una región y no depende de un único punto arquitectónico.

El siguiente experimento deberá estudiar una vecindad predeclarada alrededor de LAB-D2-v1 sin recalibrar retrospectivamente la firma.

---

# 12. Hashes de los artefactos

JSON SHA256:

21cfdfc4274be2c57725789b905b6b9432c37ec111c283ef6a21f51e86fc65b5

CSV.GZ SHA256:

3f7aea8917b2a7c1b0dbcaaea606dbf44020a2cc427331c1589c4e2281b54c76

---

## Estado

ABLACIONES CAUSALES v1 SUPERADAS — LAB-D2-v1 FORTALECIDA COMO CANDIDATA INTERNA — AUN NO REGIMEN ROBUSTO