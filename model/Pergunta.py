class Pergunta():
  def __init__(self,id: int , pergunta: str, resposta: str , alternativas: [], tema: str):
        self.__id = id
        self.__pergunta = pergunta
        self.__resposta = resposta
        self.__alternativas = []
        self.__tema = tema

  #getters

  @property
  def id(self):
    return self.__id

  @property
  def pergunta(self):
    return self.__pergunta

  @property
  def resposta(self):
    return self.__resposta

  @property
  def alternativas(self):
    return self.__alternativas

  @property
  def tema(self):
    return self.__tema 


  #setters
  @id.setter
  def id(self, id: int):
    self.__id = id 

  @pergunta.setter
  def pergunta(self, pergunta: str):
    self.__pergunta = pergunta

  @resposta.setter
  def resposta(self, resposta: str):
    self.__pergunta = resposta

  @alternativas.setter
  def alternativas(self, alternativas: []):
    self.__alternativas = alternativas

  @tema.setter
  def tema(self, tema: str):
    self.__tema = tema  
  
