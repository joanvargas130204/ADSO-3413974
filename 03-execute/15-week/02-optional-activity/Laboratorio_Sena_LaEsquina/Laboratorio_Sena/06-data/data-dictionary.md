# data-dictionary

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Diccionario de datos a nivel de campo, derivado de los formularios y reglas descritos en el SRS (RF02, RF04, RF05, CU01–CU03).

## Contenido

### Producto

| Campo | Descripción | Regla |
|-------|-------------|-------|
| nombre | Nombre del producto | Único en el catálogo (RN-D03) |
| precio | Precio de venta | Debe ser válido; si es inválido, no se guarda (CU02) |
| categoría | Categoría del producto | — |
| stock | Cantidad disponible | Se descuenta automáticamente al vender (RF03) |
| stock mínimo | Umbral de alerta | Dispara alerta al Administrador al alcanzarse (RF03) |

### Venta

| Campo | Descripción | Regla |
|-------|-------------|-------|
| fecha | Fecha y hora de la venta | — |
| productos | Lista de productos y cantidades | Hasta 15 productos por venta sin exceder 3 seg de respuesta (RNF03) |
| subtotal / total | Cálculo automático | Calculado en tiempo real (RF01) |
| método de pago | Efectivo o digital | Se registra, no se procesa la pasarela (sección 4, excluido del MVP) |
| cajero | Usuario que registró la venta | Para trazabilidad (RF07) |

### CorteDeCaja

| Campo | Descripción | Regla |
|-------|-------------|-------|
| total efectivo / total digital | Totales por método de pago | — |
| nº transacciones | Conteo de ventas del día | — |
| efectivo físico contado | Ingresado por el Administrador | — |
| diferencia | total sistema − efectivo físico | >$5.000 dispara alerta roja (CU03) |

### Fiado

| Campo | Descripción | Regla |
|-------|-------------|-------|
| cliente | Cliente asociado | — |
| monto | Monto del crédito otorgado | — |
| fecha | Fecha de otorgamiento | Base para el cálculo de vencimiento |
| abonos | Pagos parciales registrados | — |
| saldo | Monto pendiente por pagar | Alerta si supera 30 días sin abono (RF05) |

## Referencias

- [06-data/models.md](./models.md)
- [02-domain/entities-and-rules.md](../02-domain/entities-and-rules.md)
- [04-requirements/functional.md](../04-requirements/functional.md)
