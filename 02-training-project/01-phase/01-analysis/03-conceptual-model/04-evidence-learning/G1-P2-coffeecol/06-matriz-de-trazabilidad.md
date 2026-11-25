# 6. Matriz de trazabilidad (Anexo C)

Requisito → caso de uso → diagrama de actividades → plantilla → clase de dominio → entidad del MER → pantalla (la pantalla se exige solo para los casos críticos: CU-03, CU-06 y CU-11).

| Requisito | Caso de uso | Diagrama de actividades | Plantilla | Clase de dominio | Entidad del MER | Pantalla |
|---|---|---|---|---|---|---|
| RF-001 | CU-15 | — | — | — | — | — |
| RF-002 | CU-01 | — | — | Municipio | MUNICIPIO | — |
| RF-003 | CU-15 | — | — | — | — | — |
| RF-004 | CU-15 | — | — | Aliado | ALIADO | — |
| RF-005 | CU-15 | — | — | — | — | — |
| RF-006 | CU-02 | — | — | Producto, Categoria | PRODUCTO, CATEGORIA | — |
| RF-007 | CU-02 | — | — | Producto, Categoria | PRODUCTO, CATEGORIA | — |
| RF-008 | CU-02, CU-16 | — | — | Producto | PRODUCTO | — |
| RF-009 | CU-02 | — | — | — | — | — |
| RF-010 | CU-02 | — | — | — | — | — |
| RF-011 | CU-05 | — | — | Carrito, ItemCarrito, Producto | PRODUCTO | — |
| RF-012 | CU-05 | — | — | Carrito, ItemCarrito | PRODUCTO | — |
| RF-013 | CU-05 | — | — | Carrito, ItemCarrito | DETALLE_PEDIDO | — |
| RF-014 | CU-05 | — | — | Carrito, ItemCarrito, Producto | PRODUCTO | — |
| RF-015 | CU-05 | — | — | Carrito, ItemCarrito | DETALLE_PEDIDO | — |
| RF-016 | CU-05 | — | — | Carrito, Producto | PRODUCTO | — |
| RF-017 | CU-06 | actividad-realizar-checkout | CU-06 | DireccionEntrega, Cliente, Municipio | DIRECCION_ENTREGA, CLIENTE, MUNICIPIO | Pantalla 1 |
| RF-018 | CU-19 | actividad-realizar-checkout | CU-06 | DireccionEntrega | DIRECCION_ENTREGA | Pantalla 1 |
| RF-019 | CU-06 | actividad-realizar-checkout | CU-06 | Pedido, LineaPedido | PEDIDO, DETALLE_PEDIDO | Pantalla 1 |
| RF-020 | CU-06 | actividad-realizar-checkout | CU-06 | Pedido, LineaPedido | PEDIDO, DETALLE_PEDIDO | Pantalla 1 |
| RF-021 | CU-06 | actividad-realizar-checkout | CU-06 | Pedido, Carrito | PEDIDO | Pantalla 1 |
| RF-022 | CU-12 | — | — | Pedido | PEDIDO | — |
| RF-023 | CU-03 | actividad-iniciar-sesion | CU-03 | Usuario, Cliente | CLIENTE | Pantalla 2 |
| RF-024 | CU-03 | actividad-iniciar-sesion | CU-03 | Usuario, Cliente | CLIENTE | Pantalla 2 |
| RF-025 | CU-10 | — | — | Administrador | ADMINISTRADOR | — |
| RF-026 | CU-24, CU-10 | — | — | IntentoAcceso, Administrador | INTENTO_LOGIN_ADMIN, ADMINISTRADOR | — |
| RF-027 | CU-17 | actividad-iniciar-sesion | CU-03 | Usuario, Cliente | CLIENTE | Pantalla 2 |
| RF-028 | CU-03, CU-10 | actividad-iniciar-sesion | CU-03 | Usuario, Cliente, Administrador | CLIENTE, ADMINISTRADOR | Pantalla 2 |
| RF-029 | CU-18 | — | — | Cliente, Administrador | CLIENTE, ADMINISTRADOR | — |
| RF-030 | CU-07 | — | — | Cliente, NivelFidelizacion | CLIENTE, NIVEL_FIDELIZACION | — |
| RF-031 | CU-07 | — | — | Cliente, Pedido, Favorito, DireccionEntrega | CLIENTE, PEDIDO, FAVORITO, DIRECCION_ENTREGA | — |
| RF-032 | CU-21 | — | — | Pedido, LineaPedido | PEDIDO, DETALLE_PEDIDO | — |
| RF-033 | CU-07 | — | — | DireccionEntrega | DIRECCION_ENTREGA | — |
| RF-034 | CU-07 | — | — | Cliente | CLIENTE | — |
| RF-035 | CU-08 | — | — | Favorito, Producto | FAVORITO | — |
| RF-036 | CU-08 | — | — | Favorito | FAVORITO | — |
| RF-037 | CU-08 | — | — | Favorito, Producto | FAVORITO, PRODUCTO | — |
| RF-038 | CU-09, CU-20 | — | — | Cliente, NivelFidelizacion, TransaccionPuntos | CLIENTE, NIVEL_FIDELIZACION, TRANSACCION_PUNTOS | — |
| RF-039 | CU-23 | — | — | Cliente, TransaccionPuntos | CLIENTE, TRANSACCION_PUNTOS | — |
| RF-040 | CU-09 | — | — | TransaccionPuntos | TRANSACCION_PUNTOS | — |
| RF-041 | CU-22 | — | — | Recompensa, TransaccionPuntos | RECOMPENSA, TRANSACCION_PUNTOS | — |
| RF-042 | CU-09 | — | — | NivelFidelizacion, Cliente | NIVEL_FIDELIZACION, CLIENTE | — |
| RF-043 | CU-04 | — | — | MensajeContacto, Municipio | CONTACTO, MUNICIPIO | — |
| RF-044 | CU-04 | — | — | MensajeContacto | CONTACTO | — |
| RF-045 | CU-11, CU-25, CU-26 | — | CU-11 | Producto, Categoria | PRODUCTO, CATEGORIA | Pantalla 3 |
| RF-046 | CU-11 | — | CU-11 | Producto | PRODUCTO | Pantalla 3 |
| RF-047 | CU-11 | — | CU-11 | Producto, Categoria | PRODUCTO, CATEGORIA | Pantalla 3 |
| RF-048 | CU-12 | — | — | Pedido, LineaPedido, Cliente | PEDIDO, DETALLE_PEDIDO, CLIENTE | — |
| RF-049 | CU-12 | — | — | Pedido | PEDIDO | — |
| RF-050 | CU-13 | — | — | Cliente, Pedido | CLIENTE, PEDIDO | — |
| RF-051 | CU-14 | — | — | Pedido, LineaPedido, Producto | PEDIDO, DETALLE_PEDIDO, PRODUCTO | — |
| RF-052 | CU-14 | — | — | Pedido, LineaPedido, Producto, Categoria | PEDIDO, DETALLE_PEDIDO, PRODUCTO, CATEGORIA | — |
| RF-053 | CU-14 | — | — | Pedido | PEDIDO | — |
| RF-054 | CU-27 | — | — | Pedido | PEDIDO | — |

**Cobertura hasta clase y entidad: 49 de 54 requisitos funcionales (90.7 %).** Sin clase ni entidad quedan 5 requisitos, todos de prioridad baja y de presentación, que no manejan datos del negocio: RF-001 (intro animada), RF-003 (contenido informativo), RF-005 (modal promocional por sesión), RF-009 (animaciones al desplazarse) y RF-010 (indicadores de carga).

**Nota sobre el carrito:** las clases `Carrito` e `ItemCarrito` son conceptos del negocio, pero el SRS (RF-013) conserva el carrito en el navegador y no en la base de datos; por eso no tienen entidad propia en el MER y se materializan en `DETALLE_PEDIDO` cuando el cliente confirma el pedido. Los requisitos del carrito se trazan a esa entidad o a `PRODUCTO`.

Ninguna clase de dominio queda sin requisito (Usuario se traza a los requisitos de acceso, RF-023, RF-024, RF-027 y RF-028).
