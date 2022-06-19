

class Jogo():
    def __init__(self, qtd_jogadores: str, tema_escolhido, qtd_turnos):
        self.__jogadores = {1: None, 2: None}
        self.__perguntas = []
        self.__qtd_jogadores = qtd_jogadores
        self.__tema_escolhido = tema_escolhido
        self.__qtd_turnos = qtd_turnos

    def jogador_da_vez(self):
        pass

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
    def tema_escolhido(self):
        return self.__tema_escolhido

    @property
    def qtd_turnos(self):
        return self.__qtd_turnos

    @qtd_jogadores.setter
    def qtd_jogadores(self, qtd_jogadores : int):
        self.__qtd_jogadores = qtd_jogadores


    @tema_escolhido.setter
    def tema_escolhido(self, tema_escolhido):
        self.__tema_escolhido = tema_escolhido


