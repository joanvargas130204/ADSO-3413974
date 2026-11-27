# G1 · Producto 1 · Plan de análisis y casos de uso (CoffeeCol / Tantico Café)

## 1. Datos de la entrega

- **Producto:** P1 plan de análisis y casos de uso
- **Usuario de GitHub del autor:** joanvargas130204
- **Caso de estudio:** CoffeeCol / Tantico Café, plataforma e-commerce de café colombiano de especialidad
- **Trabajo en equipo del año:** sí. El SRS y sus casos de uso base los hizo el equipo de 3 aprendices (nombre del equipo: `CoffeeCol`). Lo individual aquí es el ajuste: la caracterización y selección de metodología, el plan, la matriz de cobertura, el diagrama y las relaciones «include» y «extend».

## 2. Qué reutilicé

| Artefacto | Ruta original (mi fork o equipo) | ¿Lo hice solo o en equipo? |
|---|---|---|
| SRS v2.0 (IEEE 830): RF-001 a RF-054, RNF-001 a RNF-017 | `SRS_CoffeeCol_IEEE830_SENA_ADSO.docx` (ruta en mi fork: `02-training-project/01-phase/01-analysis/02-requirements/04-evidence-learning/SRS_CoffeeCol_IEEE830_SENA_ADSO.docx`) | Equipo |
| Casos de uso CU-01 a CU-14 y sus fichas (Apéndice B del SRS) | Mismo documento | Equipo |
| Historias de usuario HU-01 a HU-09 (Apéndice A) | Mismo documento | Equipo |

## 3. Qué ajusté

| # | Artefacto | Qué cambié y por qué | Enlace al commit |
|---|---|---|---|
| 1 | Cobertura de requisitos | El SRS traza 18 de los 54 RF (Apéndice C) y deja requisitos sin caso (RF-001, 003, 004, 005, 029, 032, 039, canje de puntos). Agregué CU-15 a CU-27 y la matriz cubre los 54 RF (mejora C3) | [7c83a4c](https://github.com/joanvargas130204/ADSO-3413974/commit/7c83a4c692e5cba5ccba4268b1a0e04137e44191) |
| 2 | Relaciones entre casos | El SRS no tiene «include» ni «extend». Modelé 5 «include» y 4 «extend» con punto de extensión y justificación de una línea (mejora C4) | [7c83a4c](https://github.com/joanvargas130204/ADSO-3413974/commit/7c83a4c692e5cba5ccba4268b1a0e04137e44191) |
| 3 | Diagrama de casos de uso | Pasé de una lista de casos a un diagrama UML con frontera, 5 actores (Firebase como secundario, Temporizador que inicia el bono de cumpleaños) y generalización Cliente → Visitante; separé «Consultar/Canjear Puntos» en CU-09 y CU-22 (mejora C4) | [7c83a4c](https://github.com/joanvargas130204/ADSO-3413974/commit/7c83a4c692e5cba5ccba4268b1a0e04137e44191) |
| 4 | Metodología | El SRS no selecciona metodología; comparé RUP, Scrum, XP y RAD con 6 criterios tomados de las características del proyecto y elegí Scrum (mejora C1, C2) | [7c83a4c](https://github.com/joanvargas130204/ADSO-3413974/commit/7c83a4c692e5cba5ccba4268b1a0e04137e44191) |

## 4. Qué construí nuevo

- Caracterización, comparación de 4 metodologías y selección justificada.
- Plan de 8 actividades con responsable, fecha y entregable.
- Diagrama de casos de uso con 27 casos y justificación de cada relación.
- Matriz requisito → caso de uso (54 de 54 RF) y distinción de los 17 RNF.

## 5. Artefactos entregados

**Producto 1**

- [x] Caracterización de la solución: [01-caracterizacion-y-metodologia.md](01-caracterizacion-y-metodologia.md)
- [x] Comparación de metodologías y selección justificada: [01-caracterizacion-y-metodologia.md](01-caracterizacion-y-metodologia.md)
- [x] Plan de actividades, cronograma y entregables: [02-plan-de-analisis.md](02-plan-de-analisis.md)
- [x] Diagrama de casos de uso (fuente editable): [diagramas/casos-de-uso.dot](diagramas/casos-de-uso.dot)
- [x] Diagrama de casos de uso (imagen): [diagramas/casos-de-uso.png](diagramas/casos-de-uso.png) y [.svg](diagramas/casos-de-uso.svg)
- [x] Matriz requisito → caso de uso: [04-matriz-requisito-caso-uso.md](04-matriz-requisito-caso-uso.md)
- Apoyo: [requisitos](00-requisitos-coffeecol.md) · [casos de uso y relaciones](03-casos-de-uso.md)

## 6. Declaración de autoría

- [ ] Declaro que el ajuste y lo construido nuevo en esta carpeta es **mi trabajo individual**.
- [ ] Declaro que lo que tomé de mi equipo o de otra fuente está identificado en la sección 2.
- [ ] Entiendo que el sábado 28 de noviembre de 2026 el instructor me hará **3 preguntas orales** sobre mis productos y que, si respondo bien menos de 2, el producto sobre el que fallé queda con tope de 50.

Firma (usuario de GitHub y fecha): `joanvargas130204 · __ de noviembre de 2026`

## 7. Uso de inteligencia artificial

| Herramienta | Para qué la usé | Qué verifiqué o corregí yo |
|---|---|---|
| Claude (Anthropic) | Resumir el SRS en tablas, proponer los casos de soporte, la comparación de metodologías, el plan y el diagrama (Graphviz) a partir de mi SRS | Revisé los diagramas. |

## 8. Autocontrol antes del push

- [ ] Hice commits propios en al menos 2 días distintos entre el 21 y el 28 de noviembre.
- [ ] No subí el marco documental del instructor, plantillas sin diligenciar ni archivos de otras personas.
- [ ] Hice `push` y comprobé en GitHub que la carpeta está publicada.
