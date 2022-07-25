from model.jogador import Jogador
from view.telaJogador import TelaJogador
from DAOs.jogadorDao import JogadorDAO


class ControladorJogador:
    def __init__(self, controlador):
        self.__tela = TelaJogador(self)
        self.__jogador_dao = JogadorDAO()
        self.__controlador_principal = controlador

    #tela pede o nome, controlador adiciona o nome na listaDAO
    def incluir_jogador(self):
        nome, cpf = self.__tela.novo_jogador()
        player = Jogador(nome, cpf)
        for jogador in self.__jogador_dao.get_all():
            if jogador.nome == nome or jogador.codigo == cpf:
                self.__tela.mostra_mensagem("Cpf ou Nome indisponiveis: Impossivel adicionar jogador")
                return 0
        self.__jogador_dao.add(player)
        self.listar_jogadores()
        return player

    #tela mostra jogadores, pede o nome, controlador remove da listaDAO
    def excluir_jogador(self):
        while True:
            self.listar_jogadores()
            cpf = self.__tela.selecionar_jogador()
            for jogador in self.__jogador_dao.get_all():
                if jogador.codigo == cpf:
                    self.__jogador_dao.remove(cpf)
                    self.__tela.mostra_mensagem('o jogador foi removido do sistema!')
                    return jogador
                else:
                    self.__tela.mostra_mensagem("o cpf não corresponde a nenhum jogador, tente novamente")

    #tela mostra jogadores, pede o nome , pede o novo nome , altera o nome
    def alterar_jogador(self):
        self.listar_jogadores()
        cpf = self.__tela.selecionar_jogador()
        x = 0
        for jogador in self.__jogador_dao.get_all():
           if jogador.codigo == cpf:
               nome = self.__tela.novo_nome()
               x = 1
        if x == 0:
            self.__tela.mostra_mensagem("o cpf não corresponde a nenhum jogador, tente novamente")
        else:
            y = 0
            for jogador in self.__jogador_dao.get_all():
                if jogador.nome == nome:
                    self.__tela.mostra_mensagem("Cpf ou Nome indisponiveis: Impossivel adicionar jogador")
                    y = 1
            if y == 0:
                jogador_alterado = Jogador(nome, cpf)
                self.__jogador_dao.update(jogador_alterado)
                self.__tela.mostra_mensagem("O nome do jogador foi alterado com sucesso")

    #faz a tela mostrar todos os jogadores, ja convertendo para seus nomes e pontos para strings e ints.
    def listar_jogadores(self):
        dados_jogadores = []
        for jogador in self.__jogador_dao.get_all():
            dados_jogadores.append({"nome": str(jogador.nome), "cpf": str(jogador.codigo), "pontos": str(jogador.total_pontos())})
        self.__tela.mostrar_jogadores(dados_jogadores)



    #volta para a tela principal
    def retorna(self):
        self.__controlador_principal.inicializa_sistema()


    #abre a tela de opcoes do jogador
    #essa opçao foi removida do trabalho
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.excluir_jogador, 4: self.ranking,
                        0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()


    #organiza os jogadores por ordem de pontos ou media, mostra na tela.
    def ranking(self):
        num_jogadores = len(self.__jogador_dao.get_all())
        lista = self.__jogador_dao.get_all()
        lista_ordenada = []
        while num_jogadores != 0:
            jogador_do_top = lista[0]
            for jogador in self.__jogador_dao.get_all():
                if jogador.total_pontos() >= jogador_do_top.total_pontos():
                    jogador_do_top = jogador
            lista.remove(jogador_do_top)
            lista_ordenada.append(jogador_do_top)
            num_jogadores = num_jogadores - 1

        posicao = 0
        for jogador in lista_ordenada:
            posicao = posicao + 1
            nome = str(jogador.nome)
            t_erros = int(jogador.total_erros)
            t_acertos = int(jogador.total_acertos)
            t_pontos = int(jogador.total_pontos())
            t_jogos = int(jogador.total_jogos)
            if t_jogos == 0:
                t_jogos = 1
            p_media = float(t_pontos / t_jogos)
            self.__tela.ranking(posicao, nome, t_acertos, t_erros, t_pontos, t_jogos, p_media)
        '''    
        
        for jogador in lista_ordenada:
            posicao = posicao + 1
            t_jogos = int(jogador.total_jogos)
            t_pontos = int(jogador.total_pontos())
            acertos = int(jogador.total_acertos())
            erros = int(jogador.total_erros())
            if t_jogos == 0:
                t_jogos = 1
            p_media = float(t_pontos / t_jogos)
            dados_jogadores.append({"nome": str(jogador.nome), "acertos": acertos,
                                    "erros": erros ,"pontos": t_pontos,
                                    "jogos": t_jogos, "media": p_media})
        self.__tela.ranking(dados_jogadores)
        '''

    @property
    def jogador_dao(self):
        return self.__jogador_dao
    @property
    def tela(self):
        return self.__tela





