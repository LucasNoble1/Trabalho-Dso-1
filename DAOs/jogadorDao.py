from DAOs.dao import DAO
from model.jogador import Jogador

#cada entidade terá uma classe dessa, implementação bem simples.
class JogadorDAO(DAO):
    def __init__(self):
        super().__init__('jogador.pkl')
        self.__cache = []
    #Adiciona jogador
    def add(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador)):
            super().add(jogador)

    def update(self, jogador: Jogador):
        if((jogador is not None) and isinstance(jogador, Jogador)):
            super().update(jogador)

    #retorna o jogador, dono do cpf (key)
    def get(self, key):
        return super().get(key)

    #remove jogador dono do cpf(key)
    def remove(self, key):
        return super().remove(key)
