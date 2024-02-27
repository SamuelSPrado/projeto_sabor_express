# Projeto Restaurante

Este é um projeto Python que implementa classes para representar restaurantes e avaliações de clientes.

## Estrutura do Projeto

- `modelos/`: Contém os arquivos das classes Python.
- `README.md`: Este arquivo, contendo informações sobre o projeto.
- `.gitignore`: Arquivo de configuração do Git para ignorar arquivos e diretórios específicos.

## Funcionalidades

- `Restaurante`: Classe para representar um restaurante, incluindo nome, categoria, avaliações e estado de atividade.
- `Avaliacao`: Classe para representar uma avaliação de um cliente para um restaurante.

## Utilização

Para utilizar este projeto, siga os seguintes passos:

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter Python instalado.
3. Execute o arquivo `main.py` para ver uma demonstração do projeto.

## Exemplo de Uso

```python
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 5)
restaurante_praca.receber_avaliacao('Lais', 4)
restaurante_praca.receber_avaliacao('Emy', 2)

Restaurante.listar_restaurantes()