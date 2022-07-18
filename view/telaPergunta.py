from view.telaAbstract import Tela
#from controller.controladorPergunta import ControladorPergunta
import PySimpleGUI as sg

class TelaPergunta(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None


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

    #tela pergunta interf grafica
    def tela_pergunta_teste(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de voltar, não clicar em nada e fechar janela
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao


    #metodo para iniciar os componentes da interface grafica da tela de Pergunta
    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-----Opçoes-----')]
            [sg.Text('--------------------------')]
            [sg.Radio('1 - Cadastrar pergunta', "RD1", key='1')],
            [sg.Radio('2 - Excluir pergunta', "RD1", key='2')],
            [sg.Radio('3 - Editar pergunta', "RD1", key='3')],
            [sg.Cancel('0 - voltar')]
        ]
        self.__window = sg.Window('Perguntas').Layout(layout)
