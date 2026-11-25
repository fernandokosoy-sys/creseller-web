#!/usr/bin/env python3
"""Token OAuth de una cuenta ML para la fábrica (permiso de lectura y escritura sobre publicaciones).

Una sola vez, en https://developers.mercadolibre.com.ar/devcenter crear una app:
  - Redirect URI: una URL propia que puedas abrir (ej. https://localhost/) - se usa solo para leer el ?code=
  - Permisos: Publicación y sincronización = Lectura y escritura
  - Guardar APP ID (client id) y Clave secreta (client secret)

Variables de entorno (en tu máquina, jamás en el repo ni en el chat):
  ML_CLIENT_ID, ML_CLIENT_SECRET, ML_REDIRECT_URI

  python3 ml_token.py url                 # imprime el link; abrirlo logueado en Tutti Home y autorizar
  python3 ml_token.py canjear <code>      # code = lo que viene en ?code= de la URL a la que redirige
  python3 ml_token.py renovar             # el token dura 6 h; renueva con el refresh_token
  python3 ml_token.py mostrar             # imprime el access_token vigente (para ML_ACCESS_TOKEN)
"""
import os, sys, json, time, urllib.request, urllib.parse
CUENTA = os.environ.get("ML_CUENTA", "tutti-home")
ARCHIVO = os.path.expanduser(f"~/.fabrica_ml_{CUENTA}.json")       # fuera del repo
def env(k): return os.environ.get(k) or sys.exit(f"Falta la variable de entorno {k}")
def pedir(**datos):
    body = urllib.parse.urlencode(datos).encode()
    req = urllib.request.Request("https://api.mercadolibre.com/oauth/token", data=body,
        headers={"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: t = json.load(r)
    except urllib.error.HTTPError as e: sys.exit(f"ML rechazó el pedido: {e.code} {e.read().decode()[:300]}")
    t["vence_en"] = int(time.time()) + int(t.get("expires_in", 21600)) - 60
    fd = os.open(ARCHIVO, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: json.dump(t, f)
    print(f"Token guardado en {ARCHIVO} (user_id {t.get('user_id')}, vence en ~6 h)")
a = sys.argv[1:] or ["-h"]
if a[0] == "url":
    print("https://auth.mercadolibre.com.ar/authorization?" + urllib.parse.urlencode(
        {"response_type": "code", "client_id": env("ML_CLIENT_ID"), "redirect_uri": env("ML_REDIRECT_URI")}))
elif a[0] == "canjear" and len(a) > 1:
    pedir(grant_type="authorization_code", client_id=env("ML_CLIENT_ID"), client_secret=env("ML_CLIENT_SECRET"), code=a[1], redirect_uri=env("ML_REDIRECT_URI"))
elif a[0] == "renovar":
    t = json.load(open(ARCHIVO)); pedir(grant_type="refresh_token", client_id=env("ML_CLIENT_ID"), client_secret=env("ML_CLIENT_SECRET"), refresh_token=t["refresh_token"])
elif a[0] == "mostrar":
    t = json.load(open(ARCHIVO)); print(t["access_token"] if t["vence_en"] > time.time() else sys.exit("Token vencido: python3 ml_token.py renovar"))
else: print(__doc__)
