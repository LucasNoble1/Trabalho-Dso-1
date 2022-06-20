from controller.controladorJogo import ControladorJogo
from controller.controladorJogador import ControladorJogador
from controller.controladorPergunta import ControladorPergunta
from controller.controladorPergunta2 import ControladorPergunta2
from view.telaPrincipal import TelaPrincipal

class ControladorPrincipal:
    def __init__(self):
        self.__controlador_jogo = ControladorJogo(self)
        self.__controlador_jogador =ControladorJogador(self)
        self.__controlador_pergunta = ControladorPergunta(self)
        self.__controlador_pergunta2 = ControladorPergunta2(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_jogo(self):
        return self.__controlador_jogo
    @property
    def controlador_jogador(self):
        return self.__controlador_jogador
    @property
    def controlador_pergunta(self):
        return self.__controlador_pergunta2
    @property
    def tela_principal(self):
        return self.__tela_principal

    #abre a tela de opcoes do sistema
    def inicializa_sistema(self):
        lista_opcoes = {1: self.iniciar_jogo, 2: self.adicionar_pergunta, 3: self.tutorial}

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
    def adicionar_pergunta(self):
        self.__controlador_pergunta.abre_tela()

    #mostra o tutorial... que ainda n foi implementado
    def tutorial(self):
        self.__tela_principal.tutorial()


