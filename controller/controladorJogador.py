from model.jogador import Jogador
from view.telaJogador import TelaJogador


class ControladorJogador:
    def __init__(self, controlador):
        self.__tela = TelaJogador(self)
        self.__jogadores = []
        self.__controlador_principal = controlador

    #reseta os jogadores do controlador
    def zerar_jogadores(self):
        self.__jogadores.clear()

    #tela pede o nome, controlador adiciona o nome na lista
    def incluir_jogador(self):
        x = 1
        while x == 1:
            x = 2
            nome = self.__tela.nome_jogador("Adicione um jogador")
            for jogador in self.__jogadores:
                if jogador.nome == nome:
                    self.__tela.mostrar_mensagem("Jogador ja existe!!!!!")
                    x = 1
                else:
                    self.__jogadores.append(Jogador(nome))
        self.__tela.mostrar_mensagem("jogador adicionado com sucesso!")


    #tela mostra jogadores, pede o nome, controlador remove da lista
    #esta utilidade foi removida do trabalho
    def excluir_jogador(self):
        x = 1
        while x == 1:
            self.listar_jogadores()
            nome = self.__tela.nome_jogador("Excluir um jogador")
            for jogador in self.__jogadores:
                if jogador.nome() == nome:
                    self.__jogadores.remove(jogador(nome))
                    self.__tela.mostrar_mensagem("Jogador Excluido com sucesso")
                    x = 2
        self.__tela.mostrar_opcoes()



    #tela mostra jogadores, pede o nome , pede o novo nome , altera o nome
    #esta utilidade foi removida do trabalho
    def alterar_jogador(self):
        x = 1
        while x == 1:
            self.listar_jogadores()
            nome = self.__tela.nome_jogador("Digite o nome do jogador para ser alterado:")
            for jogador in self.__jogadores:
                if jogador.nome == nome:
                    novo_nome = self.__tela.nome_jogador("digite um novo nome")
                    jogador.nome(novo_nome)
                    x = 2
            if x == 2:
                self.__tela.mostrar_mensagem("Nome do jogador alterado com sucesso!!")
            else:
                self.__tela.mostrar_mensagem("jogador não encontrado :C ")
                self.__tela.mostrar_mensagem("tente escrever o nome corretamente ")
        self.__tela.mostrar_opcoes()




    #faz a tela mostrar todos os jogadores, ja convertendo para seus nomes e pontos para strings e ints.
    def listar_jogadores(self):
        for jogador in self.__jogadores:
            nome = str(jogador.nome())
            pontos = int(jogador.pontos())
            self.__tela.mostrar_jogador(nome,pontos)



    #volta para a tela principal
    def retorna(self):
        self.__controlador_principal.tela_principal()


    #abre a tela de opcoes do jogador
    #essa opçao foi removida do trabalho
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.pontuacao_jogadores, 4: self.excluir_jogador,
                        0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()

    #nao lembro pq eu fiz essa função :)
    def pontuacao_jogadores(self):
        if self.__jogadores == []:
            self.__tela.mostrar_mensagem("Ainda não existem jogadores cadastrados!")
            self.__tela.mostrar_mensagem("Adicione um jogador para utilizar essa função!")
        else:
            self.listar_jogadores()

    @property
    def jogadores(self):
        return self.__jogadores
            for jogador in self.__jogadores:
                if jogador.nome() == nome:
                    self.__jogadores.remove(jogador(nome))
                    self.__tela.mostrar_mensagem("Jogador Excluido com sucesso")
                    x = 2
        self.__tela.mostrar_opcoes()



    #tela mostra jogadores, pede o nome , pede o novo nome , altera o nome
    #esta utilidade foi removida do trabalho
    def alterar_jogador(self):
        x = 1
        while x == 1:
            self.listar_jogadores()
            nome = self.__tela.nome_jogador("Digite o nome do jogador para ser alterado:")
            for jogador in self.__jogadores:
                if jogador.nome == nome:
                    novo_nome = self.__tela.nome_jogador("digite um novo nome")
                    jogador.nome(novo_nome)
                    x = 2
            if x == 2:
                self.__tela.mostrar_mensagem("Nome do jogador alterado com sucesso!!")
            else:
                self.__tela.mostrar_mensagem("jogador não encontrado :C ")
                self.__tela.mostrar_mensagem("tente escrever o nome corretamente ")
        self.__tela.mostrar_opcoes()




    #faz a tela mostrar todos os jogadores, ja convertendo para seus nomes e pontos para strings e ints.
    def listar_jogadores(self):
        for jogador in self.__jogadores:
            nome = str(jogador.nome())
            pontos = int(jogador.pontos())
            self.__tela.mostrar_jogador(nome,pontos)



    #volta para a tela principal
    def retorna(self):
        self.__controlador_principal.tela_principal()


    #abre a tela de opcoes do jogador
    #essa opçao foi removida do trabalho
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.pontuacao_jogadores, 4: self.excluir_jogador,
                        0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()

    #nao lembro pq eu fiz essa função :)
    def pontuacao_jogadores(self):
        if self.__jogadores == []:
            self.__tela.mostrar_mensagem("Ainda não existem jogadores cadastrados!")
            self.__tela.mostrar_mensagem("Adicione um jogador para utilizar essa função!")
        else:
            self.listar_jogadores()

    @property
    def jogadores(self):
        return self.__jogadores





