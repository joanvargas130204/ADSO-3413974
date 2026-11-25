# B3 · Evidencia de normalización (0FN → 3FN)

Se normalizan dos tablas de mi propio modelo: **`pedido_comprobante`** (llave compuesta: dependencia parcial) y **`transaccion_puntos_amplia`** (dependencia transitiva). Notación de dependencias: `A → B` significa que A determina B.

## Tabla 1 · `pedido_comprobante` (llave compuesta)

**0FN.** Así se vería el comprobante de compra que exige el SRS (RNF-017) copiado a una sola tabla:

`pedido_comprobante(id_pedido, codigo, fecha, id_cliente, nombre_cliente, correo_cliente, direccion, id_municipio, nombre_municipio, subtotal, valor_despacho, total, productos)`

con `productos` = lista de `(id_producto, nombre_producto, id_categoria, nombre_categoria, cantidad, precio_unitario)` repetida dentro de la misma fila.

| id_pedido | codigo | id_cliente | nombre_cliente | id_municipio | nombre_municipio | productos |
|---|---|---|---|---|---|---|
| 1 | CC-0001 | 1 | Ana Pérez | 1 | Pitalito | (1, Café 500 g, 1, Tueste medio, 2, 45000) ; (2, Cápsulas, 2, Cápsulas, 1, 38000) |

**1FN (valores atómicos, sin grupos repetidos).** Violación: `productos` guarda varios productos en una celda. Se separa en una fila por producto; la llave pasa a ser **(id_pedido, id_producto)**.

| id_pedido | id_producto | codigo | id_cliente | nombre_cliente | id_municipio | nombre_municipio | nombre_producto | id_categoria | nombre_categoria | cantidad | precio_unitario |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | CC-0001 | 1 | Ana Pérez | 1 | Pitalito | Café 500 g | 1 | Tueste medio | 2 | 45000 |
| 1 | 2 | CC-0001 | 1 | Ana Pérez | 1 | Pitalito | Cápsulas | 2 | Cápsulas | 1 | 38000 |

Dependencias funcionales escritas:
- `id_pedido → codigo, fecha, id_cliente, nombre_cliente, correo_cliente, direccion, id_municipio, nombre_municipio, subtotal, valor_despacho, total` (depende solo de una parte de la llave)
- `id_producto → nombre_producto, id_categoria, nombre_categoria` (depende solo de la otra parte)
- `(id_pedido, id_producto) → cantidad, precio_unitario` (depende de la llave completa)

**2FN (sin dependencias parciales).** Violación: los datos del pedido se repiten por cada producto y los del producto por cada pedido (anomalía: cambiar el nombre de un producto exige tocar muchas filas). Se separan:

- `pedido(id_pedido, codigo, fecha, id_cliente, nombre_cliente, correo_cliente, direccion, id_municipio, nombre_municipio, subtotal, valor_despacho, total)`
- `producto(id_producto, nombre_producto, id_categoria, nombre_categoria)`
- `detalle_pedido(id_pedido, id_producto, cantidad, precio_unitario)` (PK compuesta)

**3FN (sin dependencias transitivas).** Violaciones que quedan en 2FN:
- `id_pedido → id_cliente → nombre_cliente, correo_cliente`
- `id_pedido → id_municipio → nombre_municipio`
- `id_producto → id_categoria → nombre_categoria`

Se separan `cliente`, `municipio` y `categoria`, y la dirección se vuelve entidad débil. **Resultado final** (tablas del modelo lógico): `pedido`, `detalle_pedido`, `producto`, `categoria`, `cliente`, `direccion_entrega`, `municipio`.

## Tabla 2 · `transaccion_puntos_amplia` (dependencia transitiva)

**0FN.** Un reporte de puntos pegado en una sola tabla:

`transaccion_puntos_amplia(id_transaccion, fecha, tipo, puntos, id_cliente, nombre_cliente, puntos_acumulados, nivel, id_recompensa, nombre_recompensa, puntos_requeridos)`

| id_transaccion | tipo | puntos | id_cliente | nombre_cliente | puntos_acumulados | nivel | id_recompensa | nombre_recompensa | puntos_requeridos |
|---|---|---|---|---|---|---|---|---|---|
| 7 | canje | -300 | 1 | Ana Pérez | 620 | Plata | 3 | Bolsa de 250 g | 300 |

**1FN.** Todos los valores ya son atómicos y no hay grupos repetidos; la llave es `id_transaccion`.

**2FN.** La llave es de una sola columna: no puede haber dependencias parciales. Se cumple.

**3FN.** Dependencias funcionales:
- `id_transaccion → id_cliente` y `id_cliente → nombre_cliente, puntos_acumulados` (transitiva)
- `id_cliente → puntos_acumulados → nivel` (transitiva; además `nivel` es derivable de los puntos)
- `id_transaccion → id_recompensa` y `id_recompensa → nombre_recompensa, puntos_requeridos` (transitiva)

Se separan `cliente(id_cliente, nombre, puntos_acumulados)` y `recompensa(id_recompensa, nombre, puntos_requeridos)`; `nivel` **no se guarda**: se calcula comparando `puntos_acumulados` con `nivel_fidelizacion.puntos_minimos`. **Resultado final:** `transaccion_puntos(id_transaccion, id_cliente FK, id_pedido FK, id_recompensa FK, fecha, tipo, puntos, motivo)`.

## Estado final y decisiones de desnormalización

El modelo final no tiene dependencias parciales ni transitivas entre atributos no llave. Tres decisiones se apartan de la forma pura a propósito:

| Dónde | Qué se guarda de más | Por qué se acepta |
|---|---|---|
| `detalle_pedido.precio_unitario` | Precio vigente al comprar | El precio del producto cambia; el comprobante debe conservar el pactado (RNF-017) |
| `pedido.subtotal`, `valor_despacho`, `total` | Valores calculables desde las líneas | El comprobante debe ser fiel aunque cambie la política de despacho; el `CHECK ck_pedido_total` evita incoherencias |
| `cliente.puntos_acumulados` | Suma de `transaccion_puntos` | Evita sumar el historial en cada consulta; se actualiza dentro de la misma transacción del pedido (RNF-009) |

`producto.notas_aromaticas` guarda un texto descriptivo («chocolate, panela, cítrico»). Se trata como un atributo único porque solo se muestra y nunca se consulta por nota; si el negocio quisiera filtrar por nota, pasaría a una tabla aparte (1FN estricta).
