from datetime import datetime
import uuid


class Preco:
    def __init__(self, valor: float, produto):
        self.__valor = valor
        self.__contador = 0
        self.__produto = produto
        self.__data_postagem = datetime.now()
        self.__id = uuid.uuid4

    @property
    def id(self):
        return str(self.__id)

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def data_postagem(self):
        return self.__data_postagem

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def contador(self) -> int:
        return self.__contador

    @contador.setter
    def contador(self, contador: int):
        self.__contador = contador

    @property
    def id_produto(self) -> str:
        return self.__id_produto

    @property
    def produto(self):
        return self.__produto

    @id_produto.setter
    def id_produto(self, id_produto: str):
        self.__id_produto = id_produto
