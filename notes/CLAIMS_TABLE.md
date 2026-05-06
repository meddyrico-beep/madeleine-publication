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


---

## Lote 2 — Claims fundacionales derivados de Tomo I

| ID | Tomo | Sección fuente | Claim exacto de auditoría | Tipo | Evidencia interna | Falta para validación externa | Riesgo | Estado |
|---|---|---|---|---|---|---|---|---|
| C011 | Tomo I | Base absorbida | La antigua Base Axiomática queda absorbida editorialmente por Tomo I, que funciona como fundamento público principal. | Editorial-fundacional | Tomo I integra el contenido basal y la base queda como soporte interno. | Ninguna externa; es decisión editorial interna. | Bajo | Publicable |
| C012 | Tomo I | Origen canónico | sub₀ funciona como origen canónico de lectura, no como objeto físico ni punto absoluto del espacio clásico. | Fundacional | El corpus usa sub₀ como referencia estructural. | Formalizar traducción a notación matemática estándar. | Medio | Publicable con matiz |
| C013 | Tomo I | Primitivos | Los primitivos del sistema deben leerse como condiciones de construcción interna, no como entidades físicas demostradas. | Fundacional | Tomo I trabaja con definiciones, axiomas y observaciones. | Separar explícitamente semántica interna y externa. | Bajo | Publicable |
| C014 | Tomo I | Medida y doble registro | El doble registro distingue conteo y medida para evitar reducir toda lectura estructural a magnitudes continuas clásicas. | Fundacional-operativo | Tomo I formula medida, doble registro y lectura derivada. | Comparar con marcos clásicos de medida discreta/continua. | Medio | Interno por ahora |
| C015 | Tomo I | Involución mínima | La involución mínima introduce una relación dual interna sin afirmar todavía simetría física externa. | Fundacional | Se presenta como mecanismo estructural basal. | Precisar propiedades algebraicas formales. | Medio | Publicable con matiz |
| C016 | Tomo I | Plano carlesino | El plano carlesino organiza direcciones como canales de lectura, no como simple sistema cartesiano equivalente. | Fundacional | Tomo I distingue canales y lectura proyectada. | Formalizar equivalencia/no equivalencia con coordenadas clásicas. | Medio | Interno por ahora |
| C017 | Tomo I | Trayectoria mínima | La trayectoria mínima permite leer continuidad estructural sin reducirla a posición aislada. | Fundacional | Tomo I privilegia trayectoria, lectura y acumulación. | Definir ejemplos reproducibles mínimos. | Medio | Publicable con matiz |
| C018 | Tomo I | Lectura proyectada | Toda lectura proyectada debe declararse como derivada, no como primitiva del sistema. | Metodológico-fundacional | Tomo I separa primitivos y coordenadas derivadas. | Ninguna externa; requiere consistencia interna. | Bajo | Publicable |
| C019 | Tomo I | Coherencia mínima | La coherencia mínima es una condición interna de lectura estructural, no una prueba de estabilidad física. | Fundacional | Tomo I define coherencia dentro del marco. | Conectar con métricas verificables si se quiere aplicación externa. | Medio | Publicable con matiz |
| C020 | Tomo I | Régimen verificable | Un régimen verificable exige condiciones internas explícitas antes de cualquier afirmación externa. | Fundacional-metodológico | Tomo I termina con criterio mínimo de régimen verificable. | Diseñar protocolo de verificación reproducible. | Bajo | Publicable |


---

## Lote 3 — Claims operativos derivados de Tomo II

| ID | Tomo | Sección fuente | Claim exacto de auditoría | Tipo | Evidencia interna | Falta para validación externa | Riesgo | Estado |
|---|---|---|---|---|---|---|---|---|
| C021 | Tomo II | Apertura | Tomo II no redefine el fundamento, sino que organiza su paso hacia canon, transición y jerarquía operativa. | Editorial-operativo | Tomo II se apoya en Tomo I y prepara Tomo III. | Ninguna externa; es arquitectura editorial. | Bajo | Publicable |
| C022 | Tomo II | Contrato operativo | Un contrato operativo fija cómo usar el marco sin convertir sus definiciones en resultados externos. | Operativo | Tomo II introduce condiciones de lectura y uso. | Convertir el contrato en checklist práctico. | Bajo | Publicable |
| C023 | Tomo II | Transición de nivel | Una transición de nivel solo es válida si conserva trazabilidad con el nivel anterior. | Operativo | Tomo II organiza transiciones y preparación metodológica. | Formalizar reglas mínimas de transición. | Medio | Publicable con matiz |
| C024 | Tomo II | Umbral operativo | Un umbral operativo marca cambio de régimen interno, no necesariamente cambio físico externo. | Operativo-fundacional | Tomo II distingue umbral, régimen y configuración. | Definir indicadores reproducibles de umbral. | Medio | Interno por ahora |
| C025 | Tomo II | Jerarquía mínima | La jerarquía mínima ordena dependencias internas entre niveles sin afirmar una jerarquía natural externa. | Operativo | Tomo II formula jerarquía y articulación. | Precisar relación formal entre niveles. | Medio | Publicable con matiz |
| C026 | Tomo II | Comparabilidad | Dos lecturas solo son comparables si comparten criterios mínimos de régimen, escala de lectura y trazabilidad. | Operativo-metodológico | Tomo II incluye criterio de comparabilidad. | Crear ejemplos comparativos verificables. | Bajo | Publicable |
| C027 | Tomo II | Distinción operativa | La distinción operativa evita confundir variación interna con diferencia estructural relevante. | Operativo | Tomo II separa distinción, configuración y familia. | Definir umbrales o reglas de decisión. | Medio | Interno por ahora |
| C028 | Tomo II | Configuración | Una configuración operativa es una forma organizada de lectura dentro del marco, no una entidad física por sí misma. | Operativo | Tomo II trabaja configuración y familia operativa. | Traducir configuración a estructura formal reproducible. | Medio | Publicable con matiz |
| C029 | Tomo II | Familia operativa | Una familia operativa agrupa configuraciones por continuidad de criterios, no por semejanza intuitiva. | Operativo | Tomo II desarrolla familia, traducción y protocolo. | Crear taxonomía mínima de familias. | Medio | Interno por ahora |
| C030 | Tomo II | Traducción entre niveles | La traducción entre niveles debe preservar pérdida, ganancia y cambio de lectura; no puede presentarse como equivalencia automática. | Operativo-metodológico | Tomo II dedica secciones a traducción y protocolización. | Formalizar reglas de traducción y casos límite. | Alto | Pendiente |
| C031 | Tomo II | Protocolización mínima | La protocolización mínima permite transformar lectura interna en procedimiento repetible. | Metodológico | Tomo II prepara el paso a Tomo III. | Diseñar protocolo ejecutable y reproducible. | Medio | Publicable con matiz |
| C032 | Tomo II | Trazabilidad operativa | Ninguna afirmación operativa debe separarse de su trazabilidad: fuente, transición, criterio y salida. | Metodológico | Tomo II culmina en preparación para Tomo III. | Aplicar trazabilidad a todos los claims reales. | Bajo | Publicable |
| C033 | Tomo II | Preparación para Tomo III | Tomo II funciona como filtro previo: solo lo trazable y protocolizable debe avanzar a claims públicos. | Editorial-metodológico | Tomo II prepara explícitamente la entrada a Tomo III. | Revisar correspondencia sección por sección con Tomo III. | Bajo | Publicable |

