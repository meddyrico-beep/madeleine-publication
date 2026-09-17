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
