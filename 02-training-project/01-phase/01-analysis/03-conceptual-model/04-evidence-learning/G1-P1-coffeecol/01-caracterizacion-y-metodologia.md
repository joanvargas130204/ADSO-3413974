# 1. Caracterización de la solución y selección de metodología

## 1.1 Caracterización de CoffeeCol / Tantico Café

| Aspecto | Valor | Evidencia |
|---|---|---|
| Tipo de proyecto | Aplicación web transaccional y analítica: catálogo, carrito, pedidos, fidelización y panel administrativo con indicadores | SRS v2.0, secciones 1.2 y 2.2 |
| Tamaño del equipo | Pequeño: 3 aprendices | SRS v2.0, portada y sección 1.1 |
| Estabilidad de requisitos | Alta: el SRS v2.0 (octubre de 2026) fija 54 requisitos funcionales como línea base, con prioridades (25 altas, 19 medias y 10 bajas) y los «requisitos futuros» ya separados | SRS v2.0, secciones 2.6 y 3.2 |
| Disponibilidad del cliente | Media: hubo entrevistas con productores en la versión 1.0 y hoy la validación es semanal con el instructor | Historial de versiones del SRS; calendario de la ficha |

## 1.2 Comparación de metodologías

Criterios tomados de la caracterización (1 = poco adecuada, 3 = muy adecuada):

| Criterio (de las características) | RUP | Scrum | XP | RAD |
|---|---|---|---|---|
| Equipo de 3 personas (sin roles ni artefactos pesados) | 1 | 3 | 3 | 2 |
| 54 requisitos ya priorizados (Alta, Media, Baja): se ordenan en un backlog | 2 | 3 | 2 | 1 |
| Requisitos estables con ajustes menores | 2 | 3 | 2 | 3 |
| Cliente disponible solo semanalmente (XP pide cliente en sitio) | 2 | 3 | 1 | 2 |
| Entregas incrementales verificables (catálogo, carrito y pedido, fidelización, analítica) | 2 | 3 | 3 | 3 |
| Documentación de análisis exigida por la formación (casos de uso, modelos) | 3 | 2 | 1 | 2 |
| **Total (máx. 18)** | **12** | **17** | **12** | **13** |

Observaciones:

- **RUP:** cubre bien la documentación, pero sus fases y roles son excesivos para 3 personas.
- **XP:** casi no genera documentación y pide cliente en sitio; el cliente de CoffeeCol solo está disponible semanalmente.
- **RAD:** sirve para prototipar rápido, pero no aprovecha que los requisitos ya están priorizados ni que el cliente participa poco.
- **Scrum:** el SRS ya trae prioridades y historias de usuario (Apéndice A), que se convierten directamente en Product Backlog.

## 1.3 Selección y justificación

**Metodología seleccionada: Scrum** (única, no híbrida).

1. **Equipo de 3 personas:** Scrum funciona con Product Owner, Scrum Master y equipo de desarrollo, sin estructura adicional.
2. **54 requisitos priorizados:** los 25 requisitos de prioridad alta van al primer sprint y las bajas (animaciones, intro, modal) al final; el SRS ya trae las historias HU-01 a HU-09.
3. **Cliente disponible semanalmente:** el sprint corto termina con una revisión (Sprint Review) en la sesión semanal, donde el cliente valida el incremento.
4. **Entregas incrementales:** cada sprint cierra algo usable (catálogo y carrito, luego checkout y pedidos, luego fidelización, luego panel y analítica).

Las actividades de análisis del plan ([02-plan-de-analisis.md](02-plan-de-analisis.md)) se organizan como un sprint corto de análisis con revisión al final.
