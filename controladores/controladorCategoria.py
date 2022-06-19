from entidades.categoria import Categoria
from telas.telaCategoria import TelaCategoria

CATEGORIAS = [
    "carne",
    "higiene",
    "limpeza",
    "bebida",
    "hortfruti",
]


class ControladorCategoria:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__categorias = [Categoria(c) for c in CATEGORIAS]
        self.__tela_categoria = TelaCategoria()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def categorias(self):
        return self.__categorias

    @property
    def tela_categoria(self):
        return self.__tela_categoria
