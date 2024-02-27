from modelos.restaurante import Restaurante

def main():
    restaurante_praca = Restaurante('praça', 'Gourmet')
    restaurante_praca.receber_avaliacao('Gui', 5)  # Nota válida
    restaurante_praca.receber_avaliacao('Lais', 4)  # Nota válida
    restaurante_praca.receber_avaliacao('Emy', 2)   # Nota válida

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()