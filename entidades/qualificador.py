class Qualificador():

    def __init__(self, titulo: str, descricao: str):
        self.__titulo = titulo
        self.__descricao = descricao
    
    def __str__(self):
        return self.__titulo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao