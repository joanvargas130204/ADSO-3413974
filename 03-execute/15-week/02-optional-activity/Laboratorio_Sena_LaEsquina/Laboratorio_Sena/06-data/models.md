# models

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Modelo conceptual de datos derivado de las entidades de negocio descritas en [`02-domain/entities-and-rules.md`](../02-domain/entities-and-rules.md). El diagrama de clases/entidad-relación formal debe registrarse en [`08-uml/`](../08-uml/) cuando esté disponible.

## Contenido

### Entidades conceptuales y relaciones

- **Producto** (1) — (N) **Venta**: una venta contiene uno o varios productos; un producto puede aparecer en muchas ventas.
- **Venta** (N) — (1) **Usuario**: cada venta tiene un cajero responsable (Administrador o Empleado).
- **Venta** (1) — (1) **Tiquete**: cada venta confirmada genera un tiquete.
- **Venta** (N) — (1) **CorteDeCaja**: las ventas de un día se agrupan en un corte de caja.
- **Cliente** (1) — (N) **Fiado**: un cliente puede tener uno o varios créditos (fiados) activos o históricos.
- **Fiado** (1) — (N) **Abono**: un fiado recibe uno o varios abonos hasta llegar a saldo cero.
- **Proveedor** (1) — (N) **Producto**: (alcance Could Have, RF08) un proveedor puede surtir varios productos.

### Notas de modelado

- El catálogo está limitado a 90 productos en el MVP (RF02); el modelo debe permitir crecer a 300 sin rediseño (RNF07).
- El stock se modela como atributo mutable del Producto, actualizado por evento `VentaRegistrada` (ver [`02-domain/domain-events.md`](../02-domain/domain-events.md)).

## Referencias

- [02-domain/entities-and-rules.md](../02-domain/entities-and-rules.md)
- [06-data/data-dictionary.md](./data-dictionary.md)
- [08-uml/diagram-index.md](../08-uml/diagram-index.md)
