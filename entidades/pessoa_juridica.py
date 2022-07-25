from entidades.pessoa import Pessoa


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj: str, nome, email):
        super().__init__(nome, email)
        self.__cnpj = cnpj

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj
