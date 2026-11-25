# A7 · Matriz de trazabilidad (análisis → diseño)

| Requisito | Clase(s) | Componente(s) | Decisión de diseño |
|---|---|---|---|
| RF-011 | Producto, Carrito, ItemCarrito | C1, C6 | Carrito en el navegador |
| RF-012 | Carrito, ItemCarrito | C1 | Carrito en el navegador |
| RF-014 | Carrito, CalculadoraDespacho, DespachoPorUmbral, DespachoFijo | C1, C3 | Estrategia |
| RF-017 | DireccionEntrega, CheckoutFacade, PedidoController | C2, C3 | Controlador delega en la fachada |
| RF-018 | ValidadorEntrega | C3 | Validación en servidor |
| RF-019 | Pedido, LineaPedido, CheckoutFacade | C3 | Fachada |
| RF-020 | Pedido, LineaPedido, CheckoutFacade, Conexion, PedidoRepository, ProductoRepository | C3, C7 | Fachada · transacción (RNF-009) · recálculo (RNF-006) |
| RF-021 | Carrito, PedidoController | C1, C2 | Carrito se vacía tras la respuesta |
| RF-022 | Pedido, PedidoRepository, PedidoController | C2, C3, C7 | RNF-005 token válido |
| RF-023 | AuthService, Autenticador, AutenticadorFirebase, AuthController | C2, C5 | Polimorfismo del autenticador · RNF-010 |
| RF-024 | AuthService, AutenticadorFirebase | C5 | Polimorfismo del autenticador |
| RF-025 | Administrador, AuthService, Autenticador, AutenticadorJwt, UsuarioRepository | C5, C7 | Autenticador por JWT · RNF-005 |
| RF-027 | Usuario, Cliente, AuthService, UsuarioRepository | C5, C7 | Sincronización al iniciar sesión |
| RF-028 | Usuario, AuthController | C2, C5 | Rol según el tipo de usuario |
| RF-038 | Cliente, TransaccionPuntos, PuntosService | C4, C5 | Fidelización separada del pedido |
| RF-045 | Producto, CatalogoService, ProductoRepository, ProductoController | C2, C6, C7 | RNF-005 token válido |
| RF-046 | Producto, CatalogoService, ProductoController | C2, C6 | RNF-005 token válido |

**Hacia adelante:** los 17 requisitos del subconjunto llegan a clase y componente (100 %). **Hacia atrás:** cada una de las 28 clases responde a al menos un requisito; ninguna clase queda sin requisito.

**Clase → requisitos**

| Clase | Componente | Requisitos |
|---|---|---|
| Usuario | C5 | RF-027, RF-028 |
| Cliente | C5 | RF-027, RF-038 |
| Administrador | C5 | RF-025 |
| Producto | C6 | RF-011, RF-045, RF-046 |
| Pedido | C3 | RF-019, RF-020, RF-022 |
| LineaPedido | C3 | RF-019, RF-020 |
| DireccionEntrega | C3 | RF-017 |
| TransaccionPuntos | C4 | RF-038 |
| Carrito | C1 | RF-011, RF-012, RF-014, RF-021 |
| ItemCarrito | C1 | RF-011, RF-012 |
| CheckoutFacade | C3 | RF-017, RF-019, RF-020 |
| ValidadorEntrega | C3 | RF-018 |
| CalculadoraDespacho | C3 | RF-014 |
| DespachoPorUmbral | C3 | RF-014 |
| DespachoFijo | C3 | RF-014 |
| PuntosService | C4 | RF-038 |
| AuthService | C5 | RF-023, RF-024, RF-025, RF-027 |
| Autenticador | C5 | RF-023, RF-025 |
| AutenticadorFirebase | C5 | RF-023, RF-024 |
| AutenticadorJwt | C5 | RF-025 |
| CatalogoService | C6 | RF-045, RF-046 |
| Conexion | C7 | RF-020 |
| PedidoRepository | C7 | RF-020, RF-022 |
| ProductoRepository | C7 | RF-020, RF-045 |
| UsuarioRepository | C7 | RF-025, RF-027 |
| PedidoController | C2 | RF-017, RF-021, RF-022 |
| AuthController | C2 | RF-023, RF-028 |
| ProductoController | C2 | RF-045, RF-046 |
