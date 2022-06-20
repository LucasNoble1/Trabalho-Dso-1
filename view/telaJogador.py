from view.telaAbstract import Tela
from controller.controladorJogador import ControladorJogador

class TelaJogador(Tela):
    def __init__(self, controlador: ControladorJogador ):
        super().__init__()
        if isinstance(controlador, ControladorJogador):
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
