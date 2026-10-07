# MADELEINE — Bibliography Claim Gate v1

Estado:
BIBLIOGRAPHY-CLAIM-GATE-v1

Base:
- BIBLIOGRAPHY-POSITIONING-MAP-v1
- BIBLIOGRAPHY-SOURCE-VERIFICATION-v1

Objetivo:
Decidir qué fuentes externas verificadas tienen una función real en el manuscrito público actual.

Este gate no modifica resultados experimentales ni introduce dependencias retrospectivas en el núcleo MADELEINE.

---

# 1. Resultado del cruce repositorio -> manuscrito

El manuscrito público actual no contiene menciones explícitas a:

- Shannon;
- entropía;
- información mutua;
- Kullback--Leibler;
- Markov;
- De Bruijn.

Sí contiene:

- aperiodicidad;
- dependencia histórica;
- profundidad histórica operativa;
- k* como clasificación instrumental.

La capa de laboratorio sí utiliza explícitamente:

- nulos Markov-1;
- entropía histórica;
- información mutua condicional;
- divergencia Jensen--Shannon;
- ciclo de De Bruijn para LAB-D1.

---

# 2. Decisión por fuente

## SRC-001 — Shannon 1948

DECISION: DIFERIDA

Razón:
Los conceptos informacionales que podrían justificar esta referencia permanecen en la capa de laboratorio y no aparecen todavía en la exposición pública.

No se incorporará sólo por proximidad conceptual.

## SRC-002 — Kullback y Leibler 1951

DECISION: NO INCORPORAR EN v1

Razón:
No existe uso explícito de divergencia Kullback--Leibler en el manuscrito público ni en el protocolo experimental auditado actualmente considerado.

La divergencia identificada en la capa de métricas es Jensen--Shannon, por lo que una referencia KL no debe utilizarse como sustituto bibliográfico.

## SRC-003 — Cover y Thomas

DECISION: DIFERIDA

Razón:
Es una referencia estándar adecuada para conceptos informacionales, pero dichos conceptos no se exponen actualmente con suficiente detalle en el manuscrito público.

Podrá reevaluarse si la publicación incorpora las definiciones de entropía, información mutua condicional u otras métricas informacionales.

## SRC-004 — Norris 1997

DECISION: CANDIDATA DIRECTA DE POSICIONAMIENTO

Razón:
La capa experimental utiliza procesos Markov-1 como nulos explícitos y el manuscrito público comunica dependencia y profundidad histórica.

Función permitida:
Definir o contextualizar la propiedad Markoviana estándar para delimitar la lectura de HISTORY-DEPTH.

La referencia no respaldará los resultados numéricos de MADELEINE; esos resultados permanecen respaldados por sus propios artefactos reproducibles.

No autoriza:
- identificar k* con orden Markoviano universal;
- afirmar que LAB-D2 sea un proceso físico Markoviano o no Markoviano;
- convertir HISTORY-DEPTH en una teoría general de memoria;
- atribuir el núcleo MADELEINE a teoría de cadenas de Markov.

## SRC-005 — de Bruijn 1946

DECISION: DIFERIDA

Razón:
LAB-D1 utiliza internamente un ciclo de De Bruijn, pero esta construcción no se identifica por nombre en el manuscrito público actual.

Sólo deberá incorporarse si la descripción pública de LAB-D1 explicita esa construcción.

---

# 3. Fuente adicional detectada

La sonda confirmó uso de divergencia Jensen--Shannon en LAB-FEN-001_METRICS-v1.

DECISION:
No incorporar todavía una nueva referencia.

Motivo:
La métrica Jensen--Shannon no aparece actualmente en el manuscrito público.

Si la capa de métricas se hace pública con mayor detalle, deberá verificarse una fuente específica adecuada antes de citarla.

---

# 4. Regla fuente -> claim

Una referencia externa puede entrar al manuscrito sólo cuando existe una oración pública concreta cuya comprensión o procedencia externa requiera esa fuente.

La fuente debe respaldar únicamente el componente externo de esa oración.

Los resultados propios de LAB-FEN-001 siguen siendo respaldados por:

- especificaciones congeladas;
- ejecutables;
- resultados estructurados;
- actas;
- hashes;
- historial Git.

Una referencia bibliográfica externa no sustituye esa trazabilidad.

---

# 5. Resultado del gate

SRC-001: DIFERIDA
SRC-002: NO INCORPORAR EN v1
SRC-003: DIFERIDA
SRC-004: CANDIDATA DIRECTA DE POSICIONAMIENTO
SRC-005: DIFERIDA

Número de fuentes actualmente justificadas para inserción inmediata: 1.

---

# 6. Próximo paso

Antes de crear references.bib se redactará la oración exacta de posicionamiento asociada a SRC-004 y se comprobará que:

- no altera ningún resultado congelado;
- no identifica k* con orden Markoviano;
- separa antecedente externo de instrumento MADELEINE;
- mejora el posicionamiento sin crear un claim nuevo.

BIBLIOGRAPHY-CLAIM-GATE-v1 CERRADO
