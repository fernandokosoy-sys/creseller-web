**Para Claude Code: base de conocimiento de Creseller**

Fer Kosoy tiene una consultoría de Mercado Libre Argentina (Creseller). Te dejó su criterio de trabajo en Google Drive, en la carpeta **"Creseller - Base de conocimiento"**: https://drive.google.com/drive/folders/17v6JgBj4q-OiPAqoCBENay3wJtqChVK5

**Tu objetivo:** construir diagnósticos automáticos de cuentas y publicaciones de ML aplicando su metodología.

**Cómo leerla**
1. Empezá por `00 - Índice`: dice qué contiene cada documento y qué falta.
2. Orden sugerido: 00, 09 (reglas), 02 (diagnóstico), 03 (publicaciones), 04 (Ads), 05 (logística), 06 (errores), 07 (casos), 08 (comunicación), 11 (otros temas).
3. Leé el 10 (dudas y contradicciones) para saber qué no dar por cierto.
4. Ignorá los archivos "REEMPLAZADO (borrar)" que estén fuera de la carpeta.

**Cómo tratar las marcas**
- **PENDIENTE:** Fer no lo definió. No lo inventes ni lo completes con supuestos. Dejalo como "sin criterio definido" en tu salida.
- **SIN CONFIRMAR:** es una suposición o valor por defecto de Claude, no una regla firme. Usalo como parámetro editable y avisalo.
- **Sin marca:** criterio de Fer o práctica aplicada en trabajos reales.
- El doc 09 reúne las reglas que él repite siempre. Tratalas como obligatorias.

**Datos que vas a procesar**
Exports nativos de ML (Publicaciones, Ventas, Métricas). Tienen 5 filas de metadatos y formato numérico argentino. Ver doc 09. Las referencias a publicaciones siempre van como MLA + descripción + hipervínculo.

**Lo que no tenés que hacer**
- No nombres clientes: los documentos están anonimizados y los informes deben respetarlo.
- No incluyas credenciales ni datos de compradores.
- No supongas umbrales de reputación, conversión absoluta, fotos o ROAS: no están definidos.

**Cuando algo falte**
Anotá la pregunta en tu salida y proponé una opción para que Fer decida. No la resuelvas por tu cuenta.
