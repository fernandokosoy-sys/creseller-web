"""Lista de PVP para compartir: Código, Descripción, PVP (IVA incluido). PVP = precio unitario sin IVA x MULT (por defecto 3), mas IVA.
Salida: salida/lista_pvp_<fecha>.pdf y .xlsx. El costo, el multiplicador, la factura y el proveedor no aparecen en los archivos."""
import json, sys
from decimal import Decimal as D, ROUND_HALF_UP
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
MULT = D(sys.argv[1]) if len(sys.argv) > 1 else D(3)
FECHA = "26/11/2026"; ARCH = "salida/lista_pvp_2026-11-26"
q = lambda x: D(x).quantize(D("0.01"), rounding=ROUND_HALF_UP)
f = json.load(open("data/factura_ramy_0009-00001276.json")); iva = D(str(f["iva_pct"])) / 100
filas = []
for it in f["items"]:
    pvp = q(q(str(it["precio"])) * MULT); filas.append((it["sku"], it["desc"].title(), it["cant"], pvp, q(pvp * (1 + iva)), q(pvp * it["cant"])))
ar = lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
tit = f"Lista de precios PVP - {FECHA}"
cols = ["Código", "Descripción", "PVP"]            # PVP = precio final con IVA incluido
# ---- Excel ----
wb = Workbook(); ws = wb.active; ws.title = "PVP"
ws["A1"] = tit; ws["A1"].font = Font(bold=True, size=13); ws["A2"] = "Precios en pesos argentinos, IVA incluido"
ws.append([]); ws.append(cols)
for c in ws[4]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="1F3864"); c.alignment = Alignment(horizontal="center", vertical="center")
for r in filas: ws.append([r[0], r[1], float(r[4])])
thin = Side(style="thin", color="BBBBBB")
for row in ws.iter_rows(min_row=5, max_row=4 + len(filas)):
    for c in row: c.border = Border(bottom=thin)
    row[2].number_format = '#,##0.00'
for col, w in zip("ABC", (16, 48, 18)): ws.column_dimensions[col].width = w
ws.freeze_panes = "A5"; wb.properties.creator = ""; wb.save(ARCH + ".xlsx")
# ---- PDF ----
st = getSampleStyleSheet(); doc = SimpleDocTemplate(ARCH + ".pdf", pagesize=A4, leftMargin=40, rightMargin=40, topMargin=32, bottomMargin=32, title=tit)
data = [cols] + [[r[0], r[1], ar(r[4])] for r in filas]
t = Table(data, repeatRows=1, colWidths=[80, 280, 110])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F3864")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9), ("ALIGN", (2, 0), (2, -1), "RIGHT"), ("ALIGN", (0, 0), (-1, 0), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F2F2")])]))
doc.build([Paragraph(tit, st["Title"]), Paragraph("Precios en pesos argentinos, IVA incluido", st["Normal"]), Spacer(1, 10), t])
print("OK", len(filas), "filas")
