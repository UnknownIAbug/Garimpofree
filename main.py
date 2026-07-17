import os
import telebot

from database.database import criar_banco, salvar_oportunidade
from ia.classificador import pontuar
from garimpo.buscador import buscar_oportunidades

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

criar_banco()


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🔎 GarimpoFree iniciado!\n\n"
        "Sistema inteligente de garimpo de oportunidades.\n\n"
        "Comandos disponíveis:\n"
        "/garimpo - Buscar oportunidades\n"
        "/status - Verificar sistema"
    )


@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(
        message,
        "✅ GarimpoFree funcionando corretamente."
    )


@bot.message_handler(commands=['garimpo'])
def garimpo(message):

    oportunidades = buscar_oportunidades()

    enviadas = 0

    for oportunidade in oportunidades:

        resultado = pontuar(
            oportunidade["titulo"] + " " + oportunidade["descricao"]
        )

        salvar_oportunidade(
            titulo=oportunidade["titulo"],
            descricao=oportunidade["descricao"],
            categoria=oportunidade["categoria"],
            cidade=oportunidade["cidade"],
            fonte=oportunidade["fonte"],
            link=oportunidade["link"],
            preco=oportunidade["preco"],
            score=resultado["score"],
            nivel=resultado["nivel"]
        )

        if resultado["score"] >= 8:

            bot.send_message(
                message.chat.id,
                f"""
🔥 OPORTUNIDADE ENCONTRADA

📦 Produto: {oportunidade['titulo']}

📝 Descrição:
{oportunidade['descricao']}

💰 Preço:
R$ {oportunidade['preco']}

⭐ Score:
{resultado['score']}

🏆 Classificação:
{resultado['nivel']}

📍 Cidade:
{oportunidade['cidade']}

🌐 Fonte:
{oportunidade['fonte']}

🔗 Link:
{oportunidade['link']}
"""
            )

            enviadas += 1

    bot.send_message(
        message.chat.id,
        f"""
✅ Garimpo finalizado!

Foram encontradas {enviadas} oportunidades.
"""
    )


bot.infinity_polling()
