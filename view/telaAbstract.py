from abc import ABC, abstractmethod

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass



    #garante que o valor inserido pelo usuario seja um valor valido
    #o return é necessario?~ nao sei
    def le_num_inteiro(self, mensagem: str = "" , inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
            except ValueError
                print("Valor incorreto: digite um numero valido")
                if interios_validos:
                    print("Validos validos:", inteiros_validos)
        return valor_lido

    def mostrar_mensagem(self, mensagem: str = ""):
        print("\n")
        print(mensagem)
        print("\n")

