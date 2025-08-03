import logging
import asyncio
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
from contacto_utils import guardar_contacto, cargar_contacto, contacto_existe
from ubicacion_utils import enviar_alerta_correo
from config import TOKEN  # ✅ Importamos desde config.py

logging.basicConfig(level=logging.INFO)

ESPERANDO_CORREO = 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📨 ENVIAR ALERTA DE EMERGENCIA"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🆘 Bienvenido al Bot de Alerta. Elija una opción:", reply_markup=reply_markup)

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    if texto == "📨 ENVIAR ALERTA DE EMERGENCIA":
        if not contacto_existe():
            await update.message.reply_text("🔧 No hay correo de emergencia registrado. Usa /set_contact para configurarlo.")
        else:
            await update.message.reply_text("✅ Enviando alerta...")
            ok, msg = enviar_alerta_correo()
            await update.message.reply_text(msg)

async def set_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 Por favor, ingrese el correo de emergencia:")
    return ESPERANDO_CORREO

async def guardar_correo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correo = update.message.text.strip()
    guardar_contacto(correo)
    await update.message.reply_text(f"✅ Correo guardado exitosamente: {correo}")
    return ConversationHandler.END

async def cancelar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Cancelado.")
    return ConversationHandler.END

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()  # ✅ Ya no usamos config.json

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("set_contact", set_contact)],
        states={ESPERANDO_CORREO: [MessageHandler(filters.TEXT & ~filters.COMMAND, guardar_correo)]},
        fallbacks=[CommandHandler("cancel", cancelar)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

print("🤖 Bot ejecutándose...")
app.run_polling()


