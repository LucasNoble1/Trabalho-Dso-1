from model.pergunta import Pergunta
from view.telaPergunta import TelaPergunta

class Controlador_Pergunta:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, Tela_Pergunta ):
    super().__init__(cpf, nome)
      self.__tela_Pergunta = Tela_Pergunta

  @property
  def incluir_Pergunta(self):
    #verificar se a pta ja n existe (colocar os ids em um array?)

    #caso pergunta n exista ainda
    if id.pergunta() not in perguntas:
      perguntas.append(id, pergunta, resposta, alternativas, temas)
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

  @property
  def temas(self):
    return self__temas


  def listar_perguntas_por_tema(self, tema):
    escolha_user = input()

    ''''''''
    #percorre o array de temas



    for t in temas:
      if tema.pergunta() == t:
        print("Essas são as perguntas desse tema: {}" .format(perguntas.t))