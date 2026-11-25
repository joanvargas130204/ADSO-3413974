# B2 · Modelo lógico relacional

Diagrama lógico (tablas con PK y FK): [modelo-logico.mmd](diagramas/modelo-logico.mmd) · [png](diagramas/modelo-logico.png) · [svg](diagramas/modelo-logico.svg)

**15 tablas**, 14 llaves foráneas.

| Tabla | PK | FK |
|---|---|---|
| `cliente` | (id_cliente) | — |
| `administrador` | (id_admin) | — |
| `municipio` | (id_municipio) | — |
| `categoria` | (id_categoria) | — |
| `producto` | (id_producto) | (id_categoria) → categoria |
| `direccion_entrega` | (id_cliente, consecutivo) | (id_cliente) → cliente; (id_municipio) → municipio |
| `pedido` | (id_pedido) | (id_cliente) → cliente; (id_cliente, consecutivo_direccion) → direccion_entrega |
| `detalle_pedido` | (id_pedido, id_producto) | (id_pedido) → pedido; (id_producto) → producto |
| `favorito` | (id_cliente, id_producto) | (id_cliente) → cliente; (id_producto) → producto |
| `recompensa` | (id_recompensa) | — |
| `nivel_fidelizacion` | (id_nivel) | — |
| `transaccion_puntos` | (id_transaccion) | (id_cliente) → cliente; (id_pedido) → pedido; (id_recompensa) → recompensa |
| `contacto` | (id_contacto) | (id_municipio) → municipio |
| `intento_login_admin` | (id_intento) | (id_admin) → administrador |
| `aliado` | (id_aliado) | — |

## Cuadro de reglas de transformación aplicadas

| Regla | Caso en CoffeeCol | Resultado en el modelo lógico |
|---|---|---|
| N:M se resuelve con tabla intermedia | Un pedido tiene varios productos y un producto está en varios pedidos | `detalle_pedido(id_pedido FK, id_producto FK, cantidad, precio_unitario)`, PK compuesta |
| N:M se resuelve con tabla intermedia | Un cliente marca varios productos y un producto es marcado por varios clientes | `favorito(id_cliente FK, id_producto FK, fecha_agregado)`, PK compuesta |
| 1:N: la FK va en el lado «muchos» | Una categoría tiene varios productos; un cliente tiene varios pedidos | `producto.id_categoria`, `pedido.id_cliente` |
| Entidad débil: la PK incluye la del dueño | La dirección solo existe dentro de un cliente | `direccion_entrega(id_cliente PK FK, consecutivo PK, …)` |
| FK compuesta hacia entidad débil | Un pedido se envía a una dirección del mismo cliente | `pedido(id_cliente, consecutivo_direccion)` → `direccion_entrega(id_cliente, consecutivo)`: garantiza que la dirección pertenece al cliente del pedido |
| Relación opcional (0,1): FK que admite NULL | Una transacción puede originarse en un pedido o en una recompensa | `transaccion_puntos.id_pedido NULL`, `id_recompensa NULL` |
| Atributo multivaluado: tabla aparte | Un cliente tiene varias direcciones | `direccion_entrega` (tabla propia) |
| Atributo derivado | El nivel de fidelización se deduce de los puntos | No se guarda: se calcula comparando `cliente.puntos_acumulados` con `nivel_fidelizacion.puntos_minimos` |
| Generalización Usuario → Cliente / Administrador | Datos y credenciales distintos | Una tabla por subtipo (`cliente`, `administrador`): el cliente entra por Firebase (sin clave) y el administrador con clave con hash; una tabla única llenaría de NULL |
| Entidad sin relación | Aliado | `aliado` independiente |
