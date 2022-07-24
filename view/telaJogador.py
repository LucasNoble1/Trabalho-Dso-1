from view.telaAbstract import Tela

class TelaJogador(Tela):
    def __init__(self, controlador):
        super().__init__()
        self.__controlador = controlador

    def selecionar_jogador(self):
        cpf = input("digite o cpf de um jogador:")
        return cpf
    def novo_nome(self):
        nome = input("Digite o novo nome do jogador:")
        return nome

    #armazena o nome do jogador
    def novo_jogador(self , mensagem : str ):
        while True:
            print("==========" , mensagem , "==============")
            nome = input("Digite o nome do jogador:")
            cpf = input("Digite seu cpf:")
            if nome == "" or cpf == "":
                print("AVISO: NOME e CPF não podem ser deixados em branco")
            else:
                return nome , cpf

    #mostra nome e pontuação do jogador
    def mostrar_jogador(self, nome, pontos, cpf ):
        print("cpf: ", cpf , " ===>Jogador:", nome)
        print("Pontucão do jogador:", pontos)
        print("-------------------------")

    def ranking(self, posicao, nome, acertos, erros, pontos, jogos, media):
        print("===== TOP ", posicao, " =====")
        print("=> Nome: ", nome)
        print("=> Total de acertos: ", acertos)
        print("=> total de erros: ", erros)
        print("=> Total de pontos: ", pontos)
        print("=> Total de jogos: ", jogos)
        print("=> Media de pontos por partida: ", media)

    #opcoes do jogador
    #essa função foi cortada do trabalho
    def tela_opcoes(self):
        print("-----Opçoes-----")
        print("\n")
        print("1 - Cadastrar Jogador")
        print("2 - Editar  o nome de um Jogador")
        print("3 - Excluir um jogador")
        print("4 - Ranking dos jogadores ")
        print("0 - voltar")
        print("\n")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 4, 0])
        return opcao

    def aviso_jogador_removido(self, nome):
        print('o jogador :', nome ,'foi removido do sistema')

    def aviso_jogador_nao_encontrado(self,cpf):
        print('o cpf: ', cpf ,'não corresponde a nenhum jogador')
        print('selecione um cpf valido')

    def aviso_jogador_duplicado(self):
        print("Impossivel adicionar jogador")
        print("Cpf ou Nome indisponiveis")
    def aviso_jogador_alterado(self):
        print("O nome do jogador foi alterado com sucesso")
       

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
