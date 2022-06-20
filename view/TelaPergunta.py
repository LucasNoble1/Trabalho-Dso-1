from tela import Tela

class TelaPergunta(Tela):
    def __init__(self):
      #
      super()__init__()
      if isinstance(controlador, ControladorPergunta):
        #
        self.__controlador = controlador


    def tela_opcoes(self):
    print("-------- PERGUNTAS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Pergunta")
    print("2 - Alterar Pergunta")
    print("3 - Listar Perguntas")
    print("4 - Excluir Pergunta")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao


    def seleciona_pergunta(self):
      codigo = input("Código da pergunta que deseja selecionar: ")
    return codigo

    def mostra_livro(self, dados_livro):
    print("PERGUNTA: ", dados_pergunta["pergunta"])
    print("ID DA PERGUNTA: ", dados_pergunta["id"])
    print("TEMA DA PERGUNTA: ", dados_livro["tema"])
    print("RESPOSTA DA PERGUNTA: ", dados_livro["resposta"])
    print("ALTERNATIVAS DA PERGUNTA: ", dados_livro["alternativas"])
    print("\n")

      
    def mostrar_opcoes(self):
        print("-----Opçoes-----")
        print("--------------------------")
        print("1 - Cadastrar pergunta")
        print("2 - Excluir pergunta")
        print("3 - Editar pergunta")
        print("0 - voltar")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0]
        return opcao
