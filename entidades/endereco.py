class Endereco:
    def __init__(self, cep: str, numero: str):
        self.__cep = cep
        self.__numero = numero

    @property
    def cep(self) -> str:
        return self.__cep

    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep

    @property
    def numero(self) -> str:
        return self.__numero

    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero
