# MADELEINE — F11-CORE-031.X.6.7.4
## Auditoría adversarial analítica: hessianos, ramas, resto de Taylor y presupuesto radial

**Fecha:** 13 de noviembre de 2026  
**Modelo:** D5 Native v0.6, interpretación matemática exacta sobre los reales de constantes binarias IEEE-754 congeladas.  
**Estado:** `INTERNAL_ANALYTIC_AUDIT_PASS`; revisión formal y externa independiente: `PENDING`.  
**Entradas:** `X674_ANALYTIC_REVIEW_INPUTS_v1.zip`, SHA-256 `01B4CD7CE829D0547045D4CE18A4402B2C614AC47410FDB80AD9A6DC11BA9665`.  
**Integridad:** 16/16 archivos internos coinciden con sus hashes congelados.

## 1. Enunciado exacto y alcance

Con estado de siete componentes
\[
 x_n=(\tau_n,\chi_n,v_{\tau,n},v_{\chi,n},m_n,c_n,d_n),
\]
consideramos el mapa real D5 Native v0.6 \(F_n\), con perturbaciones *añadidas después de cada paso*, solo a memoria:
\[
 x_{n+1}=F_n(x_n)+e_4\eta_n,\qquad |\eta_n|\le 6.35\cdot 10^{-6}.
\]
La condición inicial es el estado binario exacto archivado en el índice 1318. Hay 436 transiciones, hasta el índice 1754. El objetivo focalizado es
\[
 \forall\eta\in[-6.35\cdot10^{-6},6.35\cdot10^{-6}]^{436},\quad
 r(x_{1318})-r(x_{1754}(\eta))>0.02.
\]
**Interpretación:** se certifica el mapa matemático de valores reales con parámetros numéricos congelados, no la equivalencia bit a bit para todas las ejecuciones de `math.sin`, `math.cos`, `math.exp` en coma flotante de distintos sistemas.

## 2. Derivación de segundo orden

Las aceleraciones del modelo son
\[
 A_\tau=-\alpha_\tau\tau-\beta_\tau v_\tau+\gamma_\tau\sin(\chi-\tau)
 +\mu_\tau m+\nu_\tau c+\varepsilon_\tau\sin(\omega_\tau n),
\]
\[
 A_\chi=-\alpha_\chi\chi-\beta_\chi v_\chi+\gamma_\chi\sin\tau
 -\sigma_\chi(\chi-\chi_*)+\mu_\chi m-\nu_\chi(1-c)
 +\varepsilon_\chi\cos(\omega_\chi n).
\]
Las velocidades son \(v_\tau^+=v_\tau+dA_\tau\), \(v_\chi^+=v_\chi+dA_\chi\); las posiciones son \(\tau^+=\tau+d v_\tau+d^2A_\tau\) y \(\chi^+=\chi+d v_\chi+d^2A_\chi\).

Con \(e_d\) el vector de la coordenada 6 y \(e_v\) el de la velocidad correspondiente, el hessiano **directo** de la posición es
\[
D^2p^+=d^2D^2A+2d(e_d\otimes\nabla A+\nabla A\otimes e_d)
 +2A(e_d\otimes e_d)+(e_d\otimes e_v+e_v\otimes e_d).
\]
Se verificó simbólicamente su equivalencia con la regla del producto anidada implementada por X670. Las únicas segundas derivadas de aceleración son las trigonométricas de \(\gamma_\tau\sin(\chi-\tau)\) y \(\gamma_\chi\sin\tau\); el término de forzamiento depende de \(n\), no del estado.

En las cajas donde \(\tau-\chi\), \(v_\tau\), \(v_\chi\) tienen signo fijo, la actualización de memoria es afín y \(D^2m^+=0\). Con \(q=\tau-\chi\), \(u=v_\tau-v_\chi\), \(z=d-d_*\), la coherencia usa
\[
 E=\exp(-\kappa_1q^2-\kappa_2u^2-\kappa_3z^2).
\]
Si \(S_a=\sum_l\kappa_l y_l\partial_a y_l\) y \(K_{ab}=\sum_l\kappa_l\partial_a y_l\partial_b y_l\), se demuestra
\[
\partial_{ab}E=E(4S_aS_b-2K_{ab}).
\]
Se verificaron simbólicamente sus 49 entradas. Para la coherencia sin saturación es válido el mayorante
\[
H^c_{ab}=(1-\lambda)E_{\max}(4S_a^*S_b^*+2|K_{ab}|),
\]
con \(E_{\max}\ge E\) y \(S_a^*\ge |S_a|\) sobre toda la caja. El único hessiano no nulo del reloj sin saturación es \(\partial_{dd}d^+=-6k_{\rm cub}(d-d_*)\).

## 3. Garantía de que los intervalos de funciones trascendentes contienen los valores reales

El verificador X670 emplea enteros arbitrarios y fracciones exactas, no `flint` ni aproximaciones flotantes para los mayorantes. Para \(y\in[0,1/2]\), las series alternadas de seno, coseno y \(e^{-y}\) tienen términos decrecientes en valor absoluto. X670 suma 64 términos (índices 0 a 63), de modo que el primer término omitido es no negativo y encierra la función entre la suma y la suma más ese término. Los argumentos más grandes se dividen sucesivamente entre 2 y se reconstruyen mediante
\[
\sin(2y)=2\sin y\cos y,\quad
\cos(2y)=2\cos^2y-1,\quad e^{-2y}=(e^{-y})^2.
\]
Tras cada operación se redondea el extremo inferior hacia \(-\infty\) y el superior hacia \(+\infty\) a una malla de paso \(2^{-512}\). La aritmética de intervalos en las operaciones racionales preserva la inclusión. Se inspeccionó el código de `series`, `sincos`, `expneg`, `outward_t`, `mult`, `floorq` y `ceilq` y su compatibilidad con este argumento.

**Límite:** esto es una auditoría matemática y de implementación realizada aquí, no una verificación de código mediante Lean, Coq, Isabelle o un auditor externo.

## 4. Reconstrucciones de contraste independientes

Se elaboraron programas separados, sin importar X670 ni X673b, y se obtuvieron estos resultados:

| Requisito | Resultado independiente |
|---|---:|
| Hash del paquete recibido | PASS |
| Hashes de sus 16 miembros | 16/16 PASS |
| Identidades simbólicas de velocidad y posición | PASS |
| Entradas del hessiano exponencial contrastadas simbólicamente | 49 PASS |
| Defectos de referencia con intervalos racionales | 3.052 PASS |
| Máximo defecto de referencia | \(1.2742097696790142\cdot10^{-16}\) |
| Cota admisible de referencia | \(2\cdot10^{-16}\) |
| Derivadas jacobianas exportadas conteniendo intervalos racionales recalculados | 21.364/21.364 PASS |
| Gradiente radial terminal recalculado | 7/7 PASS |
| Intervalo de referencia del presupuesto radial | PASS |
| Controles de ramas de salida vía envolvente lineal+resto | 872 PASS |
| Entradas hessianas reconstruidas por fórmulas directas | 149.548 |
| Restos locales obtenidos de esos hessianos y dominados por X672 | 3.052/3.052 PASS |
| Restos locales por encima del valor congelado | 0 |
| Inclusiones de la inducción X673b | 3.045 PASS |
| Holguras inductivas nulas | 0 |
| Holgura inductiva mínima | \(10^{-18}\), paso 1319, componente 0 |

La menor holgura de ramas de entrada registrada en el modelo completo fue \(0.000107947690674943\ldots\), paso 1405, variable \(v_\chi\). La revisión independiente de las ramas de salida por la envolvente lineal y el resto arrojó márgenes inferiores positivos de alrededor de \(0.0186582\) para coherencia y \(0.0408012\) para el reloj. Los valores corresponden a la caja ampliada; no son únicamente evaluaciones del centro.

El código del segundo cálculo de hessianos empleó el hessiano **directo** de la posición, en vez de reproducir la composición anidada X670. Recalculó los 149.548 términos y contrastó los 3.052 restos escalares contra los enteros almacenados en X672: cero insuficiencias. El margen mínimo entre el entero exportado y el resto recalculado es cero unidades de \(2^{-256}\), como es esperable para cotas redondeadas ajustadas. No se pretende una segunda evaluación física experimental: son pruebas matemáticas de coherencia de las cotas.

## 5. Referencia, ramas y Taylor

Los 436 estados de referencia del testigo son puntos racionales exactos (no intervalos con anchura positiva). Las cajas de radio X672 se obtienen de las originales multiplicando por \(201/200\) y redondeando hacia arriba sobre la malla \(2^{-256}\). Se comprobaron las tres ramas de valor absoluto y los dos dominios de saturación en cada etapa; la comprobación original registra 3.052 márgenes de rama de entrada. Para cada componente y paso el defecto queda encerrado por
\[
R_{n,i}=\rho+\frac12\sum_{a,b=0}^6 H_{n,i,a,b}B_{n,a}B_{n,b},\qquad \rho=2\cdot10^{-16}.
\]
Los exponentes se majoran a partir de mínimos absolutos sobre cajas; las cotas de seno y coseno se derivan de su propiedad global 1-Lipschitz y de centros racionalmente encerrados. Los productos de intervalo y el redondeo dirigido no disminuyen los mayorantes.

Con la inclusión por Taylor válida sobre cajas convexas y los jacobianos que contienen las derivadas exactas de referencia, la propagación de perturbación y restos constituye una inducción legítima. X673b verifica los 3.045 componentes intermedios de la inducción, y utiliza la envolvente final calculada para el presupuesto radial del estado 1754.

## 6. Presupuesto radial y la amplitud exterior

La función radial real es
\[
r=r_0+p_1m+p_2c+p_3\cos\tau+p_4\sin\chi.
\]
Su gradiente terminal y el resto de segundo orden se encierran en intervalos racionales. La cota radial obtiene
\[
\underbrace{g}_{\text{separación sin perturbar}}
-\underbrace{\varepsilon_{\rm target}G}_{\text{perturbaciones}}
-\underbrace{D}_{\text{resto dinámico}}
-\underbrace{R_{\rm obs}}_{\text{observable}}
>0.
\]
El valor calculado del margen es \(+8.259118279787193860870465080540769640374659\cdot10^{-8}\).

La **caja inductiva** se cierra para \(\varepsilon_{\rm out}=6.42\cdot10^{-6}\), que es mayor que el objetivo. Sin embargo, el presupuesto radial evaluado con esa amplitud exterior es negativo. La garantía de desigualdad radial se afirma **solo para el objetivo** \(6.35\cdot10^{-6}\). Una cota negativa no constituye un contraejemplo y no establece el umbral máximo de perturbación.

La cota inicial de `0.02` que usó X663 corresponde al valor exacto del flotante binario `0.02`, ligeramente **mayor** que el racional decimal \(1/50\), con diferencia exacta \(3/7205759403792793600\). Esto es conservador para la desigualdad escrita con \(1/50\) y no invalida el margen. La inclusión independiente terminal se verificó con suficiente precisión racional para distinguir este detalle.

## 7. Distinción del alcance y riesgos residuales

1. **Alcance local:** modelo D5 Native v0.6 congelado, estado de entrada indexado 1318, 436 perturbaciones, cantidad radial concreta. No se prueba estabilidad asintótica, todas las ventanas del régimen, ni D1–D21.
2. **Mapas reales frente a `float64`:** se interpretan las constantes binarias como racionales exactos, pero las operaciones del mapa como operaciones reales. No se ha demostrado una cota de error de ejecución flotante para todas las trayectorias perturbadas.
3. **Control del código:** la revisión fue independiente en fórmulas y programas de contraste, pero no equivale a una formalización en un asistente de pruebas ni a una auditoría de seguridad de software completa.
4. **Canon fundacional:** la cota no demuestra por sí misma una correspondencia generativa LAC→D5 ni necesidad matemática de los seis canales.
5. **Originalidad:** los métodos de intervalos, Taylor, propagadores y adjuntos son conocidos; no se ha demostrado originalidad científica por obtener este certificado.
6. **Revisión externa:** faltan la ejecución de un paquete completamente autocontenido por un tercero y una revisión de pruebas/código independiente del equipo autor.

## 8. Dictamen X.6.7.4

**`INTERNAL_ANALYTIC_AUDIT_PASS`** — Las fórmulas principales, las ramas regulares, la construcción de hessianos y los restos recalculados superaron las comprobaciones adversariales disponibles. Los 3.052 restos y 21.364 jacobianos han sido contrastados mediante programas propios de revisión; no se observaron subestimaciones que contradijeran X670. La inducción y el margen radial permanecen estrictamente positivos.

**`EXTERNAL_FORMAL_VERIFICATION_PENDING`** — El resultado debe denominarse *candidato de demostración asistida por ordenador con auditoría matemática interna favorable*, no teorema aceptado por la comunidad ni certificado de todas las implementaciones flotantes.

**Próximo paso:** cierre documental X.6.7.5, mantenimiento de hashes y estado explícito; después preparar propuesta de versión GitHub/Zenodo sin reescribir los archivos congelados.
