from telas import telaPreco
class ControladorPreco:
    def __init__(self, controlador_sitema):
        self.__controlador_sistema = controlador_sitema
        self.__precos = []

    @property
    def precos(self):
        return self.__precos
    
