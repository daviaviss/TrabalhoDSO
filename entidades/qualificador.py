import uuid


class Qualificador:
    def __init__(self, titulo: str, descricao: str):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__id = uuid.uuid4()

    def __str__(self):
        return self.__titulo

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descricao(self):
        return self.__descricao

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao
