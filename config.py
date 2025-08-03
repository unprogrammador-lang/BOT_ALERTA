from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables desde el archivo .env

TOKEN = os.getenv("TOKEN")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
