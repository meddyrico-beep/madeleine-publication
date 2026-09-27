# LAB-FEN-001 — Especificación congelada de LAB-D0 v1

## Estatuto

Este documento concreta LAB-D0 antes de ejecutar resultados.

LAB-D0 es un control causal de primer orden y no debe confundirse con D0 de la jerarquía canónica D0-D11.

Versión:

LAB-D0-v1

---

## Objetivo

Comprobar que los instrumentos históricos no detectan sistemáticamente dependencia de segundo orden en un proceso cuya ley generadora depende únicamente del estado presente.

La hipótesis estructural es:

\[
P(x_{t+1}\mid x_t,x_{t-1})
=
P(x_{t+1}\mid x_t).
\]

Por construcción, la dependencia histórica condicional verdadera es nula.

---

## Alfabeto

Se congela:

\[
S=\{0,1,2,3,4\}.
\]

No existe interpretación geométrica asociada a estos símbolos.

Son únicamente estados discretos del control.

---

## Regla generadora

Para cada estado actual:

\[
x_t=i,
\]

la distribución del siguiente estado es:

\[
P(i+1 \bmod 5)=0.50,
\]

\[
P(i)=0.20,
\]

\[
P(i-1 \bmod 5)=0.15,
\]

\[
P(i+2 \bmod 5)=0.10,
\]

\[
P(i-2 \bmod 5)=0.05.
\]

La regla depende de:

\[
x_t
\]

y nunca de:

\[
x_{t-1}.
\]

La presencia de auto-transición evita una periodicidad determinista trivial.

---

## Semillas congeladas

Se usarán exactamente:

11
23
37
51
79
101
131
173

Total:

8 semillas.

---

## Longitud

Por semilla:

- burn-in: 1.000 pasos;
- trayectoria útil: 30.000 transiciones;
- entrenamiento: primeras 18.000;
- prueba: últimas 12.000.

No se modificarán estas cantidades después de observar resultados de LAB-D0-v1.

---

## Modelos predictivos

Se ajustarán dos modelos a entrenamiento.

### Modelo M1

Primer orden:

\[
P(x_{t+1}\mid x_t).
\]

### Modelo M2

Segundo orden:

\[
P(x_{t+1}\mid x_{t-1},x_t).
\]

Ambos usarán suavizado de Dirichlet:

\[
\alpha=0.5.
\]

---

## Delta_hist

Sobre el conjunto de prueba:

\[
L_1
=
-\frac{1}{n}
\sum_t
\log
P_{M1}(x_{t+1}\mid x_t),
\]

\[
L_2
=
-\frac{1}{n}
\sum_t
\log
P_{M2}(x_{t+1}\mid x_{t-1},x_t).
\]

Definimos:

\[
\Delta_{\mathrm{hist}}
=
L_1-L_2.
\]

Interpretación:

- Delta_hist > 0: el modelo histórico predice mejor fuera de muestra;
- Delta_hist = 0: no aporta mejora;
- Delta_hist < 0: el modelo histórico empeora la predicción.

No se considerará significativo un valor positivo aislado.

---

## C_hist diagnóstico

Para cada contexto observado en prueba:

\[
(x_{t-1},x_t)
\]

se compara:

\[
P_{M2}(\cdot\mid x_{t-1},x_t)
\]

con:

\[
P_{M1}(\cdot\mid x_t).
\]

Se utilizará distancia de variación total:

\[
TV(p,q)
=
\frac12
\sum_s
|p(s)-q(s)|.
\]

C_hist será la media ponderada por frecuencia de prueba de estas distancias.

Debido al error de muestreo:

\[
C_{\mathrm{hist}}
\]

no se espera exactamente igual a cero.

Por ello deberá compararse con un nulo histórico.

---

## Nulo histórico condicionado

Para cada semilla se generarán:

64 permutaciones.

La variable:

\[
x_{t-1}
\]

se permutará únicamente entre observaciones que comparten el mismo:

\[
x_t.
\]

Así se conserva la estructura de primer orden:

\[
x_t\rightarrow x_{t+1}
\]

pero se destruye cualquier relación adicional entre:

\[
x_{t-1}
\]

y:

\[
x_{t+1}
\]

condicionada por:

\[
x_t.
\]

Para cada permutación se reajustará M2 y se recalcularán:

- Delta_hist;
- C_hist.

---

## Criterio de falso positivo histórico

Para cada semilla se calculará el percentil 95 del nulo.

Se define un hit histórico solo si el valor observado supera dicho percentil.

LAB-D0-v1 supera el control si:

1. no aparecen más de 1/8 hits para Delta_hist;
2. no aparecen más de 1/8 hits para C_hist;
3. no existe una señal consistente entre semillas que indique ventaja histórica;
4. la implementación confirma que la regla generadora no consulta x[t-1].

Un resultado aislado por encima del percentil 95 no se interpretará automáticamente como historia real.

---

## Resultado esperado

Por construcción:

\[
C_{\mathrm{hist,true}}=0.
\]

Y no debería existir mejora predictiva sistemática:

\[
\Delta_{\mathrm{hist}}>0.
\]

Si el instrumento detecta historia robusta en LAB-D0, el instrumento falla y LAB-D1/LAB-D2 no deben interpretarse hasta corregirlo.

---

## Alcance

Esta fase no intenta todavía medir toda la firma:

\[
M_{G2}.
\]

Primero valida únicamente el bloque histórico:

- Delta_hist;
- C_hist;
- separación frente a un nulo condicionado.

A1, P_rel, N y U se incorporarán después de que este control negativo sobreviva.

---

## Regla anti-ajuste

Después de la primera ejecución de LAB-D0-v1 no podrán cambiarse retrospectivamente:

- transición generadora;
- semillas;
- longitudes;
- separación train/test;
- alpha;
- número de permutaciones;
- definición de Delta_hist;
- definición de C_hist;
- criterio de hit.

Cualquier cambio deberá producir LAB-D0-v2.

---

## Estado

ESPECIFICACION CONGELADA ANTES DE RESULTADOS