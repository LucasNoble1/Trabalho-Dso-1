from view.telaAbstract import Tela
from controller.controladorJogo import ControladorJogo

class TelaJogo(Tela):
    def __init__(self, controlador):
        super().__init__()
        if isinstance(controlador, ControladorJogo):
            self.__controlador = controlador

    #só usamos os metodos abstratos nela
    #GENIAL NE? nota 10
