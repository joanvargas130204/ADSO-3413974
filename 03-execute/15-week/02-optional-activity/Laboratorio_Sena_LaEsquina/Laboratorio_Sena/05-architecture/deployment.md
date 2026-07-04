# deployment

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El SRS no define una topología de despliegue formal; establece los entornos de hardware mínimos y la necesidad de operación offline. Este documento consolida esas restricciones a la espera de una ADR de arquitectura de despliegue.

## Contenido

### Entornos objetivo (RNF05)

| Plataforma | Requisito mínimo |
|------------|-------------------|
| Android | 8.0, 2 GB RAM |
| Windows | 10, 2 GB RAM |

Sin hardware especializado (datáfono propio, impresora térmica obligatoria, etc.).

### Conectividad

- El sistema debe operar con **plena funcionalidad sin internet** (RNF02).
- Al recuperar conexión, debe sincronizar en **menos de 5 minutos** (RNF02).
- El backup local se realiza al cierre de jornada; la sincronización en nube (Google Drive) ocurre cuando hay conexión (RNF08).

### Pendiente de definir (requiere ADR)

- Topología concreta (cliente único / cliente-servidor local / nube híbrida).
- Mecanismo exacto de sincronización offline-online.
- Proveedor y forma de respaldo en la nube más allá de "Google Drive" (mencionado en el SRS como referencia).

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [13-operations/backup-and-recovery.md](../13-operations/backup-and-recovery.md)
- [05-architecture/decisions/README.md](./decisions/README.md)
