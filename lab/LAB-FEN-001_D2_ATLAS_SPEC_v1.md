# LAB-FEN-001 — Atlas local paramétrico de LAB-D2-v1

## Estatuto

Este documento congela antes de resultados el primer atlas local alrededor de LAB-D2-v1.

Versión:

LAB-D2-ATLAS-v1

Basal de referencia:

LAB-D2-v1.

Resultado basal ya congelado:

8/8 seed passes conjuntos.

Resultado previo de ablaciones:

ABLATION BATTERY v1 PASS.

El objetivo de este atlas no es buscar retrospectivamente una regla que pase.

El objetivo es comprobar si la firma local de LAB-D2-v1 ocupa una región paramétrica predeclarada.

---

# 1. Regla causal basal

El alfabeto permanece:

\[
S=\{0,1,2,3,4\}.
\]

Para:

\[
a=x_{t-1},
\qquad
b=x_t,
\]

se conserva:

\[
h(a,b)
=
(b+2a)\bmod5.
\]

Los tres sucesores causales basales siguen siendo:

\[
h,
\qquad
h+1,
\qquad
h+2
\pmod5.
\]

La dependencia histórica no se modifica en este atlas.

---

# 2. Parámetro beta

Se introduce:

\[
\beta
\]

como deformación de las probabilidades dentro de la familia causal.

Antes de fuga:

\[
w_0
=
\frac13+\beta,
\]

\[
w_1
=
\frac13,
\]

\[
w_2
=
\frac13-\beta.
\]

Por construcción:

\[
w_0+w_1+w_2=1.
\]

El atlas utilizará:

\[
\beta
\in
\{
-0.10,
-0.05,
0,
0.05,
0.10
\}.
\]

En todo el rango:

\[
w_j>0.
\]

El punto:

\[
\beta=0
\]

recupera la elección uniforme dentro de la familia.

---

# 3. Parámetro epsilon

Se introduce:

\[
\varepsilon
\]

como fuga uniforme hacia el alfabeto completo.

El atlas utilizará:

\[
\varepsilon
\in
\{
0,
0.05,
0.10,
0.15
\}.
\]

Con probabilidad:

\[
1-\varepsilon
\]

se utiliza la distribución histórica deformada por beta.

Con probabilidad:

\[
\varepsilon
\]

el sucesor se distribuye uniformemente sobre:

\[
S.
\]

---

# 4. Distribución final

Para:

\[
j\in\{0,1,2\},
\]

el estado:

\[
c=(h+j)\bmod5
\]

recibe probabilidad:

\[
P(c\mid a,b;\beta,\varepsilon)
=
(1-\varepsilon)w_j
+
\frac{\varepsilon}{5}.
\]

Cada uno de los otros dos estados recibe:

\[
P(c\mid a,b;\beta,\varepsilon)
=
\frac{\varepsilon}{5}.
\]

La suma total debe ser exactamente:

\[
1.
\]

---

# 5. Punto basal

El punto conceptual:

\[
(\beta,\varepsilon)
=
(0,0)
\]

es exactamente la distribución de LAB-D2-v1:

\[
P(h)=P(h+1)=P(h+2)=\frac13.
\]

El resultado basal ya está congelado como:

8/8 seed passes.

No se recalibrará usando el atlas.

El atlas importará ese punto como referencia congelada.

---

# 6. Malla completa

La malla completa contiene:

\[
5\times4=20
\]

puntos paramétricos.

Valores beta:

- -0.10
- -0.05
- 0
- +0.05
- +0.10

Valores epsilon:

- 0
- 0.05
- 0.10
- 0.15

El punto basal:

\[
(0,0)
\]

ya posee resultado congelado.

Por tanto el ejecutable producirá nuevas trayectorias para:

\[
19
\]

puntos.

---

# 7. Núcleo regional predeclarado

Antes de observar el atlas se define el núcleo:

\[
\beta
\in
\{
-0.05,
0,
0.05
\},
\]

\[
\varepsilon
\in
\{
0,
0.05,
0.10
\}.
\]

Esto produce un rectángulo de:

\[
3\times3=9
\]

puntos.

El basal:

\[
(0,0)
\]

forma parte de este núcleo.

---

# 8. Contrato experimental

Se conservan exactamente:

- semillas 11, 23, 37, 51, 79, 101, 131, 173;
- burn-in = 1000;
- transiciones útiles = 30000;
- train = 18000;
- test = 12000;
- LAB-FEN-001-METRICS-v1;
- nulos congelados;
- T_P congelado;
- T_N congelado;
- T_U congelado;
- gate conjunto por semilla;
- requisito de 7/8 semillas.

No se recalibrará ninguna coordenada a partir del atlas.

---

# 9. Gate por semilla

Una semilla pasa únicamente si satisface conjuntamente:

\[
A1>0,
\]

\[
\Delta_{\mathrm{hist}}>0,
\]

Delta hit,

\[
C_{\mathrm{hist}}>0,
\]

C hit,

\[
P_{\mathrm{rel}}
>
0.5075018151904057,
\]

\[
N
>
0.3862533855592818,
\]

\[
U
>
0.4908272358457767.
\]

No existe compensación entre coordenadas.

---

# 10. Gate por punto paramétrico

Un punto:

\[
(\beta,\varepsilon)
\]

se clasifica como:

POINT PASS

si al menos:

\[
7/8
\]

semillas satisfacen simultáneamente el gate completo.

En caso contrario:

POINT FAIL.

---

# 11. Gate primario de región

El atlas declara:

LOCAL PARAMETRIC REGION v1 PASS

únicamente si los nueve puntos del núcleo predeclarado son POINT PASS.

Formalmente:

\[
9/9
\]

puntos del núcleo deben pasar.

No se permitirá después:

- eliminar un punto fallido;
- reducir el núcleo;
- mover sus fronteras;
- cambiar 7/8;
- cambiar los umbrales.

---

# 12. Malla extendida

Los once puntos restantes de la malla completa se consideran extensión descriptiva del atlas.

Sus resultados se registrarán todos.

No son necesarios para el booleano primario 9/9.

Servirán para observar:

- extensión de la región;
- posibles fronteras;
- degradación de métricas;
- asimetría respecto a beta;
- sensibilidad a epsilon.

No se declarará una nueva frontera formal usando esos resultados bajo v1.

---

# 13. Adyacencia

Para descripción topológica se consideran vecinos dos puntos si difieren en exactamente un paso de la malla en uno de los parámetros y coinciden en el otro.

No se permiten conexiones diagonales.

Esta definición se congela antes de observar resultados.

---

# 14. Componente basal

Después de ejecutar el atlas se calculará el componente conexo de POINT PASS que contiene:

\[
(0,0).
\]

Su tamaño se registrará como diagnóstico.

No sustituye el gate primario 9/9.

---

# 15. Generación pseudoaleatoria

Cada punto utilizará:

`random.Random(seed)`

para cada una de las ocho semillas.

Se extraerán primero:

1. x[-1];
2. x[0].

En cada transición posterior se extraerá un valor uniforme:

\[
u\in[0,1)
\]

y se seleccionará el sucesor mediante la distribución categórica final correspondiente a:

\[
(\beta,\varepsilon,a,b).
\]

El mismo esquema se utilizará en todos los puntos nuevos del atlas.

---

# 16. Basal y pseudoaleatoriedad

El punto basal no se volverá a utilizar como nueva réplica para redefinir su resultado.

Su condición PASS proviene del resultado congelado de LAB-D2-v1.

Esto evita sustituir retrospectivamente el basal por otra trayectoria pseudoaleatoria de la misma distribución.

---

# 17. Verificaciones estructurales previas

Antes de ejecutar trayectorias, el ejecutable deberá verificar para los 20 puntos:

- cinco probabilidades por contexto;
- ninguna probabilidad negativa;
- ninguna probabilidad mayor que uno;
- suma igual a uno dentro de tolerancia numérica;
- los 25 contextos históricos;
- dependencia de h respecto al pasado preservada;
- coincidencia analítica del punto (0,0) con la distribución basal D2.

Estas verificaciones no constituyen resultados fenomenológicos.

---

# 18. Falsación primaria

La hipótesis experimental local v1 queda falsada si cualquiera de los nueve puntos del núcleo obtiene:

POINT FAIL.

En ese caso:

LOCAL PARAMETRIC REGION v1 FAIL.

No se buscará retrospectivamente un rectángulo menor bajo la misma versión.

---

# 19. Interpretación permitida si pasa

Si los nueve puntos del núcleo son POINT PASS podrá afirmarse:

LAB-D2-v1 NO ES UN PUNTO AISLADO BAJO LAS PERTURBACIONES PARAMETRICAS v1 DECLARADAS.

También podrá afirmarse:

EXISTE UNA REGION PARAMETRICA LOCAL v1 EN EL DOMINIO EXPERIMENTAL DEFINIDO.

Estas afirmaciones quedan restringidas al atlas y a sus métricas.

---

# 20. Interpretación no permitida

Incluso con 9/9 no podrá afirmarse automáticamente:

- universalidad;
- necesidad matemática;
- unicidad del mecanismo;
- robustez frente a toda perturbación;
- G2-PD universal;
- geometría emergente;
- interpretación física;
- validación externa.

---

# 21. Relación con las ablaciones

Las ablaciones v1 y el atlas responden preguntas distintas.

Las ablaciones comprobaron pérdida selectiva de la firma al:

- eliminar el pasado;
- desacoplar el pasado;
- eliminar flexibilidad.

El atlas pregunta ahora si la candidata sobrevive a deformaciones cuantitativas que conservan su arquitectura causal básica.

Los dos resultados no se sustituirán entre sí.

---

# 22. Relación con DMO-004

Un REGION PASS satisfaría el requisito interno de disponer de una región paramétrica local bajo este contrato.

No bastará por sí solo para promover un régimen.

Después deberán auditarse conjuntamente:

- acuerdo entre semillas;
- separación de nulos;
- criterio de fallo explícito;
- no reducibilidad;
- regla congelada;
- trazabilidad completa.

Sólo entonces procederá evaluar formalmente el gate DMO-004.

---

# 23. Orden experimental

El orden queda congelado:

1. congelar esta especificación;
2. implementar el ejecutable;
3. verificar sintaxis y estructura sin trayectorias;
4. congelar el ejecutable;
5. ejecutar por primera vez los 19 puntos nuevos;
6. registrar todos los resultados;
7. aplicar literalmente POINT PASS;
8. aplicar literalmente el gate 9/9;
9. registrar el componente basal;
10. congelar trazas;
11. sólo después evaluar DMO-004.

---

# 24. Regla anti-ajuste

Después de la primera ejecución no podrán modificarse bajo v1:

- la malla;
- el núcleo 3x3;
- el requisito 9/9;
- el requisito 7/8 por punto;
- beta;
- epsilon;
- la distribución de transición;
- semillas;
- longitudes;
- métricas;
- umbrales;
- adyacencia;
- definición del componente basal.

Cualquier modificación requerirá:

LAB-D2-ATLAS-v2.

---

## Estado

ATLAS LOCAL PARAMETRICO LAB-D2-v1 DEFINIDO — AUN NO EJECUTADO