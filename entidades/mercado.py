from entidades.endereco import Endereco

class Mercado(Endereco):

    def __init__(self, nome_mercado: str):
        super().__init__(cep, nome_rua, numero)
        self.__nome_mercado = nome_mercado
        self.__cnpj = "" 

    @property
    def nome_mercado(self) -> str:
        return self.__nome_mercado

    @nome_mercado.setter
    def nome_mercado(self, nome_mercado: str):
        self.__nome_mercado = nome_mercado

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj
