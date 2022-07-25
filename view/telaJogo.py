from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaJogo(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None

    def vez_do_jogador(self, nome):
        sg.popup("Vez do jogador: ", nome )

    def pontuacao_jogo(self, dados_jogadores):
        string_todos_jogadores = ""
        for dado in dados_jogadores:
            string_todos_jogadores = string_todos_jogadores + "JOGADOR: " + dado["nome"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de acertos: " + dado["acertos"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de erros: " + dado["erros"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de pontos: " + dado["pontos"] + '\n\n'

        sg.Popup('---Pontuação da Partida---', string_todos_jogadores)

    def selecao_jogadores(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('_' * 40)],
            [sg.Radio('Criar um novo jogador', "RD1", key='1')],
            [sg.Radio('Selecionar Jogador Existente', "RD1", key='2')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Opções de jogadores').Layout(layout)
        self.open()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        self.close()
        return opcao



    def tela_passo_um(self):
        self.init_passo_um()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_passo_um(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Escolha a quantidade de jogadores')],
            [sg.Text('_' * 40)],
            [sg.Radio('1 jogador(MODO SOLO)', "RD1", key='1')],
            [sg.Radio('2 jogadores(MODO X1)', "RD1", key='2')],
            [sg.Radio('3 jogadores(MODO CADA UM POR SI', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Numero de jogadores').Layout(layout)

    def tela_passo_dois(self):
        self.init_passo_dois()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 3
        if values['2']:
            opcao = 5
        if values['3']:
            opcao = 7
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_passo_dois(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Escolha a quantidade de turnos')],
            [sg.Text('_' * 40)],
            [sg.Radio('3 Turnos', "RD1", key='1')],
            [sg.Radio('5 Turnos', "RD1", key='2')],
            [sg.Radio('7 Turnos', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('voltar')]
        ]
        self.__window = sg.Window('Numero de turnos').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values


  
