from abc import ABC, abstractmethod

class Endereco(ABC):

    @abstractmethod
    def __init__(self, cep: str, nome_rua: str, numero: int):
        super().__init__()
        self.__cep = cep
        self.__nome_rua = nome_rua
        self.__numero = numero

    @property
    def cep(self) -> str:
        return self.__cep

    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep

    @property
    def nome_rua(self) -> str:
        return self.__nome_rua

    @nome_rua.setter
    def nome_rua(self, nome_rua: str):
        self.__nome_rua = nome_rua

    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero