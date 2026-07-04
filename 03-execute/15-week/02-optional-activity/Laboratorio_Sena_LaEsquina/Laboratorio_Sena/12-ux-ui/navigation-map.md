# navigation-map

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Mapa de navegación derivado de los 6 módulos del MVP y de los roles definidos en el SRS (RF02–RF06, RNF04).

## Contenido

| Pantalla | Módulo | Accesible por |
|----------|--------|----------------|
| POS (Nueva Venta) | M2 — Ventas / POS | Administrador, Empleado |
| Catálogo de Productos | M1 — Inventario / Catálogo | Administrador (edición) · Empleado (lectura) |
| Corte de Caja | M4 — Corte de Caja | Administrador |
| Historial de Ventas | RF07 | Administrador (todo) · Empleado (solo sus ventas) |
| Gestión de Fiado | M6 — Gestión de Fiado | Administrador |
| Tiquete (vista de confirmación) | M5 — Tiquetes | Administrador, Empleado |

### Flujo de navegación principal (CU01 — Registrar Venta)

POS → búsqueda de producto → selección de método de pago → confirmación → Tiquete → vuelve a POS.

### Restricción de navegación por rol (RNF04)

El Empleado no debe poder navegar a reportes financieros completos ni al módulo de Corte de Caja.

## Referencias

- [01-context/scope.md](../01-context/scope.md)
- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [12-ux-ui/wireframes.md](./wireframes.md)
