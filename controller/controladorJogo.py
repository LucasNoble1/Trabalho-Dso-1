from model.jogo import Jogo
#from controller.controladorPrincipal import ControladorPrincipal
from view.telaJogo import TelaJogo

class ControladorJogo:
    def __init__(self, controlador ):
        #if isinstance(controlador, ControladorPrincipal):
        self.__controlador_principal = controlador
        self.__tela_jogo = TelaJogo(self)
        self.__jogo = None

    #chama a proxima função
    def inicia(self):
        self.passo_um()

    #salva a quantidade de jogadores
    #inclui essa quantidade de jogadores no controladorJogadores
    #salva a quantidade de turnos
    #istancia um jogo usando a qtd_turnos e qtd_jogadores
    #chama a função inicia_jogo
    def passo_um(self):
        self.__tela_jogo.mostrar_mensagem("============================")
        self.__tela_jogo.mostrar_mensagem("Passo 1: Escolha a quantidade de jogadores")
        self.__tela_jogo.mostrar_mensagem("1 -- MODO SOLO")
        self.__tela_jogo.mostrar_mensagem("2 -- MODO BORA X1 ")
        self.__tela_jogo.mostrar_mensagem("3 -- MODO CADA UM POR SI")
        self.__tela_jogo.mostrar_mensagem("0 - VOLTAR")
        self.__tela_jogo.mostrar_mensagem("\n")
        qtd_jogadores = self.__tela_jogo.le_num_inteiro("numero de jogadores:", [1, 2, 3, 0])
        if qtd_jogadores == 0:
            self.__controlador_principal.tela_principal.tela_inicial()
        x = qtd_jogadores
        while x != 0:
            self.__controlador_principal.controlador_jogador.incluir_jogador()
            x = x - 1
        self.passo_dois()

    def passo_dois(self):
        self.__tela_jogo.mostrar_mensagem("==========================")
        self.__tela_jogo.mostrar_mensagem("Passo 2 : Escolha a quantidade de turnos")
        self.__tela_jogo.mostrar_mensagem(" 1 --Iniciar um jogo com 3 turnos")
        self.__tela_jogo.mostrar_mensagem(" 2 --Iniciar um Jogo com 5 turnos")
        self.__tela_jogo.mostrar_mensagem(" 3 --Iniciar um jogo com 7 turnos")
        self.__tela_jogo.mostrar_mensagem("\n")
        qtd_turnos = self.__tela_jogo.le_num_inteiro("Digite o numero da opção desejada:", [1, 2, 3])
        if qtd_turnos == 0:
            self.passo_um()
        else:
            self.__jogo = Jogo(qtd_jogadores, qtd_turnos)
            self.inicia_jogo()

    #adiciona os jogadores do controladorJogadores na lisata do jogo
    #adiciona as perguntas do controladorPerguntas2 na lista do  jogo
    #BOATOS Q TA ERRADO KK
    #informa qual o jogador da vez
    #pede para o jogador da vez iniciar o jogo
    #chama o controlador das perguntas que continua o jogo

    def inicia_jogo(self):
        for jogador in self.__controlador_principal.controlador_jogador.jogadores():
            self.__jogo.jogadores.append(jogador)
        qtd_turnos = self.__jogo.qtd_turnos()
        while qtd_turnos != 0:
            for pergunta in self.__controlador_principal.controlador_pergunta.perguntas():
                self.__jogo.perguntas.append(pergunta)
            qtd_turnos =- 1


        jogador = str(self.__jogo.jogador_da_vez)
        self.__tela_jogo.mostrar_mensagem("==========================")
        self.__tela_jogo.mostrar_mensagem("VEZ DO JOGADOR:", jogador)
        ok = self.__tela_jogo.le_num_inteiro("DIGITE 1 para iniciar:",[1])
        if ok == 1:
            self.__controlador_principal.controlador_pergunta2.mostrar_pergunta_tela()

    #informa a qtd de turnos do jogo
    def qtd_turnos_jogo(self):
        qtd = self.__jogo.qtd_turnos()
        return qtd

    #finaliza o jogo
    #lista as pontuaçoes
    #pergunta se o jogador quer voltar ao inicio.
    #falta implementar metodos para remover todos os dados ja armazenados para garantir um recomeço sem erros.
    def finaliza_jogo(self):
        self.__tela_jogo.mostrar_mensagem("=========================")
        self.__tela_jogo.mostrar_mensagem("> FIM DO JOGO <")
        self.__tela_jogo.mostrar_mensagem(">Confira a pontuação<")
        self.__controlador_principal.controlador_jogador.listar_jogadores()
        opcao = self.__tela_jogo.le_num_inteiro("1 - digite 1 para voltar ao inicio",[1])
        if opcao == 1:
            self.__controlador_principal.inicializa_sistema()

    #instancia um jogador e aumenta em um seus acertos
    def jogador_da_vez_pontua(self):
        jogador = self.__jogo.jogador_da_vez
        jogador.acertou()

    #instancia um jogador e aumenta em um seus erros.
    def jogador_da_vez_perde(self):
        jogador = self.__jogo.jogador_da_vez
        jogador.errou()















