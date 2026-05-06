# MADELEINE — Mapa demo-claim

Rama:
v0.2.1-demo-claim-map

Base:
v0.2.0-editorial-audit

Propósito:
Conectar cada claim auditado con evidencia interna, demo disponible, ausencia explícita de demo o necesidad de validación externa.

---

## Estados posibles

### Con demo interna
Existe una demo, ejemplo, tabla, procedimiento o simulación interna asociada al claim.

### Sin demo todavía
El claim está bien formulado, pero aún no tiene evidencia operativa asociada.

### Requiere formalización
El claim necesita definición matemática más precisa antes de asociarse a demo.

### Requiere validación externa
El claim no debe publicarse como resultado hasta compararse con datos, teoría externa, revisión independiente o protocolo reproducible.

---

## Tabla demo-claim inicial

| ID | Claim resumido | Estado claim | Demo/evidencia interna | Fuente posible | Qué demuestra internamente | Qué no demuestra todavía | Validación externa necesaria | Estado público |
|---|---|---|---|---|---|---|---|---|
| C001 | Una pieza pública debe ser trazable y tener criterio de fallo. | Publicable | Criterios de Tomo III | Tomo III / CLAIMS_TABLE | Madurez metodológica interna | No valida contenido científico externo | Checklist aplicable por terceros | Publicable |
| C002 | Una demo no equivale a validación externa. | Publicable con matiz | Separación demo-claim-auditoría | Tomo III | Control de sobreafirmación | No valida demos concretas | Vincular demos reales con scripts/datos | Publicable con matiz |
| C003 | Flujo: entrada, demo, claim, auditoría, salida pública. | Publicable | Arquitectura Tomo III | Tomo III | Orden metodológico | No prueba eficacia externa | Convertir a protocolo ejecutable | Publicable |
| C004 | Todo resultado interno debe traducirse a claim explícito. | Publicable | Tabla de claims | CLAIMS_TABLE | Trazabilidad conceptual | No formaliza todos los claims | Plantilla obligatoria de claim | Publicable |
| C005 | La tabla de claims evita confundir concepto con demostración. | Publicable | CLAIMS_TABLE y CLAIMS_AUDIT_SUMMARY | notes/ | Separación editorial-científica | No valida matemáticamente cada claim | Revisión externa de tabla | Publicable |
| C006 | Un claim necesita formulación, ubicación, evidencia, fallo y riesgo. | Publicable | CLAIMS_AUDIT_SUMMARY | notes/ | Criterio mínimo de auditoría | No establece métricas cuantitativas | Rubrica externa | Publicable |
| C011 | La Base Axiomática queda absorbida por Tomo I. | Publicable | Nota interna de base absorbida | internal/base_axiomatica.pdf | Decisión editorial trazable | No es claim científico externo | Ninguna | Publicable |
| C012 | sub₀ es origen canónico de lectura. | Publicable con matiz | Canon notacional verificado sin sub0 textual | Tomo I / fuentes .tex | Consistencia simbólica interna | No define objeto físico | Formalización matemática estándar | Publicable con matiz |
| C014 | Doble registro distingue conteo y medida. | Interno | Pendiente de ejemplo mínimo | Tomo I | Define separación conceptual | No prueba superioridad frente a medida clásica | Ejemplo reproducible discreto/continuo | Interno |
| C016 | Plano carlesino organiza direcciones como canales. | Interno | Pendiente de demo geométrica mínima | Tomo I | Define lectura direccional interna | No demuestra no equivalencia cartesiana formal | Comparación con coordenadas clásicas | Interno |
| C020 | Régimen verificable exige condiciones internas explícitas. | Publicable | Criterio de régimen verificable | Tomo I | Cierra fundamento con condición de control | No valida regímenes concretos | Protocolo reproducible | Publicable |
| C023 | Transición válida conserva trazabilidad con nivel anterior. | Publicable con matiz | Arquitectura Tomo II | Tomo II | Orden operativo interno | No formaliza toda transición | Reglas mínimas de transición | Publicable con matiz |
| C024 | Umbral operativo marca cambio de régimen interno. | Interno | Pendiente de indicador | Tomo II | Define concepto operativo | No demuestra umbral físico externo | Métrica/indicador reproducible | Interno |
| C026 | Dos lecturas comparables requieren criterios comunes. | Publicable | Criterio de comparabilidad | Tomo II | Evita comparación arbitraria | No da todos los casos comparativos | Ejemplos comparativos | Publicable |
| C030 | Traducción entre niveles no es equivalencia automática. | Pendiente | Sin demo suficiente | Tomo II | Señala riesgo metodológico | No formaliza pérdida/ganancia | Reglas formales y casos límite | Pendiente |
| C032 | Toda afirmación operativa exige trazabilidad. | Publicable | Tomo II + Tomo III | Tomo II / Tomo III | Regla de control editorial | No valida afirmaciones concretas | Aplicación claim por claim | Publicable |
| C008 | Relación demo-claim debe ser explícita. | Interno | Este mapa demo-claim | notes/DEMO_CLAIM_MAP.md | Empieza trazabilidad demo-claim | Aún no completa demos reales | Completar tabla con archivos y evidencia | Interno por ahora |

---

## Demos mínimas que faltan

| Demo ID | Nombre | Claims relacionados | Estado | Prioridad |
|---|---|---|---|---|
| DMO-001 | Demo mínima de sub₀ como origen de lectura | C012 | Pendiente | Alta |
| DMO-002 | Demo de doble registro conteo/medida | C014 | Pendiente | Alta |
| DMO-003 | Demo de plano carlesino como canales direccionales | C016 | Pendiente | Alta |
| DMO-004 | Demo de régimen verificable mínimo | C020 | Pendiente | Alta |
| DMO-005 | Demo de comparabilidad entre lecturas | C026 | Pendiente | Media |
| DMO-006 | Demo de transición entre niveles con pérdida/ganancia | C030 | Pendiente | Alta |
| DMO-007 | Demo de tabla demo-claim aplicada a un caso real interno | C008 | En construcción | Alta |

---

## Regla de salida pública

Un claim puede pasar al dossier externo solo si cumple al menos una de estas condiciones:

1. Es puramente editorial-metodológico y no requiere demo científica.
2. Tiene demo interna claramente identificada y no se presenta como validación externa.
3. Declara explícitamente qué falta para validación externa.

Todo claim sin demo, con riesgo alto o con lenguaje de equivalencia fuerte debe permanecer interno o pendiente.

---

## Próximo paso

Construir las demos mínimas DMO-001 a DMO-004 antes de ampliar claims fuertes.
