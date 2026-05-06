# MADELEINE publication — reporte de limpieza
## Resumen
- Archivos antes: 932
- Tamaño antes: 69.31 MB
- Archivos después: 88
- Tamaño después: 0.86 MB
- Reducción aproximada: 68.45 MB

## Política aplicada
- Se conservan fuentes LaTeX vigentes en `manuscript/`, estilos compartidos, herramientas, PDFs finales en `artifacts/pdf/` y paquete final en `artifacts/release_final_20260418_112102/`.
- Se eliminan snapshots acumulativos, backups, auxiliares de compilación, PDFs generados dentro de `manuscript/`, `.bak`, árbol legacy `tomo1/`, candidatos diferidos y notas incrementales no rectoras.
- El ZIP limpio no incluye `.git`; el script local `tools/clean_publication_repo.ps1` no elimina `.git`.

## Eliminado por categoría
- snapshots acumulativos ZIP; ruido de historial y peso innecesario: 302 archivos, 63.59 MB
- copias de seguridad y reconstrucciones históricas; conservar fuera de la repo publicable: 260 archivos, 2.60 MB
- paquete ZIP generado dentro de la repo; evitar ZIP dentro de ZIP: 2 archivos, 0.64 MB
- release anterior reemplazado por release_final: 7 archivos, 0.33 MB
- PDF generado dentro de manuscript; salida canónica queda en artifacts/pdf o release_final: 4 archivos, 0.33 MB
- árbol legacy duplicado; fuente vigente está en manuscript/tomo1: 33 archivos, 0.28 MB
- addenda acumulativos de construcción; no corpus publicable limpio: 58 archivos, 0.21 MB
- auxiliar de compilación LaTeX (*.log): 4 archivos, 0.18 MB
- auxiliar de compilación LaTeX (*.aux): 4 archivos, 0.05 MB
- historial Git local: no debe viajar en ZIP de publicación limpio: 51 archivos, 0.03 MB
- auxiliar de compilación LaTeX (*.toc): 4 archivos, 0.03 MB
- nota incremental de construcción; no fuente rectora publicable: 74 archivos, 0.03 MB
- candidato diferido no admitido al manuscrito: 2 archivos, 0.01 MB
- notas de integración/reserva históricas; conservar fuera de repo limpia: 3 archivos, 0.00 MB
- nota auxiliar no rectora en versión limpia: 1 archivos, 0.00 MB
- backup local .bak: 2 archivos, 0.00 MB

## Elementos clave conservados
- `README.md`
- `MANIFESTO.md`
- `ADMISSION_RULES.md`
- `.gitignore`
- `manuscript/base_axiomatica/main.tex`
- `manuscript/tomo1/main.tex`
- `manuscript/tomo2/main.tex`
- `manuscript/tomo3/main.tex`
- `manuscript/shared/madeleine_style.tex`
- `tools/build.ps1`
- `tools/test.ps1`
- `tools/clean_publication_repo.ps1`
- `artifacts/pdf/tomo1.pdf`
- `artifacts/pdf/tomo2.pdf`
- `artifacts/pdf/tomo3.pdf`
- `artifacts/release_final_20260418_112102`

## Observación de compilación
En este entorno Linux la compilación con XeLaTeX no pudo verificarse por ausencia de la fuente `Latin Modern Roman` para fontspec. Esto no implica error del repo si en Windows/MiKTeX la fuente está instalada.

## Ajuste adicional
- Se eliminó `manuscript/tomo3/sections_legacy_tail_20260418_104238/` porque no está referenciado por `manuscript/tomo3/main.tex` y funcionaba como cola legacy/futuro repetitivo.
