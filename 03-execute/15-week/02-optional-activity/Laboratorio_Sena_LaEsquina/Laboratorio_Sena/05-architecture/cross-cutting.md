# cross-cutting

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Aspectos transversales derivados de los problemas D01–D06 y de los requisitos no funcionales del SRS.

## Contenido

### Seguridad y control de acceso

- Roles diferenciados: Administrador (acceso total) vs. Empleado (ventas + inventario en lectura, sin reportes financieros) — RNF04.
- Solo el Administrador puede editar el catálogo (RF02) y confirmar el corte de caja (CU03).

### Auditoría y trazabilidad

El problema "Sin auditoría" (D01–D06) es uno de los seis problemas identificados en el SRS: hoy no hay trazabilidad por empleado o producto, lo que impide detectar hora pico, producto líder o faltante de caja. El sistema debe registrar:

- Cajero responsable de cada venta (RF01, RF06).
- Historial de ventas filtrable por fecha, empleado y producto (RF07).
- Diferencias de caja por jornada (RF04).

### Manejo de errores (excepciones de casos de uso)

| Excepción | Tratamiento esperado |
|-----------|------------------------|
| Producto no encontrado en venta | Notificar al Administrador; venta permanece abierta (CU01) |
| Stock cero | Bloquear el ítem e informar al operario (CU01) |
| Caída de conexión | Activar modo offline automáticamente (CU01, RNF02) |
| Nombre de producto duplicado | Ofrecer ver el producto existente o cambiar el nombre (CU02) |
| Precio inválido | Marcar el campo en rojo; no guardar hasta corregir (CU02) |
| Diferencia de caja > $5.000 | Alerta roja con revisión de historial antes de confirmar (CU03) |
| Corte de caja ya realizado | Permitir ver el reporte o ejecutar corte de corrección (CU03) |

### Backup y continuidad

Backup local automático al cierre de jornada, con sincronización en nube si hay conexión (RNF08).

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [13-operations/incident-management.md](../13-operations/incident-management.md)
