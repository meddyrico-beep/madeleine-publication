# MADELEINE — Tabla madre de claims

Rama de trabajo:
v0.2-editorial-audit

Base congelada:
v0.1.5-publication-polish

Propósito:
Separar afirmaciones publicables, afirmaciones internas y afirmaciones pendientes de validación externa.

## Criterios de clasificación

### Publicable
El claim está formulado de manera sobria, depende de definiciones internas claras y no promete validación física o matemática externa todavía.

### Interno
El claim sirve para organizar el sistema MADELEINE, pero todavía no debe presentarse como resultado externo.

### Pendiente
El claim requiere demostración formal, experimento, comparación clásica, simulación reproducible o revisión externa antes de publicarse.

### Riesgo alto
El claim puede sonar como sobreafirmación científica si no se matiza.

---

## Tabla madre

| ID | Tomo | Sección | Claim exacto | Tipo | Evidencia interna | Falta para validación externa | Riesgo | Estado |
|---|---|---|---|---|---|---|---|---|
| C001 | Tomo I | Pendiente | Pendiente | Fundacional | Pendiente | Pendiente | Medio | Pendiente |
| C002 | Tomo II | Pendiente | Pendiente | Operativo | Pendiente | Pendiente | Medio | Pendiente |
| C003 | Tomo III | Pendiente | Pendiente | Metodológico | Pendiente | Pendiente | Medio | Pendiente |

---

## Notas de auditoría

1. No convertir definiciones internas en afirmaciones externas.
2. No usar lenguaje de demostración cuando solo hay construcción conceptual.
3. No usar lenguaje físico salvo que exista puente explícito y reproducible.
4. Priorizar claridad, trazabilidad y criterio de fallo.
5. Mantener Tomo I como fundamento sobrio.
6. Mantener Tomo II como transición/canon.
7. Mantener Tomo III como filtro de claims y salida pública.

---

## Lote 1 — Claims metodológicos derivados de Tomo III

| ID | Tomo | Sección fuente | Claim exacto de auditoría | Tipo | Evidencia interna | Falta para validación externa | Riesgo | Estado |
|---|---|---|---|---|---|---|---|---|
| C001 | Tomo III | Criterio de admisión metodológica | Una pieza solo debe entrar al corpus público si puede ser trazada, clasificada y sometida a criterio de fallo. | Metodológico | Tomo III organiza admisión, demos, claims y salida pública. | Definir checklist externo aplicable por terceros. | Bajo | Publicable |
| C002 | Tomo III | Criterio de demo seleccionada | Una demo no equivale por sí misma a validación externa; funciona como evidencia interna organizada. | Metodológico | Tomo III separa demo, claim y auditoría. | Asociar cada demo con datos, script o procedimiento reproducible. | Medio | Publicable con matiz |
| C003 | Tomo III | Puente admisión-demo-claim | La transición válida es: entrada → demo → claim → auditoría → salida pública. | Operativo | La arquitectura de Tomo III está construida como filtro progresivo. | Convertir el flujo en protocolo ejecutable o checklist. | Bajo | Publicable |
| C004 | Tomo III | Traducción a claim | Todo resultado interno debe traducirse a una afirmación explícita antes de poder evaluarse. | Metodológico | El tomo distingue contenido, lectura y claim. | Crear plantilla obligatoria de claim. | Bajo | Publicable |
| C005 | Tomo III | Tabla de claims | La tabla de claims es el instrumento que impide confundir construcción conceptual con demostración externa. | Metodológico | Tomo III dedica una capa a tabla, auditoría y salida pública. | Completar tabla con claims reales del corpus. | Bajo | Publicable |
| C006 | Tomo III | Auditoría mínima de claims | Un claim necesita al menos: formulación, ubicación, evidencia interna, criterio de fallo y riesgo residual. | Metodológico | La estructura editorial ya exige trazabilidad. | Formalizar grados de riesgo y aceptación. | Bajo | Publicable |
| C007 | Tomo III | Selección prioritaria de claims | No todo claim debe publicarse al mismo tiempo; los más sobrios y verificables deben salir primero. | Editorial-científico | Tomo III distingue publicación selectiva y salida pública. | Definir ranking de prioridad. | Bajo | Publicable |
| C008 | Tomo III | Tabla madre de demos y claims | La relación demo-claim debe ser explícita para evitar sobreinterpretación. | Metodológico | Tomo III separa demo, claim, tabla madre y dossier. | Mapear demos concretas con claims concretos. | Medio | Interno por ahora |
| C009 | Tomo III | Salida pública de claims | La salida pública debe excluir afirmaciones físicas, matemáticas o aplicadas que no tengan validación suficiente. | Editorial-científico | Política editorial sobria de Tomo III. | Revisar lenguaje final de cada PDF. | Bajo | Publicable |
| C010 | Tomo III | Dossier externo de claims | El dossier externo debe ser más corto que los tomos y debe explicar qué se afirma, qué no se afirma y qué falta validar. | Editorial-científico | Tomo III contempla dossier, mapa público y política editorial. | Crear el dossier externo mínimo. | Bajo | Publicable |

