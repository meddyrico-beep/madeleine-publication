# DMO-002 — doble registro conteo / medida

## Claim asociado

C014 — Contar y medir son operaciones irreductibles entre sí: la cronología se cuenta, la trayectoria se mide y la historia exige ambas.

## Estado del claim

Interno por ahora.

DMO-002 no pretende demostrar una irreductibilidad universal entre toda forma posible de conteo y toda forma posible de medida.

Su objetivo es más preciso:

> comprobar si, bajo una operacionalización mínima explícita, el registro de conteo y el registro de medida contienen información mutuamente no recuperable.

---

## Definición operacional

Sea una historia finita:

\[
H=(x_0,x_1,\ldots,x_k).
\]

Definimos el registro doble:

\[
\mu(H)=(n(H),\delta(H)).
\]

donde:

\[
n(H)=k
\]

es el número de transiciones entre marcas sucesivas, y:

\[
\delta(H)=\sum_{i=0}^{k-1}|x_{i+1}-x_i|
\]

es la medida acumulada de trayectoria.

En esta demo:

- \(n\) representa el registro de conteo;
- \(\delta\) representa el registro de medida.

---

## Prueba 1 — mismo conteo, distinta medida

Tomamos:

\[
A=(0,1,2)
\]

y:

\[
B=(0,2,0).
\]

Entonces:

\[
n(A)=2,\qquad \delta(A)=2
\]

mientras que:

\[
n(B)=2,\qquad \delta(B)=4.
\]

Por tanto:

\[
n(A)=n(B)
\]

pero:

\[
\delta(A)\neq\delta(B).
\]

En este dominio, el conteo por sí solo no determina la medida.

---

## Prueba 2 — misma medida, distinto conteo

Tomamos:

\[
C=(0,4)
\]

y:

\[
D=(0,1,2,3,4).
\]

Entonces:

\[
n(C)=1,\qquad \delta(C)=4
\]

mientras que:

\[
n(D)=4,\qquad \delta(D)=4.
\]

Por tanto:

\[
\delta(C)=\delta(D)
\]

pero:

\[
n(C)\neq n(D).
\]

En este dominio, la medida por sí sola no determina el conteo.

---

## Consecuencia mínima

Las dos pruebas juntas establecen:

\[
n \not\Rightarrow \delta
\]

y:

\[
\delta \not\Rightarrow n
\]

en el dominio de historias considerado.

Por tanto, las dos coordenadas del registro:

\[
\mu(H)=(n,\delta)
\]

son no redundantes dentro de esta operacionalización.

Eliminar \(n\) identifica historias que el registro doble distingue.

Eliminar \(\delta\) identifica igualmente historias que el registro doble distingue.

---

## Qué demuestra internamente

DMO-002 demuestra que:

1. pueden existir historias con igual conteo y distinta medida;
2. pueden existir historias con igual medida y distinto conteo;
3. ninguna de las dos coordenadas determina por sí sola a la otra en el dominio ensayado;
4. el par \((n,\delta)\) conserva distinciones que cualquiera de sus proyecciones individuales pierde.

---

## Qué NO demuestra

DMO-002 no demuestra:

- que toda forma matemática de contar sea universalmente irreductible a toda forma de medir;
- que sea imposible codificar el par \((n,\delta)\) mediante otra representación inyectiva;
- que el doble registro sea superior a todo formalismo clásico;
- que \(n\) y \(\delta\) correspondan automáticamente a magnitudes físicas;
- que exista validación experimental externa;
- que la tesis completa de historia, cronología y trayectoria quede demostrada por estos cuatro ejemplos.

---

## Criterio de fallo

La propiedad ensayada fallaría si, dentro del dominio considerado:

1. todo par de historias con igual \(n\) tuviera necesariamente igual \(\delta\); o
2. todo par de historias con igual \(\delta\) tuviera necesariamente igual \(n\).

Los contraejemplos A/B y C/D impiden ambas reducciones en esta operacionalización.

---

## Reproducibilidad

Script:

`demos/DMO-002_double_register.py`

El script:

- construye los cuatro casos;
- calcula \(n\) y \(\delta\);
- ejecuta las dos comprobaciones mediante `assert`;
- falla automáticamente si desaparece cualquiera de las dos propiedades.

Resultado observado:

- PRUEBA 1: superada;
- PRUEBA 2: superada;
- no se produjo `AssertionError`.

---

## Resultado

Estado:

**CONSTRUIDA — INTERNA — REPRODUCIBLE**

Resultado mínimo:

> Bajo la definición operacional de DMO-002, conteo y medida son registros no redundantes: ninguno determina por sí solo al otro.

Este resultado apoya una versión restringida de C014.

No convierte todavía la formulación general de C014 en un teorema universal.

---

## Siguiente endurecimiento

La siguiente prueba de DMO-002 deberá abandonar los cuatro ejemplos seleccionados y explorar familias completas de historias para determinar:

- cuántas colisiones produce la proyección a \(n\);
- cuántas colisiones produce la proyección a \(\delta\);
- cuánto poder discriminante añade el par \((n,\delta)\);
- bajo qué restricciones podrían aparecer dependencias entre ambos registros.

---

## Endurecimiento exhaustivo

La prueba mínima de cuatro historias fue ampliada mediante:

`demos/DMO-002_sweep.py`

El barrido enumera exhaustivamente todas las historias:

\[
H=(0,x_1,\ldots,x_n),
\]

con:

\[
x_i\in\{0,1,2,3,4\},
\qquad
1\le n\le6.
\]

El número total de historias examinadas fue:

\[
5^1+5^2+5^3+5^4+5^5+5^6
=
19530.
\]

### Cardinalidades observadas

Se obtuvieron:

\[
|\{n\}|=6,
\]

\[
|\{\delta\}|=25,
\]

y:

\[
|\{(n,\delta)\}|=90.
\]

Por tanto, el registro conjunto separa más clases que cualquiera de sus proyecciones:

\[
90>25>6.
\]

En términos relativos:

\[
\frac{90}{6}=15
\]

y:

\[
\frac{90}{25}=3.6.
\]

El par \((n,\delta)\) distingue así 15 veces más clases que el conteo aislado y 3.6 veces más que la medida aislada dentro del dominio enumerado.

---

## Estructura observada por conteo

El número de valores de medida observados para cada conteo fue:

| n | valores distintos de delta |
|---|---:|
| 1 | 5 |
| 2 | 9 |
| 3 | 13 |
| 4 | 17 |
| 5 | 21 |
| 6 | 25 |

En el dominio examinado aparece el patrón:

\[
|\Delta_n|=4n+1.
\]

Esta regularidad es observacional dentro del barrido.

Todavía no se eleva aquí a teorema general.

---

## No-determinación exhaustiva

El barrido confirma la existencia de múltiples valores de delta para un mismo n.

Por tanto:

\[
n\not\Rightarrow\delta.
\]

También confirma que numerosos valores de delta aparecen asociados a diferentes valores de n.

Por tanto:

\[
\delta\not\Rightarrow n.
\]

Las dos reducciones funcionales quedan rechazadas en el dominio exhaustivamente enumerado.

---

## Lectura informacional

Usando distribución uniforme sobre las 19530 historias enumeradas se obtuvo:

\[
H(n)=0.901426\ \text{bits},
\]

\[
H(\delta)=3.698883\ \text{bits},
\]

\[
H(n,\delta)=4.537376\ \text{bits}.
\]

Las entropías condicionales fueron:

\[
H(\delta\mid n)=3.635950\ \text{bits}>0,
\]

y:

\[
H(n\mid\delta)=0.838494\ \text{bits}>0.
\]

Por tanto, conocer completamente una de las dos coordenadas no elimina la incertidumbre sobre la otra bajo esta distribución.

---

## Precaución sobre las entropías

La enumeración uniforme sobre historias no genera una distribución uniforme sobre n.

Los valores grandes de n contienen muchas más historias porque el número de secuencias crece como:

\[
5^n.
\]

Por ello, las entropías anteriores son propiedades de esta distribución concreta y no invariantes universales del doble registro.

La no-determinación funcional, en cambio, no depende de este sesgo probabilístico: basta la existencia de historias con igual n y distinto delta, y viceversa.

---

## Resultado endurecido de DMO-002

DMO-002 dispone ahora de:

1. contraejemplos mínimos explícitos;
2. comprobaciones automáticas mediante `assert`;
3. barrido exhaustivo de 19530 historias;
4. no-determinación en ambas direcciones;
5. medida cuantitativa de información residual;
6. comparación del poder discriminante de n, delta y (n,delta).

Estado:

**CONSTRUIDA — INTERNA — REPRODUCIBLE — BARRIDO EXHAUSTIVO**

La evidencia apoya una versión restringida de C014:

> En el dominio y operacionalización de DMO-002, conteo y medida constituyen registros no redundantes: ninguno determina al otro y su registro conjunto conserva distinciones que cada registro aislado pierde.

No se afirma todavía irreductibilidad universal.

---

## Prueba de robustez con distribución equilibrada por n

Se añadió:

`demos/DMO-002_balanced.py`

El barrido utiliza las mismas 19530 historias del dominio exhaustivo, pero modifica su ponderación probabilística.

Cada valor:

\[
n\in\{1,2,3,4,5,6\}
\]

recibe peso total:

\[
P(n)=\frac{1}{6}.
\]

Condicionado a cada valor de \(n\), todas las historias correspondientes reciben el mismo peso.

Esto elimina el predominio combinatorio de las historias largas presente en la enumeración uniforme original.

### Resultado

Se obtuvo:

\[
H(n)=2.584963\ \text{bits},
\]

\[
H(\delta)=3.792081\ \text{bits},
\]

\[
H(n,\delta)=5.733477\ \text{bits}.
\]

Las entropías condicionales permanecen estrictamente positivas:

\[
H(\delta\mid n)=3.148514\ \text{bits}>0,
\]

\[
H(n\mid\delta)=1.941396\ \text{bits}>0.
\]

Por tanto, la no-redundancia informacional no desaparece al equilibrar el peso de las distintas longitudes.

### Dependencia sin determinación

La información mutua es:

\[
I(n;\delta)
=
H(n)+H(\delta)-H(n,\delta)
\approx
0.643567\ \text{bits}.
\]

Esto muestra que los registros no son estadísticamente independientes bajo esta distribución.

Sin embargo:

\[
H(\delta\mid n)>0
\]

y:

\[
H(n\mid\delta)>0,
\]

por lo que ninguno determina completamente al otro.

La lectura correcta para DMO-002 es, por tanto:

> los registros presentan dependencia estadística, pero mantienen información propia no recuperable completamente desde la otra coordenada.

### Resultado de robustez

La conclusión restringida de DMO-002 sobrevive a dos ponderaciones distintas:

1. distribución uniforme sobre las 19530 historias;
2. distribución equilibrada por \(n\).

Esto reduce la posibilidad de que la no-redundancia informacional observada sea únicamente un artefacto del predominio combinatorio de historias largas.

### Límite vigente

La prueba sigue perteneciendo a un dominio finito y a una definición concreta de:

\[
n(H)
\]

y:

\[
\delta(H).
\]

No demuestra todavía una irreductibilidad universal de contar y medir.
