# G2 · Producto 2 · Modelo de datos y verificación (CoffeeCol / Tantico Café)

## 1. Datos de la entrega

| Campo | Valor |
|---|---|
| Producto | P2 (modelo de datos y verificación) |
| Usuario de GitHub del autor | joanvargas130204 |
| Ficha | 3413974 |
| Caso elegido (nombre del proyecto) | CoffeeCol / Tantico Café (plataforma e-commerce de café colombiano de especialidad) |
| Enlace al informe de análisis o SRS del caso (ruta en tu fork) | `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx` (`SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`); modelo de análisis propio en `02-training-project/01-phase/01-analysis/03-conceptual-model/04-evidence-learning/G1-P1-coffeecol/` y `G1-P2-coffeecol/` |
| Cuenta de GitHub con la que haces los commits | joanvargas130204 |

## 2. Origen del insumo y trabajo en equipo

| Pregunta | Respuesta |
|---|---|
| ¿El SRS / informe de análisis lo elaboró un equipo? ¿Cuántas personas? | Sí, un equipo de 3 aprendices (nombre del equipo: CoffeeCol) |
| ¿Qué parte del SRS es tuya? | El SRS lo elaboramos entre los 3 integrantes del equipo; no separo una parte individual |
| ¿Los artefactos de esta entrega los hiciste tú solo? | Los elaboré con Claude (ver sección 6) a partir del SRS del equipo; la autoría de los productos de diseño es individual |
| ¿Otro aprendiz usó o te compartió archivos de esta entrega? | El SRS y el proyecto CoffeeCol los hicimos entre los 3 integrantes del equipo, con apoyo de IA; como partimos del mismo caso, los compañeros pueden tener productos parecidos |

**Subconjunto que diseño (individual):** 17 requisitos funcionales del SRS (RF-011, 012, 014, 017, 018, 019, 020, 021, 022, 023, 024, 025, 027, 028, 038, 045, 046), los que sostienen los casos críticos CU-03, CU-06 y CU-11 del análisis, y 8 RNF (004, 005, 006, 008, 009, 010, 013, 016). El modelo de datos (P2) cubre todo el sistema.

## 3. Qué reutilicé, qué ajusté y qué hice nuevo

| Artefacto | Archivo en esta carpeta | Origen (ruta en mi fork o «nuevo») | Qué ajusté o agregué |
|---|---|---|---|
| B1 Modelo conceptual | [01-modelo-conceptual.md](01-modelo-conceptual.md) | `01-analysis/03-conceptual-model/.../G1-P2-coffeecol/diagramas/mer-pata-de-gallo.mmd` | Agregué `correo` al administrador, el verbo y la cardinalidad mín/máx de cada relación y el tipo de base justificado |
| B2 Modelo lógico | [02-modelo-logico.md](02-modelo-logico.md) | MER de G1 | 15 tablas con PK/FK, cuadro de 10 reglas de transformación y diagrama lógico |
| B3 Normalización | [03-normalizacion.md](03-normalizacion.md) | nuevo | 2 tablas de 0FN a 3FN con dependencias funcionales y decisiones de desnormalización |
| B4 Diccionario | [04-diccionario-de-datos.md](04-diccionario-de-datos.md) | nuevo | 15 tablas y 82 columnas con tipo, tamaño, restricciones y dominio |
| B5 Script SQL y evidencia | [05-script-sql-y-evidencia.md](05-script-sql-y-evidencia.md), [sql/](sql/) | nuevo | Script MariaDB y SQLite, pruebas y logs de ejecución |
| B6 Políticas de seguridad | [06-politicas-de-seguridad.md](06-politicas-de-seguridad.md) | RNF de seguridad del SRS | 10 políticas, matriz de 3 roles × 15 tablas y cuentas de base de datos |
| B7 Lista de chequeo | [07-lista-de-chequeo.md](07-lista-de-chequeo.md) | nuevo | 28 criterios aplicados a P1 y P2, con 4 hallazgos corregidos |

**Qué reutilicé (resumen):** el MER de G1 (15 entidades) y la decisión de MariaDB y 3FN del SRS.

**Qué ajusté (resumen):** el MER pasó de diagrama de análisis a modelo conceptual con cardinalidades y verbos; el esquema se corrigió tras las pruebas (H-01) y tras contrastarlo con las clases de P1 (H-02).

**Qué hice completamente nuevo (resumen):** normalización, diccionario, script y pruebas, políticas de seguridad y lista de chequeo con su verificador automático.

## 4. Autoverificación de mínimos

> Marca con `x` solo lo que de verdad cumples. El instructor lo contrasta con los archivos.

- [x] B1 Modelo conceptual: ≥ 6 entidades, cardinalidades, ≥ 1 N:M y ≥ 1 1:N
- [x] B2 Modelo lógico: ≥ 8 tablas con PK/FK y cuadro de reglas de transformación
- [x] B3 Normalización: ≥ 2 tablas de 0FN a 3FN con dependencias funcionales (una con llave compuesta y una con dependencia transitiva)
- [x] B4 Diccionario de datos completo
- [x] B5 Script SQL ejecutado sin errores (evidencia adjunta) y `ON DELETE` en ≥ 3 FK
- [x] B6 ≥ 6 políticas de seguridad (con hash y sal en contraseñas y TLS) y matriz de ≥ 3 roles
- [x] B7 Lista de chequeo de ≥ 20 criterios, diligenciada sobre P1 y P2, con evidencia

**Nota sobre el motor:** la evidencia de pruebas (inserciones válidas y 16 violaciones rechazadas) es de **SQLite 3.53**. Además, el script de MariaDB se ejecutó completo el 27/11/2026 en **MariaDB 10.4.32 (XAMPP)** sin errores: 15 tablas InnoDB, 14 FK y 20 CHECK (ver `verificacion/evidencia-mariadb.txt` y `verificacion/captura-mariadb-phpmyadmin.jpg`).

## 5. Historial de commits

| Día | Qué avancé (mensaje del commit) |
|---|---|
| 25 de noviembre de 2026 | Contenido de los artefactos de diseño o de datos (6 commits) |
| 27 de noviembre de 2026 | README, SRS en el fork y carpeta de verificación |

## 6. Uso de inteligencia artificial (declaración obligatoria)

| Herramienta | Para qué la usé | Qué verifiqué o cambié después |
|---|---|---|
| Claude (Anthropic) | Proponer, a partir de mi SRS y de mi modelo de análisis de G1, el modelo conceptual y lógico, el diccionario, el script SQL con sus pruebas, las políticas de seguridad y la lista de chequeo con su verificador | Revisé los diagramas. |

## 7. Enlaces

- Informe de análisis / SRS del caso: `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`
- Carpeta de esta entrega en GitHub: https://github.com/joanvargas130204/ADSO-3413974/tree/main/02-training-project/01-phase/02-planning/06-architecture/04-evidence-learning/G2-P2-coffeecol

## 8. Declaración de autoría

Declaro que los artefactos de esta carpeta son de mi autoría, que lo que reutilicé de mi trabajo del año o de otras fuentes está indicado en la sección 3, que no entregué como propio material del instructor ni de otros aprendices, y que puedo explicar cada artefacto en la verificación oral.

Usuario de GitHub: joanvargas130204  Fecha: 27/11/2026
