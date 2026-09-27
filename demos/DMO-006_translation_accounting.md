# DMO-006 — Traducción entre niveles con pérdida, alcance y cambio de lectura

## Claim asociado

C030 — La traducción entre niveles debe preservar pérdida, ganancia y cambio de lectura; no puede presentarse como equivalencia automática.

---

## Propósito

Formalizar una contabilidad mínima para traducciones entre dominios o niveles de lectura.

La demo distingue:

- pérdida de distinciones del dominio fuente;
- estados destino no alcanzados;
- enriquecimiento representacional derivado;
- equivalencia exacta como conjuntos declarados.

La demo no establece equivalencia física, dinámica, algebraica ni geométrica entre niveles.

---

## Traducción

Sea:

\[
T:X\rightarrow Y.
\]

Definimos la imagen:

\[
T(X)=\{T(x):x\in X\}.
\]

Para cada:

\[
y\in T(X)
\]

definimos la fibra:

\[
T^{-1}(y)
=
\{x\in X:T(x)=y\}.
\]

---

## Exceso colapsado

Definimos:

\[
E(T)
=
|X|-|T(X)|.
\]

Equivalentemente:

\[
E(T)
=
\sum_{y\in T(X)}
\left(
|T^{-1}(y)|-1
\right).
\]

Esta cantidad mide cuántos elementos fuente exceden al número de clases que sobreviven tras la traducción.

En dominios finitos:

\[
E(T)=0
\iff
T \text{ es inyectiva}.
\]

---

## Pares indistinguibles

Definimos:

\[
P(T)
=
\sum_{y\in T(X)}
\binom{|T^{-1}(y)|}{2}.
\]

Esta cantidad cuenta pares distintos:

\[
x_1\neq x_2
\]

tales que:

\[
T(x_1)=T(x_2).
\]

Por tanto:

\[
P(T)=0
\iff
T \text{ es inyectiva}.
\]

Aunque E(T) y P(T) detectan ambos no inyectividad, no son la misma magnitud.

Para una fibra de tamaño tres:

\[
E=3-1=2,
\]

mientras que:

\[
P=\binom{3}{2}=3.
\]

DMO-006 incluye explícitamente este caso.

---

## Destinos no alcanzados

Definimos:

\[
U(T)
=
|Y|-|T(X)|.
\]

En dominios finitos:

\[
U(T)=0
\iff
T \text{ es sobreyectiva}.
\]

---

## Equivalencia exacta como conjuntos

Dentro de los dominios finitos declarados:

\[
T \text{ biyectiva}
\iff
E(T)=0
\land
U(T)=0.
\]

Equivalentemente:

\[
T \text{ biyectiva}
\iff
P(T)=0
\land
U(T)=0.
\]

Una biyección permite una correspondencia uno-a-uno entre los elementos de X y Y.

Esto no implica por sí mismo equivalencia de estructuras adicionales.

Si X o Y poseen dinámica, operaciones, geometría, orden u otra estructura, una equivalencia de esa estructura exige condiciones adicionales de preservación.

---

## Caso 1 — relabeling biyectivo

Se usa una correspondencia uno-a-uno entre cuatro estados fuente y cuatro estados destino.

Resultado:

- inyectiva;
- sobreyectiva;
- biyectiva;
- exceso colapsado igual a cero;
- pares indistinguibles igual a cero;
- ningún destino no alcanzado.

Este caso representa una equivalencia exacta como conjuntos declarados.

---

## Caso 2 — coarse-graining

Cuatro estados fuente se traducen a dos clases:

\[
\{0,2\}\rightarrow \mathrm{par},
\]

\[
\{1,3\}\rightarrow \mathrm{impar}.
\]

Resultado:

\[
E(T)=2,
\]

\[
P(T)=2,
\]

\[
U(T)=0.
\]

La traducción es sobreyectiva pero no inyectiva.

Hay pérdida de distinciones fuente.

---

## Caso 3 — enriquecimiento representacional derivado

Se traduce:

\[
x
\mapsto
(x,x\bmod 2).
\]

La segunda coordenada parece enriquecer la representación, pero está completamente determinada por x.

Resultado:

- inyectiva;
- no sobreyectiva;
- sin pérdida de distinciones fuente;
- cuatro estados del dominio destino declarado quedan fuera de la imagen.

La coordenada adicional constituye una ganancia de representación, no información independiente nueva.

---

## Caso 4 — proyección de canales opuestos

Se estudia:

\[
T(a,b)=a-b
\]

sobre:

\[
(a,b)\in\{0,1\}^2.
\]

Los estados:

\[
(0,0)
\]

y:

\[
(1,1)
\]

producen ambos:

\[
T=0.
\]

Por tanto la proyección no es inyectiva.

Resultado:

\[
E(T)=1,
\]

\[
P(T)=1.
\]

Este caso reproduce en una dimensión la estructura estudiada en DMO-003.

---

## Caso 5 — exclusividad de canales

Se restringe el dominio a:

\[
(0,0),(1,0),(0,1).
\]

La misma traducción:

\[
T(a,b)=a-b
\]

se vuelve biyectiva sobre:

\[
\{-1,0,1\}.
\]

Por tanto, la pérdida observada en el caso anterior depende del dominio permitido.

---

## Caso 6 — fibra de tamaño tres

Se traducen tres estados fuente a una sola clase.

La fibra tiene cardinalidad:

\[
3.
\]

Entonces:

\[
E(T)=2,
\]

pero:

\[
P(T)=3.
\]

Este caso demuestra que exceso colapsado y pares indistinguibles son magnitudes distintas.

---

## Identidades verificadas

Para los seis casos se verifica:

\[
E(T)=|X|-|T(X)|
\]

y:

\[
U(T)=|Y|-|T(X)|.
\]

También se comprueba que:

\[
T \text{ biyectiva}
\iff
E(T)=0
\land
U(T)=0.
\]

---

## Qué demuestra

DMO-006 demuestra, dentro de dominios finitos declarados, que una traducción puede auditarse mediante:

\[
T
\rightarrow
\text{fibras}
\rightarrow
E(T),P(T),U(T).
\]

Esto permite distinguir:

- traducción sin pérdida;
- traducción con colapso;
- representación ampliada pero derivada;
- destinos declarados no alcanzados;
- correspondencia biyectiva.

También demuestra que una traducción no debe llamarse equivalencia automáticamente.

---

## Qué no demuestra

DMO-006 no demuestra:

- equivalencia física entre niveles;
- equivalencia dinámica;
- equivalencia geométrica;
- equivalencia algebraica;
- que cualquier traducción relevante de MADELEINE sea finita;
- que una representación más grande contenga información independiente nueva.

Una biyección garantiza únicamente equivalencia exacta como conjuntos declarados, salvo que se demuestre preservación adicional de estructura.

---

## Relación con DMO-003

DMO-003 mostró que la proyección de canales opuestos puede ser no inyectiva cuando se permite coexistencia y biyectiva cuando se impone exclusividad.

DMO-006 reutiliza esa estructura como caso de traducción:

\[
(a,b)\mapsto a-b.
\]

Así, la pérdida o conservación de información puede expresarse mediante las fibras de la traducción.

---

## Estado

CONSTRUIDA — INTERNA — REPRODUCIBLE — CONTABILIDAD FORMAL DE TRADUCCIÓN