# dependencies

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Dependencias externas identificadas en el SRS, principalmente relacionadas con hardware, conectividad y almacenamiento en nube.

## Contenido

| Dependencia | Tipo | Detalle | Origen |
|--------------|------|---------|--------|
| Hardware del negocio | Externa | Android 8.0 / 2 GB RAM o Windows 10 / 2 GB RAM, sin hardware especializado | RNF05 |
| Conectividad a internet | Externa, intermitente | El sistema no depende de ella para operar (modo offline), pero la necesita para sincronizar y respaldar en nube | RNF02, RNF08 |
| Google Drive (o servicio de nube equivalente) | Externa | Sincronización de backup cuando hay conexión | RNF08 |
| Disponibilidad de Carlos Ruiz | Interna | Único decisor y único Administrador del sistema; cualquier definición de producto depende de su validación | Sección 1, RN02 |
| Impresora o canal PDF/WhatsApp | Externa (opcional) | Necesaria para emitir el tiquete impreso o digital | RF06 |

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [05-architecture/deployment.md](../05-architecture/deployment.md)
