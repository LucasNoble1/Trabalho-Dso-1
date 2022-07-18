from view.telaAbstract import Tela
#from controller.controladorJogador import ControladorJogador
import PySimpleGUI as sg

class TelaJogador(Tela):
    def __init__(self, controlador):
        super().__init__()
        #if isinstance(controlador, ControladorJogador):
        self.__controlador = controlador

    #armazena o nome do jogador
    def nome_jogador(self , mensagem : str ):
        print("==========" , mensagem , "==============")
        nome = input("Digite o nome do jogador:")
        print("==========================================")
        return nome

    #mostra nome e pontuação do jogador
    def mostrar_jogador(self, nome, pontos):
        print("Nome do Jogador:", nome)
        print("Pontucão do jogador:", pontos)
        print("\n")


    #opcoes do jogador
    #essa função foi cortada do trabalho
    def mostrar_opcoes(self):
        print("-----Opçoes-----")
        print("\n")
        print("1 - Cadastrar Jogador")
        print("2 - Editar um Jogador")
        print("3 - Excluir um jogador")
        print("4 - Pontuçao dos jogadores")
        print("0 - voltar")
        print("\n")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 4, 0])
        return opcao

    def tela_pergunta(self):
        self.init_components()
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
        # cobre os casos de voltar, não clicar em nada e fechar janela
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

        # metodo para iniciar os componentes da interface grafica da tela de Pergunta
    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-----Jogador-----')]
            [sg.Text('--------------------------')]
            [sg.Radio('1 - Cadastrar Jogador', "RD1", key='1')],
            [sg.Radio('2 - Editar um Jogador', "RD1", key='2')],
            [sg.Radio('3 - Excluir um jogador', "RD1", key='3')],
            [sg.Radio('4 - Pontuçao dos jogadores', "RD1", key='4')],
            [sg.Cancel('0 - Voltar')]
            ]
        self.__window = sg.Window('Jogador').Layout(layout)
