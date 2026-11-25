# B4 · Diccionario de datos

Estándar de nombrado: tablas en singular y `snake_case`; columnas en `snake_case`; llaves primarias `id_<tabla>`; llaves foráneas con el mismo nombre de la columna que referencian; restricciones con prefijo `pk_`, `fk_`, `uq_` y `ck_`. Generado desde la misma definición que los scripts SQL ([esquema-mariadb.sql](sql/esquema-mariadb.sql)).

## `cliente`

Cliente que compra con cuenta Firebase. PK: (id_cliente).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_cliente` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `uid_firebase` | VARCHAR | 128 | NOT NULL, UNIQUE | Identificador de Firebase Authentication |
| `nombre` | VARCHAR | 100 | NOT NULL | Nombre completo |
| `correo` | VARCHAR | 120 | NOT NULL, UNIQUE | Correo electrónico |
| `fecha_vinculacion` | DATE | n/a | NOT NULL | Fecha de primer acceso |
| `fecha_cumpleanos` | DATE | n/a | NULL | Fecha de cumpleaños (bono anual) |
| `puntos_acumulados` | INT | n/a | NOT NULL, DEFAULT 0, CHECK (puntos_acumulados >= 0) | Entero mayor o igual a 0 |

## `administrador`

Administrador del panel (usuario y clave con hash Bcrypt). PK: (id_admin).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_admin` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `usuario` | VARCHAR | 40 | NOT NULL, UNIQUE | Nombre de usuario de acceso |
| `nombre` | VARCHAR | 100 | NOT NULL | Nombre completo |
| `correo` | VARCHAR | 120 | NOT NULL, UNIQUE | Correo electrónico del administrador |
| `hash_contrasena` | VARCHAR | 255 | NOT NULL | Hash Bcrypt con sal incorporada (nunca la clave) |

## `municipio`

Municipio de entrega u origen de contacto. PK: (id_municipio).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_municipio` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 60 | NOT NULL, UNIQUE | Nombre del municipio |
| `altitud` | INT | n/a | NULL, CHECK (altitud IS NULL OR altitud > 0) | Metros sobre el nivel del mar, mayor a 0 |
| `notas_cata` | VARCHAR | 200 | NULL | Descripción de cata de la zona |

## `categoria`

Categoría del catálogo. PK: (id_categoria).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_categoria` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 50 | NOT NULL, UNIQUE | Nombre de la categoría |

## `producto`

Producto del catálogo. PK: (id_producto).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_producto` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 100 | NOT NULL | Nombre comercial |
| `descripcion` | VARCHAR | 500 | NULL | Descripción libre |
| `notas_aromaticas` | VARCHAR | 150 | NULL | Texto descriptivo de aromas (no se consulta por nota) |
| `precio` | DECIMAL | 10,2 | NOT NULL, CHECK (precio > 0) | Pesos COP, mayor a 0 |
| `precio_anterior` | DECIMAL | 10,2 | NULL, CHECK (precio_anterior IS NULL OR precio_anterior > 0) | Precio antes de la oferta, mayor a 0 |
| `stock` | INT | n/a | NOT NULL, DEFAULT 0, CHECK (stock >= 0) | Unidades disponibles, mayor o igual a 0 |
| `imagen` | VARCHAR | 255 | NULL | Ruta de la imagen cargada |
| `valoracion` | DECIMAL | 2,1 | NULL, CHECK (valoracion IS NULL OR (valoracion >= 0 AND valoracion <= 5)) | Entre 0,0 y 5,0 |
| `estado` | VARCHAR | 10 | NOT NULL, DEFAULT 'activo', CHECK (estado IN ('activo','retirado')) | activo o retirado |
| `id_categoria` | INT | n/a | NOT NULL, FK → categoria.id_categoria ON DELETE RESTRICT | Categoría existente |

## `direccion_entrega`

Dirección guardada de un cliente (entidad débil). PK: (id_cliente, consecutivo).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_cliente` | INT | n/a | PK, NOT NULL, FK → cliente.id_cliente ON DELETE CASCADE | Cliente dueño de la dirección |
| `consecutivo` | INT | n/a | PK, NOT NULL, CHECK (consecutivo >= 1) | Número de la dirección dentro del cliente, desde 1 |
| `id_municipio` | INT | n/a | NOT NULL, FK → municipio.id_municipio ON DELETE RESTRICT | Municipio existente |
| `destinatario` | VARCHAR | 100 | NOT NULL | Quien recibe |
| `direccion` | VARCHAR | 150 | NOT NULL | Calle, carrera y número |
| `telefono` | CHAR | 10 | NOT NULL, CHECK (length(telefono) = 10) | 10 dígitos |

## `pedido`

Pedido de un cliente. PK: (id_pedido).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_pedido` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `codigo` | VARCHAR | 20 | NOT NULL, UNIQUE | Código único de orden |
| `fecha` | DATETIME | n/a | NOT NULL | Fecha y hora del registro |
| `estado` | VARCHAR | 12 | NOT NULL, DEFAULT 'pendiente', CHECK (estado IN ('pendiente','procesando','enviado','entregado','cancelado')) | pendiente, procesando, enviado, entregado o cancelado |
| `subtotal` | DECIMAL | 12,2 | NOT NULL, CHECK (subtotal >= 0 AND valor_despacho >= 0), CHECK (total = subtotal + valor_despacho) | Suma de las líneas, mayor o igual a 0 |
| `valor_despacho` | DECIMAL | 10,2 | NOT NULL, CHECK (subtotal >= 0 AND valor_despacho >= 0), CHECK (total = subtotal + valor_despacho) | Costo de despacho, mayor o igual a 0 |
| `total` | DECIMAL | 12,2 | NOT NULL, CHECK (total = subtotal + valor_despacho) | Subtotal más despacho |
| `id_cliente` | INT | n/a | NOT NULL, FK → direccion_entrega.id_cliente ON DELETE RESTRICT | Cliente que compra |
| `consecutivo_direccion` | INT | n/a | NOT NULL, FK → direccion_entrega.consecutivo ON DELETE RESTRICT | Dirección de entrega del mismo cliente |

## `detalle_pedido`

Línea de un pedido (resuelve la N:M pedido-producto). PK: (id_pedido, id_producto).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_pedido` | INT | n/a | PK, NOT NULL, FK → pedido.id_pedido ON DELETE CASCADE | Pedido al que pertenece |
| `id_producto` | INT | n/a | PK, NOT NULL, FK → producto.id_producto ON DELETE RESTRICT | Producto vendido |
| `cantidad` | INT | n/a | NOT NULL, CHECK (cantidad > 0) | Unidades, mayor a 0 |
| `precio_unitario` | DECIMAL | 10,2 | NOT NULL, CHECK (precio_unitario > 0) | Precio pactado al comprar, mayor a 0 |

## `favorito`

Producto marcado por un cliente (resuelve la N:M cliente-producto). PK: (id_cliente, id_producto).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_cliente` | INT | n/a | PK, NOT NULL, FK → cliente.id_cliente ON DELETE CASCADE | Cliente que marca |
| `id_producto` | INT | n/a | PK, NOT NULL, FK → producto.id_producto ON DELETE CASCADE | Producto marcado |
| `fecha_agregado` | DATE | n/a | NOT NULL | Fecha en que se marcó |

## `recompensa`

Recompensa canjeable por puntos. PK: (id_recompensa).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_recompensa` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 80 | NOT NULL | Nombre de la recompensa |
| `puntos_requeridos` | INT | n/a | NOT NULL, CHECK (puntos_requeridos > 0) | Puntos necesarios, mayor a 0 |

## `nivel_fidelizacion`

Nivel de fidelización (Espresso, Plata, Oro). PK: (id_nivel).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_nivel` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 30 | NOT NULL, UNIQUE | Nombre del nivel |
| `puntos_minimos` | INT | n/a | NOT NULL, UNIQUE, CHECK (puntos_minimos >= 0) | Puntos mínimos para alcanzarlo, mayor o igual a 0 |

## `transaccion_puntos`

Movimiento de puntos de un cliente. PK: (id_transaccion).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_transaccion` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `id_cliente` | INT | n/a | NOT NULL, FK → cliente.id_cliente ON DELETE RESTRICT | Cliente dueño de los puntos |
| `id_pedido` | INT | n/a | NULL, FK → pedido.id_pedido ON DELETE RESTRICT, CHECK (tipo <> 'abono' OR id_pedido IS NOT NULL) | Pedido que originó el abono |
| `id_recompensa` | INT | n/a | NULL, FK → recompensa.id_recompensa ON DELETE SET NULL | Recompensa canjeada |
| `fecha` | DATETIME | n/a | NOT NULL | Fecha y hora del movimiento |
| `tipo` | VARCHAR | 10 | NOT NULL, CHECK (tipo IN ('abono','canje','bono')), CHECK (tipo <> 'abono' OR id_pedido IS NOT NULL) | abono, canje o bono |
| `puntos` | INT | n/a | NOT NULL, CHECK (puntos <> 0) | Puntos del movimiento, distinto de 0 |
| `motivo` | VARCHAR | 100 | NULL | Descripción |

## `contacto`

Mensaje enviado desde el formulario de contacto. PK: (id_contacto).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_contacto` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `id_municipio` | INT | n/a | NULL, FK → municipio.id_municipio ON DELETE SET NULL | Municipio de origen |
| `nombre` | VARCHAR | 100 | NOT NULL | Quien escribe |
| `empresa_finca` | VARCHAR | 100 | NULL | Empresa o finca |
| `telefono` | VARCHAR | 15 | NULL | Teléfono de contacto |
| `correo` | VARCHAR | 120 | NOT NULL | Correo de respuesta |
| `mensaje` | VARCHAR | 1000 | NOT NULL | Texto del mensaje |
| `fecha_envio` | DATETIME | n/a | NOT NULL | Fecha y hora de envío |

## `intento_login_admin`

Intento de acceso al panel (bloqueo tras 5 fallidos). PK: (id_intento).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_intento` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `id_admin` | INT | n/a | NOT NULL, FK → administrador.id_admin ON DELETE CASCADE | Administrador que intenta entrar |
| `direccion_ip` | VARCHAR | 45 | NOT NULL | Dirección IPv4 o IPv6 |
| `fecha_hora` | DATETIME | n/a | NOT NULL | Fecha y hora del intento |
| `exitoso` | TINYINT | n/a | NOT NULL, CHECK (exitoso IN (0,1)) | 1 si entró, 0 si falló |

## `aliado`

Asociación aliada que se muestra en el inicio. PK: (id_aliado).

| Columna | Tipo | Tamaño | Restricciones | Dominio / regla |
|---|---|---|---|---|
| `id_aliado` | INT | n/a | PK, autoincremental, NOT NULL | Entero positivo autoincremental |
| `nombre` | VARCHAR | 100 | NOT NULL | Nombre del aliado |
| `descripcion` | VARCHAR | 300 | NULL | Descripción corta |
| `logo` | VARCHAR | 255 | NULL | Ruta del logo |
