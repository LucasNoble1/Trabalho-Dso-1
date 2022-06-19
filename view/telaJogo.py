from telaAbstract import Tela
from controladorJogo import ControladorJogo

class TelaJogo(Tela):
    def __init__(self, controlador):
        super().__init__()
        if isinstance(controlador, ControladorJogo):
            self.__controlador = controlador

    def