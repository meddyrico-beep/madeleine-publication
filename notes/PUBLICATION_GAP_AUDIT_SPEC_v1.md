# MADELEINE — PUBLICATION GAP AUDIT v1

## Estatuto

Este documento congela antes de la auditoría los criterios de preparación para publicación.

Versión:

PUBLICATION-GAP-AUDIT-v1.

La auditoría no abre nuevos experimentos.

No modifica resultados científicos congelados.

No redefine retrospectivamente claims.

Su objetivo es medir qué falta para producir un:

PUBLICATION RELEASE CANDIDATE

apto para publicación pública como preprint técnico/reproducible.

No evalúa validación física externa.

---

# 1. Unidad de evaluación

La puntuación total será:

0 a 100.

Se compone de siete dimensiones independientes.

No se permitirá mover pesos después de observar el resultado.

---

# 2. Dimensiones y pesos

## A. Cierre científico interno

Peso:

20 puntos.

Evalúa si los resultados que forman parte de la publicación tienen:

- especificación previa cuando corresponda;
- ejecutable o demostración reproducible;
- resultado registrado;
- límites interpretativos explícitos;
- estado PASS/FAIL documentado;
- separación entre resultado interno y claim externo.

Puntuación máxima:

20.

---

## B. Higiene de claims

Peso:

15 puntos.

Evalúa:

- CLAIMS_TABLE;
- CLAIMS_AUDIT_SUMMARY;
- DEMO_CLAIM_MAP;
- dossier externo;
- correspondencia claim-evidencia;
- ausencia de promoción física no sustentada;
- terminología consistente.

Puntuación máxima:

15.

---

## C. Integración del manuscrito

Peso:

20 puntos.

Evalúa si los resultados congelados están correctamente integrados en:

- Documento Madre;
- Tomo I;
- Tomo II;
- Tomo III;
- preludio/corpus cuando corresponda;
- arquitectura/apéndices cuando corresponda.

La existencia de resultados en `lab/` sin integración editorial completa cuenta como gap.

Puntuación máxima:

20.

---

## D. Reproducibilidad y trazabilidad

Peso:

15 puntos.

Evalúa:

- scripts presentes;
- resultados estructurados;
- hashes;
- commits;
- orden spec -> executable -> result;
- working tree limpio;
- tests;
- instrucciones mínimas de reproducción;
- ausencia de artefactos derivados sin procedencia.

Puntuación máxima:

15.

---

## E. Bibliografía y posicionamiento

Peso:

10 puntos.

Evalúa:

- referencias identificables;
- fuentes primarias cuando sea posible;
- correspondencia entre citas y afirmaciones;
- posicionamiento frente a literatura relacionada;
- separación entre antecedentes y contribuciones propias;
- ausencia de referencias provisionales o placeholders.

Puntuación máxima:

10.

---

## F. Consistencia editorial y notacional

Peso:

10 puntos.

Evalúa:

- sub₀ como origen conceptual canónico;
- distinción entre D0-D11 dimensional y LAB-D0/LAB-D1/LAB-D2;
- símbolos consistentes;
- fórmulas consistentes;
- nombres de archivos/versiones;
- encabezados;
- encoding;
- referencias cruzadas;
- tablas y figuras;
- ausencia de contradicciones entre tomos.

Puntuación máxima:

10.

---

## G. Paquete de release

Peso:

10 puntos.

Evalúa:

- PDFs finales;
- README de publicación;
- instrucciones de reproducción;
- manifiesto de artefactos;
- hashes finales;
- estado Git limpio;
- tag/version final;
- ausencia de archivos temporales;
- estructura apta para depósito público.

Puntuación máxima:

10.

---

# 3. Estados por ítem

Cada ítem evaluado recibirá exactamente uno de estos estados:

PASS

PARTIAL

FAIL

NOT APPLICABLE

INSUFFICIENT EVIDENCE.

No se reinterpretarán estados después de calcular la puntuación.

---

# 4. Conversión a puntuación

Para cada ítem aplicable:

PASS = 1.0

PARTIAL = 0.5

FAIL = 0.0

INSUFFICIENT EVIDENCE = 0.0

NOT APPLICABLE se excluye del denominador de su dimensión.

La puntuación de cada dimensión será:

peso_dimension
*
puntos_obtenidos
/
puntos_aplicables.

La puntuación total será la suma de las siete dimensiones.

---

# 5. Bloqueadores

Además de la puntuación existen bloqueadores absolutos.

Un release candidate no puede declararse READY si existe cualquiera de los siguientes:

1. working tree no limpio al cierre;

2. tests bloqueantes;

3. claim físico externo presentado como establecido sin evidencia externa correspondiente;

4. resultado citado en manuscrito sin artefacto trazable cuando el resultado depende de computación;

5. contradicción canónica material entre documentos principales;

6. fuente bibliográfica esencial marcada como provisional, inexistente o no verificable;

7. PDFs principales que no compilan o faltan;

8. placeholders editoriales visibles en documentos públicos;

9. hashes/manifiesto finales inconsistentes;

10. ausencia de declaración explícita de alcance y limitaciones.

Los bloqueadores no se compensan con puntuación alta.

---

# 6. Niveles de readiness

## 0–59

NO READY.

Existen gaps estructurales importantes.

## 60–74

MAJOR REVISION.

La base existe, pero faltan componentes relevantes.

## 75–84

MINOR/STRUCTURAL REVISION.

El trabajo es publicable en principio, pero todavía no debe liberarse como release candidate.

## 85–94

PRE-RELEASE.

El núcleo está listo y faltan principalmente integración, edición o empaquetado.

## 95–100

RELEASE CANDIDATE.

Sólo si además:

blockers = 0.

---

# 7. Umbral de release

La declaración:

PUBLICATION RELEASE CANDIDATE READY

requiere simultáneamente:

score >= 95

y:

blockers = 0

y:

tests = PASS

y:

working tree = CLEAN.

No basta una puntuación de 95 si existe un bloqueador.

---

# 8. Alcance científico

El audit evalúa preparación editorial y reproducibilidad.

No convierte MADELEINE en:

- teoría física validada;
- teoría universal;
- sustitución probada de teorías clásicas;
- modelo empíricamente confirmado del mundo físico.

---

# 9. Evidencia experimental cerrada

Para esta fase se consideran congelados, entre otros:

LAB-D0-v1.

LAB-D1-v1.

LAB-D2-v1.

LAB-D2 ABLATIONS-v1.

LAB-D2 ATLAS-v1.

DMO-004 AUDIT-v1.

HISTORY-DEPTH-v1.

HISTORY-DEPTH-ATLAS-v1.

No se abrirán nuevos experimentos para mejorar la puntuación del audit.

Si el audit encuentra una carencia científica, se registrará como gap para trabajo futuro o revisión posterior.

---

# 10. Política anti-score-hacking

Después de congelar este documento no podrán modificarse bajo v1:

- pesos;
- estados;
- conversión numérica;
- bloqueadores;
- bandas de readiness;
- umbral de release.

Las correcciones editoriales posteriores podrán mejorar una segunda medición usando exactamente esta misma regla.

Si la regla necesita cambiar, deberá abrirse:

PUBLICATION-GAP-AUDIT-v2.

---

# 11. Primera medición

La primera medición debe evaluar el repo tal como existe después del cierre experimental.

No se corregirán gaps antes de registrarlos en la primera auditoría.

Esto permite distinguir:

estado inicial

de:

mejora posterior.

---

# 12. Salidas esperadas

La auditoría deberá producir:

1. score total /100;

2. score por dimensión;

3. lista completa de ítems evaluados;

4. bloqueadores;

5. gaps críticos;

6. gaps menores;

7. archivos afectados;

8. orden recomendado de corrección;

9. estimación de trabajo restante;

10. veredicto de readiness.

---

# 13. Flujo posterior

Después de la primera medición:

AUDIT
->
GAP FIXES
->
RE-AUDIT
->
RELEASE CANDIDATE.

No:

AUDIT
->
NUEVO EXPERIMENTO.

---

## Estado

PUBLICATION-GAP-AUDIT-v1 DEFINIDO — AUN NO EJECUTADO