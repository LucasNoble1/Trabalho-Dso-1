from view.telaAbstract import Tela
import PySimpleGUI as sg

class TelaPergunta(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador
        self.__window = None


    def tela_opcoes(self):
        print("\n")
        print("-----Opçoes-----")
        print("\n")
        print("1 - Criar uma Nova pergunta")
        print("2 - Alterar uma pergunta")
        print("3 - Excluir uma pergunta")
        print("0 - voltar")
        print("\n")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0])
        return opcao

    #metodo que mostra a pergunta e suas alternativas durante o jogo
    def mostrar_pergunta(self, pergunta, alt1, alt2, alt3):
        print("=============================")
        print("          PERGUNTA:         ")
        print(">", pergunta, "<")
        print("=============================")
        print("    ESCOLHA UMA ALTERNATIVA    ")
        print("1 --", alt1)
        print("2 --", alt2)
        print("3 --", alt3)
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3])

        return opcao
    def criar_pergunta(self):
        print("============================")
        print("=== CRIE SUA PERGUNTA!! :)===")
        print("============================")
        pergunta = input("Qual a Pergunta?")
        print("============================")
        print("Sua pergunta vai precisar de uma alternativa correta e duas erras")
        print("===========================")
        print("Pergunta:", pergunta)
        resposta = input("Informe a resposta correta de sua pergunta:")
        alternativa1 = input("Crie uma alternativa falsa para sua pergunta:")
        alternativa2 = input("Crie outra alternativa falsa para sua pergunta:")
        id = input("Crie um ID para a pergunta")

        return pergunta, resposta, alternativa1, alternativa2, id
    #informa q a pergunta ja existe.
    #mostra a pergunta
    #volta para a tela inicial de perguntas
    def pergunta_repetida(self,pergunta):
        print("==")
        print("ERRO!")
        print(pergunta + "JA EXISTE NO SISTEMA")
        self.__controlador.abre_tela()

    #mensagem informando que a pergunta foi adicionada
    #volta para a tela inicial de perguntas
    def pergunta_adicionada(self,pergunta):
        print("A Pergunta:" + pergunta)
        print("FOI ADICIONADA COM SUCESSO!!!")
        self.__controlador.abre_tela()
    def mostrar_perguntas(self):
        pass

    


        # tela pergunta interf grafica
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

    # metodo para iniciar os componentes da interface grafica da tela de Pergunta
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
