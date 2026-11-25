"""Etapa 0b: trae ficha (marca, material, medidas, fotos) desde la tienda del proveedor (Tiendanube). Solo lectura, pausa entre pedidos."""
import re, json, html, time, urllib.request, urllib.parse, os
BASE = "https://espaciobazar.com/productos/"
def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read().decode("utf-8", "ignore")
def parse(s):
    d = {}
    d["titulo_web"] = html.unescape((re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S) or [0, ""])[1]).strip()
    m = re.search(r'<meta property="og:description" content="([^"]*)"', s); d["descripcion_web"] = html.unescape(m.group(1)).strip() if m else ""
    tags = {}
    for k, v in re.findall(r"'leren\\u003A([a-z_]+)\\u003A([^']*)'", s):
        tags[k] = v.encode().decode("unicode_escape").replace("\\/", "/") if "\\u" in v else v
    d["tags"] = tags
    d["ficha"] = {html.unescape(a).strip(): html.unescape(b).strip() for a, b in
                  re.findall(r'title">([^<]+)</div>\s*<div class="col pl-4 text-right">([^<]*)</div>', s)}
    gal = re.findall(r'data-image="(\d+)" data-image-position="(\d+)">\s*<a href="(//[^"]+)"', s)
    d["fotos"] = ["https:" + u for _, pos, u in sorted(gal, key=lambda x: int(x[1]))]
    vs = re.search(r'LS\.variants = (\[.*?\]);\s*(?:LS\.|</script>|\n)', s, re.S)
    d["variantes"] = []
    if vs:
        try:
            for v in json.loads(vs.group(1)):
                d["variantes"].append({"sku": v.get("sku"), "stock": v.get("stock"), "image_url": "https:" + v["image_url"].replace("\\/", "/") if v.get("image_url") else None,
                                       "opciones": [v.get(f"option{i}") for i in range(3) if v.get(f"option{i}")]})
        except Exception as e: d["variantes_error"] = str(e)
    return d
def main():
    urls = json.load(open("data/sku_url_proveedor.json")); out = {}
    for sku, u in urls.items():
        try: out[sku] = {"url": u, **parse(fetch(u))}
        except Exception as e: out[sku] = {"url": u, "error": str(e)}
        time.sleep(0.5)
    json.dump(out, open("data/proveedor_web.json", "w"), ensure_ascii=False, indent=1)
    return out
if __name__ == "__main__": main()
