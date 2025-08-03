import json
import smtplib
from email.message import EmailMessage
import requests
from contacto_utils import cargar_contacto
from config import EMAIL_USER, EMAIL_PASS  # 👈 Nuevo import

def obtener_ubicacion():
    try:
        res = requests.get("http://ip-api.com/json/")
        data = res.json()
        lat = data.get("lat")
        lon = data.get("lon")
        ciudad = data.get("city", "Desconocida")
        region = data.get("regionName", "")
        pais = data.get("country", "")
        link_maps = f"https://maps.google.com/?q={lat},{lon}"
        ubicacion_texto = f"{ciudad}, {region}, {pais}"
        return ubicacion_texto, link_maps
    except:
        return "Ubicación no disponible", ""

def enviar_alerta_correo():
    correo_destino = cargar_contacto()
    if not correo_destino:
        return False, "No hay correo registrado."

    ubicacion, link = obtener_ubicacion()

    msg = EmailMessage()
    msg['Subject'] = "🆘 Alerta de Emergencia"
    msg['From'] = EMAIL_USER                     # ✅ Usamos lo del .env
    msg['To'] = correo_destino

    msg.set_content(
        f"🆘 AUXILIO, NECESITO AYUDA\n📍 Estoy en: {ubicacion}\n🌐 {link}"
    )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)   # ✅ También aquí
            smtp.send_message(msg)
        return True, f"✅ Se ha enviado la ubicación al correo de emergencia: {correo_destino}"
    except Exception as e:
        return False, f"❌ Error al enviar correo: {str(e)}"
