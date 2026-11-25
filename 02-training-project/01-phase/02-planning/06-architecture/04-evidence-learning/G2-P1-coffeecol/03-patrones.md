# A3 · Patrones de diseño aplicados

Tres patrones GoF distintos, todos visibles en el [diagrama de clases](diagramas/diagrama-clases.png).

| Patrón | Problema concreto del caso | Por qué ese patrón | Clases que lo implementan | Qué mejora en mantenibilidad |
|---|---|---|---|---|
| **Estrategia** | El despacho cuesta $12.000 y es gratis sobre $150.000 (RF-014), pero Tantico Café puede cambiar la política (envío gratis por campaña o tarifa fija) | Separa la regla de cobro de la clase que arma el pedido, y permite escoger la regla en tiempo de ejecución | `CalculadoraDespacho` (interfaz), `DespachoPorUmbral`, `DespachoFijo`; la usa `CheckoutFacade` | Una nueva política es una clase nueva; `CheckoutFacade` y `Pedido` no se modifican |
| **Fachada** | Confirmar un pedido toca seis piezas: validar datos (RF-018), recalcular el total (RNF-006), verificar y descontar stock, guardar el pedido y acreditar puntos de forma atómica (RNF-009) | El controlador necesita una sola operación `confirmarPedido`; la fachada oculta el orden y la transacción | `CheckoutFacade`, que coordina `ValidadorEntrega`, `CalculadoraDespacho`, `ProductoRepository`, `PedidoRepository` y `PuntosService` | El controlador no conoce los detalles; el orden o una regla nueva se cambia en un solo lugar |
| **Singleton** | El SRS exige que todo el acceso a datos pase por un único punto (RNF-013) y que no se abran conexiones de más con 50 peticiones por segundo (RNF-004) | Garantiza una sola instancia de la conexión PDO por petición, compartida por los repositorios | `Conexion` (`obtenerInstancia()`), usada por `PedidoRepository`, `ProductoRepository` y `UsuarioRepository` | La cadena de conexión y las credenciales (.env) se configuran en un solo archivo |

**Polimorfismo.** `AuthService` llama `autenticar()` sin saber si recibe `AutenticadorFirebase` (clientes) o `AutenticadorJwt` (administrador): agregar otro proveedor de identidad no cambia el servicio.
