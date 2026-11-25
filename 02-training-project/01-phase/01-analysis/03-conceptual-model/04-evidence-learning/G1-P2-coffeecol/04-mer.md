# 4. Modelo entidad-relación

**Notación declarada: pata de gallo** (crow's foot). Fuente editable: [mer-pata-de-gallo.mmd](diagramas/mer-pata-de-gallo.mmd) · Imagen: [png](diagramas/mer-pata-de-gallo.png) · [svg](diagramas/mer-pata-de-gallo.svg)

Lectura de símbolos: `||` exactamente uno (participación total), `o|` cero o uno (parcial), `|{` uno o más (total), `o{` cero o más (parcial).

- **15 entidades** con identificador (PK): CLIENTE, ADMINISTRADOR, DIRECCION_ENTREGA, MUNICIPIO, CATEGORIA, PRODUCTO, PEDIDO, DETALLE_PEDIDO, FAVORITO, TRANSACCION_PUNTOS, RECOMPENSA, NIVEL_FIDELIZACION, CONTACTO, INTENTO_LOGIN_ADMIN, ALIADO.
- **Relaciones N:M resueltas con entidad asociativa con atributos propios:**
  - PEDIDO ↔ PRODUCTO → DETALLE_PEDIDO (cantidad, precio_unitario)
  - CLIENTE ↔ PRODUCTO → FAVORITO (fecha_agregado)
- **Entidad débil:** DIRECCION_ENTREGA se identifica por (id_cliente, consecutivo); no existe sin su cliente. PEDIDO la referencia con la llave compuesta (id_cliente, consecutivo_direccion).
- **Cardinalidad y participación:** cada pedido tiene 1 o más líneas (`||--|{`, total); una transacción de puntos tiene 0 o 1 pedido y 0 o 1 recompensa (`|o--o{`, parcial).
- **Usuarios:** la generalización Usuario → Cliente/Administrador del dominio se resuelve con dos entidades separadas, porque los clientes entran con Firebase (sin contraseña propia) y el administrador con usuario y clave cifrada (RF-025).
- **Soporte a requisitos de datos:** `hash_contrasena` (RND-003, nunca en texto plano), `INTENTO_LOGIN_ADMIN` (RF-026), `TRANSACCION_PUNTOS` (RF-040), `NIVEL_FIDELIZACION` (RF-038; el nivel de cada cliente se calcula comparando sus puntos con el mínimo de cada nivel, por eso no hay relación directa), `fecha` de PEDIDO (conservación y comprobante, RNF-017).
- **Sin entidad:** `Carrito` e `ItemCarrito` (el SRS lo guarda en el navegador, RF-013); se materializan en DETALLE_PEDIDO al confirmar.

## Correspondencia dominio → MER

| Clase de dominio | Entidad |
|---|---|
| Usuario, Cliente | CLIENTE |
| Administrador | ADMINISTRADOR |
| Producto · Categoria · Municipio | PRODUCTO · CATEGORIA · MUNICIPIO |
| Carrito · ItemCarrito | (ninguna: vive en el navegador) |
| Pedido · LineaPedido | PEDIDO · DETALLE_PEDIDO |
| Favorito | FAVORITO |
| DireccionEntrega | DIRECCION_ENTREGA |
| NivelFidelizacion · Recompensa · TransaccionPuntos | NIVEL_FIDELIZACION · RECOMPENSA · TRANSACCION_PUNTOS |
| MensajeContacto | CONTACTO |
| IntentoAcceso | INTENTO_LOGIN_ADMIN |
| Aliado | ALIADO |
