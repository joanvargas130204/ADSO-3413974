# G2 · Producto 1 · Artefactos de diseño (CoffeeCol / Tantico Café)

## 1. Datos de la entrega

| Campo | Valor |
|---|---|
| Producto | P1 (artefactos de diseño) |
| Usuario de GitHub del autor | joanvargas130204 |
| Ficha | 3413974 |
| Caso elegido (nombre del proyecto) | CoffeeCol / Tantico Café (plataforma e-commerce de café colombiano de especialidad) |
| Enlace al informe de análisis o SRS del caso (ruta en tu fork) | `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx` (`SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`); modelo de análisis propio en `02-training-project/01-phase/01-analysis/03-conceptual-model/04-evidence-learning/G1-P1-coffeecol/` y `G1-P2-coffeecol/` |
| Cuenta de GitHub con la que haces los commits | joanvargas130204 |

## 2. Origen del insumo y trabajo en equipo

| Pregunta | Respuesta |
|---|---|
| ¿El SRS / informe de análisis lo elaboró un equipo? ¿Cuántas personas? | Sí, un equipo de 3 aprendices (nombre del equipo: CoffeeCol; integrantes: Joan Sebastian Vargas Ramos, Adrian Estiben Garrido Pedroza y Juan Matias Palacios Botello) |
| ¿Qué parte del SRS es tuya? | El SRS lo elaboramos entre los 3 integrantes del equipo; no separo una parte individual |
| ¿Los artefactos de esta entrega los hiciste tú solo? | Los elaboré con Claude (ver sección 6) a partir del SRS del equipo; la autoría de los productos de diseño es individual |
| ¿Otro aprendiz usó o te compartió archivos de esta entrega? | El SRS y el proyecto CoffeeCol los hicimos entre los 3 integrantes del equipo, con apoyo de IA; como partimos del mismo caso, los compañeros pueden tener productos parecidos |

**Subconjunto que diseño (individual):** 17 requisitos funcionales del SRS (RF-011, 012, 014, 017, 018, 019, 020, 021, 022, 023, 024, 025, 027, 028, 038, 045, 046), los que sostienen los casos críticos CU-03, CU-06 y CU-11 del análisis, y 8 RNF (004, 005, 006, 008, 009, 010, 013, 016). El modelo de datos (P2) cubre todo el sistema.

## 3. Qué reutilicé, qué ajusté y qué hice nuevo

| Artefacto | Archivo en esta carpeta | Origen (ruta en mi fork o «nuevo») | Qué ajusté o agregué |
|---|---|---|---|
| A1 Ficha de interpretación y plataforma | [01-ficha-interpretacion-y-plataforma.md](01-ficha-interpretacion-y-plataforma.md) | SRS del equipo (RF, RNF, restricciones) | Seleccioné 17 RF y 8 RNF y justifiqué lenguaje y base de datos con condiciones del caso |
| A2 Diagrama de clases | [02-diagrama-de-clases.md](02-diagrama-de-clases.md) | `01-analysis/03-conceptual-model/.../G1-P2-coffeecol/diagramas/modelo-dominio.mmd` | Pasé del modelo de dominio sin métodos a 28 clases de diseño con tipos, visibilidad, métodos, multiplicidades, composición, herencia e interfaces |
| A3 Patrones | [03-patrones.md](03-patrones.md) | nuevo | Estrategia, Fachada y Singleton aplicados sobre clases del diagrama |
| A4 Arquitectura | [04-arquitectura.md](04-arquitectura.md) | Sección de arquitectura del SRS (3 niveles) | Diagrama, tabla de 8 RNF → decisión y alternativas descartadas |
| A5 Vista de componentes | [05-componentes.md](05-componentes.md) | nuevo | 7 componentes con interfaces y mapeo a clases y requisitos |
| A6 Vista de despliegue | [06-despliegue.md](06-despliegue.md) | nuevo | 4 nodos con artefactos y protocolos |
| A7 Matriz de trazabilidad | [07-matriz-de-trazabilidad.md](07-matriz-de-trazabilidad.md) | `G1-P2-coffeecol/06-matriz-de-trazabilidad.md` | Cambié a requisito → clase → componente → decisión, en los dos sentidos |

**Qué reutilicé (resumen):** el SRS del equipo, mi modelo de dominio y mi matriz de trazabilidad de G1, y la decisión de tres capas con API REST que el SRS ya traía.

**Qué ajusté (resumen):** el modelo de dominio pasó a diagrama de clases de diseño; el atributo `municipio` de `DireccionEntrega` pasó a `idMunicipio` al contrastar con el modelo de datos de P2 (hallazgo H-03).

**Qué hice completamente nuevo (resumen):** los patrones, la vista de componentes, la vista de despliegue y la tabla de decisiones frente a los RNF.

## 4. Autoverificación de mínimos

> Marca con `x` solo lo que de verdad cumples. El instructor lo contrasta con los archivos.

- [x] A1 Ficha de interpretación: ≥ 8 RF y ≥ 3 RNF con ID; plataforma justificada
- [x] A2 Diagrama de clases: ≥ 8 clases, tipos, métodos, multiplicidades, ≥ 1 composición/agregación y ≥ 1 herencia o interfaz (con ≥ 2 implementaciones)
- [x] A3 ≥ 2 patrones GoF distintos aplicados en el diagrama (al menos uno distinto de singleton)
- [x] A4 Arquitectura con diagrama y tabla de ≥ 3 RNF → decisión
- [x] A5 Vista de componentes: ≥ 5 componentes con interfaces
- [x] A6 Vista de despliegue: ≥ 3 nodos con artefactos y protocolos
- [x] A7 Matriz de trazabilidad análisis → diseño
- [x] Fuente editable e imagen exportada de cada diagrama

## 5. Historial de commits

| Día | Qué avancé (mensaje del commit) |
|---|---|
| 25 de noviembre de 2026 | Contenido de los artefactos de diseño o de datos (6 commits) |
| 27 de noviembre de 2026 | README, SRS en el fork y carpeta de verificación |

## 6. Uso de inteligencia artificial (declaración obligatoria)

| Herramienta | Para qué la usé | Qué verifiqué o cambié después |
|---|---|---|
| Claude (Anthropic) | Proponer, a partir de mi SRS y de mi modelo de análisis de G1, el diagrama de clases, los patrones, la arquitectura, los componentes, el despliegue y la matriz de trazabilidad | Revisé los diagramas. |

## 7. Enlaces

- Informe de análisis / SRS del caso: `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`
- Carpeta de esta entrega en GitHub: https://github.com/joanvargas130204/ADSO-3413974/tree/main/02-training-project/01-phase/02-planning/06-architecture/04-evidence-learning/G2-P1-coffeecol

## 8. Declaración de autoría

Declaro que los artefactos de esta carpeta son de mi autoría, que lo que reutilicé de mi trabajo del año o de otras fuentes está indicado en la sección 3, que no entregué como propio material del instructor ni de otros aprendices, y que puedo explicar cada artefacto en la verificación oral.

Usuario de GitHub: joanvargas130204  Fecha: 27/11/2026
