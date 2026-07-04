# backup-and-recovery

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Requisito de respaldo definido en el SRS (RNF08) y disparado por el flujo de Corte de Caja (CU03).

## Contenido

| Aspecto | Requisito |
|---------|-----------|
| Frecuencia | Backup local automático al cierre de cada jornada |
| Disparador | Confirmación del corte de caja (CU03): "el sistema registra, activa backup y genera reporte en PDF" |
| Sincronización en nube | A Google Drive, condicionada a disponibilidad de conexión a internet (RNF08, RNF02) |
| Autonomía | El Administrador (Carlos Ruiz) debe poder ejecutar y verificar el backup sin asistencia técnica externa (RN02) |

### Pendiente de definir (requiere ADR)

- RPO/RTO concretos.
- Procedimiento de restauración ante pérdida de datos o falla de hardware.

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [05-architecture/deployment.md](../05-architecture/deployment.md)
