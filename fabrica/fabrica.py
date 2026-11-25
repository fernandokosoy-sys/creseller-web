#!/usr/bin/env python3
"""Fábrica de publicaciones ML (MLA): factura -> costos -> borradores -> validar -> publicar.

  python3 fabrica.py fichas        # crea/actualiza data/fichas.csv (lo que hay que completar por SKU)
  python3 fabrica.py borradores    # precios, títulos, payloads y estado de cada SKU
  python3 fabrica.py validar  --cuenta tutti-home   # POST /items/validate (no publica)
  python3 fabrica.py publicar --cuenta tutti-home   # POST /items + descripción (solo SKUs LISTO)

Token del vendedor: variable de entorno ML_ACCESS_TOKEN (una por cuenta, se corre una cuenta por vez).
"""
import csv, json, os, sys, math, re, time, urllib.request, urllib.error
from decimal import Decimal as D
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
API = "https://api.mercadolibre.com"

# ---- Parámetros (tabla de tarifas DomUp 21-sep-2026; actualizar con tarifas_ml) ----
IVA = 0.21; COM = {"clasica": 0.145, "premium": 0.273}
TRAMOS = [(15000, 1330), (24000, 2740), (33000, 3320)]; UMBRAL = 33000
MARGEN = 0.20          # sobre precio con IVA, antes de publicidad
OTROS_PCT = 0.0        # Ingresos Brutos u otros sobre precio sin IVA
LISTING = {"clasica": "gold_special", "premium": "gold_pro"}
GARANTIA = "30 días"

def precio_min(costo, tipo, envio=0.0, margen=MARGEN):
    """Precio con IVA mínimo para el margen objetivo (misma lógica que calc_precio_margen)."""
    c = COM[tipo]; k = 1/(1+IVA) * (1-OTROS_PCT) - c - margen
    for tope, fijo in TRAMOS:                       # costo fijo según tramo de precio
        p = (costo + fijo) / k
        if p <= tope: return math.ceil(p), fijo
    p = (costo + envio) / k                         # sobre umbral: sin costo fijo, envío a cargo
    return (math.ceil(p), 0) if p > UMBRAL else (UMBRAL + 1, 0)

def ganancia(precio, costo, tipo, fijo, envio=0.0):
    return precio/(1+IVA)*(1-OTROS_PCT) - costo - COM[tipo]*precio - fijo - (envio if precio >= UMBRAL else 0)

def leer_csv(p): return list(csv.DictReader(open(p, encoding="utf-8-sig"), delimiter=";"))
def escribir_csv(p, cols, rows):
    with open(p, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter=";", extrasaction="ignore"); w.writeheader(); w.writerows(rows)

FICHA_COLS = ["sku","descripcion_factura","categoria_sugerida","categoria_final","tipo_producto","marca","modelo",
  "material","color","capacidad_ml","unidades_set","largo_cm","ancho_cm","alto_cm","peso_g","gtin","fotos","notas_proveedor"]

def cmd_fichas():
    cats = json.load(open("data/categorias.json")); f = json.load(open("data/factura_ramy_0009-00001276.json"))
    prev = {r["sku"]: r for r in leer_csv("data/fichas.csv")} if os.path.exists("data/fichas.csv") else {}
    rows = []
    for it in f["items"]:
        r = prev.get(it["sku"], {c: "" for c in FICHA_COLS})
        r.update(sku=it["sku"], descripcion_factura=it["desc"], categoria_sugerida=cats[it["sku"]]["categoria"] or "")
        d = it["desc"]
        if not r.get("unidades_set"):                       # solo lo que dice la factura
            m = re.search(r"\bX ?(\d+)\b", d);  r["unidades_set"] = m.group(1) if m else ""
        if not r.get("capacidad_ml"):
            m = re.search(r"(\d+)ML", d);       r["capacidad_ml"] = m.group(1) if m else ""
        rows.append(r)
    escribir_csv("data/fichas.csv", FICHA_COLS, rows); print(f"data/fichas.csv: {len(rows)} filas")

def titulo(ficha, base, maxlen):
    partes = [ficha.get("tipo_producto") or base.title(), ficha.get("material"), ficha.get("marca"),
              ficha.get("modelo"), f'{ficha["capacidad_ml"]} ml' if ficha.get("capacidad_ml") else "", ficha.get("color")]
    t = " ".join(p for p in partes if p).strip()
    t = re.sub(r"[^\w\s.,/+%-]", "", t)               # sin símbolos, sin emojis
    while len(t) > maxlen and " " in t: t = t.rsplit(" ", 1)[0]
    return t

def descripcion(ficha, base):
    l = [f'{ficha.get("tipo_producto") or base.title()}.']
    if ficha.get("unidades_set"): l.append(f'Incluye {ficha["unidades_set"]} unidades.')
    for k, lab in (("material","Material"),("color","Color"),("capacidad_ml","Capacidad (ml)"),("marca","Marca"),("modelo","Modelo")):
        if ficha.get(k): l.append(f"{lab}: {ficha[k]}.")
    if ficha.get("largo_cm") and ficha.get("ancho_cm") and ficha.get("alto_cm"):
        l.append(f'Medidas: {ficha["largo_cm"]} x {ficha["ancho_cm"]} x {ficha["alto_cm"]} cm.')
    if ficha.get("peso_g"): l.append(f'Peso: {ficha["peso_g"]} g.')
    l.append("Producto nuevo. Consultá por stock y envíos.")
    return "\n".join(l)

def cmd_borradores(tipo="clasica"):
    cats = json.load(open("data/categorias.json")); f = json.load(open("data/factura_ramy_0009-00001276.json"))
    fichas = {r["sku"]: r for r in leer_csv("data/fichas.csv")}
    out = []; os.makedirs("salida/payloads", exist_ok=True)
    for it in f["items"]:
        s = it["sku"]; fi = fichas[s]; ct = cats[s]; costo = it["precio"]
        cat = fi["categoria_final"] or ct["categoria"]
        pc, fc = precio_min(costo, "clasica"); pp, fp = precio_min(costo, "premium")
        pre = pc if tipo == "clasica" else pp; fijo = fc if tipo == "clasica" else fp
        faltan = []
        if not fi["categoria_final"]: faltan.append("CONFIRMAR_CATEGORIA")
        if not fi["fotos"]: faltan.append("FOTOS")
        for a in ct["atributos_requeridos"]:
            if a == "BRAND" or a == "MODEL": continue        # BRAND=Genérica / MODEL=código proveedor (por defecto)
            campo = {"VOLUME_CAPACITY":"capacidad_ml","MATERIAL":"material","WIDTH":"ancho_cm","DEPTH":"largo_cm","HEIGHT":"alto_cm","LENGTH":"largo_cm"}.get(a)
            if not (campo and fi.get(campo)): faltan.append(a)
        if not (fi["largo_cm"] and fi["peso_g"]): faltan.append("MEDIDAS_PESO_ENVIO")
        t = titulo(fi, it["desc"], ct["max_title"] or 60)
        attrs = [{"id":"SELLER_SKU","value_name":s},{"id":"BRAND","value_name":fi["marca"] or "Genérica"},
                 {"id":"MODEL","value_name":fi["modelo"] or s},{"id":"ITEM_CONDITION","value_id":"2230284"}]
        for a, campo in (("MATERIAL","material"),("COLOR","color"),("VOLUME_CAPACITY","capacidad_ml"),("GTIN","gtin")):
            if fi.get(campo): attrs.append({"id":a,"value_name":fi[campo] + (" ml" if a=="VOLUME_CAPACITY" else "")})
        for a, campo in (("SELLER_PACKAGE_LENGTH","largo_cm"),("SELLER_PACKAGE_WIDTH","ancho_cm"),("SELLER_PACKAGE_HEIGHT","alto_cm"),("SELLER_PACKAGE_WEIGHT","peso_g")):
            if fi.get(campo): attrs.append({"id":a,"value_name":str(int(float(fi[campo])))})   # string numérico, sin unidad
        payload = {"title":t,"category_id":cat,"price":pre,"currency_id":"ARS","available_quantity":it["cant"],
            "buying_mode":"buy_it_now","condition":"new","listing_type_id":LISTING[tipo],
            "sale_terms":[{"id":"WARRANTY_TYPE","value_name":"Garantía del vendedor"},{"id":"WARRANTY_TIME","value_name":GARANTIA}],
            "pictures":[{"source":u} for u in fi["fotos"].split("|") if u.strip()],"attributes":attrs,
            "_descripcion":descripcion(fi, it["desc"])}
        json.dump(payload, open(f"salida/payloads/{s}.json","w"), ensure_ascii=False, indent=1)
        env = "precio >= 33.000: sumar envío a cargo del vendedor" if pre >= UMBRAL else ("premium >= 33.000: sumar envío" if pp >= UMBRAL else "")
        out.append(dict(sku=s, descripcion=it["desc"], stock=it["cant"], costo_neto=f"{costo:.2f}", costo_con_iva=f"{costo*1.21:.2f}",
            categoria=cat, categoria_path=ct["path"], titulo=t, largo_titulo=len(t),
            precio_clasica=pc, precio_premium=pp, precio_usado=pre, ganancia_unit=f"{ganancia(pre,costo,tipo,fijo):.0f}",
            margen_pct=f"{ganancia(pre,costo,tipo,fijo)/pre*100:.1f}", inversion_con_iva=f'{it["importe"]*1.21:.2f}',
            estado="LISTO" if not faltan else "FALTA: " + ", ".join(faltan), alerta=env))
    escribir_csv("salida/borradores.csv", list(out[0].keys()), out)
    listos = sum(r["estado"] == "LISTO" for r in out); print(f"salida/borradores.csv: {len(out)} SKUs, {listos} LISTO")

def http(method, path, token, body=None):
    req = urllib.request.Request(API+path, method=method, data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r: return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try: return e.code, json.load(e)
        except Exception: return e.code, {"error": str(e)}

def cmd_enviar(real, cuenta):
    token = os.environ.get("ML_ACCESS_TOKEN") or sys.exit("Falta ML_ACCESS_TOKEN (token del vendedor de la cuenta %s)" % cuenta)
    log = []
    for r in leer_csv("salida/borradores.csv"):
        if r["estado"] != "LISTO": print(f'{r["sku"]}: salteado ({r["estado"]})'); continue
        p = json.load(open(f'salida/payloads/{r["sku"]}.json')); desc = p.pop("_descripcion")
        st, res = http("POST", "/items" if real else "/items/validate", token, p)
        ok = st in (200, 201); item = res.get("id") if real and ok else ""
        if real and ok:
            time.sleep(1); http("POST", f"/items/{item}/description", token, {"plain_text": desc})
        msg = "OK" if ok else json.dumps(res.get("cause") or res, ensure_ascii=False)[:300]
        print(f'{r["sku"]}: {st} {item} {msg}'); log.append(dict(sku=r["sku"], http=st, item_id=item, resultado=msg))
        time.sleep(0.5)
    if log: escribir_csv(f'salida/log_{"publicar" if real else "validar"}_{cuenta}.csv', ["sku","http","item_id","resultado"], log)

if __name__ == "__main__":
    a = sys.argv[1:]; cuenta = a[a.index("--cuenta")+1] if "--cuenta" in a else "cuenta"
    {"fichas": cmd_fichas, "borradores": cmd_borradores,
     "validar": lambda: cmd_enviar(False, cuenta), "publicar": lambda: cmd_enviar(True, cuenta)}.get(a[0] if a else "", lambda: print(__doc__))()
