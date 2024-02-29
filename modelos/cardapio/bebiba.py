from modelos.cardapio.item_cardapio import ItemCardapio

class Bebiba(ItemCardapio):
    def __init__(self, nome, preco, tamanho: str):
        super().__init__(nome,preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self.preco * 0.05)