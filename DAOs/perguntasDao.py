from DAOs.dao import DAO
from model.pergunta import Pergunta

class PerguntaDAO(DAO):
    def __init__(self):
        super().__init__('pergunta.pkl')

    def add(self, pergunta: Pergunta):
        if((pergunta is not None) and isinstance(pergunta, Pergunta)):
            super().add(pergunta)

    def update(self, pergunta: Pergunta):
        if((pergunta is not None) and isinstance(pergunta, Pergunta)):
            super().update(pergunta)

    def get(self, key):
            return super().get(key)

    def remove(self, key):
            return super().remove(key)
