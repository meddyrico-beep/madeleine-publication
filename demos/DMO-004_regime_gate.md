# DMO-004 — Gate duro de aceptación de régimen

## Claim asociado

C020 — Un régimen verificable exige condiciones internas explícitas antes de cualquier afirmación externa.

---

## Propósito

Formalizar un criterio mínimo, determinista y auditable para decidir si una candidata puede ser aceptada como régimen interno.

Esta demo no determina si un fenómeno físico es real y tampoco valida por sí sola ninguna candidata fenomenológica concreta.

Su función es convertir una regla metodológica en un gate ejecutable con condiciones explícitas de aceptación y fallo.

---

## Regla dura

Una candidata sólo cruza el gate si satisface simultáneamente:

1. ocupa una región paramétrica;
2. presenta acuerdo entre semillas;
3. se separa de controles nulos;
4. posee criterio explícito de fallo;
5. no es reducible a un caso límite de otro régimen;
6. utiliza una regla congelada antes de evaluar resultados;
7. conserva una traza completa de ejecución.

Definimos:

\[
G(R)
=
R_{\mathrm{region}}
\land
R_{\mathrm{semillas}}
\land
R_{\mathrm{nulos}}
\land
R_{\mathrm{fallo}}
\land
R_{\mathrm{no\ reducible}}
\land
R_{\mathrm{regla\ congelada}}
\land
R_{\mathrm{traza}}.
\]

La candidata es aceptada si y sólo si:

\[
G(R)=1.
\]

---

## Implementación

Script:

`demos/DMO-004_regime_gate.py`

Los siete criterios se representan como variables booleanas explícitas.

La evaluación devuelve aceptación únicamente cuando ninguna cláusula falla y conserva la lista exacta de fallos en cualquier otro caso.

---

## Prueba 1 — caso completo

Se construyó una candidata que satisface las siete condiciones.

Resultado observado:

    GATE: ACCEPTED_AS_REGIME
    fallos: NINGUNO

---

## Prueba 2 — ablación de cláusulas

Se apagó individualmente cada una de las siete condiciones manteniendo las restantes activas.

En todos los casos la salida cambió de:

    ACCEPTED_AS_REGIME

a:

    NOT_ACCEPTED_AS_REGIME

Esto verifica que la implementación no ignora ninguna cláusula declarada.

No demuestra de forma independiente que las siete cláusulas sean requisitos universales.

---

## Prueba 3 — barrido exhaustivo

Con siete condiciones booleanas existen:

\[
2^7=128
\]

configuraciones posibles.

El barrido produjo:

- 128 configuraciones totales;
- 1 configuración aceptada;
- 127 configuraciones rechazadas.

La única configuración aceptada es aquella en la que las siete condiciones se satisfacen simultáneamente.

---

## Casos límite

La demo rechaza explícitamente:

- ausencia de región paramétrica;
- dependencia de una semilla;
- incapacidad para superar nulos;
- ausencia de criterio de fallo;
- reducibilidad a otro régimen;
- regla no congelada;
- traza incompleta.

Cada rechazo conserva su causa.

---

## Qué demuestra

DMO-004 demuestra que la regla metodológica declarada puede representarse mediante:

\[
\text{evidencia}
\rightarrow
\text{checks}
\rightarrow
\text{aceptación o fallo}
\rightarrow
\text{causa auditable}.
\]

También verifica exhaustivamente que el programa implementado acepta exactamente una de las 128 configuraciones booleanas posibles.

---

## Qué no demuestra

DMO-004 no demuestra:

- que estas siete cláusulas sean axiomas universales de verificabilidad;
- que R1, R2, R3, R4 u otra candidata satisfagan realmente el gate;
- que una candidata aceptada tenga significado físico;
- que superar el gate implique validación externa;
- que las métricas fenomenológicas sean correctas o suficientes.

Los valores de cada criterio deben proceder de experimentos y artefactos independientes.

---

## Relación con el laboratorio fenomenológico

La exploración posterior exige evitar que una realización aislada o atractiva sea promovida prematuramente a régimen.

DMO-004 separa:

\[
\text{qué ocurrió en el experimento}
\]

de:

\[
\text{si la evidencia cumple los requisitos declarados para llamarlo régimen}.
\]

La primera cuestión pertenece al laboratorio fenomenológico.

La segunda pertenece al gate de DMO-004.

---

## Estado

CONSTRUIDA — INTERNA — REPRODUCIBLE — BARRIDO EXHAUSTIVO DEL GATE