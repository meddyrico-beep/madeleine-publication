# LAB-FEN-001 — Especificación de ablaciones causales de LAB-D2-v1

## Estatuto

Este documento congela la batería de falsación de LAB-D2-v1 antes de ejecutar ninguna ablación.

Versión:

LAB-D2-ABLATIONS-v1

Referencia candidata:

LAB-D2-v1

Resultado basal congelado:

8/8 semillas superan conjuntamente la firma local LAB-FEN-001-v1.

La finalidad de esta batería no es mejorar LAB-D2-v1.

La finalidad es intentar destruir su resultado mediante intervenciones causales explícitas.

---

# 1. Regla basal

LAB-D2-v1 utiliza:

\[
h(a,b)
=
(b+2a)\bmod5,
\]

con:

\[
a=x_{t-1},
\qquad
b=x_t.
\]

La familia causal es:

\[
\mathcal S(a,b)
=
\{
h(a,b),
h(a,b)+1,
h(a,b)+2
\}
\bmod5.
\]

El sucesor se elige uniformemente dentro de esa familia.

---

# 2. Contrato que permanece fijo

Todas las ablaciones conservarán:

\[
S=\{0,1,2,3,4\}.
\]

También conservarán:

- semillas 11, 23, 37, 51, 79, 101, 131, 173;
- burn-in = 1.000;
- transiciones útiles = 30.000;
- train = 18.000;
- test = 12.000;
- métricas LAB-FEN-001-METRICS-v1;
- nulos ya definidos;
- umbrales T_P, T_N y T_U;
- gate conjunto por semilla;
- requisito global 7/8.

No se recalibrará ninguna métrica usando las ablaciones.

---

# 3. Resultado basal de referencia

LAB-D2-v1 produjo:

\[
8/8
\]

seed passes conjuntos.

La batería de ablaciones no volverá a elegir umbrales a partir de ese resultado.

El basal sirve únicamente como referencia congelada.

---

# 4. Ablación A — NO_PAST

Identificador:

ABL-NO-PAST-v1

Objetivo:

eliminar completamente la dependencia de:

\[
x_{t-1}
\]

manteniendo familia de tamaño tres y elección uniforme.

Se define:

\[
h_0(b)=b.
\]

La familia es:

\[
\mathcal S_0(b)
=
\{
b,
b+1,
b+2
\}
\bmod5.
\]

La transición utiliza únicamente:

\[
x_t.
\]

Por tanto:

\[
P(x_{t+1}\mid x_t,x_{t-1})
=
P(x_{t+1}\mid x_t)
\]

por construcción generativa.

---

# 5. Expectativa congelada para NO_PAST

Esta ablación debe destruir la señal histórica adicional.

Se espera:

\[
A1
\]

sin separación sistemática frente a Markov-1.

También se espera que:

\[
\Delta_{\mathrm{hist}}
\]

y:

\[
C_{\mathrm{hist}}
\]

no produzcan señal robusta de segundo orden.

Gate de falsación:

- A1 positivo en como máximo 1/8 semillas;
- Delta hit en como máximo 1/8 semillas;
- C hit en como máximo 1/8 semillas;
- seed_pass conjunto en 0/8 o, como máximo, 1/8.

Si NO_PAST mantiene 7/8 seed passes conjuntos, la interpretación causal de LAB-D2-v1 queda seriamente debilitada.

---

# 6. Ablación B — RANDOMIZED_PAST

Identificador:

ABL-RANDOMIZED-PAST-v1

Objetivo:

mantener formalmente la misma función:

\[
h(a,b)
\]

pero desacoplar:

\[
a
\]

del pasado real de la trayectoria.

En cada transición se genera:

\[
\tilde a_t
\sim
\mathrm{Uniforme}(S)
\]

independientemente de:

\[
x_{t-1}.
\]

La familia usada será:

\[
\mathcal S(\tilde a_t,x_t).
\]

El sucesor seguirá eligiéndose uniformemente dentro de esa familia.

---

# 7. Fuentes aleatorias en RANDOMIZED_PAST

Para preservar una separación auditable entre elección de sucesor y señal histórica falsa se utilizarán dos generadores.

Generador principal:

random.Random(seed)

Generador de pasado aleatorizado:

random.Random(seed + 1000003)

El generador principal conserva:

- estado inicial;
- elección dentro de la familia.

El segundo generador produce únicamente:

\[
\tilde a_t.
\]

No se reutilizará para elegir sucesores.

---

# 8. Expectativa congelada para RANDOMIZED_PAST

La señal usada como pasado ya no corresponde al pasado causal real.

Por tanto se espera pérdida de ventaja histórica inmediata.

Gate de falsación:

- A1 positivo en como máximo 1/8 semillas;
- Delta hit en como máximo 1/8 semillas;
- C hit en como máximo 1/8 semillas;
- seed_pass conjunto en como máximo 1/8 semillas.

Si RANDOMIZED_PAST conserva 7/8 seed passes conjuntos, la atribución del resultado al alineamiento causal del pasado deberá rechazarse o revisarse.

---

# 9. Ablación C — DETERMINISTIC_CHOICE

Identificador:

ABL-DETERMINISTIC-v1

Objetivo:

conservar exactamente la dependencia histórica de la familia pero eliminar la elección flexible dentro de ella.

Se conserva:

\[
h(a,b)
=
(b+2a)\bmod5.
\]

Pero el sucesor será siempre:

\[
x_{t+1}
=
h(a,b).
\]

No se elegirá entre tres opciones.

La regla queda:

\[
x_{t+1}
=
(x_t+2x_{t-1})\bmod5.
\]

---

# 10. Expectativa congelada para DETERMINISTIC_CHOICE

Esta ablación elimina la apertura local de LAB-D2-v1.

La dinámica resultante es determinista sobre los 25 estados de segundo orden.

Al tratarse de un sistema finito determinista, toda trayectoria termina necesariamente en un ciclo.

Por tanto la predicción principal es:

\[
U\le T_U
\]

en al menos:

\[
7/8
\]

semillas.

También se exige que:

seed_pass conjunto < 7/8.

No se exige de antemano que A1, Delta_hist o C_hist sobrevivan, porque el colapso a un atractor puede reducir el soporte observado y volver la trayectoria parcialmente reducible a primer orden.

---

# 11. Ablación D — DELAYED_PAST

Identificador:

ABL-DELAYED-PAST-v1

Objetivo:

sustituir el pasado inmediato:

\[
x_{t-1}
\]

por:

\[
x_{t-2}.
\]

La familia será:

\[
\mathcal S(x_{t-2},x_t).
\]

La elección dentro de la familia continuará siendo uniforme.

Esta ablación introduce una dependencia real más profunda, pero la desalineea respecto al detector inmediato de orden dos.

---

# 12. Estatuto de DELAYED_PAST

DELAYED_PAST es una prueba diagnóstica.

No se fija como condición necesaria de PASS/FAIL de la batería.

Razón:

\[
x_{t-1}
\]

puede transportar indirectamente información sobre:

\[
x_{t-2},
\]

por lo que la firma de segundo orden puede conservar parte de la señal.

Su resultado se registrará sin reinterpretar retrospectivamente el gate.

Si muestra residuo histórico, podrá motivar posteriormente una prueba explícita de profundidad:

\[
k>2.
\]

---

# 13. Comparabilidad

Cada ablación se evaluará con exactamente la misma firma:

\[
M_{G2}^{v1}
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

No se introducirán métricas específicas para favorecer una ablación.

---

# 14. Gate histórico conjunto auxiliar

Para auditoría se define:

\[
H_s
=
(A1>0)
\land
\text{delta hit}
\land
\text{C hit}.
\]

Este gate auxiliar no reemplaza el gate completo de D2.

Sirve únicamente para leer si una ablación conserva simultáneamente las tres señales históricas.

Se registrará:

\[
\sum_s \mathbf 1[H_s].
\]

---

# 15. Criterios primarios de falsación

La batería primaria se considera compatible con la interpretación causal de LAB-D2-v1 sólo si simultáneamente:

NO_PAST:

\[
H_s
\]

aparece en como máximo 1/8 semillas y no alcanza 7/8 seed passes completos.

RANDOMIZED_PAST:

\[
H_s
\]

aparece en como máximo 1/8 semillas y no alcanza 7/8 seed passes completos.

DETERMINISTIC_CHOICE:

\[
U\le T_U
\]

en al menos 7/8 semillas y no alcanza 7/8 seed passes completos.

DELAYED_PAST:

diagnóstico sin condición obligatoria.

---

# 16. Resultado posible de la batería

Si los tres controles primarios cumplen sus predicciones se podrá afirmar únicamente:

LAS ABLACIONES CAUSALES v1 SON COMPATIBLES CON QUE EL RESULTADO LOCAL DE LAB-D2-v1 DEPENDA DE LA COMBINACION DE HISTORIA ALINEADA Y ELECCION FLEXIBLE.

No se utilizará lenguaje de demostración causal universal.

---

# 17. Falsación de la interpretación

La interpretación actual deberá revisarse si ocurre cualquiera de los siguientes casos:

- NO_PAST mantiene 7/8 seed passes completos;
- RANDOMIZED_PAST mantiene 7/8 seed passes completos;
- NO_PAST mantiene señal histórica conjunta en 7/8;
- RANDOMIZED_PAST mantiene señal histórica conjunta en 7/8;
- DETERMINISTIC_CHOICE mantiene U por encima de T_U en 7/8 y además conserva 7/8 seed passes completos.

Estos resultados no podrán descartarse como anomalías después de observarlos.

---

# 18. No ajuste retrospectivo

Después de la primera ejecución de las ablaciones no podrán modificarse bajo v1:

- definiciones de las cuatro ablaciones;
- semillas;
- longitudes;
- generadores pseudoaleatorios;
- métricas;
- umbrales;
- definición H_s;
- criterios primarios de falsación.

Cualquier modificación exigirá:

LAB-D2-ABLATIONS-v2.

---

# 19. Orden experimental

El orden será:

1. congelar esta especificación;
2. implementar el ejecutable de ablaciones;
3. verificar únicamente sintaxis y estructura;
4. congelar el ejecutable;
5. ejecutar la batería por primera vez;
6. registrar series y resultados;
7. aplicar literalmente los criterios anteriores;
8. sólo después decidir si procede un atlas paramétrico.

---

# 20. Alcance

Una batería favorable no convierte LAB-D2-v1 en régimen robusto.

Todavía quedarán pendientes:

- región paramétrica;
- vecindad de arquitecturas;
- reproducibilidad más allá del conjunto inicial de semillas;
- pruebas de perturbación;
- no reducibilidad respecto de otros mecanismos;
- gate completo DMO-004.

---

## Estado

BATERIA DE ABLACIONES CAUSALES v1 DEFINIDA — AUN NO EJECUTADA