# MADELEINE — Publication Gap Audit Matrix v1

## Estatuto

Esta matriz materializa en ítems finitos los criterios ya congelados en:

notes/PUBLICATION_GAP_AUDIT_SPEC_v1.md

No introduce nuevos criterios.

No modifica pesos.

No asigna todavía estados.

No corrige gaps.

Su función es hacer reproducible la primera medición.

Base de preparación de esta matriz:

HEAD previo = fbd18a2

---

# 1. Estados permitidos

Cada ítem recibirá exactamente uno de estos estados:

- PASS
- PARTIAL
- FAIL
- NOT APPLICABLE
- INSUFFICIENT EVIDENCE

Conversión:

- PASS = 1.0
- PARTIAL = 0.5
- FAIL = 0.0
- INSUFFICIENT EVIDENCE = 0.0
- NOT APPLICABLE = excluido del denominador de su dimensión

---

# 2. Pesos congelados

| Dimensión | Peso | Ítems fijos |
|---|---:|---:|
| A. Cierre científico interno | 20 | 6 |
| B. Higiene de claims | 15 | 7 |
| C. Integración del manuscrito | 20 | 6 |
| D. Reproducibilidad y trazabilidad | 15 | 9 |
| E. Bibliografía y posicionamiento | 10 | 6 |
| F. Consistencia editorial y notacional | 10 | 9 |
| G. Paquete de release | 10 | 7 |
| TOTAL | 100 | 50 |

---

# 3. Matriz fija

## A. Cierre científico interno — peso 20

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| A01 | Existe especificación previa cuando corresponde. | PENDIENTE DE MEDICION | | |
| A02 | Existe ejecutable, demostración o procedimiento reproducible cuando corresponde. | PENDIENTE DE MEDICION | | |
| A03 | Existe resultado registrado. | PENDIENTE DE MEDICION | | |
| A04 | Los límites interpretativos están explícitos. | PENDIENTE DE MEDICION | | |
| A05 | El estado PASS/FAIL está documentado cuando corresponde. | PENDIENTE DE MEDICION | | |
| A06 | Existe separación explícita entre resultado interno y claim externo. | PENDIENTE DE MEDICION | | |

## B. Higiene de claims — peso 15

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| B01 | CLAIMS_TABLE existe y es utilizable. | PENDIENTE DE MEDICION | | |
| B02 | CLAIMS_AUDIT_SUMMARY existe y es utilizable. | PENDIENTE DE MEDICION | | |
| B03 | DEMO_CLAIM_MAP existe y es utilizable. | PENDIENTE DE MEDICION | | |
| B04 | El dossier externo existe y es coherente con el corpus. | PENDIENTE DE MEDICION | | |
| B05 | Existe correspondencia explícita entre claim y evidencia. | PENDIENTE DE MEDICION | | |
| B06 | No existe promoción física no sustentada. | PENDIENTE DE MEDICION | | |
| B07 | La terminología de claims es consistente entre artefactos. | PENDIENTE DE MEDICION | | |

## C. Integración del manuscrito — peso 20

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| C01 | El Documento Madre refleja los resultados que le corresponden, si aplica al release. | PENDIENTE DE MEDICION | | |
| C02 | Tomo I integra correctamente los resultados que le corresponden. | PENDIENTE DE MEDICION | | |
| C03 | Tomo II integra correctamente los resultados que le corresponden. | PENDIENTE DE MEDICION | | |
| C04 | Tomo III integra correctamente los resultados que le corresponden. | PENDIENTE DE MEDICION | | |
| C05 | Preludio/corpus integra correctamente los resultados que le corresponden, si aplica. | PENDIENTE DE MEDICION | | |
| C06 | Arquitectura/apéndices integra correctamente los resultados que le corresponden, si aplica. | PENDIENTE DE MEDICION | | |

## D. Reproducibilidad y trazabilidad — peso 15

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| D01 | Los scripts necesarios están presentes. | PENDIENTE DE MEDICION | | |
| D02 | Los resultados estructurados necesarios están presentes. | PENDIENTE DE MEDICION | | |
| D03 | Los hashes necesarios están registrados. | PENDIENTE DE MEDICION | | |
| D04 | Los commits relevantes proporcionan trazabilidad. | PENDIENTE DE MEDICION | | |
| D05 | Se respeta el orden spec -> executable -> result cuando corresponde. | PENDIENTE DE MEDICION | | |
| D06 | El working tree está limpio en el punto de medición. | PENDIENTE DE MEDICION | | |
| D07 | Los tests bloqueantes pasan. | PENDIENTE DE MEDICION | | |
| D08 | Existen instrucciones mínimas de reproducción. | PENDIENTE DE MEDICION | | |
| D09 | No existen artefactos derivados relevantes sin procedencia declarada. | PENDIENTE DE MEDICION | | |

## E. Bibliografía y posicionamiento — peso 10

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| E01 | Las referencias necesarias son identificables. | PENDIENTE DE MEDICION | | |
| E02 | Se utilizan fuentes primarias cuando es posible. | PENDIENTE DE MEDICION | | |
| E03 | Existe correspondencia entre citas y afirmaciones. | PENDIENTE DE MEDICION | | |
| E04 | El trabajo está posicionado frente a literatura relacionada. | PENDIENTE DE MEDICION | | |
| E05 | Se separan antecedentes de contribuciones propias. | PENDIENTE DE MEDICION | | |
| E06 | No existen referencias provisionales, inexistentes o placeholders. | PENDIENTE DE MEDICION | | |

## F. Consistencia editorial y notacional — peso 10

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| F01 | sub₀ se mantiene como origen conceptual canónico. | PENDIENTE DE MEDICION | | |
| F02 | Se distingue D0-D11 dimensional de LAB-D0/LAB-D1/LAB-D2. | PENDIENTE DE MEDICION | | |
| F03 | Los símbolos son consistentes. | PENDIENTE DE MEDICION | | |
| F04 | Las fórmulas son consistentes entre documentos. | PENDIENTE DE MEDICION | | |
| F05 | Los nombres de archivos y versiones son consistentes. | PENDIENTE DE MEDICION | | |
| F06 | Los encabezados son consistentes. | PENDIENTE DE MEDICION | | |
| F07 | El encoding es consistente. | PENDIENTE DE MEDICION | | |
| F08 | Las referencias cruzadas, tablas y figuras son consistentes. | PENDIENTE DE MEDICION | | |
| F09 | No existen contradicciones materiales entre tomos. | PENDIENTE DE MEDICION | | |

## G. Paquete de release — peso 10

| ID | Criterio | Estado | Evidencia | Observación |
|---|---|---|---|---|
| G01 | Existen PDFs finales de los documentos requeridos. | PENDIENTE DE MEDICION | | |
| G02 | Existe README apto para publicación. | PENDIENTE DE MEDICION | | |
| G03 | Existen instrucciones públicas de reproducción. | PENDIENTE DE MEDICION | | |
| G04 | Existe manifest de artefactos del release. | PENDIENTE DE MEDICION | | |
| G05 | Existen hashes finales consistentes. | PENDIENTE DE MEDICION | | |
| G06 | El estado Git de cierre está limpio y existe tag/version final. | PENDIENTE DE MEDICION | | |
| G07 | El paquete público está libre de archivos temporales y tiene estructura apta para depósito. | PENDIENTE DE MEDICION | | |

---

# 4. Fórmula de puntuación

Para cada dimensión:

Score_dimension = peso_dimension * suma_valores / numero_items_aplicables

donde:

numero_items_aplicables = total de ítems de la dimensión menos NOT APPLICABLE.

INSUFFICIENT EVIDENCE permanece en el denominador con valor 0.

La puntuación global es la suma de las siete dimensiones.

---

# 5. Bloqueadores

Los bloqueadores permanecen exactamente como fueron congelados en PUBLICATION_GAP_AUDIT_SPEC_v1.md.

Esta matriz no los modifica ni añade nuevos bloqueadores.

---

# 6. Primera medición

La primera medición se realizará sobre el repositorio posterior al commit que congele esta matriz.

No se corregirá ningún gap antes de registrar esa primera medición.

La evaluación deberá aportar evidencia concreta para cada estado.

---

# 7. Control anti-score-hacking

Bajo v1 quedan fijados:

- 50 ítems;
- distribución de ítems por dimensión;
- pesos;
- estados;
- conversión numérica;
- tratamiento de NOT APPLICABLE;
- tratamiento de INSUFFICIENT EVIDENCE.

Cambiar cualquiera de estos elementos exige PUBLICATION-GAP-AUDIT-v2.

---

## Estado

PUBLICATION-GAP-AUDIT-MATRIX-v1 DEFINIDA — AUN NO EVALUADA
