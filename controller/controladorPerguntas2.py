import random
from model.pergunta import Pergunta
from view.telaPergunta import TelaPergunta

class ControladorPergunta:
    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__perguntas = []
        self.__tela_pergunta = TelaPergunta(self)


    #revela as perguntas, armazena as respostas
    #pede para o controladordo jogador alterar seus pontos
    #o codigo alterna a localização da alternativa correta (ACHO Q MERECE UM 10 EM)
    #pede para o controladorJogo alterar o jogador da vez e reinicia as mesmas perguntas para ele(s)
    #por fim inicia a funcao do fim do jogo
    def mostrar_pergunta_tela(self):
        lista = [1, 2, 3]
        for i in range(self.__controlador_principal.controlador_jogo.qtd_turnos_jogo()):
            aleatorio = random.choice(lista)
            if aleatorio == 1:
                for pergunta in self.__perguntas:
                    pergunta = pergunta.pergunta()
                    alt1 = pergunta.resposta()
                    alt2 = pergunta.alternativa1()
                    alt3 = pergunta.alternativa2()

                    opcao = self.__tela_pergunta.mostrar_pergunta(pergunta, alt1, alt2, alt3)
                    if opcao == 1:
                        self.__controlador_principal.contoladorjogo.jogador_da_vez_pontua()
                    else:
                        self.__controlador_principal.controladorjogo.jogador_da_vez_perde()

            if aleatorio == 2:
                for pergunta in self.__perguntas:
                    pergunta = pergunta.pergunta()
                    alt1 = pergunta.alternativa1()
                    alt2 = pergunta.resposta()
                    alt3 = pergunta.alternativa2()

                    opcao = self.__tela_pergunta.mostrar_pergunta(pergunta, alt1, alt2, alt3)
                    if opcao == 2:
                        self.__controlador_principal.contoladorjogo.jogador_da_vez_pontua()
                    else:
                        self.__controlador_principal.controladorjogo.jogador_da_vez_perde()
            if aleatorio == 3:
                for pergunta in self.__perguntas:
                    pergunta = pergunta.pergunta()
                    alt1 = pergunta.resposta()
                    alt2 = pergunta.alternativa2()
                    alt3 = pergunta.alternativa1()

                    opcao = self.__tela_pergunta.mostrar_pergunta(pergunta, alt1, alt2, alt3)
                    if opcao == 3:
                        self.__controlador_principal.contoladorjogo.jogador_da_vez_pontua()
                    else:
                        self.__controlador_principal.controladorjogo.jogador_da_vez_perde()
            self.__controlador_principal.controladorjogo.alterar_jogador_da_vez()
        self.__controlador_principal.controladorjogo.finaliza_jogo()



    @property
    def perguntas(self):
        return self.__perguntas
    #metodos que a alicia implementou no codigo dela
    def adicionar_pergunta(self, pergunta:Pergunta):
        pass

    def editar_pergunta(self):

        pass

    def excluir_pergunta(self):
        pass
