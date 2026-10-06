# MADELEINE — Publication Master Roadmap v1

## Función

Este documento es el punto de entrada operativo para la fase final de publicación de MADELEINE.

No contiene nuevos resultados científicos.

No modifica claims congelados.

No abre experimentos.

Su función es responder en todo momento a cuatro preguntas:

1. ¿Dónde está cada pieza?
2. ¿Qué está ya cerrado?
3. ¿Qué falta para publicar?
4. ¿Cuál es el siguiente paso permitido?

---

# 1. Estado general

## Ciencia experimental

CERRADA PARA ESTA FASE.

Último cierre experimental:

HISTORY-DEPTH-ATLAS-v1.

Resultado:

- núcleo formal: 9/9 DEPTH POINT PASS;
- malla completa: 20/20 DEPTH POINT PASS;
- clasificaciones punto-semilla: 160/160 con k*=2.

Commit de resultado:

3899b26

No se abrirán nuevas baterías antes de publicación.

---

## Publication Gap Audit

Contrato congelado:

notes/PUBLICATION_GAP_AUDIT_SPEC_v1.md

Commit:

7148a19

Estado:

DEFINIDO — PRIMERA MEDICION TODAVIA PENDIENTE.

---

## Build

El build completo actual compila:

- Base Axiomática;
- Tomo I;
- Tomo II;
- Tomo III.

Última inspección:

BUILD 4/4 OK.

La compilación no sustituye la auditoría de contenido.

---

# 2. Árbol operativo principal

madeleine-publication/
|
|-- README.md
|-- MANIFESTO.md
|
|-- manuscript/
|   |
|   |-- shared/
|   |   |-- macros.tex
|   |   |-- madeleine_style.tex
|   |   `-- notation.tex
|   |
|   |-- base_axiomatica/
|   |   `-- soporte técnico interno
|   |
|   |-- tomo1/
|   |   `-- fundamento público principal
|   |
|   |-- tomo2/
|   |   `-- canon, transición y jerarquía
|   |
|   `-- tomo3/
|       `-- método, demos, claims y salida pública
|
|-- demos/
|   |
|   |-- DMO-001
|   |-- DMO-002
|   |-- DMO-003
|   |-- DMO-004
|   |-- DMO-005
|   `-- DMO-006
|
|-- lab/
|   |
|   |-- LAB-FEN-001_PROTOCOL.md
|   |-- LAB-D0
|   |-- LAB-D1
|   |-- LAB-D2
|   |-- ABLATIONS
|   |-- ATLAS
|   |-- DMO-004 AUDIT
|   |-- HISTORY-DEPTH
|   |-- HISTORY-DEPTH-ATLAS
|   |
|   `-- results/
|       `-- JSON / CSV / CSV.GZ congelados
|
|-- notes/
|   |
|   |-- CLAIMS_TABLE.md
|   |-- CLAIMS_AUDIT_SUMMARY.md
|   |-- DEMO_CLAIM_MAP.md
|   |-- EXTERNAL_DOSSIER_MIN.md
|   |-- EDITORIAL_MAP_PUBLICATION.md
|   |-- PUBLICATION_PACK_CHECKLIST.md
|   |-- PUBLICATION_GAP_AUDIT_SPEC_v1.md
|   `-- PUBLICATION_MASTER_ROADMAP_v1.md
|
|-- tools/
|   |
|   |-- build.ps1
|   |-- test.ps1
|   |-- snapshot.ps1
|   |-- clean_publication_repo.ps1
|   |-- migrate_candidate.ps1
|   `-- admit_candidate.ps1
|
|-- artifacts/
|   |
|   |-- pdf/
|   `-- releases históricos
|
`-- release/
    `-- paquetes históricos de publicación

---

# 3. Cómo entrar a cada capa

## Fundamento público

Abrir:

manuscript/tomo1/

Función:

fundamento, primitivas y arquitectura basal pública.

---

## Canon operativo

Abrir:

manuscript/tomo2/

Función:

transición, jerarquía, comparabilidad, configuración, familia, traducción y trazabilidad.

---

## Método y claims

Abrir:

manuscript/tomo3/

Función:

admisión metodológica, demos, claims, auditoría y reglas de salida pública.

---

## Resultados formales mínimos

Abrir:

demos/

Función:

DMO-001 a DMO-006.

Aquí viven las demostraciones y verificadores asociados a claims concretos.

---

## Fenomenología experimental

Abrir:

lab/

Función:

protocolos, especificaciones, ejecutables y actas experimentales.

---

## Datos experimentales congelados

Abrir:

lab/results/

Función:

resultados estructurados y series congeladas.

No editar manualmente resultados científicos.

---

## Mapa de claims

Abrir:

notes/CLAIMS_TABLE.md

y:

notes/DEMO_CLAIM_MAP.md

Función:

relación entre formulación, evidencia, demo, riesgo y estatus público.

---

## Política externa

Abrir:

notes/EXTERNAL_DOSSIER_MIN.md

Función:

qué puede afirmarse públicamente y qué no.

---

## Auditoría de publicación

Abrir:

notes/PUBLICATION_GAP_AUDIT_SPEC_v1.md

Función:

regla congelada para medir readiness.

---

## Checklist de release

Abrir:

notes/PUBLICATION_PACK_CHECKLIST.md

Función:

acabado visual y empaquetado final.

---

# 4. Estado de los grandes bloques

## A. Ciencia interna

Estado:

MUY AVANZADA / CERRADA PARA ESTA FASE.

Incluye:

- DMO-001 a DMO-006;
- LAB-D0;
- LAB-D1;
- LAB-D2;
- métricas;
- ablaciones;
- atlas local;
- DMO-004;
- HISTORY-DEPTH;
- HISTORY-DEPTH-ATLAS.

No abrir nuevos experimentos antes del release candidate.

---

## B. Claims

Estado:

AVANZADO.

Existen:

- CLAIMS_TABLE;
- CLAIMS_AUDIT_SUMMARY;
- DEMO_CLAIM_MAP;
- EXTERNAL_DOSSIER_MIN.

Pendiente:

sincronizar los resultados experimentales finales con el corpus público y volver a auditar la salida final.

---

## C. Manuscrito

Estado:

COMPILA, PERO NO ESTA TODAVIA INTEGRADO CON TODOS LOS RESULTADOS FINALES.

Gap principal:

los resultados finales de LAB-FEN-001 todavía no forman parte explícita del manuscrito público.

---

## D. Reproducibilidad

Estado:

MUY AVANZADO.

Existen:

- specs;
- ejecutables;
- resultados;
- series;
- hashes;
- historial Git;
- tests;
- builds.

Pendiente:

documentación pública compacta de reproducción y manifest final.

---

## E. Bibliografía

Estado:

PENDIENTE.

La versión inspeccionada del manuscrito no contiene todavía un sistema bibliográfico formal integrado.

Debe resolverse antes del release candidate.

---

## F. Consistencia editorial

Estado:

PARCIAL.

El canon principal está estabilizado.

Pendiente:

auditoría final de:

- notación;
- terminología;
- referencias cruzadas;
- homogeneidad visual;
- relación D0-D11 frente a LAB-D0/LAB-D1/LAB-D2;
- incorporación de resultados recientes.

---

## G. Release

Estado:

PENDIENTE.

Faltan todavía:

- acabado visual;
- PDFs definitivos;
- manifest final;
- hashes;
- snapshot;
- paquete final;
- tag final.

---

# 5. Hoja de ruta obligatoria

## FASE 0 — Cierre experimental

Estado:

DONE.

No reabrir.

---

## FASE 1 — Mapa maestro

Objetivo:

crear una única puerta de entrada al proyecto.

Salida:

PUBLICATION_MASTER_ROADMAP_v1.md

Estado:

EN CURSO.

---

## FASE 2 — Matriz fija del Publication Gap Audit

Objetivo:

convertir los criterios ya congelados en una lista finita y puntuable de ítems.

Reglas:

- no cambiar pesos;
- no cambiar criterios;
- no corregir gaps todavía.

Salida prevista:

notes/PUBLICATION_GAP_AUDIT_MATRIX_v1.md

---

## FASE 3 — Primera medición

Objetivo:

medir el repo tal como existe antes de correcciones.

Salidas previstas:

- score /100;
- score por dimensión;
- blockers;
- gaps críticos;
- gaps menores;
- archivos afectados.

Salida prevista:

notes/PUBLICATION_GAP_AUDIT_RESULT_v1.md

---

## FASE 4 — Gap fixes

Orden obligatorio:

### 4.1 Integración científica

Incorporar al corpus público únicamente los resultados que corresponda publicar.

Prioridad:

LAB-FEN-001 y resultados finales congelados.

No trasladar automáticamente todo el laboratorio al manuscrito.

---

### 4.2 Bibliografía y posicionamiento

Construir bibliografía verificable.

Distinguir:

- antecedentes;
- marcos de comparación;
- contribuciones propias;
- limitaciones.

---

### 4.3 Sincronización de claims

Actualizar:

- CLAIMS_TABLE;
- CLAIMS_AUDIT_SUMMARY;
- DEMO_CLAIM_MAP;
- EXTERNAL_DOSSIER_MIN;

cuando corresponda.

Mantener separación estricta entre:

resultado interno

y:

validación externa.

---

### 4.4 Consistencia editorial

Auditar:

- nomenclatura;
- símbolos;
- definiciones;
- referencias cruzadas;
- D0-D11;
- LAB-D0/LAB-D1/LAB-D2;
- sub₀;
- estructura entre tomos.

---

### 4.5 Acabado visual

Resolver:

- portadas;
- headers/footers;
- índices;
- aperturas;
- metadatos;
- saltos de página;
- warnings visualmente relevantes.

---

### 4.6 Package release

Generar:

- PDFs finales;
- README público;
- guía de reproducción;
- manifest;
- hashes;
- snapshot;
- ZIP;
- tag.

---

# 6. FASE 5 — Re-audit

Aplicar exactamente:

PUBLICATION-GAP-AUDIT-v1

sin cambiar:

- pesos;
- criterios;
- bloqueadores;
- umbral.

Objetivo:

score >= 95

y:

blockers = 0.

---

# 7. FASE 6 — Release candidate

Requisitos simultáneos:

- score >= 95;
- blockers = 0;
- tests PASS;
- build PASS;
- working tree CLEAN;
- manifest consistente;
- hashes finales;
- PDFs definitivos;
- snapshot final.

Sólo entonces:

PUBLICATION RELEASE CANDIDATE READY.

---

# 8. Lo que no haremos

Durante esta ruta no se abrirán:

- nuevas familias experimentales;
- nuevas calibraciones;
- nuevos atlas;
- nuevos mecanismos;
- nuevas métricas destinadas a mejorar artificialmente el score.

Si aparece una pregunta científica nueva se registra como:

FUTURE WORK.

---

# 9. Comandos de navegación rápida

Desde la raíz del repo:

```powershell
Get-Content .\notes\PUBLICATION_MASTER_ROADMAP_v1.md
```

Ver estado Git:

```powershell
git status --short
git log -1 --oneline --decorate
```

Ver claims:

```powershell
Get-Content .\notes\CLAIMS_TABLE.md
```

Ver mapa demo-claim:

```powershell
Get-Content .\notes\DEMO_CLAIM_MAP.md
```

Ver política externa:

```powershell
Get-Content .\notes\EXTERNAL_DOSSIER_MIN.md
```

Ver laboratorio:

```powershell
Get-ChildItem .\lab -File | Sort-Object Name
```

Ver resultados:

```powershell
Get-ChildItem .\lab\results -File | Sort-Object Name
```

Ver manuscritos:

```powershell
Get-ChildItem .\manuscript -Recurse -File -Filter *.tex
```

Compilar:

```powershell
.\tools\build.ps1 -Piece all
```

Validar:

```powershell
.\tools\test.ps1
```

---

# 10. Ruta resumida

CIENCIA CERRADA
->
MAPA MAESTRO
->
MATRIZ AUDIT
->
PRIMER SCORE
->
INTEGRACION
->
BIBLIOGRAFIA
->
CLAIMS
->
CONSISTENCIA
->
ACABADO
->
PACKAGE
->
RE-AUDIT
->
RELEASE CANDIDATE

---

## Estado

PUBLICATION MASTER ROADMAP v1 — RUTA FINAL DE PUBLICACION DEFINIDA
