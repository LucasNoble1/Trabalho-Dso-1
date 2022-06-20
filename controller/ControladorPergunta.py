from pergunta import Pergunta
from telaPergunta import TelaPergunta
from controladorPrincipal import ControladorPrincipal

class Controlador_Pergunta:
  
  def __init__(self, ControladorPrincipal, telaPergunta, pergunta, resposta, alternativas, temas):
    
    super().__init__(pergunta, resposta, alternativas, temas)
    self.__telaPergunta = TelaPergunta
    self.__pergunta = pergunta
    self.__perguntas = []
    self.__temas = []
    self.__alternativas = []
    self.__resposta = resposta
    self.__controladorPrincipal = ControladorPrincipal

  
  def incluir_Pergunta(self, id, pergunta, resposta, alternativas, temas):

    dados_pergunta = self.__telaPergunta.cadastrar_pergunta()
    #tal qual o controlador_livros do pequeno exemplo mvc

    if (id.pergunta() not in self.__perguntas):
      
      pergunta = Pergunta(dados_pergunta["id"], dados_pergunta["pergunta"], dados_pergunta["resposta"], dados_pergunta["alternativas"], dados_pergunta["tema"])
      self.__perguntas.append(pergunta)
    #caso pergunta n exista ainda
    else:
      self.__telaAbstract.mostrar_mensagem("ATENCAO: Pergunta ja existe")
      




  
  def excluir_Pergunta(self):
    self.mostrar_pergunta()
    id_pergunta = self.__telaPergunta.seleciona_pergunta()
    pergunta = self.pega_pergunta_por_id(id_pergunta)

    if(pergunta is not None):
      self.__perguntas.remove(pergunta)
      self.lista_pergunta()
    else:
      self.__telaAbstract.mostrar_mensagem("ATENCAO: Pergunta não existente")


  def lista_pergunta(self):
    for pergunta in self.__perguntas:
      self.__telaPergunta.mostra_pergunta({"Pergunta": pergunta.pergunta, "codigo": pergunta.id, "tema": pergunta.tema, "resposta": pergunta.resposta, "alternativas": pergunta.alternativas})    

  
  def editar_Pergunta(self):
    
    #perguntar pro user o que ele quer editar na pergunta
    self.listaPerguntas()
    codigo_Pergunta = self.__telaPergunta.seleciona_pergunta()
    pergunta = self.mostra_pergunta_por_id(id)

    

    #id: int , pergunta: str, resposta: str , alternativas: [], tema: str
    if(pergunta is not None):
      novos_dados_pergunta = self.__telaPergunta.mostra_pergunta_por_id()
      pergunta.id = novos_dados_pergunta["id"]
      pergunta.id = novos_dados_pergunta["pergunta"]
      pergunta.id = novos_dados_pergunta["resposta"]
      pergunta.id = novos_dados_pergunta["alternativas"]
      pergunta.id = novos_dados_pergunta["tema"]
      self.mostrar_pergunta()
    else:
      self.__telaAbstract.mostrar_mensagem("ATENCAO: Pergunta não existente")

  def retornar(self):
    self.__controladorPrincipal.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_pergunta, 2: self.alterar_pergunta, 3: self.listar_perguntas, 4: self.excluir_perguntas, 0: self.retornar}  


  def listar_perguntas_por_tema(self, tema):
    for pergunta in self.__perguntas:
      if(pergunta.tema == tema):
        return pergunta
    return None
    #percorre o array de temas


  def pega_pergunta_por_id(self, id: int):
    for pergunta in self.__perguntas:
      if(pergunta.id == id):
        return pergunta
    return None
