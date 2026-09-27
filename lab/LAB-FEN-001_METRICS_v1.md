# LAB-FEN-001 — Métricas fenomenológicas v1

## Estatuto

Este documento congela una operacionalización de laboratorio para la firma fenomenológica utilizada en LAB-FEN-001.

Versión:

LAB-FEN-001-METRICS-v1

Estas fórmulas:

- no pertenecen al canon basal;
- no se presentan como definiciones universales;
- no sustituyen las definiciones conceptuales del informe fenomenológico;
- sirven como instrumentos reproducibles para LAB-FEN-001.

El objetivo es impedir que persistencia, novedad o aperiodicidad sean redefinidas después de observar LAB-D2.

---

# 1. Firma objetivo

Se mantiene la firma:

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

No se reducirá a un escalar único.

Las seis coordenadas deben conservarse por separado.

---

# 2. Magnitudes ya congeladas

LAB-D0-v1 y LAB-D1-v1 ya congelaron:

\[
\Delta_{\mathrm{hist}}
=
L_1-L_2,
\]

donde:

\[
L_1
\]

es la pérdida predictiva fuera de muestra del modelo de primer orden y:

\[
L_2
\]

la pérdida predictiva fuera de muestra del modelo de segundo orden.

También se congeló:

\[
C_{\mathrm{hist}}
\]

como distancia de variación total media entre:

\[
P_{M2}(\cdot\mid x_{t-1},x_t)
\]

y:

\[
P_{M1}(\cdot\mid x_t).
\]

Estas dos métricas NO serán redefinidas.

---

# 3. Contrato común

Para LAB-FEN-001 se mantiene:

\[
S=\{0,1,2,3,4\}.
\]

Se mantienen:

- 8 semillas;
- 1.000 pasos de burn-in;
- 30.000 transiciones útiles;
- 18.000 transiciones de entrenamiento;
- 12.000 transiciones de prueba;
- suavizado alpha = 0.5;
- 64 realizaciones nulas cuando corresponda.

La trayectoria de prueba se divide además en:

\[
8
\]

ventanas consecutivas de:

\[
1500
\]

transiciones.

Por tanto:

\[
8\times1500=12000.
\]

No se solapan.

---

# 4. Nulo Markov-1 para las métricas nuevas

Se ajustará sobre entrenamiento el mismo modelo:

\[
M1:
P(x_{t+1}\mid x_t).
\]

A partir de M1 se producirán:

\[
64
\]

trayectorias sustitutas de longitud:

\[
12000
\]

por semilla.

Cada sustituto:

- utiliza únicamente dependencia de primer orden;
- conserva la dinámica Markov-1 estimada;
- tiene la misma longitud que la prueba real;
- no utiliza x[t-1] en su regla generadora.

Este será el nulo principal para A1 y P_rel.

El nulo por permutación condicionada ya utilizado para Delta_hist y C_hist se mantiene sin cambios.

Los dos tipos de nulo cumplen funciones distintas y no deben mezclarse.

---

# 5. A1 — exceso histórico sobre Markov-1

## 5.1 Cantidad bruta

Sobre los triples:

\[
(a,b,c)
=
(x_{t-1},x_t,x_{t+1})
\]

se estima la información mutua condicional:

\[
I_2
=
I(X_{t-1};X_{t+1}\mid X_t).
\]

Su estimador discreto es:

\[
\widehat I_2
=
\sum_{a,b,c}
\hat p(a,b,c)
\log
\frac{
\hat p(c\mid a,b)
}{
\hat p(c\mid b)
}.
\]

Se usarán logaritmos naturales.

La unidad será:

nats.

Los términos con frecuencia nula no contribuyen a la suma.

---

## 5.2 Corrección por nulo

Para las 64 trayectorias Markov-1 se calcula:

\[
\widehat I_2^{(r)},
\qquad
r=1,\ldots,64.
\]

Se obtiene:

\[
Q_{0.95}^{M1}(I_2)
\]

mediante el mismo percentil nearest-rank utilizado anteriormente.

Definimos:

\[
A1
=
\widehat I_2^{obs}
-
Q_{0.95}^{M1}(I_2).
\]

Por construcción operativa v1:

\[
A1>0
\]

significa que la dependencia histórica observada excede el percentil 95 de lo generado por un proceso Markov-1 de longitud comparable.

---

## 5.3 Interpretación

A1 positivo:

estructura histórica no explicada por el nulo de primer orden bajo este instrumento.

A1 igual o menor que cero:

no se ha separado del nulo Markov-1.

A1 no demuestra por sí solo causalidad física ni irreductibilidad universal.

---

# 6. P_rel — persistencia relativa

## 6.1 Representación por ventanas

Cada una de las ocho ventanas de prueba produce una distribución de trigramas:

\[
q_w(a,b,c),
\qquad
w=1,\ldots,8.
\]

El vector tiene:

\[
5^3=125
\]

componentes.

Cada q_w se normaliza a suma uno.

---

## 6.2 Distancia entre firmas

Se utiliza divergencia Jensen-Shannon:

\[
JS(p,q)
=
\frac12 KL(p\Vert m)
+
\frac12 KL(q\Vert m),
\]

con:

\[
m=\frac{p+q}{2}.
\]

Se usan logaritmos naturales.

JS es finita incluso cuando existen componentes de frecuencia cero.

---

## 6.3 Variación interna observada

Definimos:

\[
D_{\mathrm{within}}
=
\operatorname{median}_{i<j}
JS(q_i,q_j).
\]

Esta cantidad mide cuánto cambia la firma histórica entre ventanas de la misma trayectoria.

---

## 6.4 Distancia al nulo

Cada sustituto Markov-1 se divide igualmente en ocho ventanas.

Sea:

\[
q^{0}_{r,w}
\]

la distribución de trigramas de la ventana w del sustituto r.

Definimos:

\[
D_{\mathrm{null}}
=
\operatorname{median}_{r,w}
JS(q_w,q^{0}_{r,w}).
\]

---

## 6.5 Persistencia relativa

Definimos:

\[
P_{\mathrm{rel}}
=
1-
\frac{
D_{\mathrm{within}}
}{
D_{\mathrm{null}}
}.
\]

Si:

\[
D_{\mathrm{null}}=0,
\]

la métrica se declara no evaluable y el gate falla.

No se recortarán los valores negativos.

Por tanto:

\[
P_{\mathrm{rel}}>0
\]

significa que las ventanas reales se parecen más entre sí que a la referencia Markov-1.

\[
P_{\mathrm{rel}}=1
\]

corresponde al caso límite:

\[
D_{\mathrm{within}}=0.
\]

Un valor negativo significa que la firma observada varía internamente más de lo que se separa de su nulo.

---

# 7. N — novedad histórica

## 7.1 Dominio

Se utilizarán los trigramas:

\[
(x_{t-1},x_t,x_{t+1}).
\]

Existen como máximo:

\[
5^3=125
\]

historias distintas de longitud tres.

---

## 7.2 Entropía histórica

Sea:

\[
q(g)
\]

la distribución empírica de trigramas en las 12.000 transiciones de prueba.

Definimos:

\[
H_3
=
-\sum_g q(g)\log q(g).
\]

---

## 7.3 Diversidad efectiva

El número efectivo de historias es:

\[
D_3
=
\exp(H_3).
\]

Definimos la novedad normalizada:

\[
N
=
\frac{D_3}{125}.
\]

Así:

\[
0<N\le1.
\]

Un proceso concentrado en muy pocas historias tendrá N bajo.

Un proceso que utiliza muchas historias de manera distribuida tendrá N alto.

---

## 7.4 Diagnóstico adicional

Se registrará además:

\[
C_3
=
\frac{
|\{g:q(g)>0\}|
}{
125
}.
\]

C3 es cobertura de trigramas.

C3 NO sustituye a N.

Dos procesos pueden visitar el mismo número de historias pero distribuir sus frecuencias de manera muy diferente.

---

## 7.5 Interpretación

N mide diversidad histórica dentro del alfabeto finito declarado.

No significa creación de información ex nihilo.

No significa novedad física.

No significa que una historia nunca haya ocurrido anteriormente.

Su función es impedir que una trayectoria altamente persistente pero congelada sea clasificada como dinámica rica.

---

# 8. U — aperiodicidad

## 8.1 Objetivo

U debe detectar si una parte dominante de la trayectoria puede explicarse mediante repetición periódica exacta o casi exacta.

LAB-D1 debe actuar como control rígido.

---

## 8.2 Recurrencia por retardo

Sea la serie de prueba:

\[
x_0,\ldots,x_T.
\]

Para cada retardo:

\[
p=1,\ldots,1500
\]

definimos:

\[
R(p)
=
\frac{
1
}{
T+1-p
}
\sum_{t=p}^{T}
\mathbf 1[x_t=x_{t-p}].
\]

---

## 8.3 Línea basal marginal

Sea:

\[
\pi_s
\]

la frecuencia marginal del estado s en prueba.

Definimos:

\[
B
=
\sum_s \pi_s^2.
\]

B representa la coincidencia esperada entre dos extracciones independientes con las mismas frecuencias marginales.

---

## 8.4 Exceso periódico

Para cada p:

\[
E(p)
=
\max
\left(
0,
\frac{
R(p)-B
}{
1-B
}
\right).
\]

Si:

\[
B=1,
\]

la serie está congelada y se define directamente:

\[
U=0.
\]

---

## 8.5 Periodicidad dominante

Definimos:

\[
Q_{\mathrm{period}}
=
\max_{1\le p\le1500}
E(p).
\]

Se registrará también:

\[
p^\*
=
\arg\max_p E(p).
\]

---

## 8.6 Aperiodicidad

Finalmente:

\[
U
=
1-Q_{\mathrm{period}}.
\]

Por construcción:

\[
0\le U\le1.
\]

Un ciclo exacto cuyo periodo esté dentro de:

\[
1,\ldots,1500
\]

produce:

\[
U=0.
\]

Una serie sin una recurrencia periódica dominante produce valores mayores.

---

## 8.7 Límite explícito

U-v1 no excluye ciclos exactos de periodo superior a 1500.

Por tanto:

\[
U>0
\]

no constituye prueba matemática de aperiodicidad infinita.

Es un detector finito de periodicidad dominante dentro de la escala declarada.

---

# 9. Firma completa LAB-FEN-001-v1

Una ejecución deberá reportar separadamente:

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

También se registrarán como diagnósticos:

- I2 bruto;
- p95 Markov-1 de I2;
- D_within;
- D_null;
- cobertura C3;
- Q_period;
- p*;
- todos los hits históricos ya congelados.

No se calculará una media ponderada ni un score único.

---

# 10. Controles D0 y D1 antes de D2

Antes de diseñar o ejecutar LAB-D2, estas métricas deberán evaluarse sobre las series ya congeladas de:

- LAB-D0-v1;
- LAB-D1-v1.

No se regenerarán esas series para la calibración primaria.

Se usarán los artefactos ya registrados en Git.

---

# 11. Resultado esperado de los controles

LAB-D0 representa:

primer orden + apertura estocástica.

Por tanto se espera cualitativamente:

- A1 no positivo;
- Delta_hist sin hit;
- C_hist sin hit;
- P_rel bajo o no separado claramente del nulo;
- N relativamente alto;
- U relativamente alto.

LAB-D1 representa:

segundo orden fuerte + rigidez periódica.

Por tanto se espera cualitativamente:

- A1 positivo;
- Delta_hist positivo;
- C_hist positivo;
- P_rel alto;
- N menor que en LAB-D0;
- U cercano o igual a cero.

Estas expectativas fueron fijadas antes de calcular las nuevas métricas.

---

# 12. Calibración de umbrales para D2

Los valores numéricos de N alto, persistencia suficiente y aperiodicidad suficiente NO se elegirán observando D2.

Primero se calcularán las métricas sobre D0 y D1.

Sean:

\[
\widetilde P_0,
\widetilde N_0,
\widetilde U_0
\]

las medianas entre semillas de LAB-D0.

Sean:

\[
\widetilde P_1,
\widetilde N_1,
\widetilde U_1
\]

las medianas entre semillas de LAB-D1.

---

## 12.1 Gate de persistencia

Si:

\[
\widetilde P_1
>
\widetilde P_0,
\]

se define:

\[
T_P
=
\frac{
\widetilde P_0+\widetilde P_1
}{
2
}.
\]

D2 deberá satisfacer:

\[
P_{\mathrm{rel}}>T_P.
\]

Si el orden esperado no se cumple, la calibración de P_rel falla y no se fija gate para D2.

---

## 12.2 Gate de novedad

Si:

\[
\widetilde N_0
>
\widetilde N_1,
\]

se define:

\[
T_N
=
\frac{
\widetilde N_0+\widetilde N_1
}{
2
}.
\]

D2 deberá satisfacer:

\[
N>T_N.
\]

Si el orden esperado no se cumple, la calibración de N falla.

---

## 12.3 Gate de aperiodicidad

Si:

\[
\widetilde U_0
>
\widetilde U_1,
\]

se define:

\[
T_U
=
\frac{
\widetilde U_0+\widetilde U_1
}{
2
}.
\]

D2 deberá satisfacer:

\[
U>T_U.
\]

Si el orden esperado no se cumple, la calibración de U falla.

---

# 13. Gate histórico de D2

Las coordenadas históricas conservarán sus gates ya definidos.

D2 deberá mostrar:

\[
A1>0.
\]

Además Delta_hist deberá:

- ser positivo;
- superar el percentil 95 de su nulo condicionado.

C_hist deberá superar:

- el percentil 95 de su nulo condicionado.

No bastará un valor positivo aislado.

---

# 14. Regla entre semillas

Para una primera candidata LAB-D2-v1 se conserva:

\[
7/8
\]

como requisito de consistencia.

Por tanto cada condición individual del gate deberá cumplirse en al menos siete de las ocho semillas.

Esto incluye:

- A1;
- Delta_hist;
- C_hist;
- P_rel;
- N;
- U.

---

# 15. Regla conjunta

La candidata no pasa por mayoría de coordenadas.

Para cada semilla se conserva el vector completo.

Un resultado favorable requiere que exista una familia reproducible de semillas en la cual las condiciones históricas, de persistencia, novedad y aperiodicidad coexistan.

No se permitirá compensar:

- historia baja con novedad alta;
- periodicidad con persistencia;
- falta de persistencia con aperiodicidad;
- C_hist bajo con A1 alto.

---

# 16. Falsación previa a D2

Si al aplicar estas métricas a los controles congelados ocurre cualquiera de los siguientes casos:

1. LAB-D0 produce A1 sistemáticamente positivo;
2. LAB-D1 no produce A1 positivo;
3. LAB-D1 no muestra P_rel superior a LAB-D0;
4. LAB-D0 no muestra N superior a LAB-D1;
5. LAB-D0 no muestra U superior a LAB-D1;
6. U no reconoce el periodo 25 de LAB-D1;
7. las métricas dependen críticamente de una sola semilla;

entonces:

LA CAPA METRICA v1 FALLA SU CALIBRACION.

En ese caso no se diseñará LAB-D2 usando estas métricas como gate.

La corrección deberá producir:

LAB-FEN-001-METRICS-v2.

---

# 17. Jerarquía de nulos

En esta fase:

- Delta_hist y C_hist mantienen su nulo histórico condicionado;
- A1 utiliza sustitutos Markov-1;
- P_rel utiliza sustitutos Markov-1;
- N y U se calibran inicialmente contra los controles D0/D1.

Los nulos i.i.d. y Markov-2 se conservarán para extensiones de robustez.

Un nulo Markov-2 será especialmente relevante para estudiar un posible residuo G3, no para definir la existencia mínima de G2.

---

# 18. Alcance científico

Estas métricas permiten estudiar modelos discretos finitos bajo LAB-FEN-001.

No demuestran:

- universalidad de la firma;
- causalidad física;
- geometría emergente;
- teoría física nueva;
- validez externa de MADELEINE;
- aperiodicidad matemática infinita;
- irreductibilidad absoluta.

La interpretación queda restringida al experimento declarado.

---

# 19. Regla anti-ajuste retrospectivo

Después de evaluar por primera vez las nuevas métricas sobre D0 y D1 no podrán modificarse retrospectivamente:

- fórmula de A1;
- número de nulos;
- percentil;
- número de ventanas;
- tamaño de ventana;
- divergencia usada en P_rel;
- definición de N;
- longitud histórica usada en N;
- definición de U;
- rango de retardos;
- procedimiento de calibración de umbrales;
- regla 7/8.

Cualquier modificación producirá una nueva versión.

---

# 20. Orden experimental

El orden obligatorio es:

1. congelar este documento;
2. implementar las métricas;
3. congelar el ejecutable de métricas;
4. aplicarlo a las series ya congeladas de D0 y D1;
5. registrar los resultados de calibración;
6. calcular T_P, T_N y T_U;
7. congelar esos umbrales;
8. sólo entonces diseñar LAB-D2-v1.

---

## Estado

DEFINICIONES METRICAS v1 CONGELABLES ANTES DE D2