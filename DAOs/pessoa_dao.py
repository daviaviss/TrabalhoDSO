from DAOs.dao import DAO
from entidades.pessoa import Pessoa
from entidades.pessoa import Pessoa

# cada entidade terá uma classe dessa, implementação bem simples.
class PessoaDAO(DAO, Pessoa):
    def __init__(self):
        super().__init__("pessoas.pkl")

    def add(self, pessoa: Pessoa):
        if (pessoa is not None) and isinstance(pessoa, Pessoa):
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if (pessoa is not None) and isinstance(pessoa, Pessoa):
            super().update(pessoa.cpf, pessoa)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
