# LAB-FEN-001 — Profundidad histórica v1

## Estatuto

Este documento congela antes de resultados un protocolo para estimar profundidad histórica operativa.

Versión:

HISTORY-DEPTH-v1

El objetivo es distinguir dependencia histórica inmediata de dependencia histórica más profunda.

Este protocolo no modifica:

- LAB-D0-v1;
- LAB-D1-v1;
- LAB-D2-v1;
- ablaciones v1;
- atlas v1;
- DMO-004;
- métricas o resultados ya congelados.

---

# 1. Motivación

La condición DELAYED_PAST utiliza x[t-2] en su mecanismo generador.

Sin embargo, el detector histórico inmediato basado en:

(x[t-1], x[t])

no produjo señal histórica conjunta.

Esto no demuestra ausencia de historia.

Demuestra que un detector de profundidad fija puede no detectar una dependencia localizada en otro retardo.

HISTORY-DEPTH-v1 estudia explícitamente esta cuestión.

---

# 2. Modelos predictivos

Se definen modelos de orden:

M1:

P(x[t+1] | x[t])

M2:

P(x[t+1] | x[t-1], x[t])

M3:

P(x[t+1] | x[t-2], x[t-1], x[t])

M4:

P(x[t+1] | x[t-3], x[t-2], x[t-1], x[t])

No se estudiarán órdenes superiores a 4 bajo v1.

---

# 3. Pérdidas fuera de muestra

Cada modelo Mk será ajustado exclusivamente sobre train.

Se evaluará exclusivamente sobre test.

Sea:

L_k

la log-loss media fuera de muestra del modelo Mk.

Para:

k = 2, 3, 4

se define:

G_k = L_(k-1) - L_k.

Interpretación:

G_k > 0

significa que añadir el estado histórico adicional mejora la predicción fuera de muestra.

---

# 4. Variable añadida en cada nivel

G2 prueba el valor adicional de:

x[t-1]

condicionado a:

x[t].

G3 prueba el valor adicional de:

x[t-2]

condicionado a:

(x[t-1], x[t]).

G4 prueba el valor adicional de:

x[t-3]

condicionado a:

(x[t-2], x[t-1], x[t]).

---

# 5. Nulo condicional

Para cada k se construirá un nulo específico.

El valor histórico añadido en Mk se permuta dentro de estratos definidos por el contexto de orden k-1.

Así:

para G2:

x[t-1] se permuta dentro de grupos con el mismo x[t].

Para G3:

x[t-2] se permuta dentro de grupos con el mismo:

(x[t-1], x[t]).

Para G4:

x[t-3] se permuta dentro de grupos con el mismo:

(x[t-2], x[t-1], x[t]).

El par:

contexto corto -> x[t+1]

permanece intacto.

La dependencia adicional del estado histórico más antiguo queda destruida.

---

# 6. Número de permutaciones

Se utilizarán:

64

permutaciones por semilla y por profundidad.

El percentil crítico será:

Q0.95.

No se modificará retrospectivamente este número bajo v1.

---

# 7. Hit de profundidad

Para cada semilla y cada:

k = 2, 3, 4

se define:

DEPTH_HIT_k = True

si:

G_k > Q0.95(G_k_null)

y:

G_k > 0.

En cualquier otro caso:

DEPTH_HIT_k = False.

---

# 8. Profundidad histórica operativa

Se define k* de forma operativa.

k* = 1

si no existe DEPTH_HIT en:

k = 2, 3, 4.

k* = 2

si:

DEPTH_HIT_2 = True

y no aparecen hits adicionales en:

k = 3, 4.

k* = 3

si:

DEPTH_HIT_3 = True

y:

DEPTH_HIT_4 = False.

k* = 4

si:

DEPTH_HIT_4 = True.

Si aparece una combinación incompatible con estas categorías simples, por ejemplo hits separados no monotónicos, se clasificará como:

DEPTH COMPLEX.

No se forzará retrospectivamente un único k*.

---

# 9. Sistemas a evaluar

Se evaluarán cuatro sistemas ya definidos.

## HD-D0

Fuente:

LAB-D0-v1.

Expectativa predeclarada:

k* = 1.

## HD-D1

Fuente:

LAB-D1-v1.

Expectativa predeclarada:

k* = 2.

## HD-D2

Fuente:

LAB-D2-v1.

Expectativa predeclarada:

k* = 2.

## HD-DELAYED

Fuente:

ABL-DELAYED-PAST-v1.

Expectativa predeclarada:

k* = 3.

---

# 10. Semillas

Se conservan exactamente:

11,
23,
37,
51,
79,
101,
131,
173.

---

# 11. Longitudes

Se conservan:

burn-in = 1000.

transiciones útiles = 30000.

train = 18000.

test = 12000.

---

# 12. Suavizado

Los modelos categóricos utilizarán el mismo esquema de suavizado compatible con los instrumentos históricos ya congelados.

El valor deberá quedar explícito en el ejecutable.

No podrá ajustarse después de observar resultados.

---

# 13. Gate por sistema

Para una profundidad esperada se exige acuerdo de al menos:

7/8

semillas.

HD-D0 pasa su control si al menos 7/8 semillas son clasificadas:

k* = 1.

HD-D1 pasa su control si al menos 7/8 semillas son clasificadas:

k* = 2.

HD-D2 pasa su control si al menos 7/8 semillas son clasificadas:

k* = 2.

HD-DELAYED pasa su control si al menos 7/8 semillas son clasificadas:

k* = 3.

---

# 14. Gate global

HISTORY-DEPTH-v1 PASS

requiere simultáneamente:

HD-D0 PASS

y:

HD-D1 PASS

y:

HD-D2 PASS

y:

HD-DELAYED PASS.

No existe compensación entre controles.

---

# 15. Falsación

El protocolo falla si cualquiera de los cuatro sistemas no alcanza:

7/8

clasificaciones en la profundidad predeclarada.

No se cambiará el rango k=1..4 tras observar los resultados.

No se cambiará el percentil.

No se cambiará el número de nulos.

No se redefinirá k* retrospectivamente.

---

# 16. Interpretación permitida

Si HISTORY-DEPTH-v1 pasa podrá afirmarse:

EL INSTRUMENTO DISTINGUE OPERATIVAMENTE PROFUNDIDADES HISTORICAS 1, 2 Y 3 EN LOS CONTROLES CONSTRUIDOS.

También podrá afirmarse, para LAB-D2-v1:

LA DEPENDENCIA HISTORICA DETECTADA ES COMPATIBLE CON PROFUNDIDAD OPERATIVA k*=2 BAJO HISTORY-DEPTH-v1.

---

# 17. Interpretación no permitida

Incluso si el protocolo pasa no podrá afirmarse:

- que k* sea una constante física;
- que k* sea universal;
- que todo sistema tenga profundidad finita;
- que orden predictivo equivalga automáticamente a mecanismo causal;
- que no existan dependencias más profundas débiles;
- que una clasificación k* sea una geometría;
- que se haya demostrado memoria física.

---

# 18. Relación con DELAYED_PAST

DELAYED_PAST no se reinterpretará retrospectivamente.

Su resultado anterior permanece:

el detector inmediato no encontró señal histórica conjunta.

HISTORY-DEPTH-v1 formula ahora una pregunta diferente:

si un instrumento diseñado explícitamente para x[t-2] puede recuperar la dependencia generativa conocida.

---

# 19. Resultado científico buscado

Este experimento no busca hacer que LAB-D2 pase otro gate.

Busca validar o falsar una herramienta para distinguir:

historia inmediata

de:

historia más profunda.

Un resultado negativo será informativo y no alterará retrospectivamente DMO-004.

---

# 20. Orden experimental

1. congelar esta especificación;
2. construir el ejecutable;
3. verificar estructura sin evaluar series;
4. congelar el ejecutable;
5. ejecutar los cuatro sistemas;
6. registrar resultados por semilla;
7. aplicar el gate 7/8;
8. registrar cualquier patrón DEPTH COMPLEX;
9. congelar resultados;
10. interpretar sólo después.

---

# 21. Regla anti-ajuste

Después de la primera ejecución no podrán modificarse bajo v1:

- órdenes 1..4;
- definición de G_k;
- definición del nulo;
- 64 permutaciones;
- Q0.95;
- semillas;
- longitudes;
- definición de DEPTH_HIT;
- definición de k*;
- requisito 7/8;
- expectativas D0/D1/D2/DELAYED.

Cualquier cambio exigirá:

HISTORY-DEPTH-v2.

---

## Estado

HISTORY-DEPTH-v1 DEFINIDO — AUN NO EJECUTADO