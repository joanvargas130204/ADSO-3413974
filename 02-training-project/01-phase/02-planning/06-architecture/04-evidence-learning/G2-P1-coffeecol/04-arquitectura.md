# A4 · Arquitectura del software

Fuente editable: [arquitectura.mmd](diagramas/arquitectura.mmd) · Imagen: [png](diagramas/arquitectura.png) · [svg](diagramas/arquitectura.svg)

**Estilo: arquitectura en tres capas (presentación, lógica de negocio y datos) con una API REST sin estado.** El navegador habla solo con los controladores por HTTPS y JSON; los controladores llaman a los servicios; los servicios llaman a los repositorios; solo los repositorios tocan MariaDB. Ninguna capa se salta a otra (la interfaz nunca consulta la base ni Firebase escribe en ella).

**Comunicación entre componentes:** HTTPS con JSON entre navegador y API; llamadas de método dentro de PHP entre controlador, servicio y repositorio; PDO con sentencias preparadas hacia la base; HTTPS hacia Firebase para verificar identidades.

## Tabla de decisiones frente a los RNF

| RNF | Decisión de diseño | Alternativa descartada | Razón del descarte |
|---|---|---|---|
| RNF-006 total recalculado en el servidor | `CheckoutFacade` ignora los precios del carrito y recalcula subtotal, despacho y total con los precios de la base | Aceptar el total que envía el navegador | Cualquiera podría alterar el precio desde la consola del navegador |
| RNF-009 operaciones atómicas | Una transacción de base de datos en `PedidoRepository` que guarda el pedido, sus líneas, el descuento de stock y los puntos; si algo falla, todo se deshace | Guardar cada cosa por separado y corregir después | Podría quedar un pedido sin puntos o con stock descontado sin pedido |
| RNF-005 validar el token administrativo | `ProductoController` y `PedidoController.cambiarEstado` piden a `AuthService` validar firma y vigencia antes de cada operación | Validar el rol solo en la pantalla del panel | Se puede saltar llamando al endpoint directamente |
| RNF-013 acceso a datos centralizado | `Conexion` (Singleton) y repositorios; servicios y controladores no ejecutan SQL | SQL escrito dentro de cada controlador | Duplica consultas y mezcla capas |
| RNF-008 credenciales fuera del alcance público | Archivo `.env` fuera de la carpeta pública del servidor, leído solo por `Conexion` y `AutenticadorJwt` | Credenciales dentro del código | Quedarían versionadas y expuestas |
| RNF-010 Firebase no disponible | `AutenticadorFirebase` captura el fallo y la API responde un mensaje amable; el catálogo no depende de Firebase | Hacer que toda página consulte a Firebase | Una caída del servicio externo rompería la navegación |
| RNF-004 concurrencia | Servicios sin estado y conexión reutilizada por petición | Guardar el carrito en sesión del servidor | Aumenta el uso de memoria y ata al usuario a un servidor |
| Estilo | Tres capas con API REST | Monolito de páginas PHP que mezclan HTML, lógica y SQL | Mezcla responsabilidades y complica cada cambio |
