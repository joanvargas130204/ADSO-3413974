# design-system

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Principios de diseño obligatorios según los requisitos no funcionales del SRS.

## Contenido

| Principio | Requisito | Implicación de diseño |
|-----------|-----------|--------------------------|
| Idioma | RNF01 | Toda la UI en español colombiano |
| Curva de aprendizaje | RNF01 | Cualquier operario completa una venta tras ≤2 h de inducción; preferir patrones reconocibles sobre originalidad visual |
| Eficiencia de catálogo | RNF06 | Administrador agrega/edita/elimina un producto en ≤3 clics |
| Indicadores de estado de caja | CU03 | Usar semáforo 🟢/🟡/🔴 para la diferencia de caja |
| Indicadores de stock | RF03 | Alertas visibles de stock mínimo, diferenciadas para Administrador |
| Tolerancia a errores | CU02 | Campos inválidos (ej. precio) se marcan en rojo antes de poder guardar |
| Indicador de modo offline | RNF02 | El operario debe poder identificar si el sistema está operando sin conexión |

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [12-ux-ui/navigation-map.md](./navigation-map.md)
- [12-ux-ui/wireframes.md](./wireframes.md)
