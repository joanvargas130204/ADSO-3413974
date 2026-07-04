# roadmap

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El roadmap del MVP se deriva directamente de la priorización MoSCoW del SRS (sección 8) y de la meta de rendimiento (382 seg → 145 seg por transacción).

## Contenido

### Fase 1 — Must Have (núcleo del MVP)

Habilita el reemplazo de la calculadora y el cuaderno.

| ID | Nombre |
|----|--------|
| RF01 | POS — Registro de Venta |
| RF02 | Catálogo de Productos |
| RNF01 | Interfaz intuitiva |
| RNF02 | Modo offline |
| RNF05 | Hardware de bajo costo |
| RN01 | Sin licencia mensual |
| RN02 | Autonomía operativa |

### Fase 2 — Should Have (control operativo)

Agrega control de inventario, caja, fiado y comprobantes.

| ID | Nombre |
|----|--------|
| RF03 | Control de Inventario + Alertas |
| RF04 | Corte de Caja Diario |
| RF05 | Gestión de Fiado |
| RF06 | Tiquete de Venta |
| RNF03 | Rendimiento ≤3 seg |
| RNF04 | Roles diferenciados |
| RNF06 | Catálogo autogestión |
| RNF08 | Backup automático diario |

### Fase 3 — Could Have (analítica y crecimiento)

Mejora la toma de decisiones y prepara la escalabilidad.

| ID | Nombre |
|----|--------|
| RF07 | Historial de Ventas |
| RF08 | Gestión de Proveedores |
| RF09 | Pedidos Sugeridos |
| RF10 | Reporte Productos más Vendidos |
| RNF07 | Escalabilidad |

### Meta de rendimiento del roadmap

⚡ Reducir el tiempo por transacción de 382 seg a 145 seg (−62 %) al cierre de la Fase 1.

## Referencias

- [04-requirements/traceability-matrix.md](../04-requirements/traceability-matrix.md)
- [03-product/product-backlog.md](./product-backlog.md)
