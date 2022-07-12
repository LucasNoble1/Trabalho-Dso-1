from view.telaAbstract import Tela
import PySimpleGUI as sg
#from controller.controladorPrincipal import ControladorPrincipal

class TelaPrincipal(Tela):
    def __init__(self, controlador):
        super().__init__()
        #if isinstance(controlador, ControladorPrincipal):
        self.__controlador = controlador
        self.__window = None
        self.tela_inicial()
        self.init_components()


    def tela_inicial(self):
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

    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
                    [sg.Text('Made by : Alicia and Lucas')],
                    [sg.Text('_' * 40)],
                    [sg.Radio('Iniciar Jogo', "RD1", key='1')],
                    [sg.Radio('Cadastrar Pergunta', "RD1", key='2')],
                    [sg.Radio('Tutorial', "RD1", key='3')],
                    [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('QUIZ').Layout(layout)
    """
    def tela_inicial(self):
        print("========== Quiz ==========")
        print("Made by : Alicia and Lucas")
        print("==========================")
        print("\n")
        print("1 -- Iniciar o Jogo ")
        print("2 -- Cadastrar Perguntas")
        print("3 -- Tutorial ")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])
        return opcao
         

    #mostra um tutorial
    #volta sozinho tela inicial
    """
    def tutorial(self):
        print("UM DIA,SERA IMPLEMENTADO UM TUTORIAL")
        print("Mas esse dia não é HOJE")
        print("")
        self.tela_inicial()




