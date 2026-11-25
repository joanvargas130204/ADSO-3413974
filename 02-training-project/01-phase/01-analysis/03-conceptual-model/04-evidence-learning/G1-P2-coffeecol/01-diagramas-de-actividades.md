# 1. Diagramas de actividades (casos de uso críticos)

Casos críticos elegidos: **CU-06 Realizar checkout y generar pedido** (núcleo del negocio), **CU-03 Iniciar sesión con Firebase** (puerta de entrada de los clientes) y **CU-11 Gestionar productos** (operación del administrador). Los dos primeros tienen diagrama de actividades; los tres tienen plantilla extendida y pantalla.

| Diagrama | Fuente editable | Imagen | Plantilla del mismo caso |
|---|---|---|---|
| Realizar checkout | [actividad-realizar-checkout.mmd](diagramas/actividad-realizar-checkout.mmd) | [png](diagramas/actividad-realizar-checkout.png) · [svg](diagramas/actividad-realizar-checkout.svg) | [CU-06](plantillas/CU-06-realizar-checkout.md) |
| Iniciar sesión | [actividad-iniciar-sesion.mmd](diagramas/actividad-iniciar-sesion.mmd) | [png](diagramas/actividad-iniciar-sesion.png) · [svg](diagramas/actividad-iniciar-sesion.svg) | [CU-03](plantillas/CU-03-iniciar-sesion.md) |

Notación: inicio (círculo negro), fin (círculo con borde grueso), calles por actor (cuadros «Calle»), decisiones en rombo con guardas entre corchetes en **todas** las salidas. Las ramas alternas (`A`) y de excepción (`E`) llevan la misma etiqueta que en la plantilla del caso.

| Diagrama | Decisiones y sus salidas | Ramas en la plantilla |
|---|---|---|
| Realizar checkout | ¿direcciones guardadas? [con / sin]; ¿datos válidos? [válidos / inválidos]; ¿aceptó la política? [aceptó / no aceptó]; ¿hay existencias? [hay / agotado]; ¿se pudo registrar? [exitoso / fallido] | A1, E1, E2, E3, E4 |
| Iniciar sesión | ¿el servicio externo responde? [responde / no responde]; ¿método elegido? [Google / enlace mágico]; ¿el usuario aprueba? [aprueba / cancela] | A1, E1, E2 |

**Concurrencia:** en ambos casos las actividades son secuenciales (cada paso depende del resultado del anterior), por eso no hay bifurcación ni unión.

**Qué cambié respecto al SRS:** las fichas del Apéndice B (CU-03 y CU-06) mezclan el comportamiento con detalles de implementación (rutas de archivos, peticiones POST, transacciones, cookies). En los diagramas y plantillas los reescribí como intención del actor y respuesta del sistema, y agregué las excepciones que el SRS solo insinuaba (política de datos no aceptada, producto agotado).
