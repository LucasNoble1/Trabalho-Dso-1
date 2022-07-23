from DAOs.dao import DAO
from model.Pergunta import Pergunta

#cada entidade terá uma classe dessa, implementação bem simples.
class PerguntaDAO(DAO):
    def __init__(self):
        super().__init__('pergunta.pkl')

    def add(self, pergunta: Pergunta):
        if((pergunta is not None) and isinstance(pergunta, Pergunta) and isinstance(pergunta.codigo, int)):
            super().add(pergunta.codigo, pergunta)

    def update(self, pergunta: Pergunta):
        if((pergunta is not None) and isinstance(pergunta, Pergunta) and isinstance(pergunta.codigo, int)):
            super().update(pergunta.codigo, pergunta)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)