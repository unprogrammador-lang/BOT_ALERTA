import json
import os

DB_FILE = "db_contacto.json"

def cargar_contacto():
    if not os.path.exists(DB_FILE):
        return None
    with open(DB_FILE, "r") as f:
        data = json.load(f)
        return data.get("correo")

def guardar_contacto(correo):
    with open(DB_FILE, "w") as f:
        json.dump({"correo": correo}, f)

def contacto_existe():
    return os.path.exists(DB_FILE) and cargar_contacto() is not None
