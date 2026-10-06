# LAB-FEN-001 — HISTORY-DEPTH-ATLAS v1

## Estatuto

Este documento congela antes de resultados un protocolo para evaluar la estabilidad paramétrica de la profundidad histórica operativa k*.

Versión:

HISTORY-DEPTH-ATLAS-v1.

No introduce nuevas trayectorias.

No modifica:

- LAB-D2-v1;
- ATLAS-v1;
- HISTORY-DEPTH-v1;
- DMO-004.

El experimento consume exclusivamente series previamente congeladas del atlas local paramétrico v1.

---

# 1. Pregunta

LAB-D2-v1 fue clasificado bajo HISTORY-DEPTH-v1 como:

k*=2.

El atlas local paramétrico v1 mostró una región PASS alrededor del punto basal.

La pregunta ahora es:

¿permanece k*=2 dentro de esa región paramétrica?

---

# 2. Instrumento

Se reutiliza sin modificaciones el instrumento congelado:

HISTORY-DEPTH-v1.

Se mantienen:

- M1, M2, M3 y M4;
- definición de G2, G3 y G4;
- alpha = 0.5;
- 64 permutaciones;
- percentil nearest-rank Q0.95;
- definición de DEPTH_HIT;
- clasificación k*;
- semillas;
- train/test;
- contabilidad de borde.

No se recalibrará el instrumento.

---

# 3. Fuente de datos

Se utilizarán exclusivamente las series congeladas de:

LAB-FEN-001_D2_ATLAS_v1.

No se regenerarán trayectorias.

No se modificarán beta ni epsilon.

---

# 4. Núcleo predeclarado

El núcleo formal será exactamente el mismo núcleo predeclarado en ATLAS-v1:

beta:

-0.05,
0.00,
+0.05.

epsilon:

0.00,
0.05,
0.10.

Total:

9 puntos.

No se redefinirá el núcleo después de observar resultados.

---

# 5. Malla extendida

Los 11 puntos restantes de la malla ATLAS-v1 se evaluarán también.

Su función será descriptiva.

No podrán modificar retrospectivamente el gate formal del núcleo.

---

# 6. Clasificación por semilla

Para cada punto:

(beta, epsilon)

y cada semilla se calcularán:

G2,
G3,
G4,

sus nulos correspondientes,

DEPTH_HIT_2,
DEPTH_HIT_3,
DEPTH_HIT_4,

y la clasificación:

k*=1,
k*=2,
k*=3,
k*=4,

o:

DEPTH COMPLEX.

---

# 7. Expectativa predeclarada

Para los nueve puntos del núcleo se espera:

k*=2.

No se exige esta expectativa a la malla extendida para el gate formal v1.

---

# 8. Gate por punto

Un punto del núcleo será:

DEPTH POINT PASS

si al menos:

7/8

semillas son clasificadas:

k*=2.

En cualquier otro caso será:

DEPTH POINT FAIL.

No existe compensación entre semillas de distintos puntos.

---

# 9. Gate regional

HISTORY-DEPTH-ATLAS-v1 PASS

requiere:

9/9

puntos del núcleo como:

DEPTH POINT PASS.

No se permitirá compensar un punto FAIL con mejores resultados en otro.

---

# 10. Punto basal

El punto:

beta=0,
epsilon=0

debe ser consistente con el resultado congelado de HISTORY-DEPTH-v1:

8/8 semillas con k*=2.

El punto basal no se utilizará para recalibrar el instrumento.

Su función será de control de consistencia.

---

# 11. Malla completa

Para los 20 puntos se registrarán descriptivamente:

- conteo de semillas k*=1;
- conteo de semillas k*=2;
- conteo de semillas k*=3;
- conteo de semillas k*=4;
- conteo DEPTH COMPLEX;
- G2 mínimo y máximo;
- G3 mínimo y máximo;
- G4 mínimo y máximo.

---

# 12. Falsación

El gate formal falla si cualquiera de los nueve puntos del núcleo obtiene menos de:

7/8

clasificaciones k*=2.

Un punto con:

k*=3,
k*=4,

o:

DEPTH COMPLEX

no será reinterpretado para preservar el PASS.

---

# 13. Interpretación permitida si PASS

Si el núcleo obtiene 9/9 DEPTH POINT PASS podrá afirmarse:

LA PROFUNDIDAD HISTORICA OPERATIVA k*=2 ES ESTABLE EN EL NUCLEO PARAMETRICO PREDECLARADO DE LAB-D2 BAJO HISTORY-DEPTH-v1.

También podrá afirmarse:

k*=2 NO ES EXCLUSIVO DEL PUNTO BASAL DENTRO DEL NUCLEO ENSAYADO.

---

# 14. Interpretación no permitida

Incluso con PASS no podrá afirmarse:

- que k*=2 sea universal;
- que toda la familia D2 tenga k*=2;
- que k*=2 permanezca fuera de la malla ensayada;
- que k*=2 sea necesario para todo régimen posible;
- que k* sea una constante física;
- que k* constituya memoria física;
- que k* defina una geometría;
- que el resultado tenga validación externa.

---

# 15. Resultado negativo

Un FAIL no revocará retrospectivamente:

HISTORY-DEPTH-v1,

ATLAS-v1,

ni:

DMO-004.

Significará que la estabilidad del régimen y la estabilidad de su profundidad histórica no coinciden necesariamente.

---

# 16. Orden experimental

1. congelar esta especificación;
2. inspeccionar únicamente el formato de las series ATLAS-v1;
3. construir el ejecutable;
4. realizar STRUCTURE CHECK sin evaluar G_k;
5. congelar el ejecutable;
6. ejecutar una sola vez;
7. registrar resultados;
8. congelar el acta.

---

# 17. Regla anti-ajuste

Después de la primera ejecución no podrán modificarse bajo v1:

- el núcleo 3x3;
- la expectativa k*=2;
- el gate 7/8 por punto;
- el gate 9/9 regional;
- el instrumento HISTORY-DEPTH-v1;
- los nulos;
- las semillas;
- las longitudes;
- los umbrales.

Cualquier modificación requerirá:

HISTORY-DEPTH-ATLAS-v2.

---

## Estado

HISTORY-DEPTH-ATLAS-v1 DEFINIDO — AUN NO EJECUTADO