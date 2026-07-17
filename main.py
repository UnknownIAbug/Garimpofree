import os
import telebot

from database.database import criar_banco, salvar_oportunidade
from ia.classificador import pontuar

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

criar_banco()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🔎 GarimpoFree iniciado!\n\n"
        "Comandos disponíveis:\n"
        "/status\n"
        "/garimpo"
    )


@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(
        message,
        "✅ Sistema funcionando corretamente."
    )


@bot.message_handler(commands=['garimpo'])
def garimpo(message):

    titulo = "Notebook Dell gratuito"

    descricao = "Doação de notebook Dell para retirada hoje."

    resultado = pontuar(titulo + " " + descricao)

    salvar_oportunidade(
        titulo=titulo,
        descricao=descricao,
        categoria="Informática",
        cidade="Corumbá",
        fonte="Teste",
        link="https://garimpofree.com",
        preco=0,
        score=resultado["score"],
        nivel=resultado["nivel"]
    )

    bot.reply_to(
        message,
        f"""🔎 Oportunidade encontrada!

📦 {titulo}

⭐ Score: {resultado['score']}

🏆 Classificação: {resultado['nivel']}

💾 Salva no banco de dados."""
    )


bot.infinity_polling()
