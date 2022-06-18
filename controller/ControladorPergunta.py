from pergunta import Pergunta
from telaPergunta import TelaPergunta

class Controlador_Pergunta:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, TelaPergunta):
    
    super().__init__(pergunta, resposta, alternativas, temas)
    self.__telaPergunta = TelaPergunta
    self.__pergunta = pergunta
    self.__perguntas = []
    self.__temas = []
    self.__alternativas = []
    self.__resposta = resposta

  @property
  def incluir_Pergunta(self):
    #verificar se a pta ja n existe (colocar os ids em um array?)

    dados_pergunta = self.__telaPergunta.cadastrar_pergunta()
    #tal qual o controlador_livros do pequeno exemplo mvc
    pergunta = Pergunta(dados_livro["id"], dados_livro["pergunta"], dados_livro["resposta"], dados_livro["alternativas"], dados_livro["tema"])
    self.__perguntas.append(pergunta)

    #caso pergunta n exista ainda
    if id.pergunta() not in perguntas:
      perguntas.append(id, pergunta, resposta, alternativas, temas) #arrumar isso aq, duplicado(linha 23)
    else:
      print("Pergunta já foi adicionada!")
      #Colocar uma exceção nessa parte




  @property
  def excluir_Pergunta(self):
    # verificar se a pta existe no array de perguntas
    if id.pergunta() not in perguntas:
      pergunta.remove(id, pergunta, resposta, alternativas, temas)

    else:
      print("Pergunta não foi adicionada ainda, por isso não é possivel excluir")

  @property
  def editar_Pergunta(self):
    
    #perguntar pro user o que ele quer editar na pergunta
    edicao = input()
      
    if input == id:
      self.__id.pergunta = id

    elif input == pergunta:
      self.__pergunta = pergunta

    elif input == resposta:
      self.__pergunta = pergunta

    elif input == alternativas:
      self.__alternativas.pergunta = alternativas

    elif input == temas:
      self.__temas.pergunta = temas

    else:
      print("Opção inválida")

  def retornar(self):
    self.__controladorPrincipal.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.cadastrar_pergunta, 2: self.alterar_pergunta, 3: self.lista_perguntas, 4: self.excluir_perguntas, 0: self.retornar}  


  def listar_perguntas_por_tema(self, tema):
    escolha_user = input()

    ''''''''
    #percorre o array de temas



    for t in temas:
      if tema.pergunta() == t:
        print("Essas são as perguntas desse tema: {}" .format(perguntas.t))
