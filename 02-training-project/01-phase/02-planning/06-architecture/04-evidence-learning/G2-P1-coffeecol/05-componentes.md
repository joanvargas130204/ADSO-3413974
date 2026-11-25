# A5 · Vista de componentes

Fuente editable: [componentes.mmd](diagramas/componentes.mmd) · Imagen: [png](diagramas/componentes.png) · [svg](diagramas/componentes.svg)

Siete componentes con interfaces provistas y requeridas. La dirección de cada flecha va del componente que **requiere** hacia el que **provee** la interfaz; no hay ciclos, y solo el componente C7 depende de la base de datos.

| Componente | Provee | Requiere | Clases que agrupa | Requisitos que atiende |
|---|---|---|---|---|
| C1 Interfaz web (Bootstrap + JavaScript) | `IPresentacion` | `IApiRest` | Carrito, ItemCarrito | RF-011, RF-012, RF-014, RF-021 |
| C2 API REST (controladores PHP) | `IApiRest` | `ICheckout, IAutenticacion, ICatalogo` | PedidoController, AuthController, ProductoController | RF-017, RF-021, RF-022, RF-023, RF-028, RF-045, RF-046 |
| C3 Servicio de pedidos | `ICheckout` | `IDatosPedido, IDatosProducto, IPuntos` | Pedido, LineaPedido, DireccionEntrega, CheckoutFacade, ValidadorEntrega, CalculadoraDespacho, DespachoPorUmbral, DespachoFijo | RF-014, RF-017, RF-018, RF-019, RF-020, RF-022 |
| C4 Servicio de fidelización | `IPuntos` | `IDatosUsuario` | TransaccionPuntos, PuntosService | RF-038 |
| C5 Servicio de autenticación | `IAutenticacion` | `IDatosUsuario, IIdentidadExterna` | Usuario, Cliente, Administrador, AuthService, Autenticador, AutenticadorFirebase, AutenticadorJwt | RF-023, RF-024, RF-025, RF-027, RF-028, RF-038 |
| C6 Servicio de catálogo | `ICatalogo` | `IDatosProducto` | Producto, CatalogoService | RF-011, RF-045, RF-046 |
| C7 Acceso a datos (repositorios + conexión) | `IDatosPedido, IDatosProducto, IDatosUsuario` | `IBaseDatos` | Conexion, PedidoRepository, ProductoRepository, UsuarioRepository | RF-020, RF-022, RF-025, RF-027, RF-045 |

Servicios externos: Firebase Authentication (interfaz `IIdentidadExterna`) y MariaDB (interfaz `IBaseDatos`).
