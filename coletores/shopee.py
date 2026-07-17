from .base import ColetorBase


class ColetorShopee(ColetorBase):

    def buscar(self):
        produtos = [
            {
                "nome": "Produto exemplo Shopee",
                "preco": 29.90,
                "link": "https://shopee.com.br",
                "categoria": "teste"
            }
        ]

        return produtos
