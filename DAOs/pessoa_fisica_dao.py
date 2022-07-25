from DAOs.dao import DAO
from DAOs.pessoa_dao import PessoaDAO
from entidades.pessoa import Pessoa
from entidades.pessoa_fisica import PessoaFisica

# cada entidade terá uma classe dessa, implementação bem simples.
class PessoaFisicaDAO(DAO):
    def __init__(self):
        super().__init__("pessoas_fisicas.pkl")

    def add(self, pessoa_fisica: PessoaFisica):
        if (pessoa_fisica is not None) and isinstance(pessoa_fisica, PessoaFisica):
            super().add(pessoa_fisica.cpf, pessoa_fisica)

    def update(self, pessoa_fisica: PessoaFisica):
        if (pessoa_fisica is not None) and isinstance(pessoa_fisica, PessoaFisica):
            super().update(pessoa_fisica.cpf, pessoa_fisica)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
