# 3. Modelo de dominio

Fuente editable: [modelo-dominio.mmd](diagramas/modelo-dominio.mmd) · Imagen: [png](diagramas/modelo-dominio.png) · [svg](diagramas/modelo-dominio.svg)

- **18 clases conceptuales:** Usuario, Cliente, Administrador, NivelFidelizacion, Recompensa, TransaccionPuntos, Producto, Categoria, Municipio, Carrito, ItemCarrito, Pedido, LineaPedido, DireccionEntrega, Favorito, MensajeContacto, IntentoAcceso, Aliado.
- **Atributos de negocio** (2 o más) en 13 clases (las otras 5 -Administrador, Categoria, Carrito, ItemCarrito y Favorito- tienen un solo atributo propio); sin métodos, sin claves foráneas ni atributos técnicos.
- **Generalización:** Cliente y Administrador son un Usuario (distinto rol y permisos, datos básicos comunes).
- **Clases de asociación:** LineaPedido (entre Pedido y Producto: cantidad y precio unitario pactado) y Favorito (entre Cliente y Producto: fecha en que se marcó).
- **Composición:** un Pedido se compone de líneas de pedido y un Carrito contiene ítems (no existen sin su todo).
- **Multiplicidades destacadas:** un Cliente tiene 0..* direcciones guardadas y cada Pedido se envía a exactamente una; un Carrito pertenece a 0..1 Cliente, porque el visitante puede armarlo antes de iniciar sesión (CU-05).
- **Fidelización:** el nivel (Espresso, Plata, Oro) se deduce de los puntos acumulados; cada movimiento de puntos queda en TransaccionPuntos, ligado a un Pedido (abono) o a una Recompensa (canje).
