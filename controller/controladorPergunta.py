import random
from model.pergunta import Pergunta
from view.telaPergunta import TelaPergunta
from DAOs.perguntaDao import PerguntaDAO

class ControladorPergunta:
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__pergunta_dao = PerguntaDAO()
        self.__tela = TelaPergunta(self)


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
