---
name: bandas-comision
description: Recorre las ventas de una cuenta de Mercado Libre Argentina e identifica qué productos se venden pegados a un borde de las bandas de costo fijo / envío gratis, y decide qué precio ajustar. Usar con "bandas de comisión", "productos al límite", "borde de banda" y el nombre o cust_id de la cuenta.
---

# Bandas de comisión: productos vendidos al borde

## Qué busca
Productos cuyo **precio efectivo de venta** (unit_price de la orden, ya con descuentos) cae a menos de un 10% de un borde de banda, de cualquiera de los dos lados.

Bordes MLA (confirmar con `tarifas_ml`, medido 21-sep-2026):
- $15.000: costo fijo $1.330 por debajo, $2.740 por encima.
- $24.000: costo fijo $2.740 por debajo, $3.320 por encima.
- $33.000: sin costo fijo por encima, pero el envío lo paga el vendedor (alrededor de $7.000 a $9.000).

## Cuentas y herramientas
- `mcp__Creseller_Ads__cuentas_estado`: qué cuentas están conectadas. Si el cust_id no está, avisar y pedir `ml_conectar`. No inventar datos.
- Cuentas en DomUp (`mcp__domup_mcp__cuentas`): usar `escalon_costo_fijo` y `ventas_por_item` (agregados exactos, sin paginar).
- Cuentas solo en Creseller_Ads: `ml_api_get` sobre `/orders/search`.
- Mapa cust_id a cuenta: Tutti Home 1925134431 (`tutti-home`), We Glam 571325058 (`weglam`), 770 Brands 1652667547 (`770brands`).

## Procedimiento (órdenes por API)
1. Rango por defecto: últimos 30 días hasta HOY inclusive.
2. Primer llamado con `limit=1` para tener el total (`paging.total`, está al final de la respuesta).
3. Paginar con `limit=6` y `offset` de 6 en 6, con `max_chars=70000`. Medido el 20-oct: cada orden pesa unos 3 a 8 KB y `ml_api_get` corta la respuesta cerca de los 35.000 caracteres visibles, así que con `limit=20` solo se ven unas 7 órdenes por página y el resto se pierde en silencio. Verificar siempre que los offsets cubran `paging.total` (que solo aparece cuando la respuesta no se corta, por ejemplo con `limit=1`) antes de concluir. Si no se pudo cubrir todo, reportar la cobertura real.
3b. Preferir DomUp: si la cuenta está en `mcp__domup_mcp__cuentas`, `ventas_por_item` da unidades y facturación exactas por publicación en una sola llamada. Precio efectivo medio = facturación / unidades (es un promedio, puede ocultar variación de precio).
4. Ignorar órdenes con `status` cancelled o reembolsadas.
5. Por cada ítem de orden registrar: item_id, título, `unit_price` (efectivo), `gross_price` (publicado), `quantity`, `sale_fee`, `listing_type_id`.
6. Agrupar por item_id: unidades, precio efectivo (el más frecuente), precio publicado.
7. Calcular la distancia al borde más cercano en pesos y en %. Listar todo lo que quede a menos del 10%.

## Decisión por producto
- Por debajo de un borde y a menos del 3%: riesgo de cruzar con un aumento o promo. Fijar un tope de precio.
- Por encima de un borde y a menos del 10%: estimar el neto por unidad si baja justo al borde menos $1. Comisión efectiva = (sale_fee − costo fijo del tramo) / precio. Si el neto sube, recomendar bajar.
- Cerca de $33.000 desde arriba: comparar neto con envío incluido contra bajar a $32.999.
- Ordenar por unidades por plata en juego (diferencia de neto por unidad por unidades).

## Salida
Tabla con: producto, item_id, precio publicado, precio efectivo, borde cercano y distancia, unidades, neto actual vs. neto propuesto, acción recomendada. Cerrar con cobertura: cuántas órdenes se leyeron sobre el total. Si no se leyeron todas, decirlo.

## Reglas
- Solo lectura: no cambiar precios en ML sin OK explícito.
- Sin dato, decirlo. No completar de memoria.
- Duda abierta: si ML calcula el escalón sobre el precio publicado o sobre el efectivo con descuento. Se asumió el efectivo, que coincide con las comisiones observadas.

## Frecuencia sugerida
Semanal por defecto (los precios no cambian a diario). Diario solo en semanas de promos o relámpagos, cuando los precios efectivos se mueven.
