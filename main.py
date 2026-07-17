import telebot
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🔎 GarimpoFree iniciado!\n\n"
        "Sistema de busca de oportunidades ativo.\n\n"
        "Comandos:\n"
        "/garimpo - iniciar busca\n"
        "/status - verificar sistema"
    )

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(
        message,
        "✅ GarimpoFree online!"
    )

@bot.message_handler(commands=['garimpo'])
def garimpo(message):
    bot.reply_to(
        message,
        "🔍 Iniciando garimpo de oportunidades..."
    )

bot.infinity_polling()
