from telaAbstract import Tela
from controladorPrincipal import ControladorPrincipal

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
        #print("3 -- Tutorial ")
        #print("0 -- Logout")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2])


