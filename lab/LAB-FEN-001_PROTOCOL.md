# LAB-FEN-001 — Protocolo congelado D0/D1/D2 causal

## Estatuto

Este archivo pertenece al laboratorio fenomenológico y no al canon basal.

Los identificadores experimentales se escriben:

- LAB-D0
- LAB-D1
- LAB-D2

para evitar confusión con la jerarquía canónica D0–D11 de MADELEINE.

---

## Objetivo

Comparar tres arquitecturas causales bajo el mismo contrato de observación:

LAB-D0:
dinámica de primer orden.

LAB-D1:
dinámica rígida de segundo orden.

LAB-D2:
dinámica flexible de segundo orden.

El objetivo no es producir un comportamiento visualmente interesante.

El objetivo es probar si una arquitectura puede sostener simultáneamente:

- historia no reducible a primer orden;
- mejora predictiva por contexto histórico;
- dependencia causal histórica;
- persistencia;
- novedad;
- aperiodicidad.

---

## Firma objetivo

Se congela la firma:

\[
M_{G2}
=
(
A1,
\Delta_{\mathrm{hist}},
C_{\mathrm{hist}},
P_{\mathrm{rel}},
N,
U
).
\]

No se colapsará esta firma a un único escalar.

---

## LAB-D0 — control de primer orden

Regla causal:

\[
x_t
\longrightarrow
x_{t+1}.
\]

La transición futura depende únicamente del estado presente.

Hipótesis de control:

\[
C_{\mathrm{hist}}
\approx 0.
\]

El pasado anterior no debería aportar información causal adicional una vez conocido el presente.

Si LAB-D0 produce una señal histórica fuerte bajo las métricas, deberá sospecharse sesgo del estimador o del muestreo antes de interpretar el resultado.

---

## LAB-D1 — segundo orden rígido

Regla causal:

\[
(x_{t-1},x_t)
\longrightarrow
x_{t+1}.
\]

La transición es determinista para cada contexto de segundo orden.

Hipótesis de control:

- debe existir dependencia histórica genuina;
- A1, Delta_hist o C_hist pueden resultar positivos;
- la rigidez puede reducir U;
- puede aparecer periodicidad o cristalización.

LAB-D1 sirve como control positivo de causalidad histórica y control negativo de flexibilidad.

---

## LAB-D2 — segundo orden flexible

Regla causal:

\[
(x_{t-1},x_t)
\longrightarrow
\mathcal{S}_{t+1},
\]

donde:

\[
\mathcal{S}_{t+1}
\]

es un conjunto permitido de sucesores dependiente del contexto histórico.

La elección efectiva:

\[
x_{t+1}\in\mathcal{S}_{t+1}
\]

no será determinista de forma rígida.

La novedad actuará dentro del conjunto permitido, no modificando retrospectivamente las reglas después de observar resultados.

Dos trayectorias que alcanzan el mismo estado presente podrán tener conjuntos de sucesores diferentes si llegaron mediante historias diferentes.

---

## Condición objetivo de LAB-D2

Un resultado favorable deberá mantener simultáneamente:

\[
A1>0,
\]

\[
\Delta_{\mathrm{hist}}>0,
\]

\[
C_{\mathrm{hist}}>0,
\]

\[
P_{\mathrm{rel}}>0,
\]

\[
N \text{ alto},
\]

\[
U>0.
\]

No se fija todavía un umbral numérico universal para "N alto".

Ese umbral deberá derivarse frente a controles nulos y no elegirse retrospectivamente para favorecer resultados.

---

## Contrato común de comparación

LAB-D0, LAB-D1 y LAB-D2 deberán compartir:

- alfabeto de estados;
- longitud total de trayectoria;
- política de semillas;
- ventanas de análisis;
- partición entrenamiento/prueba;
- definición de métricas;
- nulos disponibles;
- formato de trazas;
- versión del protocolo.

Si cualquiera de estas condiciones cambia, DMO-005 impide considerar las firmas directamente comparables sin declarar primero una traducción.

---

## Nulos

Se usarán progresivamente:

1. i.i.d.;
2. Markov-1;
3. Markov-2 cuando la cantidad de datos lo permita.

El primer objetivo crítico es separar estructura histórica real de una simple gramática Markov-1.

---

## Separación entrenamiento / prueba

Delta_hist y las medidas predictivas históricas deberán evaluarse fuera de muestra.

No se permitirá medir mejora histórica sobre los mismos datos usados para ajustar el predictor.

---

## Ablaciones mínimas

Antes de ampliar el atlas deberán ensayarse al menos:

- eliminar dependencia de x[t-1];
- permutar la historia;
- retrasar artificialmente la señal histórica;
- reemplazar la selección de novedad;
- fijar una elección determinista dentro de los sucesores permitidos.

La pérdida esperada de señal histórica bajo estas ablaciones formará parte del criterio causal.

---

## Regla de aceptación

LAB-FEN-001 no podrá declarar un régimen robusto a partir de una sola ejecución.

DMO-004 será el gate posterior de admisión.

Una candidata deberá demostrar:

- región paramétrica;
- acuerdo entre semillas;
- separación frente a nulos;
- criterio explícito de fallo;
- no reducibilidad;
- regla congelada;
- traza completa.

---

## Regla de falsación inmediata

LAB-D2 falla como candidata G2-PD si ocurre cualquiera de estos casos de forma robusta:

1. A1 no supera al control de primer orden;
2. Delta_hist no es positivo fuera de muestra;
3. C_hist desaparece al controlar por el presente;
4. P_rel colapsa;
5. N desaparece;
6. U colapsa hacia periodicidad dominante;
7. el efecto depende de una sola semilla;
8. el efecto desaparece bajo reconstrucción independiente;
9. una ablación histórica conserva la misma señal atribuida a historia;
10. LAB-D2 se reduce operacionalmente a LAB-D0 o LAB-D1.

---

## Regla anti-ajuste retrospectivo

Una vez generado el primer lote de resultados:

- no se cambiarán las reglas de LAB-D0;
- no se cambiarán las reglas de LAB-D1;
- no se cambiarán las reglas de LAB-D2;
- no se cambiarán las métricas;
- no se cambiarán los criterios de fallo.

Cualquier modificación posterior deberá incrementar explícitamente la versión del experimento.

---

## Primera versión

Protocolo:

LAB-FEN-001-v1

Estado:

CONGELADO ANTES DE RESULTADOS