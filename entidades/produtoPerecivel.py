from datetime import date, datetime
from entidades.produto import Produto

class ProdutoPerecivel(Produto):

    def __init__(self, data_validade: date):
        super().__init__(nome, descricao)
        self.__data_validade = data_validade 

    @property
    def data_validade(self) -> date:
        return self.__data_validade

    @data_validade.setter
    def data_validade(self, data_validade: date):
        self.__data_validade = data_validade
