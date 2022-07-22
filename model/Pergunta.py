class Pergunta:
    def __init__(self, pergunta: str ,resposta : str , alternativa1 :str , alternativa2: str, codigo: str):
        self.__pergunta = pergunta
        self.__resposta = resposta
        self.__alternativa1 = alternativa1
        self.__alternativa2 = alternativa2
        self.__codigo = codigo


    @property
    def pergunta(self):
        return self.__pergunta

    @pergunta.setter
    def pergunta(self, pergunta):
        if isinstance(pergunta, str):
            self.__pergunta = pergunta
    @property
    def resposta(self):
        return self.__resposta

    @resposta.setter
    def resposta(self, resposta):
        self.__resposta = resposta

    @property
    def alternativa1(self):
        return self.__alternativa1

    @alternativa1.setter
    def alternativa1(self, alternativa1):
        self.__alternativa1 = alternativa1
    @property
    def alternativa2(self):
        return self.__alternativa2

    @alternativa2.setter
    def alternativa2(self,alternativa2):
        self.__alternativa2 = alternativa2
    @property
    def codigo(self):
        return self.__codigo
