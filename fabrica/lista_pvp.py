"""Lista de PVP a partir de la factura: PVP = precio unitario sin IVA x MULT (3). Genera salida/lista_pvp_*.xlsx y .pdf"""
import json, sys
from decimal import Decimal as D, ROUND_HALF_UP
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
MULT = D(sys.argv[1]) if len(sys.argv) > 1 else D(3)
q = lambda x: D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)
f = json.load(open("data/factura_ramy_0009-00001276.json")); iva = D(str(f["iva_pct"])) / 100
filas = []
for it in f["items"]:
    c = q(str(it["precio"])); pvp = q(c * MULT); filas.append((it["sku"], it["desc"].title(), it["cant"], c, pvp, q(pvp * (1 + iva)), q(pvp * it["cant"])))
ar = lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")      # formato argentino
tit = f"Lista de PVP (precio sin IVA x {MULT}) - base factura {f['factura']} del {f['fecha'][8:]}/{f['fecha'][5:7]}/{f['fecha'][:4]}"
cols = ["SKU", "Descripción", "Cant.", "Precio unit. sin IVA", f"PVP sin IVA (x{MULT})", "PVP con IVA 21%", "PVP total sin IVA (cant.)"]
tot = sum(r[6] for r in filas)
# ---- Excel (con fórmulas vivas: el multiplicador se cambia en B3) ----
wb = Workbook(); ws = wb.active; ws.title = "PVP"
ws["A1"] = tit; ws["A1"].font = Font(bold=True, size=13)
ws["A3"] = "Multiplicador"; ws["B3"] = int(MULT); ws["B3"].fill = PatternFill("solid", fgColor="FFF2CC"); ws["A4"] = "IVA"; ws["B4"] = float(iva)
ws.append([]); ws.append(cols)
hdr = Font(bold=True, color="FFFFFF"); thin = Side(style="thin", color="BBBBBB")
for c in ws[6]: c.font = hdr; c.fill = PatternFill("solid", fgColor="1F3864"); c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
for i, r in enumerate(filas, start=7):
    ws.append([r[0], r[1], r[2], float(r[3]), f"=ROUND(D{i}*$B$3,2)", f"=ROUND(E{i}*(1+$B$4),2)", f"=ROUND(E{i}*C{i},2)"])
n = 6 + len(filas); ws.append(["", "TOTAL", f"=SUM(C7:C{n})", "", "", "", f"=SUM(G7:G{n})"])
for c in ws[n + 1]: c.font = Font(bold=True)
for row in ws.iter_rows(min_row=7, max_row=n + 1):
    for c in row: c.border = Border(bottom=thin)
    for c in row[3:]: c.number_format = '#,##0.00'
for col, w in zip("ABCDEFG", (14, 42, 8, 17, 17, 17, 22)): ws.column_dimensions[col].width = w
ws.freeze_panes = "A7"; wb.save("salida/lista_pvp_2026-11-26.xlsx")
# ---- PDF ----
st = getSampleStyleSheet(); doc = SimpleDocTemplate("salida/lista_pvp_2026-11-26.pdf", pagesize=landscape(A4), leftMargin=28, rightMargin=28, topMargin=28, bottomMargin=28, title=tit)
data = [cols] + [[r[0], r[1], r[2], ar(r[3]), ar(r[4]), ar(r[5]), ar(r[6])] for r in filas] + [["", "TOTAL", sum(r[2] for r in filas), "", "", "", ar(tot)]]
t = Table(data, repeatRows=1, colWidths=[78, 250, 40, 100, 100, 100, 120])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8), ("ALIGN", (2, 0), (-1, -1), "RIGHT"), ("ALIGN", (0, 0), (-1, 0), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.HexColor("#F2F2F2")]), ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"), ("LINEABOVE", (0, -1), (-1, -1), 0.8, colors.black),
    ("BACKGROUND", (4, 1), (4, -2), colors.HexColor("#FFF2CC"))]))
doc.build([Paragraph(tit, st["Title"]), Paragraph(f"Proveedor: {f['proveedor']} | Montos en pesos argentinos | PVP sin IVA = precio unitario sin IVA x {MULT}", st["Normal"]), Spacer(1, 10), t])
for r in filas: print(f"{r[0]:11} {r[1][:38]:38} {r[2]:>3} | costo {ar(r[3]):>10} | PVP x{MULT} {ar(r[4]):>11} | con IVA {ar(r[5]):>11}")
print("TOTAL PVP sin IVA:", ar(tot), "| Total costo sin IVA:", ar(sum(r[3] * r[2] for r in filas)))
