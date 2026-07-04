# authentication

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El SRS no define un mecanismo técnico de autenticación (OAuth, JWT, etc.); define dos roles de negocio con permisos diferenciados (RF03, RNF04) que cualquier estrategia de autenticación/autorización debe respetar.

## Contenido

### Roles definidos en el SRS

| Rol | Acceso | Origen |
|-----|--------|--------|
| Administrador | Acceso total: catálogo, corte de caja, fiado, reportes financieros | RF02, RF04, RNF04 |
| Empleado | Ventas + inventario en lectura. Sin acceso a reportes financieros. Solo ve su propio historial de ventas | RNF04, RF07 |

### Reglas de autorización derivadas

- Solo el Administrador puede crear, editar o eliminar productos del catálogo (RF02, CU02).
- Solo el Administrador puede confirmar el corte de caja (CU03).
- Un Empleado no puede ver reportes financieros completos ni el historial de ventas de otros empleados (RF07, RNF04).

### Pendiente de definir (requiere ADR)

- Mecanismo técnico de autenticación (usuario/contraseña local, PIN, biometría, etc.), compatible con el modo offline (RNF02) y el hardware de bajo costo (RNF05).

## Referencias

- [04-requirements/non-functional.md](../04-requirements/non-functional.md)
- [02-domain/entities-and-rules.md](../02-domain/entities-and-rules.md)
