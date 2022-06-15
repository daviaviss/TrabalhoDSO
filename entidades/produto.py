from abc import ABC, abstractmethod

class Produto(ABC):

    @abstractmethod
    def __init__(self, nome: str, descricao: str):
        super().__init__()
        self.__nome = nome
        self.__descricao = descricao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

