

class Jogo():
    def __init__(self, qtd_jogadores: str, qtd_turnos):
        self.__jogadores = []
        self.__perguntas = []
        self.__qtd_jogadores = qtd_jogadores
        self.__qtd_turnos = qtd_turnos
        self.__jogador_da_vez = self.__jogadores[0]

    @property
    def jogador_da_vez(self):
        return self.__jogador_da_vez

    #alterao para o proximo jogador
    def alterar_jogador_da_vez(self):
        x = 0
        if self.__jogador_da_vez == self.__jogadores[0]:
            x = 1
        elif self.__jogador_da_vez == self.__jogadores[1]:
            x = 2
        elif x == 1:
            self.__jogador_da_vez = self.__jogadores[1]
        elif x == 2:
            self.__jogador_da_vez = self.__jogadores[2]
        return self.__jogador_da_vez

    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def perguntas(self):
        return self.__perguntas

    @property
    def qtd_jogares(self):
        return self.__qtd_jogadores


    @property
    def qtd_turnos(self):
        return self.__qtd_turnos

    @qtd_jogadores.setter
    def qtd_jogadores(self, qtd_jogadores : int):
        self.__qtd_jogadores = qtd_jogadores




