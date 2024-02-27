from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características."""
    
    restaurantes = []

    def __init__(self, nome: str, categoria: str) -> None:
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self.__nome = nome.title()
        self.__categoria = categoria.upper()
        self.__ativo = False
        self.__avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self) -> str:
        """Retorna uma representação em string do restaurante."""
        return f'{self.__nome} | {self.__categoria}'
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self) -> str:
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self.__ativo else '☐'
    
    def alternar_estado(self) -> None:
        """Alterna o estado de atividade do restaurante."""
        self.__ativo = not self.__ativo

    def receber_avaliacao(self, cliente: str, nota: float) -> None:
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5)
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self.__avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self) -> float:
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self.__avaliacoes:
            return 0.0
        soma_das_notas = sum(avaliacao.nota for avaliacao in self.__avaliacoes)
        quantidade_de_notas = len(self.__avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    @property
    def nome(self) -> str:
        """Retorna o nome do restaurante."""
        return self.__nome

    @property
    def categoria(self) -> str:
        """Retorna a categoria do restaurante."""
        return self.__categoria