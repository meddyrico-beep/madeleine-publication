# MADELEINE — Mapa de continuidad, admisión y ubicación de Fase 11

**Documento:** CORPUS_CONTINUITY_AND_ADMISSION_MAP_v1  
**Fecha:** 2026-11-13  
**Estado:** `PROPOSED_INTEGRATION_MAP / PUBLICATION_GATE_OPEN`. No autoriza por sí solo nuevas afirmaciones científicas ni una nueva release.  
**Rama de revisión:** `publication/f11-core-001-031-rc1`.  
**Principio:** adición no destructiva al corpus publicado; prioridad a fuentes canónicas y decisiones de admisión.

## 1. Autoridad y fuentes que se conservan

1. `MANIFESTO.md`: separa fundamento, canon intermedio, metodología, evidencia interna, claims y reservas; ningún bloque entra sin estatus, destino, notación y alcance.
2. `README.md` y `notes/EDITORIAL_MAP_PUBLICATION.md`: **Tomo I** es fundamento público principal; **Tomo II** es transición y jerarquía canónica; **Tomo III** es método, curación, demos, claims y salida pública.
3. `manuscript/tomo3/sections/20_criterio_de_clausura_editorial_provisional_del_sistema.tex`: el cierre editorial permite adendas posteriores sin destruir la prioridad del corpus publicado.
4. `manuscript/tomo3/sections/21_criterio_de_continuidad_reapertura_y_nueva_fase.tex`: una nueva fase requiere declarar la zona abierta, el motivo, los elementos preservados y el criterio de reintegración; no basta añadir material.
5. `manuscript/tomo3/sections/22_criterio_de_marco_estable_de_evolucion_futura.tex` y `23_criterio_de_cierre_arquitectonico_del_horizonte_futuro.tex`: continuidad de ciclos sin confundirse con reapertura o sustitución del fundamento.
6. `notes/PHASE10_FINAL_DISPOSITION_v1.md` (2026-10-26): cierra documentalmente Fase 10 **con reservas**, deja obligaciones científicas abiertas y registra expresamente `PHASE 11: NOT AUTHORIZED` **en la fecha de aquella decisión**.
7. `notes/PHASE10_SCIENTIFIC_DECISION_MATRIX_v1.md`: mapa de obligaciones R10-MAT-01–13; los siete P1 principales siguen abiertos mientras no haya pruebas específicas.

**Regla de historia:** la decisión de 2026-10-26 no se reescribe ni se hace decir que autorizó F11. Los trabajos F11-CORE-001–031 realizados después deben documentarse como trabajos nuevos, con su propio alcance, fecha, protocolo y admisión pública posterior. Un eventual acto editorial posterior no puede convertirse retrospectivamente en pre-registro de los experimentos ya efectuados.

## 2. Ubicación precisa de F11 en el corpus

| Capa publicada | Función canónica que permanece | Relación admisible de F11 | Acción permitida ahora |
|---|---|---|---|
| Tomo I / `manuscript/tomo1/` | Fundamento, primitivos, `sub₀`, doble registro y construcción basal | F11 puede **referenciar** sus conceptos, pero no demostrar por defecto su necesidad o interpretación física | **Sin mutación**; solo correspondencia documentada |
| Tomo II / `manuscript/tomo2/` | Contratos, transición, jerarquía D0–D11, comparabilidad y traducción | El estado de D5 Native puede tratarse como un **modelo estudiado** y no como prueba de un isomorfismo canónico D5, ni como equivalencia D0–D11↔LAB | **Sin mutación**; puente explícito marcado como obligación abierta |
| Tomo III / `manuscript/tomo3/` | Admisión, método, demos, claims, trazabilidad y nueva fase (cap. 20–23) | Marco normativo para admitir el caso computacional F11-031 como **evidencia interna condicionada** | Mantener el Tomo III congelado; crear un **anexo de continuidad** sujeto a gate |
| `demos/` | DMO-001–DMO-006 y sus contratos de evidencia | F11 no se convierte automáticamente en DMO ni en prueba de los claims históricos | **No renumerar ni modificar** demos anteriores |
| `lab/`, `lab/results/` | LAB-FEN-001 y datos congelados | F11 es una línea computacional posterior con protocolo y hashes propios; no reetiquetar LAB-FEN-001 | Mantener resultados previos intactos; preservar F11 en espacio propio al completar revisión de distribución |
| `notes/PHASE10_*` | Auditoría posterior a v0.2.1, resultados positivos y negativos | Registrar qué obligaciones de Fase 10 **aborda parcialmente** F11 y cuáles no | **No reescribir** conclusiones históricas ni proclamar satisfechas obligaciones abiertas |
| `notes/phase11/` | Nueva documentación de procedencia, alcance y decisión | Informe técnico, X674/X675, matriz de admisión y fuentes | **Aquí** reside el puente documental revisable |
| `artifacts/phase11/` | Artefactos derivados nuevos, separados del release histórico | PDF de F11, fuentes y paquetes complementarios si se aceptan | Mantener **en rama candidata**, corregir composición matemática antes de release |

## 3. Qué añade realmente F11-CORE-031

La afirmación candidata, con alcance limitado, es:

```text
Para D5 Native v0.6 interpretado como mapa real
con parámetros binarios congelados, desde el estado
archivado n=1318 y 436 perturbaciones postpaso
solo en memoria, |eta_n| <= 6.35e-6:

r(x_1318) - r(x_1754(eta)) > 0.02
```

Los informes internos X670–X675 registran cierre inductivo, cotas hessianas y revisión favorable; el margen inferior informado tras descontar el umbral es aproximadamente `8.259118279787194e-8`.

**Estatus admisible:** `INTERNAL_COMPUTER_ASSISTED_CANDIDATE`, con auditoría analítica interna favorable; revisión externa formal `PENDING`.

**No inferir:** equivalencia del código float64 en todos los sistemas, estabilidad asintótica, régimen universal, necesidad de seis canales, ley física, originalidad independiente, equivalencia generativa LAC→D5 ni cierre de la jerarquía D1–D21. El resultado está restringido a 436 pasos y a la perturbación indicada.

## 4. Matriz de obligaciones heredadas

| Obligación Fase 10 | Relación real con F11-031 | Estatus tras F11-031 |
|---|---|---|
| R10-MAT-01, necesidad dinámica de seis canales | El certificado D5 no excluye modelos más simples ni demuestra necesidad de seis canales | **ABIERTA** |
| R10-MAT-02, puente formal de doble registro | No se proporciona equivalencia de estructuras | **ABIERTA** |
| R10-MAT-03, traducción entre contratos | No se demuestra preservación general de operaciones | **ABIERTA** |
| R10-MAT-04, correspondencia canon-laboratorio | D5 nativo no es automáticamente D5 canónico | **ABIERTA** |
| R10-MAT-05, solidez evidencia→claim | Hay un caso computacional restringido con hipótesis verificadas internamente, no una garantía general | **ABIERTA**, caso focalizado documentado |
| R10-MAT-06, validación física independiente | No se aportan observaciones naturales independientes | **ABIERTA** |
| R10-MAT-07, originalidad científica integrada | No existe evaluación suficiente de prioridad o superioridad frente al estado del arte | **ABIERTA** |

Las reservas metodológicas y científicas negativas de Fase 10 permanecen vinculantes para las afirmaciones fuertes.

## 5. Contrato de admisión pública para F11

Aplicar el esquema de siete campos de Fase 10 a cada claim nuevo:

- **S**: alcance preciso del claim, dominio, parámetros, versión y período;
- **E**: clase de evidencia (F matemática formal, C computacional, M metodológica, E externa independiente);
- **A**: pruebas adversariales, reparaciones y resultados negativos;
- **L**: comparadores y literatura relevante (señalar si la revisión es incompleta);
- **N**: originalidad no presumida;
- **V**: veredicto apoyado exactamente por el material;
- **R**: limitaciones y obligaciones abiertas.

**F11-CORE-001–030:** registrar solo lo que documentan fuentes primarias, sin inventar las fichas ausentes de 007, 010, 011, 020, 021.  
**F11-CORE-031:** caso computacional finito con `S` y `E` delimitados, auditoría interna favorable `A`; `L`, `N`, validación externa y reproducibilidad autocontenida completa permanecen en revisión.  
**F11-CORE-032+**: requiere decisión nueva, hipótesis diferencial precisa, competidor simple, criterio de falsación y protocolo prospectivo; no queda autorizada por este mapa.

## 6. Gate editorial y reproducibilidad de RC1

**Bloqueo confirmado:** el PDF integral RC1 contiene ecuaciones LaTeX sin componer o fragmentadas (véase comentario bloqueante en PR #1). Su mera extensión de 180 páginas no satisface el criterio científico de legibilidad.

**Límite de reproducción:** el ZIP de revisión X674 publicado en RC1 no incluye las 16 entradas del paquete `X674_ANALYTIC_REVIEW_INPUTS_v1.zip`. Por tanto, no declarar reproducción autónoma completa de X670–X673b desde RC1.

Para aceptar una versión siguiente:

1. Regenerar las ecuaciones desde fuente controlada y verificar legibilidad y semántica matemática.
2. Declarar una matriz por claim F11 con procedencia, fallo, límites y relación con Tomos I–III.
3. Conservar explícitamente los resultados negativos, documentos, datos, hashes, autoría y derechos previos.
4. Resolver las condiciones de distribución y completar o delimitar el paquete de evidencia de forma verificable.
5. Validar los gates científicos y editoriales, congelar commit y archivos, sin reescribir `v0.2.1`.

## 7. Preservación GitHub–Zenodo

La versión histórica se conserva exactamente:

- Git tag `v0.2.1`; commit `fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b`.
- DOI de versión anterior: `10.5281/zenodo.23450774`.
- DOI conceptual de familia, según el registro público del repositorio: `10.5281/zenodo.23450773`.

**Flujo recomendado:** únicamente después del gate, incorporar la continuidad a `main` como adición, crear un tag de nueva versión y preparar **una nueva versión del registro Zenodo existente**, conservando el vínculo de familia y DOI de versión anterior. Verificar si el depósito original procede de integración automática GitHub–Zenodo o depósito manual; elegir **un solo flujo** para evitar duplicación o un DOI conceptual nuevo por error.

**No alterar aún `CITATION.cff`:** contiene la citación válida de la versión congelada v0.2.1. En la nueva release debe actualizarse de manera coordinada, con su DOI específico una vez asignado y con trazabilidad del proceso.

## 8. Decisión operativa

- **Autoridad canónica preservada:** Tomos I–III, Fase 10, release `v0.2.1`.
- **Posición propuesta de F11:** `notes/phase11/` y `artifacts/phase11/`, como **anexo científico de continuidad** bajo el criterio de Tomo III; no nuevo Tomo IV fundacional ni refundación de I–III.
- **Estado de PR #1:** `DRAFT / REVIEW BLOCKED`. El mapa se agrega como puente documental; no se aprueba su fusión.
- **Próxima salida verificable:** RC2 con ecuaciones legibles, matriz de relaciones/claims y control de reproducibilidad.
- **Zenodo:** sin cambios hasta aceptar la nueva versión y confirmar el mecanismo de deposición.

*Este mapa añade trazabilidad a una nueva fase de trabajo; no reescribe la historia ni otorga por sí mismo autorización científica retrospectiva.*
