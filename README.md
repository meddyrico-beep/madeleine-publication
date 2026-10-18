# MADELEINE — publication repository

Repositorio editorial, metodológico y reproducible de la fase pública actual de MADELEINE.

## Arquitectura pública

La publicación principal está organizada en tres tomos:

- **Tomo I — Fundamento, blindaje y significado**
- **Tomo II — Canon, transición y jerarquía dimensional**
- **Tomo III — Método, demos y traducción a claims**

La antigua **Base Axiomática** se conserva únicamente como soporte técnico interno de trazabilidad. El fundamento público principal está integrado en Tomo I.

## Estructura del repositorio

- `manuscript/` — fuentes LaTeX de Base técnica y Tomos I–III
- `lab/` — protocolos, ejecutables y resultados congelados de LAB-FEN-001
- `demos/` — demostraciones y gates formales/metodológicos
- `notes/` — auditorías, mapas, actas y documentación de publicación
- `tools/` — build, chequeos editoriales y snapshot
- `artifacts/` — PDFs compilados y artefactos derivados
- `tests/` — reservado para pruebas automatizadas adicionales

## Alcance científico

Este repositorio distingue explícitamente entre:

- construcción formal interna;
- resultados numéricos internos reproducibles;
- metodología de admisión y falsación;
- claims públicos;
- validación física externa.

Los resultados actuales de LAB-FEN-001 son internos y metodológicos.

No constituyen por sí solos:

- validación física externa;
- demostración de universalidad;
- sustitución de teorías clásicas;
- identificación de una constante física;
- prueba de una geometría física necesaria.

## Build de los manuscritos

Requisitos principales:

- PowerShell
- XeLaTeX
- Biber para los tomos que contienen bibliografía

Desde la raíz del repositorio:

    .\tools\build.ps1 -Piece all

También pueden compilarse piezas individuales:

    .\tools\build.ps1 -Piece base_axiomatica
    .\tools\build.ps1 -Piece tomo1
    .\tools\build.ps1 -Piece tomo2
    .\tools\build.ps1 -Piece tomo3

Los PDFs resultantes se copian a:

    artifacts/pdf/

La salida pública principal corresponde a:

    artifacts/pdf/tomo1.pdf
    artifacts/pdf/tomo2.pdf
    artifacts/pdf/tomo3.pdf

La Base Axiomática es soporte técnico interno y no sustituye a Tomo I como fundamento público.

## Gate editorial mínimo

El comando:

    .\tools\test.ps1

realiza actualmente un chequeo editorial de las fuentes LaTeX para detectar:

- mojibake;
- placeholders visibles;
- marcas `TODO`, `FIXME` o equivalentes bloqueantes.

Este script no debe interpretarse como una suite científica completa de LAB-FEN-001.

## Evidencia reproducible

La evidencia interna congelada se conserva principalmente bajo:

    lab/
    lab/results/
    demos/
    notes/

Los scripts, especificaciones y resultados deben leerse de forma conjunta.

Los artefactos numéricos congelados no deben recalibrarse silenciosamente ni reinterpretarse fuera del protocolo que los produjo.

Guía detallada de reproducción: [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Convenciones principales

- origen canónico conceptual: `sub₀`
- macro LaTeX canónico: `\subz`
- D0–D11: jerarquía dimensional/canónica
- LAB-D0, LAB-D1, LAB-D2: etiquetas experimentales independientes
- `k*`: profundidad histórica operativa bajo HISTORY-DEPTH-v1, no constante física ni orden Markoviano universal

## Estado editorial

La fase experimental LAB-FEN-001 de esta publicación está cerrada.

Los gap fixes científicos, bibliográficos, de claims, consistencia notacional y revisión visual han sido completados para la fase actual.

La infraestructura de release incluye:

- manifest dinámico de artefactos;
- hashes SHA256;
- snapshot reproducible ligado a Git HEAD;
- paquete ZIP verificable;
- guía pública de reproducción.

La declaración formal de un release candidate se realiza únicamente después de aplicar la re-auditoría global congelada y asociar la versión/tag correspondiente al mismo estado candidato.

## DOI y citación

La versión pública congelada **MADELEINE v0.2.1** está archivada en Zenodo.

- DOI de esta versión: [10.5281/zenodo.23450774](https://doi.org/10.5281/zenodo.23450774)
- DOI de todas las versiones: [10.5281/zenodo.23450773](https://doi.org/10.5281/zenodo.23450773)
- Git tag congelado: `v0.2.1`
- commit congelado: `fee2c31cfa17159a4075e1cbfbfa7e2fceba9c4b`
- GitHub Release: [MADELEINE v0.2.1](https://github.com/meddyrico-beep/madeleine-publication/releases/tag/v0.2.1)
- SHA256 del paquete canónico: `49E9B23EA8EDDA5B43AC749BDBB30873FF38B31E17E60265E14CBC6707711375`

Para citar específicamente la versión congelada `v0.2.1`, debe utilizarse el DOI de versión `10.5281/zenodo.23450774`.

El DOI `10.5281/zenodo.23450773` representa la familia de versiones archivadas de MADELEINE y no únicamente este release congelado.

El estado actual de `main` puede incorporar documentación post-publicación sin modificar el objeto histórico identificado por el tag `v0.2.1`.

Registro completo de preservación: [notes/PUBLICATION_DEPOSIT_RECORD_v0.2.1.md](notes/PUBLICATION_DEPOSIT_RECORD_v0.2.1.md).

## Historial

Las releases y snapshots anteriores se conservan como historia verificable.

No deben confundirse con el paquete final de la fase actual.
