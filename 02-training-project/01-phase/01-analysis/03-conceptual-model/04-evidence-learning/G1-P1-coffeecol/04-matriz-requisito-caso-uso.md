# 4. Matriz requisito → caso de uso

## 4.1 Requisitos funcionales

| Requisito | Resumen | Caso(s) de uso |
|---|---|---|
| RF-001 | Pantalla de bienvenida animada con paso automático a inicio tras 3 s | CU-15 |
| RF-002 | Mapa interactivo del Huila (37 municipios) con altitud y perfil cafetero | CU-01 |
| RF-003 | Secciones informativas: historia, perfil sensorial y tueste artesanal | CU-15 |
| RF-004 | Carrusel de cooperativas y caficultores aliados | CU-15 |
| RF-005 | Ventana modal promocional una vez por sesión de navegación | CU-15 |
| RF-006 | Listar el inventario en 5 categorías de producto | CU-02 |
| RF-007 | Filtrar el catálogo por categoría sin recargar la página | CU-02 |
| RF-008 | Tarjeta de producto con foto, nombre, notas, categoría, valoración y precios | CU-02, CU-16 |
| RF-009 | Animaciones de entrada al desplazarse por la página | CU-02 |
| RF-010 | Indicadores de carga mientras llegan los datos del catálogo | CU-02 |
| RF-011 | Agregar productos al carrito desde la tarjeta o el detalle | CU-05 |
| RF-012 | Aumentar, disminuir o quitar ítems desde el panel lateral del carrito | CU-05 |
| RF-013 | Conservar el carrito entre sesiones de navegación | CU-05 |
| RF-014 | Calcular subtotal, despacho ($12.000; gratis sobre $150.000) y total | CU-05 |
| RF-015 | Botón flotante con contador de unidades del carrito | CU-05 |
| RF-016 | Retirar del carrito los productos que ya no existen en el catálogo | CU-05 |
| RF-017 | Formulario de checkout con nombres, apellidos, correo, teléfono, municipio y dirección | CU-06 |
| RF-018 | Validar correo, teléfono de 10 dígitos y campos vacíos antes de enviar | CU-19 |
| RF-019 | Resumen desglosado del pedido antes de la confirmación | CU-06 |
| RF-020 | Registrar el pedido con un código único de orden | CU-06 |
| RF-021 | Confirmación con número de pedido y vaciado del carrito | CU-06 |
| RF-022 | Ciclo de estados del pedido: pendiente, procesando, enviado, entregado o cancelado | CU-12 |
| RF-023 | Acceso de clientes con cuenta de Google | CU-03 |
| RF-024 | Acceso de clientes con enlace mágico enviado al correo | CU-03 |
| RF-025 | Acceso del administrador con usuario y clave cifrada, con sesión de 60 min | CU-10 |
| RF-026 | Bloqueo temporal del administrador tras 5 intentos fallidos en 15 min | CU-24, CU-10 |
| RF-027 | Sincronizar al usuario en la base tras acceder con Firebase | CU-17 |
| RF-028 | Verificar el rol y llevar al usuario a su módulo | CU-03, CU-10 |
| RF-029 | Cierre seguro de sesión | CU-18 |
| RF-030 | Panel de perfil con avatar, nombre, correo, fecha de vinculación y nivel | CU-07 |
| RF-031 | Estadísticas del cliente: puntos, pedidos, favoritos y direcciones | CU-07 |
| RF-032 | Historial cronológico de compras con el estado de cada paquete | CU-21 |
| RF-033 | Añadir, editar y eliminar direcciones guardadas | CU-07 |
| RF-034 | Registrar la fecha de cumpleaños una sola vez | CU-07 |
| RF-035 | Marcar o desmarcar productos como favoritos | CU-08 |
| RF-036 | Guardar favoritos exigiendo sesión activa | CU-08 |
| RF-037 | Ver los favoritos guardados en el perfil | CU-08 |
| RF-038 | Acreditar 1 punto por cada $1.000 y asignar nivel Espresso, Plata u Oro | CU-09, CU-20 |
| RF-039 | Bono anual de 100 puntos en el mes de cumpleaños | CU-23 |
| RF-040 | Bitácora auditable de abonos y deducciones de puntos | CU-09 |
| RF-041 | Canje de recompensas: 10 % de descuento, café gratis y kit barista | CU-22 |
| RF-042 | Barra de progreso hacia el siguiente nivel | CU-09 |
| RF-043 | Formulario de contacto: nombre, finca, teléfono, correo, municipio y mensaje | CU-04 |
| RF-044 | Guardar los mensajes de contacto para seguimiento comercial | CU-04 |
| RF-045 | Alta de productos con nombre, descripción, precio, categoría, stock e imagen | CU-11, CU-25, CU-26 |
| RF-046 | Eliminar productos del catálogo activo | CU-11 |
| RF-047 | Buscar, ordenar y filtrar el inventario administrativo | CU-11 |
| RF-048 | Listar órdenes con comprador, total, fecha y detalle de productos | CU-12 |
| RF-049 | Actualizar el estado de los pedidos con sesión de administrador válida | CU-12 |
| RF-050 | Consultar clientes con historial de compras y saldo de puntos | CU-13 |
| RF-051 | KPIs: ventas del día y del mes, pedidos de hoy, ticket promedio y café más vendido | CU-14 |
| RF-052 | Cuatro gráficos: ventas diarias, top 5, por categoría y tendencia mensual | CU-14 |
| RF-053 | Filtrar las métricas por rango: hoy, 7 días, 30 días, mes, año o personalizado | CU-14 |
| RF-054 | Exportar reportes a CSV e imprimir en PDF | CU-27 |

**Cobertura: 54 de 54 requisitos funcionales (100 %).** No hay requisitos funcionales sin caso de uso ni casos de uso sin requisito.

## 4.2 Requisitos no funcionales (no generan casos de uso propios)

Se distinguen de los funcionales porque describen cómo debe comportarse el sistema, no una función que el actor invoca. Los que afectan el comportamiento de un caso aparecen como regla de negocio en su plantilla (G1-P2) o como decisión de diseño (G2):

| Requisito no funcional | Dónde se refleja |
|---|---|
| RNF-001 a RNF-004 (rendimiento) | Diseño y pruebas (G2); no son casos de uso |
| RNF-005 token administrativo | Regla de CU-10 y de todos los casos del administrador |
| RNF-006 recálculo del total | Regla de negocio de CU-06 |
| RNF-007, RNF-008 CORS y secretos | Diseño (G2) |
| RNF-009 atomicidad | Regla de negocio de CU-06 y CU-22 |
| RNF-010 caída de Firebase | Flujo de excepción de CU-03 |
| RNF-011, RNF-012 usabilidad | Prototipo (G1-P2) |
| RNF-013 a RNF-015 | Diseño (G2) |
| RNF-016 Ley 1581 | Regla de negocio de CU-06 |
| RNF-017 Ley 527 | Regla de negocio de CU-06 (resumen fiel y comprobante) |
