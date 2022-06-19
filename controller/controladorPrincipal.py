from controladorJogo import ControladorJogo
from controladorJogador import ControladorJogador
from controladorPergunta import ControladorPergunta
from telaPrincipal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.__controlador_jogo = ControladorJogo(self)
        self.__controlador_jogador =ControladorJogador(self)
        self.__controlador_pergunta = ControladorPergunta(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_jogo(self):
        return self.__controlador_jogo
    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
    @property
    def controlador_pergunta(self):
        return self.__controlador_pergunta
    @property
    def tela_principal(self):
        return self.__tela_principal

    def inicializa_sistema(self):
        self.__.tela_principal.tela_inicial()

    def iniciar_jogo(self):
        self.__controlador_jogo.inicia()
