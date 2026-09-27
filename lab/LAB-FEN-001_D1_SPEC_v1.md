# LAB-FEN-001 — Especificación congelada de LAB-D1 v1

## Estatuto

Este documento concreta LAB-D1 antes de ejecutar resultados.

LAB-D1 es el control positivo de dependencia histórica de segundo orden.

No debe confundirse con D1 de la jerarquía canónica D0-D11.

Versión:

LAB-D1-v1

---

## Objetivo

Comprobar que el mismo bloque instrumental que no detectó historia robusta en LAB-D0-v1 sí detecta dependencia histórica cuando la regla generadora depende explícitamente de:

\[
(x_{t-1},x_t).
\]

LAB-D1 está diseñado como control positivo de historia causal y como control negativo de aperiodicidad.

---

## Contrato común con LAB-D0

Se conservan exactamente:

- alfabeto de cinco estados;
- ocho semillas;
- burn-in;
- longitud útil;
- partición train/test;
- suavizado;
- número de nulos;
- definición de Delta_hist;
- definición de C_hist;
- procedimiento de permutación condicionada;
- percentil 95;
- política de señal entre semillas.

No se redefinirán los estimadores después de haber observado LAB-D0.

El ejecutable de LAB-D1 deberá reutilizar el bloque instrumental congelado en:

`lab/LAB-FEN-001_D0.py`

sin modificar las funciones de estimación.

---

## Alfabeto

\[
S=\{0,1,2,3,4\}.
\]

Los símbolos carecen de interpretación geométrica.

---

## Construcción de segundo orden

Se congela la secuencia cíclica:

\[
B=
0010203041121314223244.
\]

Como lista:

\[
B=
(
0,0,1,0,2,0,3,0,4,
1,1,2,1,3,1,4,
2,2,3,2,4,
3,3,4,4
).
\]

Su longitud es:

\[
|B|=25.
\]

Leyendo B cíclicamente, cada par ordenado:

\[
(a,b)\in S^2
\]

aparece exactamente una vez.

Por tanto:

\[
|\{(B_i,B_{i+1})\}|=25=|S|^2.
\]

---

## Regla generadora

Para cada par:

\[
(B_i,B_{i+1}),
\]

se define:

\[
F(B_i,B_{i+1})=B_{i+2},
\]

con índices tomados módulo 25.

Así:

\[
x_{t+1}
=
F(x_{t-1},x_t).
\]

La regla es determinista y explícitamente de segundo orden.

---

## Propiedad histórica

Para un mismo estado presente:

\[
x_t=b,
\]

existen diferentes valores de:

\[
x_{t-1}
\]

que producen diferentes sucesores.

Por tanto el estado presente aislado no determina el futuro.

Formalmente existen:

\[
a_1\neq a_2
\]

tales que:

\[
F(a_1,b)
\neq
F(a_2,b).
\]

Esta propiedad deberá verificarse programáticamente para los cinco estados presentes.

---

## Propiedad de cobertura

La tabla de segundo orden contiene:

\[
25
\]

contextos distintos.

Debe comprobarse que:

\[
\{(x_{t-1},x_t)\}=S^2.
\]

No se permitirá una tabla parcial.

---

## Rigidez

El estado dinámico de segundo orden es el par:

\[
(x_{t-1},x_t).
\]

La construcción recorre de manera determinista los 25 pares de B y vuelve al contexto inicial.

Por tanto el ciclo declarado tiene periodo:

\[
25.
\]

LAB-D1 no pretende ser aperiodico.

Al contrario, su rigidez es parte del control.

---

## Semillas

Se conservan exactamente las mismas semillas que LAB-D0-v1:

11
23
37
51
79
101
131
173

Cada semilla determinará únicamente la fase inicial del mismo ciclo congelado.

La regla F no cambia entre semillas.

---

## Longitudes

Se conservan:

- burn-in: 1.000 pasos;
- trayectoria útil: 30.000 transiciones;
- entrenamiento: 18.000;
- prueba: 12.000.

Como:

\[
30000
\]

es múltiplo de:

\[
25,
\]

la trayectoria útil contiene un número entero de ciclos completos.

Train y test también contienen números enteros de ciclos completos:

\[
18000/25=720,
\]

\[
12000/25=480.
\]

Esto evita que una semilla obtenga una ventaja artificial por corte de fase.

---

## Modelos predictivos

Se mantienen sin modificación:

### M1

\[
P(x_{t+1}\mid x_t).
\]

### M2

\[
P(x_{t+1}\mid x_{t-1},x_t).
\]

Suavizado:

\[
\alpha=0.5.
\]

---

## Delta_hist

Se reutiliza exactamente:

\[
\Delta_{\mathrm{hist}}
=
L_1-L_2.
\]

LAB-D1 debería producir:

\[
\Delta_{\mathrm{hist}}>0,
\]

porque M2 conoce el contexto que determina el sucesor y M1 no.

---

## C_hist

Se reutiliza la distancia TV entre:

\[
P_{M2}(\cdot\mid x_{t-1},x_t)
\]

y:

\[
P_{M1}(\cdot\mid x_t).
\]

LAB-D1 debería producir un:

\[
C_{\mathrm{hist}}
\]

claramente separado de su nulo histórico condicionado.

---

## Nulo

Se conserva exactamente el nulo de LAB-D0-v1:

la variable:

\[
x_{t-1}
\]

se permuta entre observaciones con el mismo:

\[
x_t.
\]

Esto conserva la gramática de primer orden pero destruye la asociación histórica adicional:

\[
x_{t-1}
\rightarrow x_{t+1}
\mid x_t.
\]

Se mantienen:

\[
64
\]

permutaciones por semilla.

---

## Gate positivo LAB-D1-v1

LAB-D1-v1 supera el control positivo histórico si se cumplen simultáneamente:

1. Delta_hist supera el percentil 95 de su nulo en al menos 7/8 semillas;
2. C_hist supera el percentil 95 de su nulo en al menos 7/8 semillas;
3. Delta_hist es positivo en al menos 7/8 semillas;
4. la tabla generadora contiene los 25 contextos de segundo orden;
5. el sucesor depende efectivamente de x[t-1] para cada estado presente;
6. la regla generadora es determinista;
7. el periodo estructural declarado de 25 contextos se verifica.

---

## Criterio 7/8

Se conserva la regla predeclarada:

\[
P(X\ge 7\mid n=8,p=0.5)
=
\frac{9}{256}
\approx0.0352.
\]

No se modificará tras observar resultados.

---

## Resultado esperado

El patrón objetivo del control es:

\[
\mathrm{LAB\text{-}D0}:
\quad
\Delta_{\mathrm{hist}}\not>nulo,
\quad
C_{\mathrm{hist}}\not>nulo,
\]

frente a:

\[
\mathrm{LAB\text{-}D1}:
\quad
\Delta_{\mathrm{hist}}>nulo,
\quad
C_{\mathrm{hist}}>nulo.
\]

Si aparece esta separación, el instrumento habrá superado un control negativo y un control positivo bajo el mismo contrato.

---

## Rigidez esperada

LAB-D1 contiene historia causal por construcción, pero también periodicidad rígida.

Por tanto un resultado positivo en Delta_hist y C_hist:

NO

será suficiente para una G2-PD.

LAB-D1 demuestra deliberadamente que:

\[
\text{historia causal}
\not\Rightarrow
\text{aperiodicidad}.
\]

---

## Regla de fallo

LAB-D1-v1 falla como control positivo si:

- Delta_hist no se separa del nulo;
- C_hist no se separa del nulo;
- la señal depende de pocas semillas;
- M1 resulta tan predictivo como M2;
- la tabla no cubre los 25 contextos;
- el sucesor puede reducirse a función del estado presente;
- el periodo estructural no coincide con la construcción declarada.

Si LAB-D1 falla, LAB-D2 no deberá interpretarse hasta comprender el fallo instrumental.

---

## Alcance

LAB-D1 no valida todavía:

- A1;
- P_rel;
- N;
- U como estimadores completos;
- G2-PD;
- ningún régimen fenomenológico nuevo.

Su función inmediata es calibrar el detector histórico frente a un control positivo conocido.

---

## Regla anti-ajuste

Después de la primera ejecución no podrán modificarse retrospectivamente:

- B;
- la tabla F;
- semillas;
- longitudes;
- train/test;
- alpha;
- nulos;
- métricas;
- gate positivo.

Cualquier cambio producirá:

LAB-D1-v2.

---

## Estado

ESPECIFICACION CONGELADA ANTES DE RESULTADOS