import json, csv, sys
from decimal import Decimal as D, ROUND_HALF_UP
q = lambda x: D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)
f = json.load(open("data/factura_ramy_0009-00001276.json"))
iva = D(str(f["iva_pct"]))/100
rows=[]; suma=D(0); dudas=0
for it in f["items"]:
    p=D(str(it["precio"])); c=D(it["cant"]); imp=D(str(it["importe"]))
    suma+=imp
    duda=[]
    if abs(p*c-imp)>D("1"): duda.append(f"precio x cant = {q(p*c)} vs importe factura {imp}")
    rows.append(dict(proveedor=f["proveedor"],sku=it["sku"],descripcion=it["desc"],
        moneda_original="ARS",precio_original=q(p),iva_origen="sin_iva",alicuota_iva="21.00",
        usd_sin_iva="",usd_con_iva="",ars_sin_iva=q(p),ars_con_iva=q(p*(1+iva)),
        pagina=1,duda="; ".join(duda),cant=it["cant"],un_bulto=it["un_bulto"],importe=imp))
print("Suma importes:", suma, "| Subtotal factura:", f["subtotal_factura"], "| dif:", suma-D(str(f["subtotal_factura"])))
print("IVA calculado:", q(suma*iva), "| IVA factura:", f["iva_factura"], "| Total:", q(suma*(1+iva)), "vs", f["total_factura"])
print("Lineas:", len(rows), "| unidades:", sum(r["cant"] for r in rows))
cols=["proveedor","sku","descripcion","moneda_original","precio_original","iva_origen","alicuota_iva","usd_sin_iva","usd_con_iva","ars_sin_iva","ars_con_iva","pagina","duda"]
with open("salida/costos_consolidado_2026-11-25.csv","w",newline="",encoding="utf-8-sig") as fh:
    w=csv.DictWriter(fh,fieldnames=cols,delimiter=";",extrasaction="ignore"); w.writeheader(); w.writerows(rows)
cols2=["proveedor","sku","descripcion","costo_ars_sin_iva","costo_ars_con_iva","costo_usd_sin_iva","alicuota_iva","largo_cm","ancho_cm","alto_cm","peso_kg","fecha_tc","tipo_cambio"]
with open("salida/entrada_modelo_costos_2026-11-25.csv","w",newline="",encoding="utf-8-sig") as fh:
    w=csv.writer(fh,delimiter=";"); w.writerow(cols2)
    for r in rows: w.writerow([r["proveedor"],r["sku"],r["descripcion"],r["ars_sin_iva"],r["ars_con_iva"],"",r["alicuota_iva"],"","","","","2026-11-25",""])
# duplicados / outliers
from collections import Counter
print("SKU duplicados:", [k for k,v in Counter(r["sku"] for r in rows).items() if v>1])
for r in rows:
    if r["duda"]: print("DUDA", r["sku"], r["duda"])
