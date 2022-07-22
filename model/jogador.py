

class Jogador():
    def __init__(self,nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__acertos = 0
        self.__erros = 0
        self.__jogou = False

    @property
    def cpf(self):
        return self.__cpf

    #calcula os pontos
    def pontos(self):
        e = self.__erros
        a = self.__acertos
        pontos = a - e
        return pontos

    #aumento os acertos
    def acertou(self):
        self.__acertos = self.__acertos + 1

    #diminui os erros
    def errou(self):
        self.__erros = self.__erros + 1

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

    @property
    def jogou(self):
        return self.__jogou

    @jogou.setter
    def jogou(self, condicao):
        self.__jogou = condicao
