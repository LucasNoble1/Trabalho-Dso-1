from view.telaAbstract import Tela
from controller.controladorPergunta import ControladorPergunta

class TelaPergunta(Tela):
    def __init__(self, controlador: ControladorPergunta):
        super().__init__()
        self.__controlador = controlador


    #ué


    def cadastrar_pergunta(self):
        pass
    def excluir_pergunta(self):
        pass

    def editar_pergunta(self):
        pass

      
    def mostrar_opcoes(self):
        print("-----Opçoes-----")
        print("--------------------------")
        print("1 - Cadastrar pergunta")
        print("2 - Excluir pergunta")
        print("3 - Editar pergunta")
        print("0 - voltar")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0])
        return opcao
