# risks

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Riesgos identificados a partir del contexto de negocio y los problemas documentados en el SRS (sección 1 y 2).

## Contenido

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|---------------|---------|------------|
| Resistencia moderada de Carlos Ruiz (único decisor) a adoptar el sistema | Media | Alto | Curva de aprendizaje ≤2 h (RNF01), autonomía operativa sin soporte externo (RN02) |
| Más errores de Julián Torres en hora pico (12 p.m.–2 p.m.) | Alta | Medio | UI intuitiva (RNF01), cálculo automático de total y cambio (RF01) |
| Pérdida de datos por falla de hardware de bajo costo | Media | Alto | Backup automático diario + sincronización en nube (RNF08) |
| Conexión a internet intermitente en el punto de venta | Alta | Alto | Modo offline con sincronización <5 min (RNF02) |
| Catálogo llega al límite de 90 productos antes de tiempo | Media | Medio | Diseño preparado para escalar a 300 productos (RNF07) |
| Pérdidas no cuantificadas en fiado por falta de registro | Alta (ya materializado: $336.000 COP, D02) | Alto | Módulo de Fiado con abonos y alertas de vencimiento (RF05) |

## Referencias

- [01-context/overview.md](../01-context/overview.md)
- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
