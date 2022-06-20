from entidades.endereco import Endereco
from entidades.pessoa_juridica import PessoaJuridica


class Mercado:
    def __init__(self, nome_mercado: str, cep, numero, cnpj, proprietario):
        self.__nome = nome_mercado
        self.__cnpj = cnpj
        self.__endereco = Endereco(cep, numero)
        self.__proprietario: PessoaJuridica = proprietario
        self.__produtos = []

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def produtos(self):
        return self.__produtos

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def proprietario(self):
        return self.__proprietario

    @nome.setter
    def nome(self, nome_mercado: str):
        self.__nome = nome_mercado

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj
