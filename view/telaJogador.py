from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaJogador(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador



    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Jogadores')],
            [sg.Text('_' * 40)],
            [sg.Radio('Cadastrar um jogador', "RD1", key='1')],
            [sg.Radio('Editar nome de um jogador', "RD1", key='2')],
            [sg.Radio('Excluir jogador', "RD1", key='3')],
            [sg.Radio('RANKING', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções').Layout(layout)


    def selecionar_jogador(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('--- Digite o CPF do jogador ---', font=("Helvica", 20))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecione um jogador').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def novo_nome(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('--- Digite o NOVO NOME do jogador ---', font=("Helvica", 20))],
            [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Alterar Nome').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome


    def novo_jogador(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('--- Criar Jogador---', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

        ]
        self.__window = sg.Window('Novo Jogador').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        self.close()
        if nome == '' or cpf == '':
            self.mostra_mensagem('AVISO:NOME e CPF não podem ser deixados em branco')
        else:
            return nome, cpf

    def mostrar_jogadores(self, dados_jogadores):
        string_todos_jogadores = ""
        for dado in dados_jogadores:
            string_todos_jogadores = string_todos_jogadores + "JOGADOR: " + dado["nome"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "CPF: " + str(dado["cpf"]) + '\n\n'


        sg.Popup('Lista de JOGADORES', string_todos_jogadores)

    def ranking(self, posicao, nome, acertos, erros, pontos, jogos, media):
        print("===== TOP ", posicao, " =====")
        print("=> Nome: ", nome)
        print("=> Total de acertos: ", acertos)
        print("=> total de erros: ", erros)
        print("=> Total de pontos: ", pontos)
        print("=> Total de jogos: ", jogos)
        print("=> Media de pontos por partida: ", media)

    def ranking2(self, dados_jogadores):
        string_todos_jogadores = ""
        for dado in dados_jogadores:
            string_todos_jogadores = string_todos_jogadores + "COLOCAÇÃO: " + dado["posicao"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "JOGADOR: " + str(dado["nome"]) + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de acertos: " + dado["acertos"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de erros: " + dado["erros"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de pontos: " + dado["pontos"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Numero de jogos: " + dado["jogos"] + '\n'
            string_todos_jogadores = string_todos_jogadores + "Media de pontos por jogo: " + dado["media"] + '\n\n'

        sg.Popup('-------- Ranking dos JOGADORES ----------', string_todos_jogadores)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

