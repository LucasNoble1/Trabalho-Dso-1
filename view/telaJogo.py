from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaJogo(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None

    def tela_passo_um(self):
        print("\n")
        print("Passo 1: Escolha a quantidade de jogadores")
        print("------------------------------------------")
        print("1 -- MODO SOLO")
        print("2 -- MODO BORA X1")
        print("3 -- MODO CADA UM POR SI")
        print("\n")
        num_jogadores = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])
        print("Passo 2: Escolha a quantidade de turnos")
        print("------------------------------------------")
        print("1 -- iniciar um jogo com >3< TURNOS")
        print("2 -- iniciar um jogo com >5< TURNOS")
        print("3 -- iniciar um jogo com >7< TURNOS")
        print("0 - VOLTAR PARA A TELA PRINCIPAL")
        print("\n")
        num_turnos = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0])
        return num_jogadores , num_turnos

    def selecao_jogadores(self):
        print("1 -- Criar novo jogador")
        print("2 -- Selecionar Jogador")
        resposta = self.le_num_inteiro("selecione uma opção:", [1, 2])
        return resposta

    def vez_do_jogador(self, nome):
        print("========================")
        print("Vez do jogador : ", nome)
        print("QUE A FORÇA ESTEJA COM VOCÊ!!!")
        print("=============================")
        ok = self.le_num_inteiro("DIGITE 1 para iniciar:", [1])
        return ok

    def tela_fim(self):
        print("\n")
        print("====================")
        print(">>>FIM DO JOGO<<<")


    def pontuacao_jogo(self, nome, acertos, erros, pontos):
        print("Confira a pontuação")
        print("Jogador: ", nome)
        print("acertos: ", acertos)
        print("erros: ", erros)
        print("pontuação: ", pontos)
        print("----------------------")


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

  
