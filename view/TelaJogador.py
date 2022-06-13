from tela import Tela

class TelaJogador(Tela):
    def __init__(self):
        super()__init__()
         pass


    def cadastrar_jogador(self):
        pass
    def excluir_jogador(self):
        pass
    def mostrar_opcoes(self):
        print("-----Opçoes-----")
        print("--------------------------")
        print("1 - Cadastrar Jogador")
        print("2 - Excluir um Jogador")
        print("3 - Editar um jogador")
        print("0 - voltar")
        opcao = self.le_num_inteiro("Selecione uma opção:", [1, 2, 3, 0]
        return opcao
