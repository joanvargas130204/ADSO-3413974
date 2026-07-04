# admin-manual

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Manual para Carlos Ruiz (Administrador), basado en CU02 — Gestionar Catálogo y CU03 — Corte de Caja Diario. Meta: operar el sistema con autonomía total, sin soporte técnico externo (RN02).

## Contenido

### Gestionar el catálogo (≤3 clics, RNF06)

1. Entra al módulo Catálogo y elige Nuevo / Editar / Eliminar.
2. Completa el formulario: nombre, precio, categoría, stock y stock mínimo.
3. Guarda. El sistema valida los datos y actualiza el POS de todos los empleados en tiempo real.

**Mensajes que puedes ver:**

| Mensaje | Qué significa |
|---------|----------------|
| Nombre duplicado | Ya existe un producto con ese nombre; puedes verlo o cambiar el nombre nuevo |
| Precio inválido (campo en rojo) | Corrige el precio antes de poder guardar |
| Botón "Nuevo" deshabilitado | Ya tienes 90 productos registrados (límite del MVP) |

### Cerrar la caja del día (CU03)

1. Entra al módulo Corte de Caja al finalizar la jornada.
2. Revisa el resumen: nº de transacciones, total efectivo, total digital y desglose por empleado.
3. Cuenta el efectivo físico e ingrésalo en el sistema.
4. El sistema calcula la diferencia y la marca en 🟢 (sin diferencia), 🟡 (diferencia menor) o 🔴 (diferencia mayor a $5.000 COP).
5. Si hay alerta roja, revisa el historial de ventas antes de confirmar.
6. Confirma el cierre: el sistema activa el backup automático y genera el reporte en PDF.

### Gestionar el fiado (RF05)

Registra el monto, fecha y cliente de cada crédito otorgado. Registra los abonos a medida que el cliente paga. El sistema te alertará si un fiado lleva más de 30 días sin abono.

## Referencias

- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [13-operations/backup-and-recovery.md](../13-operations/backup-and-recovery.md)
