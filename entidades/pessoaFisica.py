from entidades.pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, cpf: str):
        super().__init__(nome, email)
        self.__cpf = cpf 

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
