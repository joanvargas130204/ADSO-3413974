# -*- coding: utf-8 -*-
"""Verificación automática de consistencia del modelo de análisis G1-P2 (CoffeeCol).
Uso (desde la carpeta G1-P2-coffeecol):  python3 verificacion/verificar_consistencia.py"""
import re, glob, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(R, p), encoding="utf8").read()
fails, oks = [], []
def chk(nombre, cond, detalle=""):
    (oks if cond else fails).append(nombre + ("" if cond else " -> " + detalle))

dom = rd("diagramas/modelo-dominio.mmd"); mer = rd("diagramas/mer-pata-de-gallo.mmd")
tr = rd("06-matriz-de-trazabilidad.md")
clases = re.findall(r"^\s*class (\w+)", dom, re.M)
ents = re.findall(r"^\s*([A-Z_]+) \{", mer, re.M)
chk("Dominio >= 8 clases", len(clases) >= 8, str(len(clases)))
chk("MER >= 6 entidades", len(ents) >= 6, str(len(ents)))

# 1. clases y entidades de la matriz existen en los modelos
filas = [l.split("|")[1:-1] for l in tr.splitlines() if l.startswith("| RF-")]
chk("Matriz con 54 requisitos", len(filas) == 54, str(len(filas)))
cl_usadas, en_usadas = set(), set()
for f in filas:
    for c in f[4].split(","):
        c = c.strip()
        if c and c != "—": cl_usadas.add(c)
    for e in f[5].split(","):
        e = e.strip()
        if e and e != "—": en_usadas.add(e)
chk("Clases de la matriz existen en el dominio", cl_usadas <= set(clases), str(cl_usadas - set(clases)))
chk("Entidades de la matriz existen en el MER", en_usadas <= set(ents), str(en_usadas - set(ents)))
chk("Toda clase de dominio tiene al menos un requisito", set(clases) <= cl_usadas, str(set(clases) - cl_usadas))
chk("Toda entidad del MER tiene al menos un requisito", set(ents) <= en_usadas, str(set(ents) - en_usadas))
nt = sum(1 for f in filas if f[4].strip() != "—" and f[5].strip() != "—")
chk("Trazabilidad >= 90 % hasta clase y entidad", nt / 54 >= 0.9, f"{nt}/54")

# 2. dominio: atributos, sin métodos ni FK
bloques = re.findall(r"class (\w+) \{(.*?)\}", dom, re.S)
con2 = [n for n, b in bloques if len([x for x in b.strip().splitlines() if x.strip()]) >= 2]
chk("Dominio: >= 5 clases con 2 o más atributos", len(con2) >= 5, str(len(con2)))
chk("Dominio sin métodos", not any("(" in b for _, b in bloques), "hay paréntesis en atributos")
chk("Dominio sin claves foráneas", not any(re.search(r"\bid_|\bFK\b|_id\b", b) for _, b in bloques), "atributo tipo id_/FK")
chk("Dominio con generalización", "<|--" in dom)
# 3. MER: PK en cada entidad
bm = dict(re.findall(r"^\s*([A-Z_]+) \{(.*?)\}", mer, re.S | re.M))
sinpk = [e for e, b in bm.items() if "PK" not in b]
chk("MER: toda entidad tiene PK", not sinpk, str(sinpk))
chk("MER: relaciones N:M resueltas (DETALLE_PEDIDO, FAVORITO)", all(e in bm for e in ("DETALLE_PEDIDO", "FAVORITO")))
chk("MER: entidad débil DIRECCION_ENTREGA con PK compuesta", bm.get("DIRECCION_ENTREGA", "").count("PK") >= 2)

# 3b. coherencia de relaciones dominio vs MER
dom_rel = re.search(r"Cliente .*--> .*NivelFidelizacion", dom) is not None
mer_rel = re.search(r"^\s*\w+\s+[|o}{]+--[|o}{]+\s+\w+\s*:.*$", mer, re.M) and any("NIVEL_FIDELIZACION" in l and "--" in l for l in mer.splitlines())
chk("Relación Cliente-NivelFidelizacion: dominio y MER coinciden", dom_rel == bool(mer_rel), f"dominio={dom_rel}, MER={bool(mer_rel)}")
cl_chk = re.search(r"en (\d+) clases", rd("03-modelo-de-dominio.md"))
chk("03-modelo-de-dominio.md: el conteo de clases con 2+ atributos es el real", cl_chk and int(cl_chk.group(1)) == len(con2), f"dice {cl_chk.group(1) if cl_chk else '?'}, real {len(con2)}")
# 4. conceptos de las plantillas presentes en los modelos
def tpl(n): return rd(glob.glob(os.path.join(R, "plantillas", n + "*"))[0].replace(R + "/", ""))
t11, t06, t03 = tpl("CU-11"), tpl("CU-06"), tpl("CU-03")
prod = dict(re.findall(r"class (\w+) \{(.*?)\}", dom, re.S)).get("Producto", "")
chk("CU-11 usa 'stock' y Producto lo tiene", "stock" in t11.lower() and "stock" in prod.lower())
chk("CU-11 permite retirar y Producto tiene estado", ("retirar" in t11.lower()) and re.search(r"estado|activo|disponible", prod, re.I) is not None, "Producto sin atributo de estado/retiro")
chk("CU-06 acredita puntos y existe TransaccionPuntos", "puntos" in t06 and "TransaccionPuntos" in clases)
chk("CU-06 verifica existencias y Producto tiene stock", "existencias" in t06 and "stock" in prod.lower())
chk("CU-06 usa dirección de entrega y existe DireccionEntrega", "DireccionEntrega" in clases and "DIRECCION_ENTREGA" in ents)
chk("CU-03 usa Firebase y el dominio lo representa en Usuario", "Firebase" in t03 and "Usuario" in clases)

# 5. plantillas: pasos, alterno, excepción
for nombre, t in (("CU-03", t03), ("CU-06", t06), ("CU-11", t11)):
    pasos = len(re.findall(r"(?:^|<br>|\| )\d+\. ", t))
    chk(f"{nombre}: >= 6 pasos principales", pasos >= 6, str(pasos))
    chk(f"{nombre}: >= 1 alterno y >= 1 excepción", "**A1.**" in t and "**E1.**" in t)
    chk(f"{nombre}: sin detalle de implementación", not re.search(r"\bPOST\b|\bGET\b|\bSQL\b|\.php|\.js\b|cookie|JWT|localStorage|\btoken\b|transacci", t), "palabra técnica")

# 6. diagramas de actividad: guardas en todas las salidas y ramas A/E reflejadas
for nombre, t in (("actividad-realizar-checkout", t06), ("actividad-iniciar-sesion", t03)):
    d = rd(f"diagramas/{nombre}.mmd")
    rombos = re.findall(r"(\w+)\{", d)
    sin = []
    for r in rombos:
        sal = [l for l in d.splitlines() if re.search(rf"\b{r}\b\s*-->", l)]
        if len(sal) < 2 or any("|" not in l for l in sal): sin.append(r)
    chk(f"{nombre}: guardas en todas las salidas de decisión", not sin, str(sin))
    ramas = set(re.findall(r"\*\*([AE]\d)\.\*\*", t))
    ramas_d = set(re.findall(r"\b([AE]\d)\b", d))
    chk(f"{nombre}: ramas A/E de la plantilla aparecen en el diagrama", ramas <= ramas_d, str(ramas - ramas_d))
    chk(f"{nombre}: fuente editable y PNG/SVG", all(os.path.exists(os.path.join(R, "diagramas", nombre + x)) for x in (".mmd", ".png", ".svg")))

# 7. prototipo
for s in glob.glob(os.path.join(R, "prototipo", "*.svg")):
    chk(os.path.basename(s) + " rotulada con el CU", "Atiende: CU-" in open(s, encoding="utf8").read())
chk("Prototipo >= 3 pantallas", len(glob.glob(os.path.join(R, "prototipo", "*.png"))) >= 3)

# 8. enlaces relativos de todos los .md
rotos = []
for md in glob.glob(os.path.join(R, "**", "*.md"), recursive=True):
    for m in re.findall(r"\]\(([^)#]+)\)", open(md, encoding="utf8").read()):
        if m.startswith("http"): continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(md), m))): rotos.append((os.path.basename(md), m))
chk("Enlaces relativos válidos", not rotos, str(rotos))

print("CHEQUEOS OK:", len(oks)); print("FALLAS:", len(fails))
for f in fails: print("  FALLA:", f)
sys.exit(1 if fails else 0)
