

class Jogador():
    def __init__(self,nome: str, codigo: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__acertos = 0
        self.__erros = 0
        self.__jogou = False
        self.__total_jogos = 0
        self.__total_erros = 0
        self.__total_acertos = 0

    def atualizar_status(self):
        self.__total_erros = self.__total_erros + self.__erros
        self.__total_acertos = self.__total_acertos + self.__acertos
        self.__total_jogos = self.__total_jogos + 1
        self.__erros = 0
        self.__acertos = 0

    @property
    def codigo(self):
        return self.__codigo

    #calcula os pontos
    def pontos(self):
        e = self.__erros
        a = self.__acertos
        pontos = a - e
        return pontos

    def total_pontos(self):
        e = self.__total_erros
        a = self.__total_acertos
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

    @property
    def total_acertos(self):
        return self.__total_acertos

    @property
    def total_erros(self):
        return self.__total_erros

    @property
    def total_jogos(self):
        return self.__total_jogos

    @total_jogos.setter
    def total_jogos(self,total_jogos):
        self.__total_jogos = total_jogos
    def media(self):
         x = self.total_pontos() / self.__total_jogos
         return x
