

class Jogador():
    def __init__(self,nome: str):
        self.__nome = nome
        self.__acertos = 0
        self.__erros = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def acertos(self):
        return self.__acertos

    @property
    def erros(self):
        return self.__erros

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def pontos(self):
        pontos = self.__acertos - self.__erros
        return pontos