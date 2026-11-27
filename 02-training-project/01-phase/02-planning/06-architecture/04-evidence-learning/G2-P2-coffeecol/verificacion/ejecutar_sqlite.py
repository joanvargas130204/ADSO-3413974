# -*- coding: utf-8 -*-
"""Ejecuta sql/esquema-sqlite.sql en un motor real (SQLite) y prueba las restricciones. Uso: python3 verificacion/ejecutar_sqlite.py"""
import sqlite3, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = sqlite3.connect(":memory:"); db.execute("PRAGMA foreign_keys = ON")
print("Motor: SQLite", sqlite3.sqlite_version)
fallas = 0
try:
    db.executescript(open(os.path.join(R, "sql", "esquema-sqlite.sql"), encoding="utf8").read())
    n = db.execute("SELECT count(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
    print(f"[OK] Script ejecutado sin errores: {n} tablas creadas")
except Exception as e:
    print("[FALLA] El script no ejecuta:", e); sys.exit(1)
def ok(msg, sql, params=()):
    global fallas
    try: db.execute(sql, params); print("[OK]", msg)
    except Exception as e: fallas += 1; print("[FALLA]", msg, "->", e)
def rechaza(msg, sql, esperado):
    """La sentencia debe rechazarse POR LA RAZÓN prevista (CHECK, UNIQUE o FOREIGN KEY), no por otra."""
    global fallas
    try: db.execute(sql); fallas += 1; print("[FALLA] debía rechazarse:", msg)
    except sqlite3.IntegrityError as e:
        if esperado in str(e): print("[OK] rechazado por", esperado + ":", msg, "->", e)
        else: fallas += 1; print(f"[FALLA] rechazado por motivo distinto (esperaba {esperado}): {msg} -> {e}")
# datos válidos
for s in ["INSERT INTO categoria VALUES (1,'Tueste medio')","INSERT INTO municipio VALUES (1,'Pitalito',1300,'Panela y cacao')",
 "INSERT INTO cliente VALUES (1,'uidA','Ana Pérez','ana@correo.com','2026-11-01',NULL,0)",
 "INSERT INTO administrador VALUES (1,'admin','Administrador','admin@tantico.co','$2y$12$hashdeejemplo')",
 "INSERT INTO producto VALUES (1,'Café 500 g','Tueste medio',NULL,45000,NULL,40,NULL,4.5,'activo',1)",
 "INSERT INTO direccion_entrega VALUES (1,1,1,'Ana Pérez','Calle 5 # 3-20','3001234567')",
 "INSERT INTO pedido VALUES (1,'CC-0001','2026-11-25 10:00:00','pendiente',90000,12000,102000,1,1)",
 "INSERT INTO detalle_pedido VALUES (1,1,2,45000)",
 "INSERT INTO transaccion_puntos VALUES (1,1,1,NULL,'2026-11-25 10:00:01','abono',102,'Compra CC-0001')",
 "INSERT INTO favorito VALUES (1,1,'2026-11-25')"]:
    ok("dato válido: " + s[:45], s)
# violaciones
rechaza("precio <= 0", "INSERT INTO producto VALUES (2,'X',NULL,NULL,0,NULL,1,NULL,NULL,'activo',1)", "CHECK")
rechaza("stock negativo", "INSERT INTO producto VALUES (2,'X',NULL,NULL,10,NULL,-1,NULL,NULL,'activo',1)", "CHECK")
rechaza("estado de producto inválido", "INSERT INTO producto VALUES (2,'X',NULL,NULL,10,NULL,1,NULL,NULL,'borrado',1)", "CHECK")
rechaza("correo repetido", "INSERT INTO cliente VALUES (2,'uidB','Otro','ana@correo.com','2026-11-02',NULL,0)", "UNIQUE")
rechaza("teléfono de 9 dígitos", "INSERT INTO direccion_entrega VALUES (1,2,1,'Ana','Calle 1','300123456')", "CHECK")
rechaza("total distinto de subtotal + despacho", "INSERT INTO pedido VALUES (2,'CC-0002','2026-11-25 11:00:00','pendiente',100,12000,5,1,1)", "CHECK")
rechaza("estado de pedido inválido", "INSERT INTO pedido VALUES (2,'CC-0002','2026-11-25 11:00:00','perdido',100,0,100,1,1)", "CHECK")
rechaza("código de pedido repetido", "INSERT INTO pedido VALUES (2,'CC-0001','2026-11-25 11:00:00','pendiente',100,0,100,1,1)", "UNIQUE")
rechaza("pedido a dirección que no existe para ese cliente", "INSERT INTO pedido VALUES (2,'CC-0002','2026-11-25 11:00:00','pendiente',100,0,100,1,9)", "FOREIGN KEY")
rechaza("producto con categoría inexistente", "INSERT INTO producto VALUES (2,'X',NULL,NULL,10,NULL,1,NULL,NULL,'activo',99)", "FOREIGN KEY")
rechaza("abono sin pedido", "INSERT INTO transaccion_puntos VALUES (2,1,NULL,NULL,'2026-11-25 10:00:02','abono',5,'x')", "CHECK")
rechaza("cantidad 0 en detalle", "INSERT INTO detalle_pedido VALUES (1,1,0,45000)", "CHECK")
# acciones referenciales
rechaza("borrar categoría con productos (RESTRICT)", "DELETE FROM categoria WHERE id_categoria=1", "FOREIGN KEY")
rechaza("borrar producto vendido (RESTRICT)", "DELETE FROM producto WHERE id_producto=1", "FOREIGN KEY")
rechaza("borrar cliente con pedidos (RESTRICT)", "DELETE FROM cliente WHERE id_cliente=1", "FOREIGN KEY")
rechaza("borrar pedido con puntos acreditados debe conservarse el historial", "DELETE FROM pedido WHERE id_pedido=1", "FOREIGN KEY")
ok("alta de cliente sin pedidos para probar CASCADE", "INSERT INTO cliente VALUES (2,'uidC','Luis','luis@correo.com','2026-11-02',NULL,0)")
ok("dirección del cliente 2", "INSERT INTO direccion_entrega VALUES (2,1,1,'Luis','Calle 9','3109876543')")
ok("favorito del cliente 2", "INSERT INTO favorito VALUES (2,1,'2026-11-25')")
ok("borrar cliente 2 (CASCADE a direcciones y favoritos)", "DELETE FROM cliente WHERE id_cliente=2")
n = db.execute("SELECT (SELECT count(*) FROM direccion_entrega WHERE id_cliente=2)+(SELECT count(*) FROM favorito WHERE id_cliente=2)").fetchone()[0]
print("[OK]" if n == 0 else "[FALLA]", "CASCADE dejó", n, "filas huérfanas")
fallas += (n != 0)
print("RESULTADO:", "sin fallas" if fallas == 0 else f"{fallas} falla(s)")
sys.exit(1 if fallas else 0)
