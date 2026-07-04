# entities-and-rules

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Entidades de negocio y reglas/invariantes derivadas de los requerimientos funcionales (RF01–RF10) y casos de uso (CU01–CU03) del SRS. Para el esquema de persistencia de estas mismas entidades, ver [`06-data/models.md`](../06-data/models.md) y [`06-data/data-dictionary.md`](../06-data/data-dictionary.md).

## Contenido

### Entidades principales

| Entidad | Atributos de negocio | Origen SRS |
|---------|----------------------|------------|
| Producto | nombre, precio, categoría, stock, stock mínimo | RF02, M1 |
| Venta | fecha, productos, cantidades, subtotal, total, método de pago, cajero | RF01, M2 |
| Usuario | nombre, rol (Administrador/Empleado), turno | RF03, M3, RNF04 |
| CorteDeCaja | fecha, total efectivo, total digital, nº transacciones, efectivo físico contado, diferencia, estado | RF04, M4 |
| Tiquete | fecha, productos, total, cajero, canal (impreso/PDF/WhatsApp) | RF06, M5 |
| Cliente | nombre, identificador | RF05, M6 |
| Fiado (Crédito) | cliente, monto, fecha, abonos, saldo pendiente | RF05, M6 |
| Proveedor | contacto, productos, últimos precios de compra | RF08 (Could Have) |

### Reglas de negocio / invariantes

| Regla | Descripción | Origen |
|-------|-------------|--------|
| RN-D01 | Solo el Administrador puede crear, editar o eliminar productos del catálogo | RF02 |
| RN-D02 | El catálogo no puede superar 90 productos; al llegar al límite, el botón "Nuevo" se deshabilita con mensaje explicativo | CU02 |
| RN-D03 | No pueden existir dos productos con el mismo nombre; el sistema ofrece ver el existente o cambiar el nombre | CU02 |
| RN-D04 | Una venta con un producto en stock cero queda bloqueada para ese ítem hasta reabastecer | CU01 |
| RN-D05 | Al confirmar una venta, el sistema descuenta automáticamente el stock vendido | RF03, CU01 |
| RN-D06 | Cuando el stock de un producto alcanza su mínimo, se genera una alerta visible solo para el Administrador | RF03 |
| RN-D07 | El sistema alerta cuando un Fiado supera 30 días sin abono | RF05 |
| RN-D08 | Una diferencia de caja superior a $5.000 COP genera alerta roja y exige revisión del historial antes de confirmar el cierre | CU03 |
| RN-D09 | Un Empleado solo puede ver su propio historial de ventas, nunca reportes financieros completos | RF07, RNF04 |
| RN-D10 | Si 3 o más productos están en su mínimo, el sistema sugiere un pedido al proveedor con cantidades (Could Have) | RF09 |

## Referencias

- [04-requirements/functional.md](../04-requirements/functional.md)
- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [06-data/data-dictionary.md](../06-data/data-dictionary.md)
