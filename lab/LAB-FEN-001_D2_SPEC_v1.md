# LAB-FEN-001 — Especificación congelada de LAB-D2 v1

## Estatuto

Este documento define LAB-D2-v1 antes de escribir o ejecutar su dinámica.

Versión:

LAB-D2-v1

LAB-D2 es una construcción experimental interna.

No pertenece al canon basal y no debe confundirse con D2 de la jerarquía canónica D0-D11.

Su objetivo es comprobar si una dinámica de segundo orden puede combinar simultáneamente:

- dependencia histórica;
- persistencia;
- diversidad histórica;
- ausencia de periodicidad dominante.

---

# 1. Posición experimental

LAB-D0-v1 representa:

\[
\text{apertura sin historia irreductible}.
\]

LAB-D1-v1 representa:

\[
\text{historia fuerte con ciclo rígido}.
\]

LAB-D2-v1 busca:

\[
\text{historia}
+
\text{flexibilidad}
+
\text{persistencia}
+
\text{aperiodicidad}.
\]

No se interpola un peso entre D0 y D1.

Se cambia la arquitectura causal.

---

# 2. Alfabeto

Se conserva:

\[
S=\{0,1,2,3,4\}.
\]

Los estados son símbolos discretos sin interpretación geométrica en esta fase.

---

# 3. Estado causal

La regla generadora recibe exactamente:

\[
(x_{t-1},x_t).
\]

Por tanto LAB-D2-v1 es una dinámica de segundo orden.

---

# 4. Familia de sucesores

Sean:

\[
a=x_{t-1},
\qquad
b=x_t.
\]

Se define:

\[
h(a,b)
=
(b+2a)\bmod5.
\]

La familia permitida es:

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

Para los 25 contextos:

\[
|\mathcal S(a,b)|=3.
\]

---

# 5. Dependencia histórica

Para un presente fijo:

\[
b,
\]

los cinco pasados posibles:

\[
a\in S
\]

generan cinco familias distintas.

Por tanto el conjunto de futuros posibles depende explícitamente de:

\[
x_{t-1}.
\]

Esta dependencia deberá comprobarse estructuralmente en el ejecutable antes de producir resultados.

---

# 6. Flexibilidad

A diferencia de LAB-D1-v1, un contexto no determina un único sucesor.

Cada contexto permite exactamente tres.

Por tanto la regla generadora es histórica pero no determinista.

---

# 7. Regla de elección

Dada:

\[
\mathcal S(a,b)
=
\{s_1,s_2,s_3\},
\]

el sucesor se selecciona uniformemente:

\[
P(x_{t+1}=s_i\mid a,b)
=
\frac13.
\]

Para cualquier estado no perteneciente a la familia:

\[
P(x_{t+1}=s\mid a,b)=0.
\]

---

# 8. Novedad operacional

LAB-D2-v1 no utilizará:

- refuerzo;
- premio retrospectivo;
- frecuencia histórica acumulada;
- elección del estado menos visitado;
- controlador adaptativo;
- pesos ajustables.

La apertura se implementa únicamente mediante elección uniforme dentro de la familia histórica permitida.

Esta es una decisión de laboratorio v1 y no una definición universal de novedad.

---

# 9. Soporte estructural

Existen:

\[
5^2=25
\]

contextos.

Cada contexto admite tres sucesores.

Por tanto existen exactamente:

\[
25\times3=75
\]

trigramas permitidos.

El ejecutable deberá verificar exactamente 75.

---

# 10. Grafo causal de segundo orden

Cada nodo es:

\[
(a,b).
\]

Cada transición tiene la forma:

\[
(a,b)
\rightarrow
(b,c)
\]

con:

\[
c\in\mathcal S(a,b).
\]

Antes de cualquier resultado el ejecutable deberá verificar:

- 25 nodos;
- grado de salida 3 en todos los nodos;
- 75 aristas;
- conectividad fuerte;
- exactamente los auto-bucles estructurales previstos.

Los auto-bucles previstos son:

\[
(0,0),
\qquad
(2,2),
\qquad
(4,4).
\]

Estas verificaciones son controles de implementación, no evidencia fenomenológica.

---

# 11. Ausencia de periodo impuesto

La regla no contiene un ciclo global preprogramado.

La presencia de auto-bucles y múltiples salidas impide que la construcción sea el ciclo determinista de LAB-D1.

Esto no demuestra de antemano que la trayectoria observada sea aperiódica.

La aperiodicidad será medida posteriormente mediante U-v1.

---

# 12. Semillas

Se utilizan exactamente:

11
23
37
51
79
101
131
173

No se añadirán semillas después de observar resultados.

---

# 13. Longitudes

Se conservan:

- burn-in = 1.000;
- transiciones útiles = 30.000;
- train = 18.000;
- test = 12.000.

---

# 14. Estado inicial

Para cada semilla:

- x[-1] se toma uniformemente de S;
- x[0] se toma uniformemente de S.

Se utilizará exclusivamente:

random.Random(seed)

como fuente pseudoaleatoria de esa trayectoria.

---

# 15. Generación

Después del estado inicial, cada paso realiza:

1. leer (x[t-1], x[t]);
2. calcular h(a,b);
3. construir los tres sucesores permitidos;
4. elegir uniformemente uno de ellos;
5. avanzar al nuevo contexto.

No existirá ninguna variable de memoria adicional oculta.

---

# 16. Contrato instrumental

LAB-D2-v1 utilizará sin modificación las métricas congeladas:

\[
A1,
\Delta_{\mathrm{hist}},
C_{\mathrm{hist}},
P_{\mathrm{rel}},
N,
U.
\]

Fuentes:

`lab/LAB-FEN-001_METRICS_v1.md`

`lab/LAB-FEN-001_THRESHOLDS_v1.md`

---

# 17. Umbrales congelados

Se mantienen:

\[
T_P
=
0.5075018151904057,
\]

\[
T_N
=
0.3862533855592818,
\]

\[
T_U
=
0.4908272358457767.
\]

No se recalibrarán usando resultados de D2.

---

# 18. Gate conjunto por semilla

Una semilla sólo pasa si simultáneamente:

    A1 > 0

    delta_hist > 0

    delta_hit == True

    c_hist > 0

    c_hit == True

    P_rel > 0.5075018151904057

    N > 0.3862533855592818

    U > 0.4908272358457767

No se permite compensación entre coordenadas.

---

# 19. Gate global

LAB-D2-v1 supera su primera firma local únicamente si:

\[
\text{seed passes}\ge7/8.
\]

Las siete semillas deben pasar conjuntamente todas las condiciones.

No se utilizarán mayorías independientes por métrica.

---

# 20. Interpretación de PASS

Un PASS significará únicamente:

CANDIDATA INTERNA QUE SUPERA LA FIRMA LOCAL LAB-FEN-001-v1.

No significará:

- G2-PD robusta;
- régimen aceptado;
- geometría emergente;
- resultado físico;
- claim externo.

Un único punto favorable no constituye una región paramétrica.

---

# 21. Interpretación de FAIL

Un FAIL será un resultado experimental válido.

Después de observarlo no podrán modificarse bajo v1:

- h(a,b);
- tamaño 3 de la familia;
- distribución uniforme;
- semillas;
- longitudes;
- métricas;
- umbrales;
- gate 7/8.

Una arquitectura modificada deberá llamarse:

LAB-D2-v2.

---

# 22. Fase posterior a un PASS

Sólo después de un PASS local se permitirá estudiar:

- región paramétrica;
- ablaciones;
- perturbaciones;
- eliminación del pasado;
- permutación del pasado;
- retrasos;
- determinización de la familia;
- reducción a primer orden.

Después deberá aplicarse el gate de DMO-004.

---

# 23. Condición de régimen

Para considerar posteriormente un régimen deberán verificarse:

1. región paramétrica;
2. acuerdo entre semillas;
3. separación frente a nulos;
4. criterio explícito de fallo;
5. no reducibilidad;
6. regla congelada;
7. trazabilidad completa.

LAB-D2-v1 por sí sola no puede satisfacer todavía esta condición completa.

---

# 24. Orden obligatorio

El orden experimental queda fijado:

1. congelar esta especificación;
2. escribir el ejecutable;
3. verificar sintaxis y estructura;
4. congelar el ejecutable;
5. ejecutar por primera vez;
6. guardar serie y resultados;
7. aplicar los gates sin modificarlos;
8. registrar PASS o FAIL;
9. decidir la siguiente fase sólo después.

---

## Estado

LAB-D2-v1 DISEÑADA — AUN NO EJECUTADA