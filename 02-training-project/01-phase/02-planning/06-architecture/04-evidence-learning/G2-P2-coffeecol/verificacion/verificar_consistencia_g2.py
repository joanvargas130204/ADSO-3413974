# -*- coding: utf-8 -*-
"""Verificación automática de consistencia de G2-P1 y G2-P2 (CoffeeCol). Uso (desde G2-P2-coffeecol): python3 verificacion/verificar_consistencia_g2.py"""
import re, os, sys, glob
R2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R1 = os.path.join(os.path.dirname(R2), "G2-P1-coffeecol")
rd = lambda base, p: open(os.path.join(base, p), encoding="utf8").read()
fails, oks = [], []
def chk(n, c, d=""): (oks if c else fails).append(n + ("" if c else " -> " + d))
snake = lambda s: re.sub(r"([A-Z])", lambda m: "_" + m.group(1).lower(), s)

# ---------- P1 ----------
cd = rd(R1, "diagramas/diagrama-clases.mmd")
bloques = re.findall(r"class (\w+) \{(.*?)\n  \}", cd, re.S)
clases = [b[0] for b in bloques]
chk("P1: >= 8 clases", len(clases) >= 8, str(len(clases)))
attrs = {c: re.findall(r"^\s*([+\-#])(\w+): (\S+)\s*$", b, re.M) for c, b in bloques}
mets = {c: re.findall(r"^\s*[+\-#](\w+)\((.*?)\)\s*(\S+)?\s*$", b, re.M) for c, b in bloques}
sin_tipo = [c for c, b in bloques for l in b.splitlines() if re.match(r"\s*[+\-#]\w+\s*$", l)]
chk("P1: atributos con tipo y visibilidad", not sin_tipo, str(sin_tipo))
chk("P1: hay clases con métodos con parámetros", sum(1 for c in mets if any(m[1] for m in mets[c])) >= 8)
asoc = [l for l in cd.splitlines() if re.search(r"\s(-->|\*--)\s", l)]
sin_mult = [l.strip() for l in asoc if len(re.findall(r'"[^"]+"', l)) < 2]
chk("P1: multiplicidad en los dos extremos de toda asociación", not sin_mult, str(sin_mult))
chk("P1: composición", "*--" in cd); chk("P1: herencia", "<|--" in cd)
impl = re.findall(r"(\w+) <\|\.\. (\w+)", cd)
por_if = {}
for i, c in impl: por_if.setdefault(i, []).append(c)
chk("P1: interfaz con >= 2 implementaciones", any(len(v) >= 2 for v in por_if.values()), str(por_if))
# matriz
mx = rd(R1, "07-matriz-de-trazabilidad.md")
fil = [l.split("|")[1:-1] for l in mx.splitlines() if l.startswith("| RF-")]
cl_mx = {c.strip() for f in fil for c in f[1].split(",")}
chk("P1: toda clase del diagrama está en la matriz (ninguna sin requisito)", set(clases) <= cl_mx, str(set(clases) - cl_mx))
chk("P1: toda clase de la matriz existe en el diagrama", cl_mx <= set(clases), str(cl_mx - set(clases)))
ficha = rd(R1, "01-ficha-interpretacion-y-plataforma.md")
rf_ficha = set(re.findall(r"^\| (RF-\d+) ", ficha, re.M)); rf_mx = {f[0].strip() for f in fil}
chk("P1: matriz cubre el 100 % de los RF de la ficha", rf_ficha == rf_mx, f"ficha={len(rf_ficha)} matriz={len(rf_mx)}")
chk("P1: ficha con >= 8 RF y >= 3 RNF", len(rf_ficha) >= 8 and len(re.findall(r"^\| RNF-\d+ ", ficha, re.M)) >= 3)
comp = rd(R1, "05-componentes.md")
cl_comp = {c.strip() for l in comp.splitlines() if re.match(r"\| C\d", l) for c in l.split("|")[4].split(",")}
chk("P1: clases de los componentes existen en el diagrama", cl_comp <= set(clases), str(cl_comp - set(clases)))
chk("P1: toda clase pertenece a un componente", set(clases) <= cl_comp, str(set(clases) - cl_comp))
chk("P1: >= 5 componentes", len([l for l in comp.splitlines() if re.match(r"\| C\d", l)]) >= 5)
pat = rd(R1, "03-patrones.md")
nombres_pat = set(re.findall(r"`(\w+)`", pat)) & set(re.findall(r"\b[A-Z]\w+\b", cd))
chk("P1: las clases de los patrones están en el diagrama", {c for c in re.findall(r"`([A-Z]\w+)`", pat)} <= set(clases), str({c for c in re.findall(r"`([A-Z]\w+)`", pat)} - set(clases)))
arq = rd(R1, "04-arquitectura.md")
chk("P1: >= 3 RNF con decisión en la arquitectura", len(set(re.findall(r"^\| (RNF-\d+)", arq, re.M))) >= 3)
ficha_rnf = set(re.findall(r"^\| (RNF-\d+) ", ficha, re.M))
chk("P1: los RNF de la arquitectura están en la ficha", set(re.findall(r"^\| (RNF-\d+)", arq, re.M)) <= ficha_rnf, str(set(re.findall(r"^\| (RNF-\d+)", arq, re.M)) - ficha_rnf))
dep = rd(R1, "diagramas/despliegue.mmd")
aristas = [l for l in dep.splitlines() if "-->" in l]
chk("P1: >= 3 nodos y protocolo en cada conexión", len(re.findall(r"subgraph N\d", dep)) >= 3 and all(re.search(r"HTTPS|TCP", a) for a in aristas))
# componentes sin ciclos de dependencia
cm = rd(R1, "diagramas/componentes.mmd")
gr = {}
for a, b in re.findall(r"(C\d)\s*-- .*? -->\s*(C\d)", cm): gr.setdefault(a, set()).add(b)
def ciclo(n, vis=()):
    return n in vis or any(ciclo(m, vis + (n,)) for m in gr.get(n, ()))
chk("P1: sin ciclos de dependencia entre componentes", not any(ciclo(n) for n in gr))
chk("P1: la interfaz web no depende directamente de la base de datos", "C1" in gr and not (gr["C1"] & {"C7"}))
for n in ("diagrama-clases", "arquitectura", "componentes", "despliegue"):
    chk(f"P1: {n} con fuente e imagen", all(os.path.exists(os.path.join(R1, "diagramas", n + e)) for e in (".mmd", ".png", ".svg")))

# ---------- P2 ----------
def tablas(sql):
    out = {}
    for n, cuerpo in re.findall(r"CREATE TABLE (\w+) \((.*?)\n\)", sql, re.S):
        cols = {}
        for l in cuerpo.splitlines():
            m = re.match(r"\s+(\w+) (\w+(?:\(\d+(?:,\d+)?\))?)", l)
            if m and m.group(1) != "CONSTRAINT": cols[m.group(1)] = m.group(2)
        out[n] = (cols, cuerpo)
    return out
sm, sl = rd(R2, "sql/esquema-mariadb.sql"), rd(R2, "sql/esquema-sqlite.sql")
tm, tl = tablas(sm), tablas(sl)
chk("P2: >= 8 tablas", len(tm) >= 8, str(len(tm)))
chk("P2: scripts MariaDB y SQLite definen las mismas tablas y columnas", {k: v[0] for k, v in tm.items()} == {k: v[0] for k, v in tl.items()})
chk("P2: toda tabla tiene PK", all("PRIMARY KEY" in v[1] for v in tm.values()))
chk("P2: >= 3 CHECK y >= 3 ON DELETE", len(re.findall(r"CHECK \(", sm)) >= 3 and len(re.findall(r"ON DELETE", sm)) >= 3)
dic = rd(R2, "04-diccionario-de-datos.md")
dd = {}
for n, cuerpo in re.findall(r"## `(\w+)`(.*?)(?=\n## `|\Z)", dic, re.S):
    cols = {}
    for l in cuerpo.splitlines():
        m = re.match(r"\| `(\w+)` \| (\w+) \| ([\w,]+|n/a) \|", l)
        if m: cols[m.group(1)] = m.group(2) + ("" if m.group(3) == "n/a" else f"({m.group(3)})")
    dd[n] = cols
chk("P2: diccionario con las mismas tablas que el script", set(dd) == set(tm), str(set(dd) ^ set(tm)))
dif = [(t, c) for t in tm if t in dd for c in set(tm[t][0]) ^ set(dd[t])]
chk("P2: diccionario con las mismas columnas que el script", not dif, str(dif[:5]))
dif2 = [(t, c, tm[t][0][c], dd[t].get(c)) for t in tm if t in dd for c in tm[t][0] if c in dd[t] and tm[t][0][c] != dd[t][c]]
chk("P2: diccionario con los mismos tipos que el script", not dif2, str(dif2[:5]))
lg = rd(R2, "02-modelo-logico.md")
chk("P2: modelo lógico lista las mismas tablas", set(re.findall(r"^\| `(\w+)` \|", lg, re.M)) == set(tm))
er = rd(R2, "diagramas/modelo-conceptual.mmd")
ents = {e.lower() for e in re.findall(r"^\s*([A-Z_]+) \{", er, re.M)}
chk("P2: cada entidad conceptual es una tabla", ents <= set(tm), str(ents - set(tm)))
chk("P2: cada tabla viene de una entidad conceptual", set(tm) <= ents, str(set(tm) - ents))
# FK acción referencial coherente con CHECK
for t, (cols, cuerpo) in tm.items():
    for fk in re.findall(r"FOREIGN KEY \((.*?)\).*?ON DELETE SET NULL", cuerpo):
        for c in fk.split(","):
            usado = [l for l in cuerpo.splitlines() if "CHECK" in l and re.search(r"\b" + c.strip() + r"\b.*IS NOT NULL", l)]
            chk(f"P2: SET NULL sobre {t}.{c.strip()} no contradice un CHECK de obligatoriedad", not usado, "; ".join(u.strip() for u in usado))
# cruce P1 <-> P2: atributos de las clases vs columnas
mapa = {"Cliente": ["cliente"], "Administrador": ["administrador"], "Usuario": ["cliente", "administrador"], "Producto": ["producto"], "Pedido": ["pedido"],
        "LineaPedido": ["detalle_pedido"], "DireccionEntrega": ["direccion_entrega"], "TransaccionPuntos": ["transaccion_puntos"]}
for c, tbs in mapa.items():
    for _, a, _t in attrs.get(c, []):
        col = snake(a)
        for t in tbs:
            if col not in tm[t][0] and not (a == "idUsuario" or col == "id_" + t):
                chk(f"P1↔P2: {c}.{a} existe como columna de {t}", False, f"falta {t}.{col}")
chk("P1↔P2: atributos de las clases mapeadas existen como columnas", not [f for f in fails if f.startswith("P1↔P2")])
print("CHEQUEOS OK:", len(oks)); print("FALLAS:", len(fails))
for f in fails: print("  FALLA:", f)
sys.exit(1 if fails else 0)
