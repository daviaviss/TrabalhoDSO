from entidades.endereco import Endereco
from entidades.pessoaJuridica import PessoaJuridica



class Mercado:

    def __init__(self, nome_mercado: str, cep, numero, cnpj, proprietario):
        self.__nome = nome_mercado
        self.__cnpj = cnpj
        self.__endereco = Endereco(cep, numero)
        self.__proprietario: PessoaJuridica = proprietario

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
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
