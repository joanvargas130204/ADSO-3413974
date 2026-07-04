# traceability-matrix

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Matriz de trazabilidad entre módulos, requisitos, historias de usuario y problemas identificados en el SRS (secciones 2, 4, 5, 6, 8 y 9).

## Contenido

| Requisito | Módulo SRS | Historia de usuario | Problema que mitiga | Prioridad |
|-----------|------------|----------------------|-----------------------|-----------|
| RF01 | M2 — Ventas / POS | HU01 (CU01) | Cobro lento (120 seg con calculadora) | 🔴 Must Have |
| RF02 | M1 — Inventario / Catálogo | HU02 (CU02) | Precios incorrectos (8/90 desactualizados) | 🔴 Must Have |
| RF03 | M1 — Inventario / Catálogo | HU01 (CU01) | Sin control de inventario | 🟠 Should Have |
| RF04 | M4 — Corte de Caja | HU03 (CU03) | Sin auditoría / diferencias de caja | 🟠 Should Have |
| RF05 | M6 — Gestión de Fiado | — | Cartera sin trazabilidad ($336.000 COP) | 🟠 Should Have |
| RF06 | M5 — Tiquetes | HU01 (CU01) | Sin auditoría por transacción | 🟠 Should Have |
| RF07 | — | — | Sin auditoría por empleado/producto | 🟡 Could Have |
| RF08 | — | — | Sin control de inventario (pedidos por memoria) | 🟡 Could Have |
| RF09 | — | — | Sin control de inventario (quiebres de stock) | 🟡 Could Have |
| RF10 | — | — | Sin auditoría (hora pico, producto líder) | 🟡 Could Have |
| RNF01 | Transversal | HU01, HU02 | Resistencia a la tecnología, curva de aprendizaje | 🔴 Must Have |
| RNF02 | Transversal | HU01 | Conexión intermitente en el punto de venta | 🔴 Must Have |
| RNF03 | M2 — Ventas / POS | HU01 | Meta de rendimiento 382→145 seg | 🟠 Should Have |
| RNF04 | M3 — Usuarios y Roles | HU01, HU03 | Sin auditoría / control de acceso | 🟠 Should Have |
| RNF05 | Transversal | — | Hardware limitado del negocio | 🔴 Must Have |
| RNF06 | M1 — Inventario / Catálogo | HU02 | Precios incorrectos / autonomía | 🟠 Should Have |
| RNF07 | Transversal | — | Crecimiento futuro (90→300 productos) | 🟡 Could Have |
| RNF08 | M4 — Corte de Caja | HU03 | Pérdida de información ante fallas | 🟠 Should Have |
| RN01 | Transversal | — | Restricción presupuestal del negocio | 🔴 Must Have |
| RN02 | M1, M3, M4 | HU02, HU03 | Resistencia a la tecnología (Carlos Ruiz) | 🔴 Must Have |

## Referencias

- [04-requirements/functional.md](./functional.md)
- [04-requirements/non-functional.md](./non-functional.md)
- [04-requirements/user-stories.md](./user-stories.md)
- [01-context/overview.md](../01-context/overview.md)
