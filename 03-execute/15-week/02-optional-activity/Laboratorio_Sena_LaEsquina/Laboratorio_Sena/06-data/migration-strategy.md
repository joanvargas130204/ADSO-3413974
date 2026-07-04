# migration-strategy

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El SRS no describe un sistema previo con base de datos a migrar: la operación actual es 100 % manual (cuaderno + calculadora). No existe, por tanto, una migración de datos desde un sistema legado.

## Contenido

### Carga inicial (no es "migración" en sentido estricto)

El único insumo a digitalizar al iniciar el sistema es información que hoy vive en papel:

| Origen manual | Destino en el sistema | Responsable |
|----------------|------------------------|-------------|
| Cuaderno de precios (90 productos) | Catálogo (M1) | Administrador (RF02) |
| Cuaderno de fiado ($336.000 COP registrados, D02) | Módulo de Fiado (M6) | Administrador (RF05) |

### Estrategia de cambios futuros

- Cualquier cambio de esquema de datos posterior al MVP debe quedar registrado como ADR en [`05-architecture/decisions/`](../05-architecture/decisions/).
- El crecimiento del catálogo de 90 a 300 productos (RNF07) no debe requerir una migración estructural, solo una ampliación de capacidad.

## Referencias

- [01-context/overview.md](../01-context/overview.md)
- [06-data/data-dictionary.md](./data-dictionary.md)
- [13-operations/backup-and-recovery.md](../13-operations/backup-and-recovery.md)
