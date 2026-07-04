# incident-management

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El SRS no define un proceso formal de gestión de incidentes técnicos, pero sí define un escenario operativo equivalente: la diferencia de caja, tratada como excepción crítica en CU03.

## Contenido

### Escenario: Diferencia de caja (CU03)

| Aspecto | Detalle |
|---------|---------|
| Disparador | Diferencia entre el efectivo físico contado y el total calculado por el sistema |
| Umbral | Mayor a $5.000 COP |
| Respuesta del sistema | Alerta roja con opción de revisar el historial antes de confirmar el cierre |
| Responsable de resolución | Administrador (Carlos Ruiz) |
| Casos especiales | Si el corte ya fue realizado, se permite ver el reporte o ejecutar un corte de corrección |

### Pendiente de definir

- Proceso de gestión de incidentes técnicos (caídas del sistema, errores de sincronización offline) no está definido en el SRS y debe completarse en una fase posterior, coordinado con [`05-architecture/cross-cutting.md`](../05-architecture/cross-cutting.md).

## Referencias

- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [05-architecture/cross-cutting.md](../05-architecture/cross-cutting.md)
