# G1 · Producto 2 · Modelo de análisis y verificación (CoffeeCol / Tantico Café)

## 1. Datos de la entrega

- **Producto:** P2 modelo de análisis y verificación
- **Usuario de GitHub del autor:** joanvargas130204
- **Caso de estudio:** CoffeeCol / Tantico Café
- **Trabajo en equipo del año:** sí. El SRS y las fichas de casos de uso las hizo el equipo de 3 aprendices (nombre del equipo: `CoffeeCol`; integrantes: Joan Sebastian Vargas Ramos, Adrian Estiben Garrido Pedroza y Juan Matias Palacios Botello). Lo individual aquí es el modelo de análisis (diagramas, plantillas, dominio, MER, prototipo) y su verificación.

## 2. Qué reutilicé

| Artefacto | Ruta original | ¿Lo hice solo o en equipo? |
|---|---|---|
| Fichas de casos de uso CU-03, CU-06 y CU-11 (Apéndice B del SRS) | `SRS_CoffeeCol_IEEE830_SENA_ADSO.docx` (ruta en mi fork: `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`) | Equipo |
| Requisitos RF-001 a RF-054 y RNF-001 a RNF-017 | Mismo documento | Equipo |
| Casos de uso CU-15 a CU-27 y relaciones include/extend | `../G1-P1-coffeecol/03-casos-de-uso.md` | Individual (P1) |

## 3. Qué ajusté

| # | Artefacto | Qué cambié y por qué | Enlace al commit |
|---|---|---|---|
| 1 | Fichas CU-03, CU-06 y CU-11 → plantillas | Quité detalles de implementación (rutas, peticiones, transacciones, cookies) y los reescribí como intención del actor y respuesta del sistema; agregué las excepciones política de datos no aceptada y producto agotado | [122922e](https://github.com/joanvargas130204/ADSO-3413974/commit/122922e796650795f2223d9d6ac5b685b1d538e3) |
| 2 | Diagrama de iniciar sesión | Corregí el orden (método antes de contactar al servicio) y el enlace mágico, que pasaba por una aprobación que la plantilla no tiene (hallazgo 4) | [122922e](https://github.com/joanvargas130204/ADSO-3413974/commit/122922e796650795f2223d9d6ac5b685b1d538e3) |
| 3 | Modelo de dominio / MER | Quité la asociación Cliente–Nivel (el MER deduce el nivel de los puntos) y agregué el estado de Producto para poder retirarlo (hallazgos 2 y 3) | [122922e](https://github.com/joanvargas130204/ADSO-3413974/commit/122922e796650795f2223d9d6ac5b685b1d538e3) |
| 4 | Matriz de trazabilidad | Tracé Usuario a los requisitos de acceso y corregí el conteo de clases con 2 o más atributos (hallazgos 1 y 5) | [2254ac4](https://github.com/joanvargas130204/ADSO-3413974/commit/2254ac42caa3189e06bb52aad5cc71c9de1b025e) |

## 4. Qué construí nuevo

- 2 diagramas de actividades con calles y guardas, 3 plantillas extendidas, modelo de dominio (18 clases) y MER en pata de gallo (15 entidades).
- 3 pantallas del prototipo rotuladas con su caso de uso.
- Matriz de trazabilidad de los 54 RF (49 llegan a clase y entidad, 90,7 %).
- Lista de chequeo de 21 criterios, script de verificación, informe y registro de 6 hallazgos con antes y después.

## 5. Artefactos entregados

- [x] Diagramas de actividades (fuente editable e imagen): [01-diagramas-de-actividades.md](01-diagramas-de-actividades.md)
- [x] Plantillas extendidas: [plantillas/](plantillas/)
- [x] Modelo de dominio: [03-modelo-de-dominio.md](03-modelo-de-dominio.md)
- [x] MER (pata de gallo): [04-mer.md](04-mer.md)
- [x] Prototipo: [05-prototipo.md](05-prototipo.md)
- [x] Matriz de trazabilidad: [06-matriz-de-trazabilidad.md](06-matriz-de-trazabilidad.md)
- [x] Informe de análisis: [07-informe-de-analisis.md](07-informe-de-analisis.md)
- [x] Lista de chequeo: [08-lista-de-chequeo.md](08-lista-de-chequeo.md)
- [x] Registro de ajustes: [09-registro-de-ajustes.md](09-registro-de-ajustes.md)
- [x] Verificación: [verificacion/](verificacion/)

## 6. Declaración de autoría

- [ ] Declaro que el ajuste y lo construido nuevo en esta carpeta es **mi trabajo individual**.
- [x] Declaro que lo que tomé de mi equipo o de otra fuente está identificado en la sección 2.
- [x] Entiendo que el sábado 28 de noviembre de 2026 el instructor me hará **3 preguntas orales** sobre mis productos y que, si respondo bien menos de 2, el producto sobre el que fallé queda con tope de 50.

Firma (usuario de GitHub y fecha): `joanvargas130204 · 27 de noviembre de 2026`

## 7. Uso de inteligencia artificial

| Herramienta | Para qué la usé | Qué verifiqué o corregí yo |
|---|---|---|
| Claude (Anthropic) | Proponer los diagramas, las plantillas, el modelo de dominio, el MER, el prototipo y el script de verificación a partir de mi SRS | Revisé los diagramas. |

## 8. Autocontrol antes del push

- [x] Hice commits propios en al menos 2 días distintos entre el 21 y el 28 de noviembre.
- [x] No subí el marco documental del instructor, plantillas sin diligenciar ni archivos de otras personas.
- [x] Hice `push` y comprobé en GitHub que la carpeta está publicada.
