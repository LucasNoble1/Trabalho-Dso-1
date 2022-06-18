from Jogador.py import Jogador
from TelaJogador.py import TelaJogador
from controladorPrincipal import ControladorPrincipal


class ControladorJogador():
    def __init__(self, controlador : ControladorPrincipal):
        self.__tela = TelaJogador()
        self.__jogadores = []
        if isinstance(controlador, ControladorPrincipal):
            self.__controlador_principal = controlador



    #tela pede o nome, controlador adiciona o nome na lista.
      def incluir_jogador(self):
        x = 1
        while x == 1:
            x = 2
            nome = self.__tela.nome_jogador("Adicione um jogador")
            for jogador in self.__jogadores:
                if jogador.nome == nome:
                    self.__tela.mostrar_mensagem("Jogador ja existe!!!!!")
                    x = 1
        self.__jogadores.append(Jogador(nome))
        self.__tela.mostrar_mensagem("jogador adicionado com sucesso!")
        self.__tela.mostrar_opcoes()

   #tela mostra jogadores, pede o nome, controlador remove da lista
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




    #faz a tela mostrar todos os jogadores, ja convertendo para string :)
    def listar_jogadores(self):
        for jogador in self.__jogadores:
            nome = jogador.nome()
            self.__tela.mostrar_jogador(nome)

    #volta para a tela principal
    def retorna(self):
        self.__controlador_principal.abre_tela()


    #abre a tela de opcoes do jogador
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.pontuacao_jogadores, 4: self.excluir_jogador,
                        0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()

    def pontuacao_jogador(self,jogador):
        pass

    def pontuacao_jogadores(self):
        if self.__jogadores == []:
            self.__tela.mostrar_mensagem("Ainda não existem jogadores cadastrados!")
            self.__tela.mostrar_mensagem("Adicione um jogador para utilizar essa função!")
        else:
            self.listar_jogadores()
            self.__tela.mostrar_opcoes()





