import random
from model.jogo import Jogo
from view.telaJogo import TelaJogo
from DAOs.jogoDao import JogoDAO


class ControladorJogo:
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__tela = TelaJogo(self)
        self.__jogo = None
        self.__jogo_dao = JogoDAO()





    #salva a quantidade de jogadores
    #inclui essa quantidade de jogadores no controladorJogadores
    #salva a quantidade de turnos
    #istancia um jogo usando a qtd_turnos e qtd_jogadores
    #chama a função inicia_jogo
    def inicia(self):
        num_jogadores  = self.__tela.tela_passo_um()
        if num_jogadores == 0:
            self.__controlador_principal.inicializa_sistema()
        qtd_turnos = self.__tela.tela_passo_dois()
        if qtd_turnos == 0:
            self.__controlador_principal.inicializa_sistema()
        self.__jogo = Jogo(num_jogadores, qtd_turnos)

        #inclui jogadores
        x = num_jogadores
        teste = len(self.__controlador_principal.controlador_jogador.jogador_dao.get_all())
        if teste == 0:
            while x != 0:
                jogador = self.__controlador_principal.controlador_jogador.incluir_jogador()
                self.__jogo.jogadores.append(jogador)
                x = x - 1
        else:
            while x != 0:
                escolha = self.__tela.selecao_jogadores()
                if escolha == 1:
                    jogador = self.__controlador_principal.controlador_jogador.incluir_jogador()
                    self.__jogo.jogadores.append(jogador)
                else:
                    y = 0
                    while y == 0:
                        y = 1
                        self.__controlador_principal.controlador_jogador.listar_jogadores()
                        cpf = self.__controlador_principal.controlador_jogador.tela.selecionar_jogador()
                        jogador = self.__controlador_principal.controlador_jogador.jogador_dao.get(cpf)
                        self.__jogo.jogadores.append(jogador)

                        if jogador == None:
                            y = 0
                        elif y == 0:
                            self.__controlador_principal.controlador_jogador.tela.mostra_mensagem("o cpf não corresponde a nenhum jogador, tente novamente")

                x = x - 1

        #seta numero de perguntas
        numero_jogadores = self.__jogo.numero_jogadores
        numero_perguntas = self.__jogo.qtd_turnos * numero_jogadores

        while numero_perguntas != 0:
            lista = self.__controlador_principal.controlador_pergunta.pergunta_dao.get_all()
            pergunta_aleatoria = random.choice(lista)
            self.__jogo.perguntas.append(pergunta_aleatoria)
            numero_perguntas = numero_perguntas - 1

        if num_jogadores == 1:
            self.iniciar_jogo_um_jogador()
        elif num_jogadores == 2:
            self.iniciar_jogo_dois_jogadores()
        elif num_jogadores == 3:
            self.iniciar_jogo_tres_jogadores()


    def iniciar_jogo_um_jogador(self):
        j1 = self.__jogo.um_jogador()
        nome = j1.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j1)
        self.finaliza_jogo()

    def iniciar_jogo_dois_jogadores(self):
        j1, j2 = self.__jogo.dois_jogadores()
        nome = j1.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j1)
        nome = j2.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j2)
        self.finaliza_jogo()

    def iniciar_jogo_tres_jogadores(self):
        j1, j2, j3 = self.__jogo.tres_jogadores()
        nome = j1.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j1)
        nome = j2.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j2)
        nome = j3.nome
        jogador_nome = str(nome)
        self.__tela.vez_do_jogador(jogador_nome)
        self.__controlador_principal.controlador_pergunta.mostrar_pergunta_tela(j3)
        self.finaliza_jogo()


    #informa a qtd de turnos do jogo
    def qtd_turnos_jogo(self):
        qtd = self.__jogo.qtd_turnos
        return qtd

    #finaliza o jogo
    #lista as pontuaçoes
    #pergunta se o jogador quer voltar ao inicio.
    #falta implementar metodos para remover todos os dados ja armazenados para garantir um recomeço sem erros.
    def finaliza_jogo(self):
        self.__jogo_dao.add(self.__jogo)
        self.__tela.mostra_mensagem(">>FIM DO JOGO<<")
        dados_jogadores = []
        for jogador in self.__jogo.jogadores:
            nome = str(jogador.nome)
            ac = str(jogador.acertos)
            er = str(jogador.erros)
            po = str(jogador.pontos())
            jogador.atualizar_status()
            dados_jogadores.append({"nome": nome, "acertos": ac,"erros": er,"pontos":po })
        self.__tela.pontuacao_jogo(dados_jogadores)
        self.__jogo = None
        self.__controlador_principal.inicializa_sistema()

    @property
    def jogo(self):
        return self.__jogo
    @property
    def tela(self):
        return self.__tela














