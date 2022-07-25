from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaPrincipal(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None

    def tela_inicial(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Made by : Alicia and Lucas')],
            [sg.Text('_' * 40)],
            [sg.Radio('Iniciar Jogo', "RD1", key='1')],
            [sg.Radio('Perguntas', "RD1", key='2')],
            [sg.Radio('Jogadores', "RD1", key='3')],
            [sg.Radio('Fechar Sistema', "RD1", key='0')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('QUIZ').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values




