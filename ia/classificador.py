# ia/classificador.py

PALAVRAS_ALTO_VALOR = [
    "iphone",
    "macbook",
    "notebook",
    "playstation",
    "ps5",
    "xbox",
    "nintendo",
    "geladeira",
    "ar condicionado",
    "bicicleta",
    "moto",
    "carro",
    "ferramenta",
    "máquina",
    "ouro",
    "prata",
    "relógio",
    "apple",
    "samsung",
    "dell",
    "lenovo"
]

PALAVRAS_OPORTUNIDADE = [
    "grátis",
    "gratuito",
    "doação",
    "desapego",
    "urgente",
    "mudança",
    "retirada",
    "liquidação",
    "queima",
    "abaixo",
    "metade",
    "promoção"
]


def pontuar(texto):

    texto = texto.lower()

    score = 0

    for palavra in PALAVRAS_ALTO_VALOR:
        if palavra in texto:
            score += 5

    for palavra in PALAVRAS_OPORTUNIDADE:
        if palavra in texto:
            score += 3

    if score >= 20:
        nivel = "🔥 EXCELENTE"

    elif score >= 12:
        nivel = "🟢 BOA"

    elif score >= 6:
        nivel = "🟡 MÉDIA"

    else:
        nivel = "⚪ BAIXA"

    return {
        "score": score,
        "nivel": nivel
    }
