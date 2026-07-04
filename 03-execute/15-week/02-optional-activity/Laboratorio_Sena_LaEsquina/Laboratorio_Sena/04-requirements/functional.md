# functional

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Requisitos funcionales del SRS — Supermercado La Esquina v1.0 (abril 2026), sección 5.

## Contenido

| ID | Nombre | Descripción | Prioridad |
|----|--------|--------------|-----------|
| RF01 | POS — Registro de Venta | Seleccionar productos del catálogo; el sistema calcula total y registra método de pago (efectivo/digital). Elimina suma manual (120 seg, 44 % del tiempo). | 🔴 Must Have |
| RF02 | Catálogo de Productos | CRUD de hasta 90 productos (nombre, precio, categoría, stock, mínimo). Búsqueda por nombre. Solo el Administrador puede editar. | 🔴 Must Have |
| RF03 | Control de Inventario + Alertas | Descuento automático de stock al vender. Alerta visible al Administrador cuando se alcanza el mínimo. | 🟠 Should Have |
| RF04 | Corte de Caja Diario | Resumen al cierre: total efectivo, total digital, nº de transacciones y diferencia vs. caja física. | 🟠 Should Have |
| RF05 | Gestión de Fiado | Registrar créditos a clientes: monto, fecha, abonos y saldo. Alerta si supera 30 días sin abono. | 🟠 Should Have |
| RF06 | Tiquete de Venta | Al finalizar cada venta: tiquete con fecha, productos, total y cajero. Imprimible o PDF/WhatsApp. | 🟠 Should Have |
| RF07 | Historial de Ventas | Filtros por fecha, empleado y producto. Empleados solo ven sus propias ventas. | 🟡 Could Have |
| RF08 | Gestión de Proveedores | Registro de proveedores con contacto, productos y últimos precios de compra. | 🟡 Could Have |
| RF09 | Pedidos Sugeridos | Si 3+ productos están en mínimo, sugiere pedido al proveedor con cantidades. | 🟡 Could Have |
| RF10 | Reporte Productos más Vendidos | Top 10 semanal/mensual por unidad y valor; hora pico de transacciones. | 🟡 Could Have |

## Referencias

- [04-requirements/non-functional.md](./non-functional.md)
- [04-requirements/user-stories.md](./user-stories.md)
- [04-requirements/traceability-matrix.md](./traceability-matrix.md)
- [01-context/scope.md](../01-context/scope.md)
