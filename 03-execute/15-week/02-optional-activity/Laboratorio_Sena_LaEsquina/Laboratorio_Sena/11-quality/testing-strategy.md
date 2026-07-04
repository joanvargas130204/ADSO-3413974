# testing-strategy

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Metas de calidad medibles definidas en el SRS, que deben verificarse mediante pruebas.

## Contenido

### Pruebas de rendimiento

| Métrica | Línea base | Meta | Origen |
|---------|------------|------|--------|
| Tiempo por transacción | 382 seg | 145 seg (−62 %) | Meta de rendimiento, sección 2 |
| Tiempo de cálculo de suma manual eliminado | 120 seg (44 % de la transacción) | 0 seg (automatizado) | RF01 |
| Respuesta al registrar venta (≤15 productos) | — | ≤3 seg en hardware mínimo | RNF03 |
| Sincronización al recuperar conexión | — | <5 min | RNF02 |

### Pruebas funcionales por caso de uso

| Caso de uso | Casos de prueba mínimos |
|-------------|---------------------------|
| CU01 — Registrar Venta | Venta exitosa, producto no encontrado, stock cero, caída de conexión |
| CU02 — Gestionar Catálogo | Alta/edición/eliminación exitosa, nombre duplicado, precio inválido, límite de 90 productos |
| CU03 — Corte de Caja | Cierre sin diferencia, diferencia >$5.000, corte ya realizado |

### Pruebas de usabilidad

- Verificar que un operario sin experiencia técnica complete una venta tras ≤2 horas de inducción (RNF01).
- Verificar que el Administrador agregue/edite/elimine un producto en ≤3 clics (RNF06).

### Pruebas de compatibilidad

- Ejecutar la suite en Android 8.0 / 2 GB RAM y Windows 10 / 2 GB RAM (RNF05).

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
