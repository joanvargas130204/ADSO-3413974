# B5 · Script SQL de creación y evidencia de ejecución

| Archivo | Para qué |
|---|---|
| [sql/esquema-mariadb.sql](sql/esquema-mariadb.sql) | Script para MariaDB 10.4 / MySQL (el motor del SRS, XAMPP) |
| [sql/esquema-sqlite.sql](sql/esquema-sqlite.sql) | El mismo esquema para SQLite, con el que se ejecutó la evidencia |
| [verificacion/ejecutar_sqlite.py](verificacion/ejecutar_sqlite.py) | Ejecuta el script y prueba las restricciones |
| [verificacion/evidencia-ejecucion-1.txt](verificacion/evidencia-ejecucion-1.txt) · [evidencia-ejecucion-2.txt](verificacion/evidencia-ejecucion-2.txt) | Log de la primera y de la segunda ejecución |

Contenido: **15 tablas**, PK en todas, 14 FK con `ON DELETE` declarado (5 CASCADE, 7 RESTRICT y 2 SET NULL) y `ON UPDATE CASCADE`, `NOT NULL` y `UNIQUE` donde corresponde y 20 `CHECK`.

**Qué se ejecutó y en qué motor (dicho con honestidad).** La evidencia se obtuvo en **SQLite 3.53** con `PRAGMA foreign_keys = ON`: el script crea las 15 tablas sin errores y el programa de pruebas inserta datos válidos y comprueba que el motor rechaza, por la razón prevista, 16 violaciones (precio no positivo, correo repetido, total incoherente, FK inexistente, borrado restringido, etc.) y que `CASCADE` borra direcciones y favoritos del cliente. El script de MariaDB es el mismo modelo generado de la misma definición; solo difiere en `AUTO_INCREMENT` y `ENGINE=InnoDB`. **No se ejecutó aquí en MariaDB**; el paso de ejecutarlo en XAMPP y capturar pantalla queda para el autor.

La primera ejecución dio **1 falla** y la segunda **0 fallas** (ver [hallazgo H-01](07-lista-de-chequeo.md)).
