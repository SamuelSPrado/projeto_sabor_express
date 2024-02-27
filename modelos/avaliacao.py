class Avaliacao:
    def __init__(self, cliente: str, nota: float) -> None:
        """
        Inicializa uma instância de Avaliacao.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída à avaliação (entre 1 e 5)
        """
        if not isinstance(cliente, str):
            raise TypeError("O cliente deve ser uma string.")
        if not isinstance(nota, (int, float)):
            raise TypeError("A nota deve ser um número.")
        if nota < 1 or nota > 5:
            raise ValueError("A nota deve estar entre 1 e 5.")

        self._cliente = cliente
        self._nota = nota