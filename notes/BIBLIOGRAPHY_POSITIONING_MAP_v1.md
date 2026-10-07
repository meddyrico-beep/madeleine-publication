# MADELEINE — Bibliography & Positioning Map v1

Estado:
BIBLIOGRAPHY-POSITIONING-MAP-v1

Objetivo:
Definir qué funciones bibliográficas necesita el corpus público antes de seleccionar o insertar referencias concretas.

Este mapa no valida externamente MADELEINE y no establece equivalencias con los marcos citados.

---

# 1. Regla general

Una referencia sólo podrá incorporarse si cumple una función concreta y verificable dentro del manuscrito.

No se admitirán:

- citas decorativas;
- referencias introducidas únicamente por proximidad terminológica;
- atribuciones históricas no verificadas;
- equivalencias entre MADELEINE y un marco externo que no hayan sido demostradas;
- referencias secundarias cuando exista una fuente primaria adecuada y verificable;
- fuentes provisionales o imposibles de verificar.

---

# 2. Clases bibliográficas requeridas

## A. Fundamentos de información y comparación

Función:
Dar contexto estándar a nociones externas utilizadas o potencialmente utilizadas en la capa experimental, como información, divergencia y comparación probabilística.

Condición de entrada:
Sólo citar conceptos que aparezcan efectivamente en la exposición pública o cuya presencia sea necesaria para documentar una métrica usada.

No autoriza:
Identificar las métricas de MADELEINE con una teoría de información completa.

## B. Procesos estocásticos, dependencia histórica y orden

Función:
Contextualizar la distinción entre dependencia del estado actual y dependencia de historia finita cuando se exponga HISTORY-DEPTH.

Condición de entrada:
Usar literatura estándar o primaria para conceptos externos de proceso, dependencia condicional u orden histórico.

No autoriza:
Interpretar k* como orden físico universal, memoria física ni orden verdadero absoluto del proceso.

## C. Secuencias, periodicidad y aperiodicidad

Función:
Contextualizar construcciones de control o nociones de periodicidad/aperiodicidad utilizadas en LAB-FEN-001.

Condición de entrada:
La referencia debe corresponder a una construcción o concepto que se mencione expresamente en el manuscrito público.

No autoriza:
Convertir el comportamiento de los controles construidos en una clasificación general de sistemas dinámicos.

## D. Sistemas dinámicos y estabilidad

Función:
Dar contexto disciplinar a términos externos como estabilidad, régimen, persistencia o dinámica cuando puedan ser confundidos con usos técnicos clásicos.

Condición de entrada:
La cita debe servir para marcar diferencia de uso, no para reclamar equivalencia.

No autoriza:
Presentar los regímenes internos de MADELEINE como equivalentes a estabilidad clásica sin demostración.

## E. Posicionamiento frente a marcos clásicos

Función:
Explicar de forma sobria qué relación sí y qué relación no se está afirmando entre MADELEINE y marcos matemáticos o físicos establecidos.

Condición de entrada:
Las referencias seleccionadas deben representar correctamente el marco externo y utilizarse sólo para delimitar alcance o comparación explícita.

No autoriza:
Claims de sustitución, superación, reducción o equivalencia no demostrados.

---

# 3. Zonas del manuscrito que pueden requerir citas

## Tomo I

- definiciones propias del sistema: normalmente no requieren cita externa;
- términos con posible lectura clásica: sólo requieren cita si se establece comparación explícita;
- cláusulas que dicen que MADELEINE no es todavía teoría física validada: no requieren por sí solas cita bibliográfica.

## Tomo II

- comparabilidad, traducción y representación pueden requerir contexto externo únicamente cuando se compare formalmente con literatura existente;
- la arquitectura interna D0--D11 no debe vestirse retrospectivamente con bibliografía ajena.

## Tomo III

- LAB-FEN-001;
- dependencia histórica;
- periodicidad y aperiodicidad;
- métricas informacionales si se exponen;
- controles construidos;
- sección específica de antecedentes y posicionamiento.

Este tomo será el punto principal de entrada de bibliografía técnica.

---

# 4. Separación obligatoria

Cada inserción bibliográfica deberá distinguir:

ANTECEDENTE EXTERNO:
concepto, resultado, método o vocabulario ya existente en la literatura.

CONSTRUCCION MADELEINE:
definición, regla, instrumento, demo o resultado producido dentro del corpus.

RELACION:
comparación, uso instrumental, diferencia o ausencia de equivalencia.

Nunca se omitirá esta separación cuando la proximidad terminológica pueda sugerir dependencia o equivalencia.

---

# 5. Prioridad de fuentes

Orden preferente:

1. artículo o monografía primaria cuando sea la fuente natural del concepto;
2. referencia estándar de alta autoridad para definiciones consolidadas;
3. revisión académica sólo cuando sea necesaria para panorama o posicionamiento;
4. evitar fuentes divulgativas para sustentar afirmaciones técnicas.

Cada entrada deberá ser verificable mediante metadatos bibliográficos suficientes.

---

# 6. Criterio de suficiencia para el release

La bibliografía de la primera publicación no tiene que ser exhaustiva.

Debe ser suficiente para:

- identificar las fuentes externas realmente utilizadas;
- separar antecedentes de contribuciones propias;
- contextualizar los métodos o conceptos técnicos externos que aparecen en el manuscrito;
- permitir comparación disciplinada con literatura relevante;
- evitar que nomenclatura interna sea confundida con terminología clásica establecida.

---

# 7. Flujo de incorporación

MAPA -> VERIFICACION DE FUENTES -> REFERENCES.BIB -> CITAS PUNTUALES -> NOTA DE POSICIONAMIENTO -> BUILD -> AUDITORIA

No se introducirán primero citas y después se decidirá qué justifican.

---

# 8. Estado

BIBLIOGRAPHY-POSITIONING-MAP-v1 DEFINIDO — FUENTES CONCRETAS AUN NO SELECCIONADAS
