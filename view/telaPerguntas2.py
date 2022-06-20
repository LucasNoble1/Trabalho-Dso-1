from view.telaAbstract import Tela
from controller.controladorPergunta2 import ControladorPergunta2

class TelaPergunta(Tela):
    def __init__(self, controlador):
        super().__init__()
        if isinstance(controlador, ControladorPergunta2):
            self.__controlador = ControladorPergunta2()


    #metodo que mostra a pergunta e suas alternativas durante o jogo
    def mostrar_pergunta(self, pergunta, alt1, alt2, alt3):
        print("=============================")
        print("          PERGUNTA:         ")
        print(">", pergunta, "<")
        print("=============================")
        print("    ESCOLHA UMA ALTERNATIVA    ")
        print("1 --", alt1)
        print("2 --", alt2)
        print("3 --", alt3)
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])

        return opcao
