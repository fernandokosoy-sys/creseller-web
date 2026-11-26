"""Etapa 3: arma data/fichas.csv combinando web del proveedor + catálogos PDF (Max-Plast 3-11-26, Espacio Bazar 2-11-26) + decisiones manuales.
Lo ya cargado en `categoria_confirmada` / `notas` de un fichas.csv previo se conserva."""
import json, csv, re, os
from fabrica import FICHA_COLS, escribir_csv, leer_csv
web = json.load(open("data/proveedor_web.json")); f = json.load(open("data/factura_ramy_0009-00001276.json"))
# SKU: (largo, ancho, alto cm, peso g, capacidad_ml, material, fuente_medidas, conflicto)
C = {
 "MAX-1649": (23.5, 8, 23, 348, 1100, "Plástico", "cat. Max-Plast; peso=cartón 4,17kg/12", ""),
 "MAX-0053": (30.5, 7.5, 10, 191, 400, "Plástico", "cat. Max-Plast; peso=cartón 4,59kg/24 (ficha dice 148 g)", ""),
 "MAX-0054": (22.5, 7.5, 16, 215, 700, "Plástico", "cat. Max-Plast; peso=cartón 5,15kg/24 (ficha dice 38 g, error)", ""),
 "MAX-2911": ("", "", "", "", 4700, "Plástico", "sin medidas ni peso en catálogos", ""),
 "MAX-0396": (33, 10, 26, 708, 860, "Plástico", "cat. Max-Plast; peso=cartón 4,25kg/6 (ficha dice 600 g)", ""),
 "MAX-0355": (33, 8, 29, 768, 1300, "Plástico", "cat. Max-Plast", ""),
 "MAX-0359": (31, 20, 9, 473, 3000, "Plástico", "cat. Max-Plast, pieza más grande", ""),
 "MAX-1631": (28.5, 28.5, 14.5, 755, 5300, "Plástico", "cat. Max-Plast, pieza más grande", "cartón 3,3kg/12 no cierra con 755 g"),
 "MAX-0329": (65, 45, 37, 1783, "", "Plástico", "cat. Max-Plast; peso=cartón 10,7kg/6", "web 57x46x35,5 vs catálogo 65x45x37; catálogo dice 'jute', foto y web: plástico"),
 "MAX-2939": ("", "", "", "", 3500, "", "sin medidas ni peso; web sin material", ""),
 "MAX-0026": ("", "", "", 520, "", "Plástico", "peso cat. Max-Plast", "web 39x22x6,5 vs catálogo 38,5x22,5x22,5: medir"),
 "MAX-1670": (32, 17, 24, 800, "", "Plástico", "web (catálogo trae alto 4 cm, error); peso cat.", ""),
 "MAX-1654": (25.5, 17, 24, 650, "", "Plástico", "cat. Max-Plast", ""),
 "MAX-2903": (28, 23, 36, 1350, "", "Plástico", "cat. Max-Plast; peso=cartón 8,1kg/6", ""),
 "HDG00131-2": ("", "", "", "", 1400, "Vidrio", "sin medidas ni peso", ""),
 "RJW-24507": (40, "", "", "", "", "Aluminio", "solo largo 40 cm", ""),
 "RJW-24508": (40, "", "", "", "", "Aluminio", "solo largo 40 cm", ""),
 "RXH-24413": (26, 17, 30, "", "", "Metal", "web/cat. EB; material visto en foto, sin dato escrito", ""),
 "RYJ-24371": (26, 26, 18, "", "", "Metal", "cat. EB (alambre/metal), redondo 26x18", ""),
 "RYJ-24365": (35, 21.5, 16, "", "", "Metal", "cat. EB (alambre/metal)", ""),
 "RYJ-24363": (30.5, 20, 13, "", "", "Metal", "cat. EB (alambre/metal)", ""),
 "ROLL-24300": (7, 7, 10, "", 230, "Vidrio", "web/cat. EB: 10x7 cm", "factura dice 240 ML, web y catálogo 230 ml"),
 "ROLL-24299": (5, 5, 6, "", 80, "Vidrio", "web/cat. EB: 6x5 cm", "factura dice 70 ML, catálogo 80 ml"),
}
CAT = {"MAX-1649":"MLA412348","MAX-0053":"MLA376317","MAX-0054":"MLA376317","MAX-2911":"MLA376317","MAX-0396":"MLA404785","MAX-0355":"MLA404785",
 "MAX-0359":"MLA376317","MAX-1631":"MLA376317","MAX-0329":"MLA393046","MAX-2939":"MLA414028","MAX-0026":"","MAX-1670":"MLA416551","MAX-1654":"MLA416551",
 "MAX-2903":"MLA6656","HDG00131-2":"MLA376317","RJW-24507":"MLA6734","RJW-24508":"MLA6734","RXH-24413":"MLA413429","RYJ-24371":"MLA455176",
 "RYJ-24365":"MLA455176","RYJ-24363":"MLA455176","ROLL-24300":"MLA1594","ROLL-24299":"MLA1594"}
TIPO = {"RJW-24507":"Luz Led Slim con Sensor y USB","RJW-24508":"Luz Led con Sensor y 3 Luces USB","RXH-24413":"Frutero 2 Pisos",
 "MAX-2903":"Banquito Plegable","MAX-0329":"Cesto para Ropa Sucia con Tapa","MAX-2939":"Centrifugador Escurridor de Verduras"}
prev = {r["sku"]: r for r in leer_csv("data/fichas.csv")} if os.path.exists("data/fichas.csv") else {}
rows = []
for it in f["items"]:
    s = it["sku"]; w = web[s]; L, A, H, P, cap, mat, fuente, conf = C[s]
    t = w["tags"]; colores = w["ficha"].get("COLORES", "")
    surt = "surtid" in w["descripcion_web"].lower() or colores.count(",") >= 1
    base = re.sub(r"\s*-?\s*\b[A-Z]*\d[\w-]*\s*$", "", w["titulo_web"]).strip()
    base = re.sub(r"\s+", " ", base).replace(" X ", " x ")
    fotos = "|".join(u.replace(".webp", ".jpg") for u in w["fotos"][:10])
    m = re.search(r"\bX ?(\d+)\b", it["desc"])
    r = {c: "" for c in FICHA_COLS}
    r.update(sku=s, descripcion_factura=it["desc"], categoria_sugerida=CAT[s], categoria_final=CAT[s], tipo_producto=TIPO.get(s, base),
        marca="Max-Plast" if t.get("marca") else "", modelo=s, material=mat, color="Surtido" if surt else (t.get("color") or ""),
        capacidad_ml=cap, unidades_set=m.group(1) if m else "", largo_cm=L, ancho_cm=A, alto_cm=H, peso_g=P, fotos=fotos,
        notas_proveedor=("; ".join(x for x in [f"medidas/peso: {fuente}", f"CONFLICTO: {conf}" if conf else "", f"colores web: {colores}" if colores else "", f"web: {w['url']}"] if x)))
    r["categoria_confirmada"] = prev.get(s, {}).get("categoria_confirmada", "")
    rows.append(r)
escribir_csv("data/fichas.csv", FICHA_COLS + ["categoria_confirmada"], rows)
print(f"data/fichas.csv: {len(rows)} filas | con fotos: {sum(bool(r['fotos']) for r in rows)} | con peso: {sum(bool(r['peso_g']) for r in rows)} | con 3 medidas: {sum(bool(r['largo_cm'] and r['ancho_cm'] and r['alto_cm']) for r in rows)}")
