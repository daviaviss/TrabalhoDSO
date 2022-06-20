from entidades.preco import Preco
from entidades.produto import Produto
from telas import tela_preco


class ControladorPreco:
    def __init__(self, controlador_sitema):
        self.__controlador_sistema = controlador_sitema
        self.__precos = []
        self.__tela_preco = tela_preco.TelaPreco()

    @property
    def tela_preco(self):
        return self.__tela_preco

    @property
    def precos(self):
        return self.__precos

    def busca_preco(self, preco, produto):
        for p in self.__precos:
            if p.valor == preco and p.produto == produto:
                return p
        return False

    def cadastra_preco(self) -> float:
        return self.tela_preco.pega_valor_preco()
