# non-functional

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Requisitos no funcionales (calidad, rendimiento, operación) y requisitos de negocio del SRS — Supermercado La Esquina v1.0, secciones 6 y 7.

## Contenido

### Requisitos no funcionales (RNF)

| ID | Nombre | Requisito | Prioridad |
|----|--------|-----------|-----------|
| RNF01 | Interfaz intuitiva | Cualquier operario completa una venta tras ≤2 h de inducción. UI en español colombiano. | 🔴 Must Have |
| RNF02 | Modo offline | Opera con plena funcionalidad sin internet. Sincroniza en <5 min al recuperar conexión. | 🔴 Must Have |
| RNF03 | Rendimiento ≤3 seg | Registro de venta con hasta 15 productos: respuesta en ≤3 seg en hardware mínimo. | 🟠 Should Have |
| RNF04 | Roles diferenciados | Administrador: acceso total. Empleado: solo ventas e inventario en lectura, sin ver reportes financieros. | 🟠 Should Have |
| RNF05 | Hardware de bajo costo | Funciona en Android 8.0 / 2 GB RAM o Windows 10 / 2 GB RAM. Sin hardware especializado. | 🔴 Must Have |
| RNF06 | Catálogo autogestión | Administrador agrega/edita/elimina productos en ≤3 clics, sin asistencia técnica. | 🟠 Should Have |
| RNF07 | Escalabilidad | Arquitectura que soporte 300 productos o un segundo punto de venta sin rediseño. | 🟡 Could Have |
| RNF08 | Backup automático diario | Copia local al cierre de jornada; sincronización en nube (Google Drive) si hay conexión. | 🟠 Should Have |

### Requisitos de negocio (RN)

| ID | Nombre | Requisito | Prioridad |
|----|--------|-----------|-----------|
| RN01 | Sin licencia mensual | Costo único o licencia anual asequible. Sin suscripciones recurrentes de alto costo. | 🔴 Must Have |
| RN02 | Autonomía operativa | Carlos Ruiz puede reiniciar, actualizar precios y cerrar caja sin asistencia técnica externa. | 🔴 Must Have |

## Referencias

- [04-requirements/functional.md](./functional.md)
- [04-requirements/traceability-matrix.md](./traceability-matrix.md)
- [05-architecture/cross-cutting.md](../05-architecture/cross-cutting.md)
