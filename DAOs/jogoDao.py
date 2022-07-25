from DAOs.dao import DAO
from model.jogo import Jogo

#cada entidade terá uma classe dessa, implementação bem simples.
class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo)):
            super().add(jogo)

    def update(self, jogo: Jogo):
        if((jogo is not None) and isinstance(jogo, Jogo)):
            super().update(jogo)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
