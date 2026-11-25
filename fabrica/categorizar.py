"""Etapa 2: categoría ML sugerida + ficha técnica de cada SKU (solo API pública, sin token)."""
import json, urllib.request, urllib.parse, time, sys
API = "https://api.mercadolibre.com"
def get(path):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(API+path, headers={"User-Agent":"fabrica-publicaciones"}), timeout=25) as r:
                return json.load(r)
        except Exception as e:
            err = e; time.sleep(1.5)
    return {"_error": str(err)}
def consulta(desc):  # texto en minúscula, sin códigos de proveedor
    return desc.lower().replace(" x "," ").replace("vs usos","usos").replace("c/tapa","con tapa").replace("tuper","tupper")
f = json.load(open("data/factura_ramy_0009-00001276.json"))
out = {}
for it in f["items"]:
    q = consulta(it["desc"])
    r = get("/sites/MLA/domain_discovery/search?limit=3&q="+urllib.parse.quote(q))
    cands = [{"category_id":c["category_id"],"category":c["category_name"],"domain":c["domain_id"]} for c in r] if isinstance(r,list) else []
    top = cands[0]["category_id"] if cands else None
    cat = get(f"/categories/{top}") if top else {}
    attrs = get(f"/categories/{top}/attributes") if top else []
    req = [a["id"] for a in attrs if isinstance(a,dict) and "required" in (a.get("tags") or {})] if isinstance(attrs,list) else []
    out[it["sku"]] = {"consulta":q,"candidatas":cands,"categoria":top,
        "path":" > ".join(p["name"] for p in cat.get("path_from_root",[])),
        "max_title":(cat.get("settings") or {}).get("max_title_length"),
        "atributos_requeridos":req,
        "atributos_total":len(attrs) if isinstance(attrs,list) else 0}
    print(f'{it["sku"]:11} {it["desc"][:38]:38} -> {top} {out[it["sku"]]["path"][-60:]} | req={req}')
    time.sleep(0.3)
json.dump(out, open("data/categorias.json","w"), ensure_ascii=False, indent=1)
