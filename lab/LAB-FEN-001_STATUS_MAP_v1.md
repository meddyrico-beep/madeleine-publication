# LAB-FEN-001 — Mapa consolidado de estado v1

## Estatuto

Este documento consolida el estado alcanzado por LAB-FEN-001 después de:

- calibración LAB-D0-v1;
- calibración LAB-D1-v1;
- construcción LAB-D2-v1;
- ablaciones causales v1;
- atlas local paramétrico v1;
- auditoría DMO-004 v1.

No introduce nuevas métricas.

No introduce nuevos experimentos.

No modifica resultados anteriores.

Su función es separar explícitamente:

1. resultados internos establecidos;
2. observaciones descriptivas;
3. interpretaciones permitidas;
4. cuestiones todavía abiertas.

---

# 1. Secuencia experimental

La secuencia congelada es:

LAB-D0-v1
->
LAB-D1-v1
->
LAB-D2-v1
->
ABLATIONS-v1
->
ATLAS-v1
->
DMO-004 AUDIT-v1.

---

# 2. LAB-D0-v1

## Función

Control negativo de primer orden.

## Resultado

LAB-D0-v1 PASS.

Delta hits:

0/8.

C hits:

0/8.

No aparece una señal histórica consistente bajo el detector congelado.

## Lo que establece

El bloque de detección no produce de forma sistemática una señal histórica positiva cuando el generador no utiliza el pasado inmediato.

## Lo que no establece

No demuestra que todo proceso de primer orden posible produzca exactamente el mismo comportamiento numérico.

---

# 3. LAB-D1-v1

## Función

Control positivo de dependencia histórica rígida y periódica.

## Resultado

Delta hits:

8/8.

C hits:

8/8.

Dependencia histórica estructural:

presente.

Regla:

determinista.

Periodo:

25.

## Lo que establece

El bloque histórico detecta una dependencia de segundo orden construida explícitamente.

## Lo que no establece

No constituye por sí mismo un régimen flexible.

No constituye evidencia de aperiodicidad.

No constituye descubrimiento causal observacional.

---

# 4. LAB-D2-v1

## Arquitectura

Estado causal:

(x[t-1], x[t]).

Familia de sucesores:

tres estados permitidos dependientes del contexto histórico.

Elección:

uniforme dentro de la familia.

## Resultado local

Seed passes conjuntos:

8/8.

Se satisfacen simultáneamente:

A1 > 0,

Delta_hist > 0,

Delta hit,

C_hist > 0,

C hit,

P_rel > T_P,

N > T_N,

U > T_U.

## Estado inicial obtenido

CANDIDATA INTERNA QUE SUPERA LA FIRMA LOCAL.

---

# 5. Ablaciones causales v1

## NO_PAST

La dependencia del pasado inmediato se elimina.

Resultado:

0/8 seed passes.

La señal histórica conjunta desaparece.

## RANDOMIZED_PAST

El pasado real se sustituye por una señal independiente.

Resultado:

0/8 seed passes.

La diversidad y la aperiodicidad pueden mantenerse altas mientras desaparece la señal histórica conjunta.

## DETERMINISTIC_CHOICE

Se conserva dependencia histórica pero se elimina la elección flexible.

Resultado:

0/8 seed passes.

Señal histórica conjunta:

5/8.

U <= T_U:

8/8.

En la ejecución observada:

U = 0

en las ocho semillas.

## DELAYED_PAST

La regla utiliza x[t-2].

Bajo el detector histórico inmediato:

0/8 señal histórica conjunta.

Esta condición era diagnóstica.

No demuestra ausencia de historia más profunda.

## Resultado de batería

ABLATION BATTERY v1 PASS.

---

# 6. Lectura mecanística restringida

Dentro de LAB-FEN-001-v1, los resultados son compatibles con que la firma completa de LAB-D2-v1 dependa conjuntamente de:

historia causal alineada

+

elección flexible.

Esta afirmación queda restringida a los mecanismos y controles ensayados.

No constituye una necesidad matemática universal.

No constituye causalidad física.

---

# 7. Atlas local paramétrico v1

## Parámetros

beta:

deformación de probabilidades dentro de la familia causal.

epsilon:

fuga uniforme hacia el alfabeto completo.

## Núcleo predeclarado

9 puntos.

Resultado:

9/9 POINT PASS.

## Malla completa

20 puntos.

Resultado:

20/20 POINT PASS.

## Componente conexo del basal

20/20 puntos.

## Resultado

LOCAL PARAMETRIC REGION v1 PASS.

---

# 8. Qué establece el atlas

LAB-D2-v1 no es un punto aislado dentro de las perturbaciones paramétricas v1 declaradas.

Existe una región paramétrica local PASS bajo el contrato experimental utilizado.

---

# 9. Qué no establece el atlas

El atlas no localiza la frontera exterior.

El resultado 20/20 no significa que toda extensión paramétrica vaya a pasar.

Sólo significa que la frontera no apareció dentro de la ventana v1 ensayada.

---

# 10. Observaciones descriptivas del atlas

Al aumentar epsilon dentro de la malla estudiada se observa descriptivamente:

- disminución de A1;
- disminución de Delta_hist;
- disminución de C_hist;
- disminución general de P_rel;
- aumento general de N;
- mantenimiento de U en valores altos.

Estas tendencias no están promovidas a leyes.

No constituyen todavía un análisis formal de frontera.

---

# 11. Auditoría DMO-004

Criterios evaluados:

region_parametric:

PASS.

seed_agreement:

PASS.

null_separation:

PASS.

explicit_failure_criterion:

PASS.

non_reducible:

PASS.

frozen_rule:

PASS.

complete_trace:

PASS.

Resultado:

7/7 PASS.

Veredicto:

DMO-004 PASS.

---

# 12. Estado interno actual

La promoción máxima permitida es:

REGIMEN INTERNO ADMITIDO BAJO LAB-FEN-001-v1 Y DMO-004.

La expresión "régimen" en este documento significa régimen interno bajo el gate declarado.

No significa régimen físico demostrado.

---

# 13. Resultados establecidos dentro del laboratorio

A fecha de esta consolidación quedan establecidos dentro de sus contratos respectivos:

1. LAB-D0 funciona como control negativo de historia inmediata.

2. LAB-D1 funciona como control positivo de historia rígida de segundo orden.

3. LAB-D2 supera la firma local completa en 8/8 semillas.

4. Las ablaciones primarias predeclaradas son superadas.

5. La firma LAB-D2 no sobrevive como firma completa al eliminar el pasado real.

6. Una señal histórica independiente no sustituye al pasado causal real bajo los controles ensayados.

7. La determinización destruye la aperiodicidad requerida en el control ensayado.

8. LAB-D2 ocupa una región paramétrica local predeclarada.

9. Los 20 puntos explorados pertenecen al componente PASS conectado al basal.

10. LAB-D2 satisface los siete criterios internos de DMO-004.

---

# 14. No-reducibilidad: alcance exacto

La afirmación permitida es:

NO REDUCIBLE A LOS LIMITES INTERNOS ENSAYADOS EN LAB-FEN-001-v1.

Los límites ensayados incluyen:

- primer orden;
- ausencia de pasado;
- pasado independiente;
- elección histórica determinista;
- control histórico periódico rígido.

No se afirma:

IRREDUCIBILIDAD FRENTE A TODO MODELO POSIBLE.

---

# 15. Cuestiones abiertas

Permanecen abiertas al menos las siguientes preguntas.

## A. Frontera exterior

No sabemos todavía dónde deja de pasar el régimen al aumentar las perturbaciones.

## B. Profundidad histórica

DELAYED_PAST muestra que el detector inmediato no basta para caracterizar dependencias de otros retardos.

Debe construirse un protocolo explícito para k*.

## C. Necesidad frente a contingencia

Todavía debe distinguirse qué elementos de LAB-D2 son necesarios para el régimen y cuáles son elecciones particulares de implementación.

## D. Generalización arquitectónica

No se ha probado una familia amplia de reglas causales alternativas.

## E. Fenomenología posterior

Todavía debe estudiarse cómo este régimen se relaciona con persistencia, memoria, reorganización, colapso, jerarquía y niveles posteriores.

## F. Geometría

No debe introducirse una interpretación geométrica obligatoria a partir de estos resultados.

## G. Física

No existe todavía validación física externa.

---

# 16. Próximos experimentos posibles

Existen tres líneas naturales.

A. ATLAS-BOUNDARY-v1

Buscar explícitamente la frontera exterior sin alterar el atlas v1.

B. HISTORY-DEPTH-v1

Construir un detector escalonado de profundidad histórica para:

k = 1, 2, 3, ...

C. MECHANISM-FAMILY-v1

Probar familias causales alternativas para distinguir propiedades necesarias de detalles de LAB-D2.

Estas líneas deben abrir protocolos nuevos antes de observar resultados.

---

# 17. Orden metodológico recomendado

El orden recomendado desde este punto es:

1. preservar LAB-D2-v1 y DMO-004 sin modificaciones;
2. estudiar profundidad histórica;
3. localizar fronteras externas;
4. estudiar familias alternativas;
5. construir fenomenología de nivel superior;
6. sólo después reconsiderar geometría;
7. mantener cualquier claim físico separado hasta disponer de evidencia externa específica.

---

# 18. Estado final de esta fase

CONTROL NEGATIVO:

VALIDADO INTERNAMENTE.

CONTROL POSITIVO:

VALIDADO INTERNAMENTE.

FIRMA LOCAL LAB-D2:

PASS.

ABLACIONES CAUSALES:

PASS.

REGION PARAMETRICA LOCAL:

PASS.

DMO-004:

7/7 PASS.

ESTADO:

REGIMEN INTERNO ADMITIDO BAJO LAB-FEN-001-v1 Y DMO-004.

CLAIM FISICO EXTERNO:

NO REALIZADO.