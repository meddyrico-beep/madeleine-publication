# LAB-FEN-001 — Resultado HISTORY-DEPTH-v1

## Estatuto

Primera ejecución de:

HISTORY-DEPTH-v1.

Protocolo:

`lab/LAB-FEN-001_HISTORY_DEPTH_SPEC_v1.md`

Ejecutable:

`lab/LAB-FEN-001_HISTORY_DEPTH.py`

Resultado estructurado:

`lab/results/LAB-FEN-001_HISTORY_DEPTH_v1_results.json`

Resumen tabular:

`lab/results/LAB-FEN-001_HISTORY_DEPTH_v1_summary.csv`

El protocolo y el ejecutable fueron congelados antes de esta ejecución.

No se regeneraron trayectorias.

Se utilizaron exclusivamente series previamente congeladas.

---

# 1. Definición operativa

Se compararon modelos predictivos:

M1:

P(x[t+1] | x[t])

M2:

P(x[t+1] | x[t-1], x[t])

M3:

P(x[t+1] | x[t-2], x[t-1], x[t])

M4:

P(x[t+1] | x[t-3], x[t-2], x[t-1], x[t]).

Para cada salto:

G_k = L_(k-1) - L_k.

Un DEPTH_HIT requiere:

G_k > 0

y:

G_k > Q0.95 del nulo condicional correspondiente.

Se utilizaron:

64 permutaciones.

Método de percentil:

nearest-rank.

Suavizado:

alpha = 0.5.

---

# 2. Contabilidad de borde

Las series congeladas contienen 30001 estados.

Para mantener contextos completos:

G2 utiliza 17999 ejemplos de train.

G3 utiliza 17998.

G4 utiliza 17997.

Cada comparación utiliza:

12000 ejemplos de test.

En cada G_k los modelos corto y largo comparten exactamente el mismo conjunto de targets.

---

# 3. HD-D0

Expectativa predeclarada:

k*=1.

Resultado:

8/8 semillas clasificadas como:

k*=1.

No se observan hits en G2, G3 ni G4.

Resultado de sistema:

PASS.

---

# 4. HD-D1

Expectativa predeclarada:

k*=2.

Resultado:

8/8 semillas clasificadas como:

k*=2.

G2:

aproximadamente +1.606666 en las ocho semillas.

G3:

0.

G4:

0.

La dependencia adicional queda concentrada en el salto de orden 1 a orden 2.

Resultado de sistema:

PASS.

---

# 5. HD-D2

Expectativa predeclarada:

k*=2.

Resultado:

8/8 semillas clasificadas como:

k*=2.

G2:

aproximadamente +0.508 a +0.510.

G3:

negativo y sin hit.

G4:

negativo y sin hit.

Bajo HISTORY-DEPTH-v1 no se detecta ganancia predictiva adicional más allá del orden 2.

Resultado de sistema:

PASS.

---

# 6. HD-DELAYED

Expectativa predeclarada:

k*=3.

Resultado:

8/8 semillas clasificadas como:

k*=3.

G2:

negativo y sin hit.

G3:

aproximadamente +0.499 a +0.501.

G4:

negativo y sin hit.

Resultado de sistema:

PASS.

---

# 7. Resultado global

HD-D0:

8/8 — PASS.

HD-D1:

8/8 — PASS.

HD-D2:

8/8 — PASS.

HD-DELAYED:

8/8 — PASS.

Resultado final:

HISTORY-DEPTH-v1 PASS.

---

# 8. Resolución de DELAYED_PAST

El resultado anterior de DELAYED_PAST bajo el detector inmediato permanece válido.

Ese detector no encontró dependencia histórica conjunta basada en:

(x[t-1], x[t]).

HISTORY-DEPTH-v1 muestra ahora que la misma serie presenta una ganancia fuerte al introducir:

x[t-2].

Por tanto, dentro de estos controles construidos, la ausencia de señal a profundidad 2 no implica ausencia de dependencia histórica.

La dependencia puede estar localizada a una profundidad diferente.

---

# 9. Escalera observada

La clasificación predeclarada fue recuperada exactamente:

D0:

k*=1.

D1:

k*=2.

D2:

k*=2.

DELAYED:

k*=3.

No apareció ninguna clasificación:

DEPTH COMPLEX.

No apareció:

k*=4.

---

# 10. Lectura permitida

Dentro de HISTORY-DEPTH-v1 puede afirmarse:

EL INSTRUMENTO DISTINGUE OPERATIVAMENTE PROFUNDIDADES HISTORICAS 1, 2 Y 3 EN LOS CONTROLES CONSTRUIDOS.

Para LAB-D2-v1 puede afirmarse:

LA DEPENDENCIA HISTORICA DETECTADA ES COMPATIBLE CON PROFUNDIDAD OPERATIVA k*=2 BAJO HISTORY-DEPTH-v1.

Para DELAYED_PAST puede afirmarse:

LA DEPENDENCIA GENERATIVA CON RETARDO x[t-2] ES RECUPERADA POR EL SALTO G3 BAJO HISTORY-DEPTH-v1.

---

# 11. Lo que no demuestra

Este resultado no demuestra:

- que k* sea universal;
- que k* sea una constante física;
- que todo proceso tenga profundidad histórica finita;
- que todo mecanismo de orden 3 sea detectable con este instrumento;
- que ausencia de hit implique ausencia absoluta de dependencia;
- que orden predictivo equivalga automáticamente a causalidad física;
- que no existan dependencias débiles más profundas;
- que k* constituya una geometría;
- memoria física externa.

---

# 12. Consecuencia metodológica

La profundidad histórica debe tratarse como variable experimental.

No debe fijarse a priori en:

k=2

ni identificarse automáticamente con memoria completa.

El detector debe ser adecuado al retardo que pretende evaluar.

Este resultado fortalece la introducción de:

k*

como profundidad histórica operativa variable dentro del programa fenomenológico.

---

# 13. Relación con DMO-004

HISTORY-DEPTH-v1 no modifica ni reabre el resultado:

DMO-004 PASS.

Constituye una caracterización posterior del régimen interno ya admitido.

LAB-D2-v1 permanece sin cambios.

---

# 14. Hashes

JSON SHA256:

0d4468e27dfb91e053eb9698b856ef3acde8df7e3039336b750e8c8980d0a579

CSV SHA256:

c7460fde6cfeaad1a6d27449cc78fb358f6e6071bf2a29f3387492bf1057ff2d

---

## Estado

HISTORY-DEPTH-v1 PASS — ESCALERA 1/2/2/3 RECUPERADA 8/8 EN LOS CUATRO CONTROLES — k* OPERATIVO VARIABLE — SIN CLAIM FISICO EXTERNO