# B7 · Lista de chequeo diligenciada (aplicada a P1 y P2)

**28 criterios medibles** agrupados por artefacto, con severidad, resultado de la **primera pasada** (sobre mi primer borrador), resultado de la **segunda** (después de corregir) y evidencia. Se aplican a los artefactos de **ambos** productos. Verificador automático: [verificar_consistencia_g2.py](verificacion/verificar_consistencia_g2.py) y [ejecutar_sqlite.py](verificacion/ejecutar_sqlite.py).

| ID | Artefacto | Criterio de aceptación (medible) | Severidad | 1.ª pasada | 2.ª pasada | Evidencia |
|---|---|---|---|---|---|---|
| LC-01 | Clases | Cada clase traza a ≥ 1 requisito de la matriz y cada RF llega a una clase | Mayor | Cumple | Cumple | P1 `07-matriz-de-trazabilidad.md`; verificador (chequeos P1 de matriz) |
| LC-02 | Clases | ≥ 8 clases con atributos tipados, visibilidad y métodos con parámetros | Mayor | Cumple | Cumple | P1 `diagramas/diagrama-clases.mmd` (28 clases) |
| LC-03 | Clases | Toda asociación lleva multiplicidad en los dos extremos | Menor | Cumple | Cumple | Verificador: líneas `-->` y `*--` del diagrama |
| LC-04 | Clases | ≥ 1 composición, ≥ 1 herencia y una interfaz con ≥ 2 implementaciones | Mayor | Cumple | Cumple | `Pedido *-- LineaPedido`; `Usuario <|-- Cliente`; `CalculadoraDespacho` y `Autenticador` |
| LC-05 | Clases | Ninguna clase mezcla interfaz, lógica de negocio, persistencia o notificación | Mayor | Cumple | Cumple | Revisión de las 28 clases: controladores solo delegan, entidades sin SQL, repositorios sin reglas |
| LC-06 | Patrones | ≥ 2 patrones GoF distintos, uno distinto de singleton, visibles en el diagrama | Mayor | Cumple | Cumple | P1 `03-patrones.md` (estrategia, fachada, singleton); verificador |
| LC-07 | Patrones | Cada patrón dice el problema del caso, por qué ese patrón y qué mejora | Menor | Cumple | Cumple | P1 `03-patrones.md`, tabla |
| LC-08 | Arquitectura | Tabla con ≥ 3 RNF, decisión y alternativa descartada con su razón | Mayor | Cumple | Cumple | P1 `04-arquitectura.md` (8 RNF) |
| LC-09 | Arquitectura | La presentación no accede a datos ni a la base directamente (sin capas saltadas) | Crítico | Cumple | Cumple | P1 `diagramas/arquitectura.mmd` y verificador (C1 no depende de C7) |
| LC-10 | Componentes | ≥ 5 componentes con interfaz provista y requerida nombradas | Mayor | Cumple | Cumple | P1 `05-componentes.md` (7 componentes) |
| LC-11 | Componentes | Toda clase pertenece a un componente y los componentes no tienen ciclos | Mayor | Cumple | Cumple | Verificador (clases de la tabla y ciclos del grafo) |
| LC-12 | Despliegue | ≥ 3 nodos con artefactos y protocolo o puerto en cada conexión | Menor | Cumple | Cumple | P1 `06-despliegue.md` (4 nodos) |
| LC-13 | Despliegue | La base de datos no se expone a internet y el `.env` está fuera de la carpeta pública | Crítico | Cumple | Cumple | P1 `06-despliegue.md`, nodos 2 y 3 |
| LC-14 | Modelo de datos | Toda tabla tiene PK y toda relación 1:N tiene su FK | Crítico | Cumple | Cumple | P2 `sql/esquema-mariadb.sql`; verificador |
| LC-15 | Modelo de datos | Las N:M están resueltas con tabla intermedia con atributos propios | Crítico | Cumple | Cumple | `detalle_pedido`, `favorito` |
| LC-16 | Modelo de datos | Sin atributos multivaluados ni dependencias parciales o transitivas (3FN) | Crítico | Cumple | Cumple | P2 `03-normalizacion.md` (2 tablas, 0FN a 3FN) |
| LC-17 | Modelo de datos | Cada entidad conceptual es una tabla y cada tabla viene de una entidad | Mayor | Cumple | Cumple | Verificador (entidades del `.mmd` vs tablas) |
| LC-18 | Modelo de datos | Los atributos de las clases de P1 existen como columnas de P2 | Mayor | **No cumple** (H-02, H-03) | Cumple | Verificador, chequeos P1↔P2 |
| LC-19 | Diccionario | El diccionario coincide con el script en tablas, columnas y tipos (100 %) | Mayor | Cumple | Cumple | Verificador (diccionario vs script) |
| LC-20 | Script | El script ejecuta sin errores, con ≥ 3 CHECK y ≥ 3 ON DELETE | Crítico | Cumple | Cumple | P2 `verificacion/evidencia-ejecucion-2.txt` |
| LC-21 | Script | Cada restricción rechaza el dato inválido **por la razón prevista** | Mayor | **No cumple** (H-01) | Cumple | `evidencia-ejecucion-1.txt`, línea de «borrar pedido» |
| LC-22 | Seguridad | ≥ 2 políticas por cada principio (integridad, confidencialidad, disponibilidad) | Mayor | Cumple | Cumple | P2 `06-politicas-de-seguridad.md` (10 políticas) |
| LC-23 | Seguridad | Contraseñas con hash y sal (no cifradas) y datos en tránsito por TLS | Crítico | Cumple | Cumple | Políticas 4 y 5; `administrador.hash_contrasena` |
| LC-24 | Seguridad | Matriz de ≥ 3 roles contra las tablas con los permisos | Mayor | Cumple | Cumple | P2 `06-politicas-de-seguridad.md`, matriz (3 roles × 15 tablas) |
| LC-25 | Seguridad | Existe una decisión visible para cada RNF de seguridad de la ficha (005, 006, 008) | Mayor | Cumple | Cumple | P1 `04-arquitectura.md`: filas RNF-005, RNF-006 y RNF-008 |
| LC-26 | Seguridad | Datos personales con finalidad y autorización previa (Ley 1581) | Mayor | Cumple | Cumple | Política 6; RNF-016 |
| LC-27 | Trazabilidad | La matriz cubre el 100 % de los RF del subconjunto (17 de 17) | Mayor | Cumple | Cumple | P1 `07-matriz-de-trazabilidad.md`; verificador |
| LC-28 | Herramienta | El verificador no produce falsos positivos (cada falla se confirma a mano) | Menor | **No cumple** (H-04) | Cumple | `resultado-verificacion-1.txt`, primera falla |

Resumen: primera pasada 25 de 28 criterios cumplen y 3 no; segunda pasada, 28 de 28. Resultados del verificador: [primera](verificacion/resultado-verificacion-1.txt) (33 correctos, 5 fallas) y [segunda](verificacion/resultado-verificacion-2.txt) (37 correctos, 0 fallas), y de las pruebas SQL: [primera](verificacion/evidencia-ejecucion-1.txt) (1 falla) y [segunda](verificacion/evidencia-ejecucion-2.txt) (0 fallas).

## Registro de hallazgos y ajustes

| ID | Artefacto | Hallazgo | Requisito afectado | Severidad | Corrección | Verificado |
|---|---|---|---|---|---|---|
| H-01 | Script SQL (P2) | `fk_tp_pedido` tenía `ON DELETE SET NULL`, pero `ck_tp_abono_pedido` exige que un abono tenga pedido: al borrar un pedido el motor lo rechazaba por el CHECK y no por la llave, y la regla de conservar el historial quedaba mal expresada. Lo mostró el log al exigir la razón del rechazo | RF-038, RNF-017 | Mayor | `ON DELETE RESTRICT` en `fk_tp_pedido`: un pedido con puntos no se puede borrar | `evidencia-ejecucion-2.txt`: «rechazado por FOREIGN KEY» |
| H-02 | Modelo de datos (P2) y clases (P1) | La clase abstracta `Usuario` tiene `correo`, pero la tabla `administrador` no tenía esa columna (tampoco el MER de G1) | RF-025 | Mayor | Columna `administrador.correo` (NOT NULL, UNIQUE) en esquema, diccionario, modelo lógico y conceptual | Verificador: P1↔P2 cumple |
| H-03 | Clases (P1) | `DireccionEntrega.municipio` era un texto, pero en la base la dirección apunta a `municipio` por llave | RF-017 | Menor | Atributo `-idMunicipio: int` en la clase | Verificador: P1↔P2 cumple |
| H-04 | Verificador | El primer verificador contaba la fila de encabezado de la tabla de componentes como si fuera un componente y daba una falla falsa | — | Menor | Se filtraron las filas con `C<número>` | Segunda pasada sin falla falsa |
