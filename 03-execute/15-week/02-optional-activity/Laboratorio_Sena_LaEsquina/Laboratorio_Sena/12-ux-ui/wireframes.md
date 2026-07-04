# wireframes

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Referencias textuales de las pantallas clave, a la espera de wireframes visuales en `assets/images/`. Derivadas de los flujos normales de CU01–CU03.

## Contenido

### Pantalla POS (CU01)

- Buscador de productos por nombre.
- Lista de productos seleccionados con subtotal en tiempo real.
- Selector de método de pago (efectivo/digital).
- Si es efectivo: campo de monto recibido + cálculo de cambio.
- Botón de confirmar venta.

### Pantalla Catálogo (CU02)

- Lista de productos con nombre, precio, categoría, stock.
- Botones Nuevo / Editar / Eliminar (deshabilitado "Nuevo" al llegar a 90 productos).
- Formulario con validación de precio (campo en rojo si inválido).

### Pantalla Corte de Caja (CU03)

- Resumen: nº de transacciones, total efectivo, total digital, desglose por empleado.
- Campo de efectivo físico contado.
- Indicador de diferencia (🟢/🟡/🔴), con alerta roja si supera $5.000 COP.
- Botón de confirmar cierre.

## Referencias

- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [12-ux-ui/navigation-map.md](./navigation-map.md)
- [assets/images/](../assets/images/)
