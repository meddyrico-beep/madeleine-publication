# MADELEINE — Publication Gap Audit Result v1

## Base de medición

HEAD evaluado: 666a761

Branch: v0.2.1-demo-claim-map

Working tree al inicio: CLEAN

Tests bloqueantes: PASS

Build completo: PASS

Esta es la primera medición formal previa a correcciones de gaps.

---

# 1. Resultado global

| Dimensión | Peso | Score |
|---|---:|---:|
| A. Cierre científico interno | 20 | 20.00 |
| B. Higiene de claims | 15 | 12.86 |
| C. Integración del manuscrito | 20 | 10.00 |
| D. Reproducibilidad y trazabilidad | 15 | 14.17 |
| E. Bibliografía y posicionamiento | 10 | 0.00 |
| F. Consistencia editorial y notacional | 10 | 7.22 |
| G. Paquete de release | 10 | 2.86 |
| TOTAL | 100 | 67.10 |

Banda:

MAJOR REVISION

Blockers confirmados:

1

---

# 2. Estados de los 50 ítems

| ID | Estado | Motivo resumido |
|---|---|---|
| A01 | PASS | Existen especificaciones previas en las cadenas experimentales relevantes. |
| A02 | PASS | Existen ejecutables, demos y procedimientos reproducibles. |
| A03 | PASS | Existen actas y resultados estructurados registrados. |
| A04 | PASS | Los resultados declaran límites interpretativos y alcance interno. |
| A05 | PASS | Los estados PASS/FAIL están documentados cuando corresponde. |
| A06 | PASS | Se mantiene separación explícita entre resultado interno y validación externa. |
| B01 | PASS | CLAIMS_TABLE existe y es utilizable. |
| B02 | PASS | CLAIMS_AUDIT_SUMMARY existe y es utilizable. |
| B03 | PASS | DEMO_CLAIM_MAP existe y es utilizable. |
| B04 | PARTIAL | EXTERNAL_DOSSIER_MIN existe, pero parte de su diagnóstico y próxima fase quedó desactualizada frente al cierre experimental. |
| B05 | PASS | Existe correspondencia explícita entre claims y evidencia interna. |
| B06 | PASS | No se detectó promoción física externa no sustentada. |
| B07 | PARTIAL | Parte del estado editorial y terminología de auditoría aún no está sincronizada con los resultados finales. |
| C01 | NOT APPLICABLE | Documento Madre no forma parte del release operativo actual del repo. |
| C02 | PARTIAL | Tomo I está construido y compila, pero no integra todavía explícitamente los resultados LAB-FEN-001 finales. |
| C03 | PARTIAL | Tomo II está construido y compila, pero no integra todavía explícitamente los resultados finales correspondientes. |
| C04 | PARTIAL | Tomo III contiene la arquitectura metodológica, pero no integra todavía la batería experimental final. |
| C05 | NOT APPLICABLE | No existe un Preludio/Corpus independiente como pieza de release actual. |
| C06 | NOT APPLICABLE | No existe una pieza independiente Arquitectura/Apéndices dentro del release operativo actual. |
| D01 | PASS | Los scripts necesarios están presentes. |
| D02 | PASS | Los resultados estructurados necesarios están presentes. |
| D03 | PARTIAL | Hay hashes explícitos en múltiples actas, pero no cobertura homogénea final de todos los artefactos del paquete. |
| D04 | PASS | Git proporciona trazabilidad detallada de la evolución relevante. |
| D05 | PASS | Se conserva el orden spec -> executable -> result cuando corresponde. |
| D06 | PASS | Working tree limpio en el punto de medición. |
| D07 | PASS | test.ps1 termina sin errores bloqueantes. |
| D08 | PASS | Specs, protocolos y actas proporcionan instrucciones internas mínimas de reproducción. |
| D09 | PASS | No se detectaron resultados científicos relevantes sin procedencia trazable. |
| E01 | FAIL | No existe sistema de referencias bibliográficas integrado. |
| E02 | FAIL | No existe selección documentada de fuentes primarias. |
| E03 | FAIL | No existen citas formales asociadas a afirmaciones del manuscrito. |
| E04 | FAIL | No existe posicionamiento bibliográfico formal frente a literatura relacionada. |
| E05 | FAIL | No existe todavía separación bibliográfica formal entre antecedentes y contribuciones propias. |
| E06 | INSUFFICIENT EVIDENCE | Al no existir bibliografía, no puede auditarse todavía la calidad o provisionalidad de sus entradas. |
| F01 | PASS | sub₀ conserva representación canónica mediante macros compartidas. |
| F02 | PASS | La jerarquía D0-D11 y los controles LAB-D0/LAB-D1/LAB-D2 permanecen nominalmente diferenciados. |
| F03 | INSUFFICIENT EVIDENCE | Falta auditoría exhaustiva símbolo por símbolo. |
| F04 | INSUFFICIENT EVIDENCE | Falta auditoría exhaustiva fórmula por fórmula entre documentos. |
| F05 | PASS | Los nombres y versiones principales siguen una estructura consistente. |
| F06 | PARTIAL | La homogeneidad final de headers, footers y presentación sigue pendiente en el checklist. |
| F07 | PASS | No se detectaron fallos bloqueantes actuales de encoding o serialización editorial. |
| F08 | PASS | El build no detectó referencias rotas bloqueantes; queda trabajo visual menor. |
| F09 | PASS | No se confirmó contradicción material entre los tomos principales. |
| G01 | PARTIAL | Los PDFs actuales existen y compilan, pero todavía no constituyen paquete final trackeado de release. |
| G02 | PARTIAL | README existe, pero es mínimo y contiene una ruta local de Windows. |
| G03 | FAIL | No existe todavía guía pública suficiente de reproducción. |
| G04 | PARTIAL | Existe MANIFEST_PUBLICATION, pero corresponde a una fase anterior. |
| G05 | FAIL | No existe conjunto final actualizado de hashes del release actual. |
| G06 | PARTIAL | El working tree está limpio, pero HEAD actual no tiene tag final de release. |
| G07 | FAIL | No existe todavía paquete público final cerrado y verificado. |

---

# 3. Blockers

## Activado

BLOCKER-09 — manifest/hashes finales inconsistentes con el estado actual.

El MANIFEST_PUBLICATION existente tiene build stamp 20260418_110159 y pertenece a una fase anterior. No existe todavía un manifest final actualizado, hashes finales, snapshot final y ZIP final del estado corriente.

## No activados

BLOCKER-01 — working tree limpio.
BLOCKER-02 — tests bloqueantes PASS.
BLOCKER-03 — no se detectó claim físico externo no sustentado presentado como establecido.
BLOCKER-04 — los resultados computados finales no están actualmente citados en el manuscrito sin artefacto trazable.
BLOCKER-05 — no se confirmó contradicción canónica material entre documentos principales.
BLOCKER-06 — ausencia de bibliografía se registra como gap de dimensión E; no se detectó una fuente esencial citada que sea provisional, inexistente o unverificable.
BLOCKER-07 — los cuatro PDFs principales compilan.
BLOCKER-08 — no se confirmó placeholder editorial visible; la búsqueda amplia produjo falsos positivos por palabras españolas como todo/todos.
BLOCKER-10 — existen declaraciones explícitas de alcance y limitaciones.

---

# 4. Diagnóstico

El cuello de botella actual no es la ciencia experimental interna.

Los tres gaps dominantes son:

1. integración de los resultados finales en el manuscrito;
2. bibliografía y posicionamiento;
3. cierre del paquete de release.

No se abrirán nuevos experimentos para mejorar esta puntuación.

---

# 5. Orden de corrección

1. Integración científica de los resultados ya congelados.
2. Bibliografía y posicionamiento disciplinado.
3. Sincronización final de claims y dossier externo.
4. Auditoría notacional y editorial.
5. README y guía pública de reproducción.
6. Acabado visual.
7. Manifest, hashes, snapshot, ZIP y tag.
8. Re-audit con la misma matriz v1.

---

## Resultado

PUBLICATION-GAP-AUDIT-v1 = 67.10/100

BLOCKERS = 1

VERDICT = MAJOR REVISION

PRIMERA MEDICION CERRADA — SIN CORRECCIONES DE GAP APLICADAS
