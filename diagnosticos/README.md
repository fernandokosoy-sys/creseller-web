# Diagnósticos

El agente `diagnostico-ml` (`.claude/agents/diagnostico-ml.md`) guarda acá el diagnóstico básico de cada cuenta de Mercado Libre. Un archivo por corrida: `AAAA-MM-DD-<nickname>.md`.

Uso: "usá diagnostico-ml para diagnosticar la publicación <link>" o "... la cuenta <nickname>". Revisa por pisos (terreno, cimientos, estructura, terminaciones, instalaciones, terraza) y marca aciertos y errores.

Para repetirlo en automático (ej. cada lunes sobre una lista de cuentas) se puede programar con una tarea programada que invoque al agente. El agente es solo lectura: no modifica cuentas ni contacta a nadie.
