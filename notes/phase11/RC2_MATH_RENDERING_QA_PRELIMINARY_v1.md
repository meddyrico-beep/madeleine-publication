# MADELEINE — RC2: informe editorial de fórmulas (preliminar)

**Fecha:** 2026-11-13  
**Estado:** `MATH_RENDERING_PARTIALLY_REPAIRED / SCIENTIFIC_PUBLICATION_GATE_OPEN`  
**Alcance:** revisión editorial de la monografía F11-CORE-001–031. No cambia las fuentes congeladas X670–X675, los Tomos I–III ni `v0.2.1`.

## 1. Estado verificable de la edición RC2

Se ha reconstruido una edición preliminar utilizando la fuente longitudinal `F11(2).txt` y los anexos X674 y X675, sin cambiar las afirmaciones científicas de las fuentes.

| Control | Resultado |
|---|---:|
| Páginas de RC2 | 209 |
| Marcadores de navegación | 71 |
| Bloques matemáticos delimitados compuestos en PDF | 1120 |
| Pasajes con extracción matemática fragmentada | 176 |
| Pasajes con TeX sin delimitadores fiables | 25 |
| Cierres de bloque matemático huérfanos | 90 |
| Total incidencias pendientes de cotejo | **291** |
| Bloques de texto fuera de página | 0 en QA estructural |
| Páginas con menos de 80 caracteres extraídos | 0 |
| Fragmentos literales `\\frac`, `\\boxed`, `\\begin`, `\\sum`, `\\left`, `\\right` | 0 páginas |
| Anexos X674 y X675 | Conservados íntegros |

**SHA-256 del PDF preliminar RC2 (no publicado todavía en el repositorio):**  
`A0B2B37177DF53D29778F65FEFC09A923B2861D211E2A810D5DAAAC2FA9D532B`.

La composición matemática se realizó con MathJax→SVG→PDF vectorial. Que el resultado sea legible no confirma por sí solo la exactitud semántica de todas las 1120 fórmulas.

## 2. Deducción editorial, no científica

Las 291 incidencias **proceden de la representación/segmentación del texto de referencia F11(2).txt**. No equivalen a 291 falsaciones matemáticas. No se han reconstruido esas expresiones por intuición ni se han utilizado para aumentar los claims. Se necesita cotejo individual con fuente primaria alternativa cuando exista.

El PDF RC2 y el registro detallado permanecen en revisión local; **no reemplazan todavía** al PDF RC1 ya incluido en la rama.

## 3. Criterios bloqueantes

1. Corregir o documentar con fuente fiable cada expresión materialmente necesaria para las demostraciones centrales.
2. Revisar semánticamente las expresiones compuestas (fracciones, índices, signos, condiciones de hipótesis).
3. Resolver accesibilidad e indexación del PDF: aún se observan caracteres NUL en la extracción textual de algunas páginas, sin constatar defecto visual de igual extensión.
4. Completar la matriz pública claim↔fuente↔evidencia↔contradicción↔alcance, subordinada a `MANIFESTO.md`, Tomo III capítulos 20–23 y `notes/PHASE10_FINAL_DISPOSITION_v1.md`.
5. Revisar el conjunto de reproducción: el ZIP público X674 de RC1 carece de las 16 entradas congeladas de `X674_ANALYTIC_REVIEW_INPUTS_v1.zip`; no declarar replay autocontenido.
6. Ejecutar un nuevo gate de render, hashes, licencias, privacidad y admisión antes de reemplazar un binario en la rama.

## 4. Ubicación canónica y preservación

- Tomo I = fundamento; Tomo II = canon y jerarquía; Tomo III = método y continuidad.
- F11 = anexo de investigación posterior con evidencia interna bajo criterios de Tomo III, no un Tomo IV fundacional ni una sustitución de I–III.
- El cierre 2026-10-26 de Fase 10 que registró `PHASE 11: NOT AUTHORIZED` permanece histórico; el trabajo F11 se documenta como desarrollo posterior y no como preautorización retrospectiva.
- Las obligaciones R10-MAT-01–07 permanecen abiertas a nivel fuerte.
- La historia Git/Zenodo `v0.2.1` y su DOI no deben modificarse.

**Decisión:** `RC2 PREVIEW AVAILABLE / MERGE NOT AUTHORIZED / ZENODO UNCHANGED`.

**Próximo gate:** completar el cotejo matemático y la revisión semántica, regenerar versión candidata, verificar hashes y documentos de apoyo.