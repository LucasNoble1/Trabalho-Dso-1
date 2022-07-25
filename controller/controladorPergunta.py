import random
from model.pergunta import Pergunta
from view.telaPergunta import TelaPergunta
from DAOs.perguntaDao import PerguntaDAO

class ControladorPergunta:
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__pergunta_dao = PerguntaDAO()
        self.__tela = TelaPergunta(self)
        lista = []
        p1 = Pergunta("Dos personagens a seguir quem ja matou o Kuririn?", "Frieza", "irmao do Jorel", "Deadpool",
                      "101")
        p2 = Pergunta("Dos titulos a seguir, qual pertnce a um filme da trilogia original de Star Wars?",
                      "O Imperio Contra-Ataca", "O Despertar da Força", " A Ameaça Fantasma", "102")
        p3 = Pergunta("Em Star Wars, quem ficou responsavel pelo Treinamento de Anakin Skywalker?", "Obi-Wan Kenobi",
                      "Luke Skywalker", "Han-Solo", "103")
        p4 = Pergunta("Em Star Wars, quem era o Pai biologico da Princesa Leia?", "Anakin Skaywalker", "Yoda",
                      "Han-solo", "104")
        p5 = Pergunta("Nos filmes do MCU, que joia do infinito Doutor Estranho carregava em seu colar?", "Tempo",
                      "Espaço", "Alma", "105")
        p6 = Pergunta(
            "Nos filmes do MCU, qual foi a ultima joia do infinito que Thanos obteve, antes de dar seu estalo? ",
            "Mente", "Alma", "Poder", "106")
        p7 = Pergunta("Nos filmes do MCU, em qual filme Loki morre ?", "Vingadores:Guerra Infinita",
                      "Vingadores:Era de Ultron", "Thor: Ragnarok", "107")
        p8 = Pergunta("Em Harry Potter, qual feitiço causou a marca que Harry tem em sua testa?", "Avada Kedavra",
                      "Cruciatos", "Expelliarmus", "108")
        p9 = Pergunta("Em Harry Potter, qual dos itens a seguir  é uma das reliqueas da morte?",
                      "Capa da invisibilidade", "Nimbus2000", "Quadribol", "109")
        p10 = Pergunta("No primeiro episodio de  Stranger Things, que personagem foi levado para o mundo invertido?",
                       "Will", "Vecna", "11", "110")
        p11 = Pergunta("Qual dos pokemons a seguir é um pokemom do tipo Agua?", "Lapras", "Pikachu", "Jigglypuff",
                       "111")
        p12 = Pergunta("Qual é a evolucão do Pikachu?", "Raichu", "Pichu", "Charizard", "112")
        p13 = Pergunta("Em Star Trek,qual das frases a seguir é dita por Spock?", "Vida longa e prospera!",
                       "Que a força esteja com você!", "Ohana quer dizer familia", "113")
        p14 = Pergunta("Em Star Trek, qual o nome da nave pricipal pilotada pelo capitão Kirk² ",
                       "USS ENTERPRISE", "MILLENNIUM FALCON", " MILANO", "114")
        p15 = Pergunta("No Filme Liga da justiça, com ajuda de qual artefato o super-homem pode voltar a vida?",
                       "Caixa-Materna",
                       "kriptonita", "Esferas do Dragao", "115")
        p16 = Pergunta("Qual o nome do Pai do Naruto Uzumaki?", "Minato Namikaze", "Nagato Uzumaki",
                       "Tio Patinhas Uzumaki",
                       "116")

        lista.append(p1)
        lista.append(p2)
        lista.append(p3)
        lista.append(p4)
        lista.append(p5)
        lista.append(p6)
        lista.append(p7)
        lista.append(p8)
        lista.append(p9)
        lista.append(p10)
        lista.append(p11)
        lista.append(p12)
        lista.append(p13)
        lista.append(p14)
        lista.append(p15)
        lista.append(p16)
        for i in lista:
            self.adicionar_pergunta(i)


    def retorna(self):
        self.__controlador_principal.inicializa_sistema()

    #revela as perguntas, armazena as respostas
    #pede para o controladordo jogador alterar seus pontos
    #o codigo alterna a localização da alternativa correta (ACHO Q MERECE UM 10 EM)
    #pede para o controladorJogo alterar o jogador da vez e reinicia as mesmas perguntas para ele(s)
    #por fim inicia a funcao do fim do jogo
    def mostrar_pergunta_tela(self, jogador):
        jogador = jogador
        nome = str(jogador.nome)
        lista = [1, 2, 3]
        lista_perguntas = self.__controlador_principal.controlador_jogo.jogo.perguntas
        for i in range(self.__controlador_principal.controlador_jogo.jogo.qtd_turnos):
            aleatorio = random.choice(lista)
            obj_pergunta = random.choice(lista_perguntas)
            lista_perguntas.remove(obj_pergunta)
            pergunta = obj_pergunta.pergunta
            if aleatorio == 1:
                    alt1 = obj_pergunta.resposta
                    alt2 = obj_pergunta.alternativa1
                    alt3 = obj_pergunta.alternativa2

                    opcao = self.__tela.mostrar_pergunta(pergunta, alt1, alt2, alt3, nome)
                    if opcao == 1:
                        jogador.acertou()
                    else:
                        jogador.errou()

            if aleatorio == 2:
                alt1 = obj_pergunta.alternativa2
                alt2 = obj_pergunta.resposta
                alt3 = obj_pergunta.alternativa1

                opcao = self.__tela.mostrar_pergunta(pergunta, alt1, alt2, alt3, nome)
                if opcao == 2:
                    jogador.acertou()
                else:
                    jogador.errou()
            if aleatorio == 3:
                alt1 = obj_pergunta.alternativa2
                alt2 = obj_pergunta.alternativa1
                alt3 = obj_pergunta.resposta

                opcao = self.__tela.mostrar_pergunta(pergunta, alt1, alt2, alt3, nome)
                if opcao == 3:
                    jogador.acertou()
                else:
                    jogador.errou()



    def abre_tela(self):
        lista_opcoes = {1: self.criar_pergunta, 2: self.editar_pergunta,
                        3: self.excluir_pergunta,
                        0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela.tela_opcoes()]()

    def criar_pergunta(self):
        pergunta = 0
        while pergunta == 0:
            pergunta, resposta, alternativa1, alternativa2, codigo = self.__tela.criar_pergunta()
        duplicado = False
        for i in self.__pergunta_dao.get_all():
            if i.pergunta == pergunta:
                duplicado = True
        if duplicado == True:
            self.__tela.mostra_mensagem("Erro! Essa pergunta ja existe no sistema!")
        else:
            codigo = str(codigo)
            x = Pergunta(pergunta,resposta,alternativa1,alternativa2, codigo)
            self.adicionar_pergunta(x)
            self.__tela.mostra_mensagem("Pergunta adicionada com sucesso!!!")





    #remover inputs
    #metodo de alteração e não edição
    def editar_pergunta(self):
        x = self.__pergunta_dao.get_all()
        dados_pergunta = []
        for i in x:
            dados_pergunta.append({"codigo" : str(i.codigo),"pergunta": str(i.pergunta)})
        self.__tela.mostrar_todas_perguntas(dados_pergunta)
        codigo = self.__tela.pedir_pergunta()
        existe = False
        for i in self.__pergunta_dao.get_all():
            if i.codigo == codigo:
                obj = i
                existe = True
                pergunta = str(i.pergunta)
                resposta = str(i.resposta)
                alternativa1 = str(i.alternativa1)
                alternativa2 = str(i.alternativa2)
                alteracao, chave = self.__tela.editar_pergunta(pergunta, resposta, alternativa1, alternativa2)
                if chave == 0:
                    self.__tela.tela_opcoes()
                elif chave == 1:
                    novo_obj = Pergunta(alteracao, resposta, alternativa1, alternativa2, codigo)
                    self.__pergunta_dao.update(novo_obj)
                elif chave == 2:
                    novo_obj = Pergunta(pergunta, alteracao, alternativa1, alternativa2, codigo)
                    self.__pergunta_dao.update(novo_obj)
                elif chave == 3:
                    novo_obj = Pergunta(pergunta, resposta, alteracao, alternativa2, codigo)
                    self.__pergunta_dao.update(novo_obj)
                elif chave == 4:
                    novo_obj = Pergunta(pergunta, resposta, alternativa1, alteracao, codigo)
                    self.__pergunta_dao.update(novo_obj)

        if existe == False:
            self.__tela.mostra_mensagem("O codigo não corresponde a nenhuma pergunta!")

    def excluir_pergunta(self):
        x = self.__pergunta_dao.get_all()
        dados_pergunta = []
        for dado in x:
            dados_pergunta.append({'codigo': dado.codigo, 'pergunta': dado.pergunta})
        self.__tela.mostrar_todas_perguntas(dados_pergunta)
        codigo = str(self.__tela.pedir_pergunta())
        removeu = False
        for i in x:
            if i.codigo == codigo:
                removeu = True
                self.__pergunta_dao.remove(i)
                self.__tela.mostra_mensagem("A pergunta foi excluida com sucesso!")
        if removeu == False:
            self.__tela.mostra_mensagem("Aviso: esse codigo não pertence a nenhuma pergunta")

    def adicionar_pergunta(self, pergunta:Pergunta):
        self.__pergunta_dao.add(pergunta)

    @property
    def tela(self):
        return self.__tela
    @property
    def controlador_principal(self):
        return self.__controlador_principal
    @property
    def pergunta_dao(self):
        return self.__pergunta_dao
