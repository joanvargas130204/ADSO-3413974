# B6 · Políticas de seguridad de los datos

## Políticas (3 principios × 2 o más)

| # | Principio | Política (medida concreta sobre el caso) | Dónde se ve |
|---|---|---|---|
| 1 | Integridad | Restricciones `CHECK` y llaves foráneas: precio y cantidad positivos, stock no negativo, `total = subtotal + valor_despacho`, estado de pedido en la lista permitida | `sql/esquema-mariadb.sql`; pruebas en `evidencia-ejecucion-2.txt` |
| 2 | Integridad | Registrar el pedido, sus líneas, el descuento de stock y los puntos en **una sola transacción** (todo o nada); el total se recalcula en el servidor y no se acepta el del navegador | RNF-009, RNF-006; `CheckoutFacade` y `PedidoRepository` (G2-P1) |
| 3 | Integridad | `ON DELETE RESTRICT` sobre productos, clientes y pedidos con historial; los productos «se retiran» con `estado = 'retirado'` en lugar de borrarse | `producto.estado`, `fk_det_producto`, `fk_pedido_cliente` |
| 4 | Confidencialidad | Contraseñas del administrador con **hash Bcrypt y sal** (la sal viaja dentro del hash; nunca la clave en texto plano ni «cifrada»); los clientes no tienen contraseña (Firebase) | `administrador.hash_contrasena VARCHAR(255)` |
| 5 | Confidencialidad | Datos en tránsito siempre por **TLS** (HTTPS 443) entre navegador, API y Firebase; credenciales de la base y llaves de Firebase en `.env` fuera de la carpeta pública | RNF-008; vista de despliegue (G2-P1) |
| 6 | Confidencialidad | **Datos personales** (nombre, correo, teléfono y dirección de cliente; datos de contacto): finalidad informada (gestionar compras, entregas y fidelización), autorización previa con casilla obligatoria antes de confirmar el pedido, y derecho a conocer, actualizar y suprimir (Ley 1581 de 2012) | RNF-016; `cliente`, `direccion_entrega`, `contacto` |
| 7 | Confidencialidad | Mínimo privilegio: la API usa una cuenta de base de datos que solo hace `SELECT/INSERT/UPDATE/DELETE` sobre el esquema `coffeecol` (sin crear ni borrar tablas) y cada cliente ve solo sus filas | [sql/seguridad-cuentas.sql](sql/seguridad-cuentas.sql) |
| 8 | Disponibilidad | **Respaldo** completo con `mysqldump` todos los días a las 2:00 a. m., retención de 14 días y copia en otro equipo distinto del servidor | Acta de respaldos |
| 9 | Disponibilidad | **Prueba de restauración** cada mes en una base de pruebas, con acta (fecha, archivo, tiempo y resultado) | Acta mensual |
| 10 | Disponibilidad | Bloqueo temporal del administrador tras 5 intentos fallidos en 15 minutos para frenar fuerza bruta; la base solo acepta conexiones de la red local del servidor de aplicación | `intento_login_admin`, RF-026; despliegue |

## Matriz de roles contra tablas (permisos efectivos a través de la API)

S = SELECT · I = INSERT · U = UPDATE · D = DELETE · «propio» = solo sus filas · — = sin acceso

| Tabla | Visitante | Cliente | Administrador |
|---|---|---|---|
| `cliente` | — | S, U propio | S |
| `administrador` | — | — | S propio |
| `municipio` | S | S | S |
| `categoria` | S | S | S, I, U |
| `producto` | S (activos) | S (activos) | S, I, U (retirar = U de `estado`) |
| `direccion_entrega` | — | S, I, U, D propio | S |
| `pedido` | — | S propio, I (checkout) | S, U (estado) |
| `detalle_pedido` | — | S propio, I (checkout) | S |
| `favorito` | — | S, I, D propio | — |
| `recompensa` | S | S | S, I, U |
| `nivel_fidelizacion` | S | S | S, U |
| `transaccion_puntos` | — | S propio | S |
| `contacto` | I | I | S |
| `intento_login_admin` | — | — | S |
| `aliado` | S | S | S, I, U, D |

Los permisos de la matriz los aplica la capa de servicios con el rol del token (RNF-005); las cuentas de base de datos limitan además el daño posible si la API fuera comprometida.
