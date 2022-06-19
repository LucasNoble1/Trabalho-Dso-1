from jogo import Jogo
from telaJogo import TelaJogo
from controladorPrincipal import ControladorPrincipal

class ControladorJogo:
    def __init__(self, controlador : ControladorPrincipal):
        if isinstance(controlador, ControladorPrincipal):
            self.__controlador_principal = controlador
            self.__tela_jogo = TelaJogo(self)
            self.__jogo = None

    def inicia(self):
        self.__tela_jogo.mostrar_mensagem("============================")
        self.__tela_jogo.mostrar_mensagem("Passo 1: escolha a quantidade de jogadores")
        self.__tela_jogo.mostrar_mensagem("1 -- MODO SOLO")
        self.__tela_jogo.mostrar_mensagem("2 -- MODO BORA X1 ")
        self.__tela_jogo.mostrar_mensagem("3 -- MODO CADA UM POR SI")
        self.__tela_jogo.mostrar_mensagem("0 - voltar")
        self.__tela_jogo.mostrar_mensagem("\n")
        num_jogadores = self.__tela_jogo.le_num_inteiro("numero de jogadores:", [1, 2, 3, 0])



        # EU PAREI AQUUUUUUUUI < ====================================