from DAOs.dao import DAO
from model.jogo import Jogo

#cada entidade terá uma classe dessa, implementação bem simples.
class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo) and isinstance(jogo.nome, int)):
            super().add(jogo.nome, jogo)

    def update(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo) and isinstance(jogo.nome, int)):
            super().update(jogo.id, jogo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)