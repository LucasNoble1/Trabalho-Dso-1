from controller.controladorJogo import ControladorJogo
from controller.controladorJogador import ControladorJogador
from controller.controladorPergunta import ControladorPergunta
from view.telaPrincipal import TelaPrincipal


class ControladorPrincipal:
    def __init__(self):
        #self.__instance = None
        self.__controlador_jogo = ControladorJogo(self)
        self.__controlador_jogador =ControladorJogador(self)
        self.__controlador_pergunta = ControladorPergunta(self)
        self.__tela_principal = TelaPrincipal(self)

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

    #abre a tela de opcoes do sistema
    def inicializa_sistema(self):
        lista_opcoes = {0: self.encerrar_sistema ,1: self.iniciar_jogo, 2: self.pergunta_opcoes, 3: self.jogador_opcoes, 4 : self.tutorial}

        continua = True
        while continua:
            lista_opcoes[self.__tela_principal.tela_inicial()]()

    #inicia o controladorjogo
    def iniciar_jogo(self):
        self.__controlador_jogo.inicia()
    #inicia as rodadas de perguntas
    def rodada_jogo(self):
        self.__controlador_pergunta.mostrar_pergunta()

    #sera implementado mais tarde
    def pergunta_opcoes(self):
        self.__controlador_pergunta.abre_tela()

    def jogador_opcoes(self):
        self.__controlador_jogador.abre_tela()

    def tutorial(self):
        self.__tela_principal.tutorial()

    def encerrar_sistema(self):
        exit(0)


