🆘 Bot de Alerta de Emergencia
Descripción:
Este bot de Telegram está desarrollado en Python y permite enviar alertas rápidas por correo electrónico a un contacto de emergencia, con solo presionar un botón. Ideal para casos de peligro o asistencia urgente.

🚀 Funcionalidades:
Registrar correo de emergencia con /set_contact.

Enviar alerta con ubicación automática.

Funciona 24/7 en segundo plano.

Seguro: configuración protegida en archivo .env.

📦 Requisitos:
Python 3.11+

python-telegram-bot v20.7

geocoder, smtplib, dotenv

⚙️ Instalación:
git clone https://github.com/tu_usuario/nombre-del-repo.git
cd nombre-del-repo
pip install -r requirements.txt
🔐 Configuración:
TOKEN=tu_token_de_telegram
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=contraseña_app

Ejecuta el bot:
python bot_main.py
🧪 Uso:
Ejecuta /start para ver el menú.

Presiona "📨 ENVIAR ALERTA DE EMERGENCIA" para activar el envío.

Si no tienes correo configurado, usa /set_contact.

📁 Estructura del proyecto:
/bot_alerta
│
├── bot_main.py
├── contacto_utils.py
├── ubicacion_utils.py
├── .env
├── .gitignore
└── README.md

