

class Perguntas2:
    def __init__(self, pergunta: str ,resposta : str , alternativa1 :str , alternativa2):
        self.__pergunta = pergunta
        self.__resposta = resposta
        self.__alternativa1 = alternativa1
        self.__alternativa2 = alternativa2

    @property
    def pergunta(self):
        return self.__pergunta
    @property
    def resposta(self):
        return self.__resposta
    @property
    def alternativa1(self):
        return self.__alternativa1
    @property
    def alternativa2(self):
        return self.__alternativa2

