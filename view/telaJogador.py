from telaAbstract import Tela
from ControladorJogador import ControladorJogador

class TelaJogador(Tela):
    def __init__(self, controlador: ControladorJogador ):
        super()__init__()
         self.__controlador = controlador


    def nome_jogador(self , mensagem : str ):
        print("==========" , mensagem , "==============")
        nome = input("Digite o nome do jogador:")
        print("==========================================")
        return nome


    def mostrar_jogador(self, nome):
        print("Nome do Jogador:", nome )

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
