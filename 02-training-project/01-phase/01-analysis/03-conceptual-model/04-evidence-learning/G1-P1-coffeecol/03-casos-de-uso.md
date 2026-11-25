# 3. Casos de uso y justificación de relaciones

Diagrama: [`diagramas/casos-de-uso.png`](diagramas/casos-de-uso.png) · fuente editable: [`diagramas/casos-de-uso.dot`](diagramas/casos-de-uso.dot) (también [`.svg`](diagramas/casos-de-uso.svg)). Se regenera con `dot -Tpng -Gdpi=95 casos-de-uso.dot -o casos-de-uso.png`.

## 3.1 Actores

- **Primarios:** Visitante, Cliente registrado, Administrador.
- **Secundario:** Firebase Authentication (sistema externo que valida la identidad; solo recibe información y no inicia casos).
- **Iniciador de proceso automático:** Temporizador del sistema, que dispara el bono de cumpleaños (CU-23).
- **Generalización:** Cliente registrado **es un** Visitante (hereda catálogo, mapa, carrito, contacto e información de la marca).

## 3.2 Origen: qué tomé del SRS y qué agregué

El Apéndice B del SRS define 14 casos de uso (CU-01 a CU-14). Conservé esa numeración. Al cruzarlos con los 54 requisitos, **varios requisitos no tenían caso** (RF-001, 003, 004, 005, 029, 032, 039 y, dentro de «Consultar/Canjear Puntos», la parte de canje) y el SRS no modela ninguna relación «include» ni «extend». Por eso agregué CU-15 a CU-27. El SRS traza en su Apéndice C solo 18 de los 54 requisitos; esta matriz traza los 54.

## 3.3 Lista de casos de uso (verbo + objeto, un objetivo por caso)

| Caso de uso | Origen | Actor que lo inicia | Objetivo | Requisitos |
|---|---|---|---|---|
| CU-01 | SRS | Visitante | Ver el origen cafetero en el mapa del Huila | RF-002 |
| CU-02 | SRS | Visitante / Cliente | Explorar y filtrar el catálogo por categoría | RF-006, RF-007, RF-008, RF-009, RF-010 |
| CU-03 | SRS | Visitante (cliente que entra) | Acceder con Google o enlace mágico | RF-023, RF-024, RF-028 |
| CU-04 | SRS | Visitante / Caficultor | Enviar un mensaje a la empresa | RF-043, RF-044 |
| CU-05 | SRS | Visitante / Cliente | Agregar, quitar y cambiar cantidades del carrito y ver el total | RF-011, RF-012, RF-013, RF-014, RF-015, RF-016 |
| CU-06 | SRS | Cliente registrado | Confirmar la compra y obtener el número de pedido | RF-017, RF-019, RF-020, RF-021 |
| CU-07 | SRS | Cliente registrado | Ver su perfil y administrar direcciones y cumpleaños | RF-030, RF-031, RF-033, RF-034 |
| CU-08 | SRS | Cliente registrado | Marcar y consultar productos favoritos | RF-035, RF-036, RF-037 |
| CU-09 | SRS (parte «consultar» de «Consultar/Canjear Puntos») | Cliente registrado | Ver puntos, nivel y bitácora de puntos | RF-038, RF-040, RF-042 |
| CU-10 | SRS | Administrador | Acceder al panel con usuario y clave | RF-025, RF-026, RF-028 |
| CU-11 | SRS | Administrador | Mantener actualizado el catálogo de productos | RF-045, RF-046, RF-047 |
| CU-12 | SRS | Administrador | Consultar pedidos y cambiar su estado | RF-022, RF-048, RF-049 |
| CU-13 | SRS | Administrador | Consultar clientes, su historial y sus puntos | RF-050 |
| CU-14 | SRS | Administrador | Ver KPIs y gráficos por rango de fechas | RF-051, RF-052, RF-053 |
| CU-15 | Agregado (RF-001, 003, 004, 005 no tenían caso) | Visitante | Conocer la marca: bienvenida, historia, aliados y promoción | RF-001, RF-003, RF-004, RF-005 |
| CU-16 | Agregado (extiende CU-02) | (extiende CU-02) | Ver el detalle de un producto | RF-008 |
| CU-17 | Agregado (incluido en CU-03) | (incluido en CU-03) | Registrar o actualizar al usuario tras acceder | RF-027 |
| CU-18 | Agregado (RF-029 no tenía caso) | Cliente / Administrador | Cerrar la sesión de forma segura | RF-029 |
| CU-19 | Agregado (incluido en CU-06) | (incluido en CU-06) | Validar los datos de entrega | RF-018 |
| CU-20 | Agregado (incluido en CU-06) | (incluido en CU-06) | Acreditar los puntos de la compra | RF-038 |
| CU-21 | Agregado (RF-032 no tenía caso) | Cliente registrado | Consultar el historial de pedidos y su estado | RF-032 |
| CU-22 | SRS (parte «canjear»; extiende CU-09) | (extiende CU-09) | Canjear puntos por una recompensa | RF-041 |
| CU-23 | Agregado (RF-039 es automático) | Temporizador del sistema | Acreditar el bono anual de cumpleaños | RF-039 |
| CU-24 | Agregado (incluido en CU-10) | (incluido en CU-10) | Controlar los intentos fallidos de acceso | RF-026 |
| CU-25 | Agregado (extiende CU-11) | (extiende CU-11) | Cargar o reemplazar la imagen de un producto | RF-045 |
| CU-26 | Agregado (incluido en CU-25) | (incluido en CU-25) | Validar tipo y extensión de la imagen | RF-045 |
| CU-27 | Agregado (extiende CU-14) | (extiende CU-14) | Exportar el reporte a CSV o imprimirlo en PDF | RF-054 |

Decisión sobre CRUD (regla 1 de arbitraje): «Gestionar carrito», «Gestionar productos», «Administrar perfil y direcciones» y «Gestionar favoritos» agrupan sus operaciones y no se fragmentan en crear, leer, actualizar y eliminar, porque no hay actor ni reglas distintas por operación.

## 3.4 Justificación de cada relación

**«include» (lo que siempre ocurre dentro del caso base; la flecha va del base al incluido):**

| Relación | Justificación en una línea |
|---|---|
| CU-03 Iniciar sesión con Firebase → CU-17 Sincronizar usuario | Tras todo acceso exitoso el sistema registra o actualiza al usuario; nunca se omite (RF-027). |
| CU-06 Realizar checkout → CU-19 Validar datos de entrega | Todo pedido valida correo, teléfono y campos obligatorios antes de enviarse (RF-018). |
| CU-06 Realizar checkout → CU-20 Acumular puntos por compra | Todo pedido confirmado acredita puntos en la misma operación (RF-038). |
| CU-10 Iniciar sesión de administrador → CU-24 Controlar intentos de acceso | En cada intento se revisa el límite de fallos antes de autenticar (RF-026). |
| CU-25 Cargar imagen de producto → CU-26 Validar archivo de imagen | Toda imagen cargada se valida por tipo y extensión antes de guardarse. |

**«extend» (lo opcional o condicional; la flecha va del que extiende al base; con punto de extensión):**

| Relación | Punto de extensión | Justificación en una línea |
|---|---|---|
| CU-16 Ver detalle de producto → CU-02 Explorar catálogo | «seleccionar producto» | Solo ocurre si el visitante abre un producto; explorar el catálogo se completa sin abrir detalles. |
| CU-22 Canjear recompensa → CU-09 Consultar puntos y nivel | «elegir recompensa» | Solo ocurre si el cliente decide canjear y le alcanzan los puntos; consultar puntos no obliga a canjear. |
| CU-25 Cargar imagen de producto → CU-11 Gestionar productos | «adjuntar imagen» | Solo ocurre cuando el administrador carga o reemplaza una imagen (por ejemplo, al editar solo el precio no se toca). Si el equipo exige imagen en toda alta, esa parte sería «include». |
| CU-27 Exportar reporte → CU-14 Consultar KPIs y analítica | «exportar reporte» | Solo ocurre si el administrador pide el archivo; ver los indicadores no lo requiere. |

**Generalización:** Cliente registrado → Visitante. El cliente hace todo lo del visitante más sus casos propios, por eso no se repiten las asociaciones de CU-01, CU-02, CU-04, CU-05 y CU-15 para él.

## 3.5 Autocontrol de notación

- 27 casos de uso, todos con verbo más objeto y un solo objetivo.
- Frontera del sistema dibujada; los 5 actores están fuera de ella.
- 5 «include», 4 «extend» y 1 generalización, todos justificados; sin ciclos ni casos duplicados.
- Todo caso tiene iniciador: un actor, o un caso base que lo incluye o lo extiende (regla 6). Firebase solo recibe información y no se cuenta como iniciador; CU-23 lo inicia el Temporizador.
