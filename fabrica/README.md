# Fábrica de publicaciones ML

Flujo: **factura -> costos -> fichas -> borradores (precio, título, payload) -> validar -> publicar**.

| Paso | Comando | Resultado |
|---|---|---|
| 1. Costos | `python3 costos.py` | `salida/costos_consolidado_*.csv`, `salida/entrada_modelo_costos_*.csv` |
| 2. Categorías | `python3 categorizar.py` | `data/categorias.json` (predictor ML, API pública) |
| 3. Fichas | `python3 fabrica.py fichas` | `data/fichas.csv`: completar marca, material, medidas, peso, fotos |
| 4. Borradores | `python3 fabrica.py borradores` | `salida/borradores.csv` + `salida/payloads/<SKU>.json` |
| 5. Validar | `ML_ACCESS_TOKEN=... python3 fabrica.py validar --cuenta X` | `POST /items/validate` (no publica) |
| 6. Publicar | `ML_ACCESS_TOKEN=... python3 fabrica.py publicar --cuenta X` | `POST /items` + descripción, solo SKUs en estado LISTO |

Un SKU pasa a LISTO cuando tiene categoría confirmada (`categoria_final`), fotos, atributos requeridos de su categoría y medidas/peso de embalaje.
Marca = "Genérica" y modelo = código del proveedor por defecto (confirmar).

Precio: `P = (costo + costo fijo) / (1/1,21 - comision - margen)`, margen sobre precio con IVA antes de publicidad (calibrado con la calculadora de Creseller Ads).
Sobre $33.000 el modelo no suma el envío a cargo del vendedor: ajustar `envio` por SKU.

Para otra factura: copiar `data/factura_*.json` con el mismo formato y correr los pasos 1 a 4.
