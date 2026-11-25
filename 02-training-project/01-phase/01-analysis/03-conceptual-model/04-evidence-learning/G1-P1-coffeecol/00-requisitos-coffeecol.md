# Requisitos de CoffeeCol / Tantico Café (base del análisis)

Fuente: **SRS de CoffeeCol / Tantico Café, versión 2.0 (IEEE Std 830-1998)**, elaborado por el equipo del proyecto (tres aprendices). Este documento no copia el SRS: lo resume con numeración idéntica (RF-001 a RF-054, RNF-001 a RNF-017) para poder trazar cada requisito en el análisis. El texto completo está en el SRS del equipo.

**Sistema:** plataforma web transaccional de comercio electrónico de café colombiano de especialidad, con mapa del Huila, programa de fidelización y analítica comercial. **Fuera de alcance (SRS 1.2.2):** pasarelas de pago reales, despacho automatizado con transportadoras, facturación electrónica DIAN y aplicación móvil nativa.

## Actores (SRS 2.3 y Apéndice B)

| Actor | Tipo | Descripción |
|---|---|---|
| Visitante | Primario | Navega el sitio público: mapa, catálogo, carrito y contacto |
| Cliente registrado | Primario | Visitante autenticado con Google o enlace mágico: pedidos, perfil, favoritos, puntos |
| Administrador | Primario | Opera el negocio desde el panel protegido |
| Firebase Authentication | Secundario (sistema externo) | Valida la identidad de los clientes; no inicia casos de uso |
| Temporizador del sistema | Iniciador de proceso automático | Dispara el bono anual de cumpleaños (RF-039) |

## Requisitos funcionales

| ID | Requisito | Prioridad | Actor principal |
|---|---|---|---|
| RF-001 | Pantalla de bienvenida animada con paso automático a inicio tras 3 s | Baja | Visitante |
| RF-002 | Mapa interactivo del Huila (37 municipios) con altitud y perfil cafetero | Media | Visitante |
| RF-003 | Secciones informativas: historia, perfil sensorial y tueste artesanal | Baja | Visitante |
| RF-004 | Carrusel de cooperativas y caficultores aliados | Baja | Visitante |
| RF-005 | Ventana modal promocional una vez por sesión de navegación | Baja | Visitante |
| RF-006 | Listar el inventario en 5 categorías de producto | Alta | Visitante / Cliente |
| RF-007 | Filtrar el catálogo por categoría sin recargar la página | Alta | Visitante / Cliente |
| RF-008 | Tarjeta de producto con foto, nombre, notas, categoría, valoración y precios | Alta | Visitante / Cliente |
| RF-009 | Animaciones de entrada al desplazarse por la página | Baja | Visitante / Cliente |
| RF-010 | Indicadores de carga mientras llegan los datos del catálogo | Baja | Visitante / Cliente |
| RF-011 | Agregar productos al carrito desde la tarjeta o el detalle | Alta | Visitante / Cliente |
| RF-012 | Aumentar, disminuir o quitar ítems desde el panel lateral del carrito | Alta | Visitante / Cliente |
| RF-013 | Conservar el carrito entre sesiones de navegación | Media | Visitante / Cliente |
| RF-014 | Calcular subtotal, despacho ($12.000; gratis sobre $150.000) y total | Alta | Visitante / Cliente |
| RF-015 | Botón flotante con contador de unidades del carrito | Baja | Visitante / Cliente |
| RF-016 | Retirar del carrito los productos que ya no existen en el catálogo | Media | Visitante / Cliente |
| RF-017 | Formulario de checkout con nombres, apellidos, correo, teléfono, municipio y dirección | Alta | Cliente registrado |
| RF-018 | Validar correo, teléfono de 10 dígitos y campos vacíos antes de enviar | Alta | Cliente registrado |
| RF-019 | Resumen desglosado del pedido antes de la confirmación | Alta | Cliente registrado |
| RF-020 | Registrar el pedido con un código único de orden | Alta | Cliente registrado |
| RF-021 | Confirmación con número de pedido y vaciado del carrito | Media | Cliente registrado |
| RF-022 | Ciclo de estados del pedido: pendiente, procesando, enviado, entregado o cancelado | Alta | Administrador |
| RF-023 | Acceso de clientes con cuenta de Google | Alta | Visitante |
| RF-024 | Acceso de clientes con enlace mágico enviado al correo | Alta | Visitante |
| RF-025 | Acceso del administrador con usuario y clave cifrada, con sesión de 60 min | Alta | Administrador |
| RF-026 | Bloqueo temporal del administrador tras 5 intentos fallidos en 15 min | Alta | Administrador |
| RF-027 | Sincronizar al usuario en la base tras acceder con Firebase | Alta | Cliente registrado |
| RF-028 | Verificar el rol y llevar al usuario a su módulo | Alta | Cliente / Administrador |
| RF-029 | Cierre seguro de sesión | Media | Cliente / Administrador |
| RF-030 | Panel de perfil con avatar, nombre, correo, fecha de vinculación y nivel | Alta | Cliente registrado |
| RF-031 | Estadísticas del cliente: puntos, pedidos, favoritos y direcciones | Media | Cliente registrado |
| RF-032 | Historial cronológico de compras con el estado de cada paquete | Alta | Cliente registrado |
| RF-033 | Añadir, editar y eliminar direcciones guardadas | Media | Cliente registrado |
| RF-034 | Registrar la fecha de cumpleaños una sola vez | Baja | Cliente registrado |
| RF-035 | Marcar o desmarcar productos como favoritos | Media | Cliente registrado |
| RF-036 | Guardar favoritos exigiendo sesión activa | Media | Cliente registrado |
| RF-037 | Ver los favoritos guardados en el perfil | Baja | Cliente registrado |
| RF-038 | Acreditar 1 punto por cada $1.000 y asignar nivel Espresso, Plata u Oro | Alta | Cliente registrado |
| RF-039 | Bono anual de 100 puntos en el mes de cumpleaños | Media | Cliente registrado |
| RF-040 | Bitácora auditable de abonos y deducciones de puntos | Media | Cliente registrado |
| RF-041 | Canje de recompensas: 10 % de descuento, café gratis y kit barista | Media | Cliente registrado |
| RF-042 | Barra de progreso hacia el siguiente nivel | Baja | Cliente registrado |
| RF-043 | Formulario de contacto: nombre, finca, teléfono, correo, municipio y mensaje | Media | Visitante / Caficultor |
| RF-044 | Guardar los mensajes de contacto para seguimiento comercial | Media | Visitante / Caficultor |
| RF-045 | Alta de productos con nombre, descripción, precio, categoría, stock e imagen | Alta | Administrador |
| RF-046 | Eliminar productos del catálogo activo | Alta | Administrador |
| RF-047 | Buscar, ordenar y filtrar el inventario administrativo | Media | Administrador |
| RF-048 | Listar órdenes con comprador, total, fecha y detalle de productos | Alta | Administrador |
| RF-049 | Actualizar el estado de los pedidos con sesión de administrador válida | Alta | Administrador |
| RF-050 | Consultar clientes con historial de compras y saldo de puntos | Media | Administrador |
| RF-051 | KPIs: ventas del día y del mes, pedidos de hoy, ticket promedio y café más vendido | Alta | Administrador |
| RF-052 | Cuatro gráficos: ventas diarias, top 5, por categoría y tendencia mensual | Media | Administrador |
| RF-053 | Filtrar las métricas por rango: hoy, 7 días, 30 días, mes, año o personalizado | Media | Administrador |
| RF-054 | Exportar reportes a CSV e imprimir en PDF | Media | Administrador |

## Requisitos no funcionales (SRS 3.3 a 3.6)

| ID | Categoría | Requisito |
|---|---|---|
| RNF-001 | Rendimiento | El catálogo carga y se muestra en menos de 3,0 s |
| RNF-002 | Rendimiento | Las operaciones del carrito responden en menos de 200 ms |
| RNF-003 | Rendimiento | KPIs y gráficos en menos de 4,0 s con 10.000 registros |
| RNF-004 | Rendimiento | El servidor soporta 50 peticiones simultáneas por segundo sin perder transacciones |
| RNF-005 | Seguridad | Todo endpoint administrativo valida la firma y vigencia del token |
| RNF-006 | Seguridad | El total de cada orden se recalcula en el servidor desde la base de datos |
| RNF-007 | Seguridad | CORS restrictivo, solo orígenes homologados |
| RNF-008 | Seguridad | Credenciales y llaves fuera del alcance público (archivo .env) |
| RNF-009 | Fiabilidad | Crear órdenes y canjear puntos son operaciones atómicas (transacción) |
| RNF-010 | Fiabilidad | Si Firebase no responde, se avisa al usuario sin romper el catálogo |
| RNF-011 | Usabilidad | Interfaz adaptativa de 360 px a 1920 px |
| RNF-012 | Usabilidad | Retroalimentación visual en toda espera (indicadores, botones deshabilitados) |
| RNF-013 | Mantenibilidad | Acceso a datos centralizado en un único archivo |
| RNF-014 | Mantenibilidad | Componentes comunes de interfaz modularizados |
| RNF-015 | Portabilidad | Funciona en las dos últimas versiones de Chrome, Firefox, Edge y Safari |
| RNF-016 | Legal | Ley 1581 de 2012: casilla obligatoria de aceptación de la política de datos |
| RNF-017 | Legal | Ley 527 de 1999: resumen fiel de la compra, transporte desglosado y comprobante |

## Supuestos del análisis

1. Los casos de uso CU-01 a CU-14 son los del Apéndice B del SRS; los CU-15 a CU-27 son casos que agregué para cubrir requisitos que el SRS no asignaba a ningún caso o para modelar «include» y «extend» (se explican en `03-casos-de-uso.md`).
2. El análisis describe qué hace el sistema; las tecnologías del SRS (PHP, MariaDB, Firebase, Chart.js) se dejan para el diseño (G2).
3. Los pagos se registran como pedido pendiente: la liquidación se simula (SRS 1.2.2).
