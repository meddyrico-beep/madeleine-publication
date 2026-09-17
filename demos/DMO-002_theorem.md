# DMO-002 — Proposición analítica del doble registro

## Dominio

Sea:

\[
H=(x_0,x_1,\ldots,x_n)
\]

una historia con:

\[
x_0=0
\]

y:

\[
x_i\in\{0,1,\ldots,m\}.
\]

Definimos:

\[
\delta(H)
=
\sum_{i=0}^{n-1}|x_{i+1}-x_i|.
\]

Sea:

\[
\Delta_n^{(m)}
=
\{\delta(H):H\text{ tiene exactamente }n\text{ transiciones}\}.
\]

---

## Proposición 1 — conjunto completo de medidas

Para todo:

\[
m\ge1,\qquad n\ge1,
\]

se cumple:

\[
\boxed{
\Delta_n^{(m)}
=
\{0,1,\ldots,mn\}
}
\]

y, por tanto:

\[
\boxed{
|\Delta_n^{(m)}|
=
mn+1
}.
\]

---

## Demostración

Toda transición satisface:

\[
|x_{i+1}-x_i|\le m.
\]

Luego:

\[
0\le\delta(H)\le mn.
\]

Por tanto:

\[
\Delta_n^{(m)}
\subseteq
\{0,1,\ldots,mn\}.
\]

Falta demostrar la inclusión contraria.

Sea:

\[
k\in\{0,1,\ldots,mn\}.
\]

Por división euclídea:

\[
k=qm+r,
\]

con:

\[
q\ge0,
\qquad
0\le r<m.
\]

Construimos una historia desde \(0\).

Primero realizamos \(q\) saltos completos de longitud \(m\), alternando:

\[
0\to m\to0\to m\to\cdots.
\]

Estos saltos aportan:

\[
qm
\]

a la medida acumulada.

Si:

\[
r=0,
\]

las transiciones restantes mantienen la posición actual y aportan longitud cero.

Si:

\[
r>0,
\]

hacemos una transición adicional de longitud \(r\).

Si la posición actual es \(0\), tomamos:

\[
0\to r.
\]

Si la posición actual es \(m\), tomamos:

\[
m\to m-r.
\]

En ambos casos la nueva posición sigue perteneciendo a:

\[
\{0,\ldots,m\}.
\]

Las transiciones restantes mantienen la posición alcanzada.

Cuando \(r>0\), de:

\[
k=qm+r\le mn
\]

se sigue:

\[
q\le n-1,
\]

por lo que la transición residual cabe dentro de las \(n\) transiciones disponibles.

La medida total construida es:

\[
qm+r=k.
\]

Por tanto, todo entero:

\[
k\in\{0,\ldots,mn\}
\]

es realizable.

Así:

\[
\boxed{
\Delta_n^{(m)}
=
\{0,1,\ldots,mn\}
}.
\]

Y su cardinalidad es:

\[
\boxed{
|\Delta_n^{(m)}|=mn+1
}.
\]

QED.

---

## Corolario 1 — el conteo no determina la medida

Para un valor fijo de \(n\):

\[
|\Delta_n^{(m)}|=mn+1.
\]

Si:

\[
m\ge1,
\]

entonces:

\[
mn+1>1.
\]

Por tanto, un mismo conteo \(n\) admite múltiples valores de \(\delta\).

Así:

\[
\boxed{
n\not\Rightarrow\delta
}
\]

dentro de este dominio.

---

## Corolario 2 — la medida no determina el conteo

Para cualquier:

\[
m\ge1,
\]

la medida:

\[
\delta=1
\]

puede realizarse para cualquier:

\[
n\ge1
\]

mediante una transición:

\[
0\to1
\]

seguida de \(n-1\) permanencias.

Por tanto, el mismo valor de \(\delta\) puede asociarse a diferentes conteos.

Así:

\[
\boxed{
\delta\not\Rightarrow n
}
\]

cuando se comparan historias con diferentes números de transiciones.

---

## Corolario 3 — número de clases de medida

Si:

\[
1\le n\le N,
\]

el conjunto global de medidas posibles es:

\[
\{0,1,\ldots,mN\}.
\]

Por tanto:

\[
\boxed{
|\{\delta\}|=mN+1
}.
\]

---

## Corolario 4 — número de pares del doble registro

Para cada \(n\):

\[
|\Delta_n^{(m)}|=mn+1.
\]

Por tanto:

\[
|\{(n,\delta)\}|
=
\sum_{n=1}^{N}(mn+1).
\]

Luego:

\[
\boxed{
|\{(n,\delta)\}|
=
\frac{mN(N+1)}{2}+N
}.
\]

---

## Recuperación exacta del barrido DMO-002

Para:

\[
m=4,
\qquad
N=6,
\]

se obtiene:

\[
|\{\delta\}|
=
4(6)+1
=
25.
\]

Además:

\[
|\{(n,\delta)\}|
=
\frac{4(6)(7)}{2}+6
=
90.
\]

Y para cada \(n\):

\[
|\Delta_n|
=
4n+1.
\]

Esto produce exactamente:

\[
5,\ 9,\ 13,\ 17,\ 21,\ 25.
\]

Por tanto, las cardinalidades observadas por
`DMO-002_sweep.py`
quedan derivadas analíticamente.

---

## Resultado para C014

DMO-002 dispone ahora de una proposición matemática dentro de su dominio:

> Bajo la operacionalización discreta de DMO-002, el conteo n y la medida acumulada delta son coordenadas no redundantes: ninguno determina al otro.

Esto es más fuerte que los contraejemplos iniciales y que el barrido computacional aislado.

No demuestra, sin embargo, que toda noción posible de contar y medir sea universalmente irreductible.

La conclusión continúa restringida al dominio y definiciones declarados.
