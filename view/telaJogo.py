from view.telaAbstract import Tela
import PySimpleGUI as sg
#from controller.controladorJogo import ControladorJogo

class TelaJogo(Tela):
    def __init__(self, controlador):
        super().__init__()
        #if isinstance(controlador):
        self.__controlador = controlador
        self.__window = None

    def tela_passo_um(self):
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
            [sg.Text('Escolha a quantidade de jogadores')],
            [sg.Text('_' * 40)],
            [sg.Radio('1 jogador(MODO SOLO)', "RD1", key='1')],
            [sg.Radio('2 jogadores(MODO X1)', "RD1", key='2')],
            [sg.Radio('3 jogadores(MODO CADA UM POR SI', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('voltar')]
        ]
        self.__window = sg.Window('Passo 1').Layout(layout)

    #só usamos os metodos abstratos nela
    #GENIAL NE? nota 10
