# observability

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El problema "Sin auditoría" (D01–D06) descrito en el SRS es la motivación directa de los requisitos de observabilidad de negocio: hoy es imposible detectar hora pico, producto líder o faltante de caja.

## Contenido

### Métricas e indicadores requeridos por el SRS

| Indicador | Origen | Uso |
|-----------|--------|-----|
| Nº de transacciones por jornada | RF04 | Corte de caja |
| Total efectivo / total digital | RF04 | Corte de caja |
| Diferencia de caja | CU03 | Alertas operativas |
| Historial de ventas por fecha, empleado y producto | RF07 | Auditoría |
| Top 10 productos más vendidos (semanal/mensual) | RF10 (Could Have) | Decisiones de inventario |
| Hora pico de transacciones | RF10 (Could Have) | Planeación de turnos |
| Productos en stock mínimo | RF03 | Alertas de reabastecimiento |

### Pendiente de definir

- Métricas técnicas (logs, trazas, dashboards de infraestructura) no están definidas en el SRS; corresponde a una fase de diseño técnico posterior.

## Referencias

- [01-context/overview.md](../01-context/overview.md)
- [04-requirements/functional.md](../04-requirements/functional.md)
