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

    def lista_categorias(self):
        for c in self.categorias:
            self.tela_categoria.mostra_categoria(c)

    def busca_categoria(self, nome):
        for c in self.categorias:
            if c.nome == nome:
                return c
        return False

    def pega_categoria(self) -> Categoria:
        opcao = self.tela_categoria.mostra_categorias()
        return self.busca_categoria(CATEGORIAS[opcao])
