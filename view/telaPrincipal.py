from view.telaAbstract import Tela
from controller.controladorPrincipal import ControladorPrincipal

class TelaPrincipal(Tela):
    def __init__(self, controlador):
        super().__init__()
        if isinstance(controlador, ControladorPrincipal):
            self.__controlador = controlador




    def tela_inicial(self):
        print("========== Quiz ==========")
        print("Made by : Alicia and Lucas")
        print("==========================")
        print("\n")
        print("1 -- Iniciar o Jogo ")
        print("2 -- Cadastrar Perguntas")
        print("3 -- Tutorial ")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])
        return opcao

    #mostra um tutorial
    #volta sozinho tela inicial
    def tutorial(self):
        print("UM DIA,SERA IMPLEMENTADO UM TUTORIAL")
        print("Mas esse dia não é HOJE")
        print("")
        self.tela_inicial()


