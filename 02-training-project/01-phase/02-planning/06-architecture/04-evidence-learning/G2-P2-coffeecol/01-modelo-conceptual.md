# B1 · Modelo conceptual

Notación: **pata de gallo** (ER). Fuente editable: [modelo-conceptual.mmd](diagramas/modelo-conceptual.mmd) · Imagen: [png](diagramas/modelo-conceptual.png) · [svg](diagramas/modelo-conceptual.svg)

**Tipo de base de datos: relacional.** Los pedidos exigen consistencia (RNF-009), las relaciones cliente–pedido–producto son fijas y el SRS exige MariaDB en 3FN. Una base documental duplicaría precios y direcciones dentro de cada pedido sin garantizar integridad entre ellos.

**Origen y ajuste.** Parto del MER que hice en G1-P2 (15 entidades) y lo ajusto al motor relacional: agregué el `correo` del administrador (lo exige la clase `Usuario` del diseño de G2-P1) y cada relación lleva verbo y cardinalidad mínima y máxima en la tabla de abajo. Cada entidad traza a requisitos del SRS.

## Relaciones con verbo y cardinalidad (mín, máx)

| Relación | Entidad A (mín, máx) | Verbo | Entidad B (mín, máx) | Tipo |
|---|---|---|---|---|
| CLIENTE – DIRECCION_ENTREGA | (1, 1) | guarda | (0, N) | 1:N |
| CLIENTE – PEDIDO | (1, 1) | realiza | (0, N) | 1:N |
| PEDIDO – PRODUCTO | (1, N) | contiene (DETALLE_PEDIDO) | (0, N) | **N:M** |
| CLIENTE – PRODUCTO | (0, N) | marca (FAVORITO) | (0, N) | **N:M** |
| CATEGORIA – PRODUCTO | (0, N) | clasifica | (1, 1) | 1:N |
| MUNICIPIO – DIRECCION_ENTREGA | (0, N) | ubica | (1, 1) | 1:N |
| DIRECCION_ENTREGA – PEDIDO | (0, N) | recibe | (1, 1) | 1:N |
| CLIENTE – TRANSACCION_PUNTOS | (0, N) | acumula | (1, 1) | 1:N |
| PEDIDO – TRANSACCION_PUNTOS | (0, 1) | genera | (0, N) | 1:N opcional |
| RECOMPENSA – TRANSACCION_PUNTOS | (0, 1) | se canjea en | (0, N) | 1:N opcional |
| ADMINISTRADOR – INTENTO_LOGIN_ADMIN | (1, 1) | recibe | (0, N) | 1:N |
| MUNICIPIO – CONTACTO | (0, 1) | origina | (0, N) | 1:N opcional |

`DIRECCION_ENTREGA` es entidad débil: su identificador es (id_cliente, consecutivo). Las dos N:M se resuelven con las entidades asociativas `DETALLE_PEDIDO` (cantidad, precio_unitario) y `FAVORITO` (fecha_agregado).

## Trazabilidad de las entidades

| Entidad | Requisitos del SRS |
|---|---|
| ADMINISTRADOR | RF-025, RF-026, RF-028, RF-029 |
| ALIADO | RF-004 |
| CATEGORIA | RF-006, RF-007, RF-045, RF-047 … |
| CLIENTE | RF-017, RF-023, RF-024, RF-027 … |
| CONTACTO | RF-043, RF-044 |
| DETALLE_PEDIDO | RF-013, RF-015, RF-019, RF-020 … |
| DIRECCION_ENTREGA | RF-017, RF-018, RF-031, RF-033 |
| FAVORITO | RF-031, RF-035, RF-036, RF-037 |
| INTENTO_LOGIN_ADMIN | RF-026 |
| MUNICIPIO | RF-002, RF-017, RF-043 |
| NIVEL_FIDELIZACION | RF-030, RF-038, RF-042 |
| PEDIDO | RF-019, RF-020, RF-021, RF-022 … |
| PRODUCTO | RF-006, RF-007, RF-008, RF-011 … |
| RECOMPENSA | RF-041 |
| TRANSACCION_PUNTOS | RF-038, RF-039, RF-040, RF-041 |
