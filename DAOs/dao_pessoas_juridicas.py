from DAOs.dao import DAO
from DAOs.pessoa_dao import PessoaDAO
from entidades.pessoa import Pessoa
from entidades.pessoa_juridica import PessoaJuridica

# cada entidade terá uma classe dessa, implementação bem simples.
class PessoaJuridicaDAO(DAO):
    def __init__(self):
        super().__init__("pessoas_juridicas.pkl")

    def add(self, pessoa_juridca: PessoaJuridica):
        if (pessoa_juridca is not None) and isinstance(pessoa_juridca, PessoaJuridica):
            super().add(pessoa_juridca.cnpj, pessoa_juridca)

    def update(self, pessoa_juridca: PessoaJuridica):
        if (pessoa_juridca is not None) and isinstance(pessoa_juridca, PessoaJuridica):
            super().update(pessoa_juridca.cnpj, pessoa_juridca)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
