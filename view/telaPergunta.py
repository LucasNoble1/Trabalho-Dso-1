from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaPergunta(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None

    def mostrar_pergunta(self, pergunta, alt1, alt2, alt3, nome):
        print("=============================")
        print("jogador da vez: ", nome)
        print("          PERGUNTA:         ")
        print(">", pergunta, "<")
        print("=============================")
        print("    ESCOLHA UMA ALTERNATIVA    ")
        print("1 --", alt1)
        print("2 --", alt2)
        print("3 --", alt3)
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])
        return opcao
    
    # metodo que mostra a pergunta e suas alternativas durante o jogo
    def mostrar_pergunta2(self, pergunta, alt1, alt2, alt3, nome):
        self.init_pergunta(pergunta, alt1, alt2, alt3, nome)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        self.close()
        return opcao

    def init_pergunta(self, pergunta, alt1, alt2, alt3, nome):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Jogador da vez:', nome)],
            [sg.Text('---------PERGUNTA:----------')],
            [sg.Text(pergunta, font=("Helvica", 15))],
            [sg.Text('_' * 40)],
            [sg.Radio(alt1, "RD1", key='1')],
            [sg.Radio(alt2, "RD1", key='2')],
            [sg.Radio(alt3, "RD1", key='3')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Opções: JOGADORES').Layout(layout)
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
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('PERGUNTAS')],
            [sg.Text('_' * 40)],
            [sg.Radio('Criar uma nova pergunta', "RD1", key='1')],
            [sg.Radio('Editar uma pergunta', "RD1", key='2')],
            [sg.Radio('Excluir uma pergunta', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Opções').Layout(layout)

    def criar_pergunta(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('-- Criar nova Pergunta --', font=("Helvica", 15))],
            [sg.Text('Pergunta: ', size=(15, 1)), sg.InputText('', key='pergunta')],
            [sg.Text('Resposta: ', size=(15, 1)), sg.InputText('', key='resposta')],
            [sg.Text('Alternativa 1: ', size=(15, 1)), sg.InputText('', key='alternativa1')],
            [sg.Text('Alternativa 2:', size=(15, 1)), sg.InputText('', key='alternativa2')],
            [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

        ]
        self.__window = sg.Window('Adicionar Pergunta').Layout(layout)

        button, values = self.open()
        pergunta = values['pergunta']
        resposta = values['resposta']
        alternativa1 = values['alternativa1']
        alternativa2 = values['alternativa2']
        codigo = values['codigo']
        self.close()
        if pergunta == '' or resposta == ''or alternativa1 == ''or alternativa2 == ''or codigo == '' or button in (None, 'Cancelar') :
            self.mostra_mensagem('AVISO:nenhuma das categorias podem ser deixadas em branco')
            return 0, 0, 0, 0, 0
        else:
            return pergunta, resposta, alternativa1, alternativa2, codigo

    def mostrar_todas_perguntas(self,dados_perguntas):
        string_todos_perguntas = ""
        for dado in dados_perguntas:
            string_todos_perguntas = string_todos_perguntas + dado["codigo"] + "===> " + dado["pergunta"] + '\n'

        sg.Popup('Lista de Perguntas', string_todos_perguntas)

    def editar_pergunta(self, pergunta, resposta, alternativa1, alternativa2):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Selecione a opção que deseja alterar')],
            [sg.Text('_' * 40)],
            [sg.Radio('PERGUNTA: '+pergunta, "RD1", key='1')],
            [sg.Radio('RESPOSTA: '+resposta, "RD1", key='2')],
            [sg.Radio('ALTERNATIVA 1: '+alternativa1, "RD1", key='3')],
            [sg.Radio('ALTERNATIVA 2: '+alternativa2, "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Editar Pergunta').Layout(layout)
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
        if button in (None, 'Cancelar'):
            self.close()
            opcao = "0", 0
            return opcao
        self.close()
        if opcao == 1:
            sg.ChangeLookAndFeel('Reddit')
            layout = [
                [sg.Text('Pergunta antiga: ' + pergunta, size=(50, 1))],
                [sg.Text('Digite a nova pergunta:', size=(50,1))],
                [sg.Text('Pergunta: ', size=(15, 1)), sg.InputText('', key='alteracao')],
                [sg.Button('Confirmar')]

            ]
            self.__window = sg.Window('Selecione uma pergunta').Layout(layout)

            button, values = self.open()
            alteracao = values['alteracao']
            return alteracao, opcao
        elif opcao == 2:
            sg.ChangeLookAndFeel('Reddit')
            layout = [
                [sg.Text('Resposta antiga: '+resposta, size=(50, 1))],
                [sg.Text('Digite a nova resposta:', size=(50, 1))],
                [sg.Text('Resposta: ', size=(15, 1)), sg.InputText('', key='alteracao')],
                [sg.Button('Confirmar')]

            ]
            self.__window = sg.Window('Selecione uma pergunta').Layout(layout)

            button, values = self.open()
            alteracao = values['alteracao']
            return alteracao, opcao
        elif opcao == 3:
            sg.ChangeLookAndFeel('Reddit')
            layout = [
                [sg.Text('Alternativa antiga: ' + alternativa1, size=(50, 1))],
                [sg.Text('Digite a nova alternativa 1', size=(50, 1))],
                [sg.Text('Alternativa: ', size=(15, 1)), sg.InputText('', key='alteracao')],
                [sg.Button('Confirmar')]

            ]
            self.__window = sg.Window('Selecione uma pergunta').Layout(layout)

            button, values = self.open()
            alteracao = values['alteracao']
            return alteracao, opcao
        elif opcao == 4:
            sg.ChangeLookAndFeel('Reddit')
            layout = [
                [sg.Text('Alternativa antiga: ' + alternativa2)],
                [sg.Text('Digite a nova alternativa 2', size=(50, 1))],
                [sg.Text('Alternativa: ', size=(15, 1)), sg.InputText('', key='alteracao')],
                [sg.Button('Confirmar')]

            ]
            self.__window = sg.Window('Selecione uma pergunta').Layout(layout)

            button, values = self.open()
            alteracao = values['alteracao']
            return alteracao, opcao


    def pedir_pergunta(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Digite o codigo da Pergunta', font=("Helvica", 15))],
            [sg.Text('codigo: ', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar')]

        ]
        self.__window = sg.Window('Selecione uma pergunta').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo


    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
