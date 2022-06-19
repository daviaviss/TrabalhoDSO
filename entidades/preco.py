class Preco():

    def __init__(self, valor: float):
        self.__valor = valor
        self.__contador = 0
        self.__produto = None

    @property
    def valor(self) -> float:
        return self.__valor

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