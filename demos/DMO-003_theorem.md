# DMO-003 — Teorema de proyección de seis canales

## Dominio

Sea el estado de seis canales:

\[
c=(x_+,x_-,y_+,y_-,z_+,z_-)
\]

con:

\[
x_\pm,y_\pm,z_\pm\in\{0,1,\ldots,m\}.
\]

Definimos la proyección cartesiana:

\[
P(c)=
(x_+-x_-,
 y_+-y_-,
 z_+-z_-).
\]

---

## Proposición 1 — imagen de la proyección

La imagen de \(P\) es:

\[
\{-m,\ldots,m\}^3.
\]

Por tanto:

\[
|\operatorname{Im}P|
=
(2m+1)^3.
\]

El espacio completo de seis canales contiene:

\[
(m+1)^6
\]

estados.

---

## Proposición 2 — cardinalidad exacta de cada fibra

Para una coordenada:

\[
d=a-b,
\qquad
a,b\in\{0,\ldots,m\},
\]

el número de pares que producen \(d\) es:

\[
m+1-|d|.
\]

Por independencia de los tres pares de canales, para:

\[
v=(d_x,d_y,d_z)
\]

se obtiene:

\[
\boxed{
|P^{-1}(v)|
=
(m+1-|d_x|)
(m+1-|d_y|)
(m+1-|d_z|)
}.
\]

---

## Demostración unidimensional

Sea:

\[
d\ge0.
\]

La condición:

\[
a-b=d
\]

implica:

\[
a=b+d.
\]

Como:

\[
0\le b\le m-d,
\]

existen exactamente:

\[
m-d+1
=
m+1-|d|
\]

soluciones.

Para:

\[
d<0
\]

el argumento es simétrico intercambiando \(a\) y \(b\).

Por tanto:

\[
|P^{-1}(d)|=m+1-|d|.
\]

La fórmula tridimensional resulta multiplicando las cardinalidades de las tres coordenadas.

QED.

---

## Corolario 1 — no inyectividad del espacio completo

Para:

\[
m\ge1,
\]

la proyección completa no es inyectiva.

Por ejemplo:

\[
(1,0,0,0,0,0)
\]

y:

\[
(2,1,0,0,0,0)
\]

son estados distintos pero tienen la misma proyección:

\[
(1,0,0).
\]

Por tanto, la lectura cartesiana puede perder información presente en los seis canales.

---

## Corolario 2 — número de vectores con preimagen única

Una fibra tiene cardinalidad uno si y solo si:

\[
m+1-|d_x|
=
m+1-|d_y|
=
m+1-|d_z|
=
1.
\]

Esto exige:

\[
|d_x|=|d_y|=|d_z|=m.
\]

Existen exactamente:

\[
2^3=8
\]

vectores de este tipo.

Por tanto, para \(m\ge1\), el número de vectores cartesianos con múltiples preimágenes es:

\[
\boxed{
(2m+1)^3-8
}.
\]

Para:

\[
m=2,
\]

esto produce:

\[
5^3-8
=
125-8
=
117,
\]

exactamente el resultado obtenido en DMO-003.

---

## Corolario 3 — fibra del vector cero

Para:

\[
v=(0,0,0)
\]

se obtiene:

\[
|P^{-1}(0,0,0)|
=
(m+1)^3.
\]

Con:

\[
m=2
\]

hay:

\[
27
\]

estados de canales distintos que proyectan sobre el mismo vector cartesiano nulo.

---

## Régimen de exclusividad

Definimos el subconjunto:

\[
C_{\mathrm{exc}}
=
\{
c:
x_+x_-=0,\;
y_+y_-=0,\;
z_+z_-=0
\}.
\]

Para cada eje existen exactamente:

\[
2m+1
\]

estados exclusivos:

\[
(0,0),
(1,0),\ldots,(m,0),
(0,1),\ldots,(0,m).
\]

Por tanto:

\[
|C_{\mathrm{exc}}|
=
(2m+1)^3.
\]

---

## Proposición 3 — equivalencia bajo exclusividad

La restricción:

\[
P|_{C_{\mathrm{exc}}}
\]

es biyectiva sobre:

\[
\{-m,\ldots,m\}^3.
\]

Para una coordenada \(d\):

\[
d\ge0
\Rightarrow
(d,0),
\]

y:

\[
d<0
\Rightarrow
(0,-d).
\]

Esta representación es única.

Por tanto, bajo exclusividad de canales opuestos, el estado de seis canales es equivalente a una codificación separada de signo y magnitud de un vector cartesiano.

---

## Resultado para MADELEINE

DMO-003 establece una distinción precisa.

### Sin exclusividad

Si canales opuestos pueden coexistir y dicha coexistencia forma parte del estado:

\[
P
\]

es muchos-a-uno.

Entonces los seis canales contienen información que la lectura cartesiana neta elimina.

### Con exclusividad

Si cada par de canales opuestos es mutuamente exclusivo:

\[
P
\]

es biyectiva.

En ese régimen, la representación de seis canales no añade por sí sola grados de libertad respecto de un vector cartesiano.

---

## Consecuencia para C016

La formulación fuerte:

> el plano carlesino no es equivalente a una representación cartesiana

no puede sostenerse sin especificar la estructura de los canales.

La formulación restringida demostrada es:

> Una representación de seis canales contiene información adicional respecto de su proyección cartesiana exactamente cuando conserva grados de libertad que la diferencia entre canales opuestos no determina.

DMO-003 no demuestra todavía una geometría nueva.

Demuestra cuándo la representación de canales es redundante y cuándo la proyección cartesiana pierde información.
