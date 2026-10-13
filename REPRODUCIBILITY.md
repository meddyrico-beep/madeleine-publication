# MADELEINE — Reproducibility

## 1. Alcance

Este documento describe cómo verificar y reproducir los artefactos de la fase pública actual de MADELEINE.

Se distinguen tres operaciones diferentes:

1. build editorial de los manuscritos;
2. verificación no destructiva de la estructura experimental;
3. reproducción completa de los resultados numéricos congelados.

La reproducción numérica completa debe realizarse en un clone o copia descartable del repositorio porque varios scripts escriben o sobrescriben archivos bajo `lab/results/`.

No se recomienda ejecutar la reproducción completa sobre el checkout canónico usado para preparar una release.

## 2. Entorno validado

El entorno local utilizado para esta fase fue:

- Windows 11;
- PowerShell;
- Python 3.13.5;
- XeLaTeX;
- Biber.

Los scripts Python auditados para esta fase utilizan únicamente módulos de la biblioteca estándar de Python.

No existe actualmente una dependencia Python externa declarada ni se requiere un `requirements.txt` para los scripts incluidos en esta fase.

Esta afirmación describe el entorno validado de la release y no garantiza compatibilidad automática con cualquier versión anterior o futura de Python.

## 3. Build editorial

Desde la raíz del repositorio:

    .\tools\build.ps1 -Piece all

El script compila:

- Base Axiomática técnica;
- Tomo I;
- Tomo II;
- Tomo III.

Los PDFs resultantes se copian a `artifacts/pdf/`.

La salida pública principal es:

    artifacts/pdf/tomo1.pdf
    artifacts/pdf/tomo2.pdf
    artifacts/pdf/tomo3.pdf

La Base Axiomática se conserva como soporte técnico interno.

## 4. Gate editorial

Ejecutar:

    .\tools\test.ps1

Este gate comprueba actualmente las fuentes LaTeX frente a mojibake y placeholders editoriales bloqueantes.

No es una suite científica completa.

## 5. Verificación estructural no destructiva

Los siguientes comandos comprueban contratos, arquitectura o schemas sin regenerar las trayectorias principales:

    python .\lab\LAB-FEN-001_D2.py --check-structure
    python .\lab\LAB-FEN-001_D2_ABLATIONS.py --check-structure
    python .\lab\LAB-FEN-001_D2_ATLAS.py --check-structure
    python .\lab\LAB-FEN-001_D2_DMO004_AUDIT.py --check-structure
    python .\lab\LAB-FEN-001_HISTORY_DEPTH.py --check-structure
    python .\lab\LAB-FEN-001_HISTORY_DEPTH_ATLAS.py --check-structure

Estos gates son apropiados para la verificación de una release cuando no se desea alterar los resultados congelados.

## 6. Artefactos numéricos congelados

Los resultados versionados se encuentran bajo:

    lab/results/

Incluyen artefactos de:

- LAB-D0;
- LAB-D1;
- calibración METRICS-v1;
- LAB-D2;
- ablaciones de LAB-D2;
- atlas local de LAB-D2;
- auditoría DMO-004;
- HISTORY-DEPTH-v1;
- HISTORY-DEPTH-ATLAS-v1.

Los archivos `*_RESULT_v1.md` y `*_SPEC_v1.md` asociados documentan respectivamente el resultado y el contrato experimental.

## 7. Reproducción científica completa

ADVERTENCIA: ejecutar esta sección únicamente en un clone o copia descartable.

El orden de reproducción es:

    python .\lab\LAB-FEN-001_D0.py
    python .\lab\LAB-FEN-001_D1.py
    python .\lab\LAB-FEN-001_METRICS_v1.py
    python .\lab\LAB-FEN-001_D2.py
    python .\lab\LAB-FEN-001_D2_ABLATIONS.py
    python .\lab\LAB-FEN-001_D2_ATLAS.py
    python .\lab\LAB-FEN-001_D2_DMO004_AUDIT.py
    python .\lab\LAB-FEN-001_HISTORY_DEPTH.py
    python .\lab\LAB-FEN-001_HISTORY_DEPTH_ATLAS.py

El orden refleja las dependencias entre controles, calibración, candidata D2, ablaciones, atlas y profundidad histórica.

Una reproducción correcta debe evaluarse frente a las especificaciones y actas versionadas, no únicamente frente a texto impreso en consola.

## 8. Demos formales y metodológicas

Las demos pueden ejecutarse directamente con Python:

    python .\demos\DMO-002_balanced.py
    python .\demos\DMO-002_double_register.py
    python .\demos\DMO-002_formula_verify.py
    python .\demos\DMO-002_sweep.py
    python .\demos\DMO-003_channels_projection.py
    python .\demos\DMO-003_formula_verify.py
    python .\demos\DMO-004_regime_gate.py
    python .\demos\DMO-005_comparability_gate.py
    python .\demos\DMO-006_translation_accounting.py

Estas demos tienen alcance formal o metodológico interno.

No constituyen por sí solas validación física externa.

## 9. Conservación del checkout canónico

Antes y después de una verificación de release se recomienda comprobar:

    git status --short

En el checkout canónico de release la salida esperada es vacía.

Si una reproducción numérica completa modifica archivos versionados bajo `lab/results/`, no debe mezclarse ese estado con el proceso de empaquetado final.

## 10. Interpretación de los resultados

LAB-FEN-001 y sus extensiones constituyen evidencia interna bajo protocolos declarados.

Los resultados actuales no establecen por sí solos:

- validación física externa;
- universalidad;
- identificación de una constante física;
- orden Markoviano universal;
- necesidad física de una geometría determinada;
- sustitución de teorías clásicas.

En particular, `k*` representa profundidad histórica operativa bajo HISTORY-DEPTH-v1 y dentro del dominio ensayado.

## 11. Trazabilidad

Para interpretar una salida deben consultarse conjuntamente:

    lab/*_SPEC_v1.md
    lab/*_RESULT_v1.md
    lab/results/
    demos/
    notes/

La fuerza de cualquier claim público queda limitada por el protocolo, dominio y evidencia que lo soportan.
