# technical-backlog

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Pendientes técnicos derivados de los requisitos "Could Have" y de las exclusiones explícitas del MVP en el SRS (sección 4).

## Contenido

### Diferido del MVP (Could Have — sección 8 del SRS)

| ID | Nombre | Motivo del diferimiento |
|----|--------|---------------------------|
| RF07 | Historial de Ventas | No bloquea el reemplazo de la calculadora; depende de tener datos acumulados |
| RF08 | Gestión de Proveedores | Requiere acuerdo previo sobre el modelo de datos de proveedor |
| RF09 | Pedidos Sugeridos | Depende de RF03 (alertas de stock mínimo) estar estable primero |
| RF10 | Reporte Productos más Vendidos | Requiere historial de ventas (RF07) como base |
| RNF07 | Escalabilidad a 300 productos / 2ª sede | Decisión de arquitectura pendiente de ADR |

### Explícitamente fuera de alcance (no es deuda técnica, es decisión de producto)

- Integración automática con pasarelas de pago (Nequi, Daviplata, datáfono).
- Facturación electrónica DIAN.
- Gestión contable / declaración de impuestos.
- App o portal para clientes finales.
- Integración con sistemas de proveedores.
- Múltiples sucursales.

## Referencias

- [01-context/scope.md](../01-context/scope.md)
- [03-product/roadmap.md](../03-product/roadmap.md)
