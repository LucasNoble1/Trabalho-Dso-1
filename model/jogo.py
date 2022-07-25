

class Jogo:
    def __init__(self, numero_jogadores: str, qtd_turnos: str):
        self.__jogadores = []
        self.__perguntas = []
        self.__numero_jogadores = numero_jogadores
        self.__qtd_turnos = qtd_turnos


    @property
    def jogadores(self):
        return self.__jogadores

    @property
    def perguntas(self):
        return self.__perguntas

    @property
    def numero_jogadores(self):
        return self.__numero_jogadores

    @property
    def qtd_turnos(self):
        return self.__qtd_turnos

    def um_jogador(self):
        j1 = self.__jogadores[0]
        return j1

    def dois_jogadores(self):
        j1 = self.__jogadores[0]
        j2 = self.__jogadores[1]
        return j1, j2

    def tres_jogadores(self):
        j1 = self.__jogadores[0]
        j2 = self.__jogadores[1]
        j3 = self.__jogadores[2]
        return j1, j2, j3


