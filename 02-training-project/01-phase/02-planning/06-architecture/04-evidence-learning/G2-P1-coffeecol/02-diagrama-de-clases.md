# A2 · Diagrama de clases

Fuente editable: [diagrama-clases.mmd](diagramas/diagrama-clases.mmd) · Imagen: [png](diagramas/diagrama-clases.png) · [svg](diagramas/diagrama-clases.svg)

- **28 clases** en cuatro áreas, ninguna mezcla áreas distintas: dominio (10), lógica de negocio (11), persistencia (4) y presentación (3).
- **Atributos tipados con visibilidad** y métodos con parámetros y tipo de retorno; todas las asociaciones llevan multiplicidad en los dos extremos.
- **Composición** (es parte de): `Pedido` *— `LineaPedido` y `Carrito` *— `ItemCarrito`; no existen sin su todo.
- **Herencia** (es un): `Cliente` y `Administrador` son un `Usuario` (clase abstracta).
- **Interfaces con 2 implementaciones** (polimorfismo): `CalculadoraDespacho` → `DespachoPorUmbral`, `DespachoFijo`; `Autenticador` → `AutenticadorFirebase`, `AutenticadorJwt`.
- **Cohesión:** `Pedido` solo guarda datos y su total; guardarlo es de `PedidoRepository`; calcular el despacho es de `CalculadoraDespacho`; los controladores solo traducen JSON y delegan.
- `Carrito` e `ItemCarrito` viven en el navegador (RF-013 del SRS lo conserva allí); el servidor nunca confía en ellos y recalcula el total (RNF-006).

| Área | Clases |
|---|---|
| Dominio | Usuario, Cliente, Administrador, Producto, Pedido, LineaPedido, DireccionEntrega, TransaccionPuntos, Carrito, ItemCarrito |
| Lógica de negocio | CheckoutFacade, ValidadorEntrega, CalculadoraDespacho, DespachoPorUmbral, DespachoFijo, PuntosService, AuthService, Autenticador, AutenticadorFirebase, AutenticadorJwt, CatalogoService |
| Persistencia | Conexion, PedidoRepository, ProductoRepository, UsuarioRepository |
| Presentación (API) | PedidoController, AuthController, ProductoController |
