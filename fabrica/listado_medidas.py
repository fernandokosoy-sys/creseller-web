"""Listado por SKU de medidas y peso: dato actual, origen, estado y casillas para cargar el valor real (embalaje)."""
import csv, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
rows = list(csv.DictReader(open("data/fichas.csv", encoding="utf-8-sig"), delimiter=";"))
num = lambda v: float(v) if v not in ("", None) else None
wb = Workbook(); ws = wb.active; ws.title = "Medidas y peso"
ws["A1"] = "Medidas y peso por SKU - datos actuales y valores reales a completar"; ws["A1"].font = Font(bold=True, size=13)
ws["A2"] = "Gris = dato actual (provisorio, del producto o catálogo). Rojo = falta. Amarillo = completar con balanza y cinta métrica, con el producto en su caja de envío (cm y gramos)."
hdr = ["Código", "Descripción", "Largo actual (cm)", "Ancho actual (cm)", "Alto actual (cm)", "Peso actual (g)", "Estado", "Origen del dato", "Observación",
       "LARGO REAL (cm)", "ANCHO REAL (cm)", "ALTO REAL (cm)", "PESO REAL (g)"]
ws.append([]); ws.append(hdr)
GRIS = PatternFill("solid", fgColor="EDEDED"); ROJO = PatternFill("solid", fgColor="F8CBAD"); AMA = PatternFill("solid", fgColor="FFF2CC"); AZUL = PatternFill("solid", fgColor="1F3864")
thin = Side(style="thin", color="BBBBBB"); borde = Border(left=thin, right=thin, top=thin, bottom=thin)
for c in ws[4]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = AZUL; c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
for c in ws[4][9:]: c.fill = PatternFill("solid", fgColor="7F6000")
resumen = {"completo": 0, "sin peso": 0, "sin medidas": 0, "sin ambos": 0}
for r in rows:
    L, A, H, P = (num(r[k]) for k in ("largo_cm", "ancho_cm", "alto_cm", "peso_g"))
    meds = all(v is not None for v in (L, A, H)); peso = P is not None
    estado = "Provisorio completo" if meds and peso else "Falta peso" if meds else "Falta medidas" if peso else "Falta medidas y peso"
    resumen["completo" if meds and peso else "sin peso" if meds else "sin medidas" if peso else "sin ambos"] += 1
    n = r["notas_proveedor"]; fuente = (re.search(r"medidas/peso: ([^;]*)", n) or [0, ""])[1]
    conf = (re.search(r"CONFLICTO: ([^;]*)", n) or [0, ""])[1]
    ws.append([r["sku"], r["descripcion_factura"].title(), L, A, H, P, estado, fuente, conf, None, None, None, None])
    i = ws.max_row
    for col, v in zip("CDEF", (L, A, H, P)): ws[f"{col}{i}"].fill = GRIS if v is not None else ROJO
    for col in "JKLM": ws[f"{col}{i}"].fill = AMA
    ws[f"G{i}"].fill = ROJO if "Falta" in estado else GRIS
    if conf: ws[f"I{i}"].fill = ROJO
    for c in ws[i]: c.border = borde; c.alignment = Alignment(vertical="center", wrap_text=True)
for col, w in zip(range(1, 14), (14, 34, 11, 11, 11, 11, 20, 42, 44, 12, 12, 12, 12)): ws.column_dimensions[get_column_letter(col)].width = w
ws.row_dimensions[4].height = 32; ws.freeze_panes = "C5"; ws.merge_cells("A2:M2"); ws["A2"].alignment = Alignment(wrap_text=True); ws.row_dimensions[2].height = 30
wb.save("salida/listado_medidas_peso.xlsx")
print(resumen, "| filas:", len(rows))
