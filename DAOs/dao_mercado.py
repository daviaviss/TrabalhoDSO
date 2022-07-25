from DAOs.dao import DAO
from DAOs.pessoa_dao import PessoaDAO
from entidades.pessoa import Pessoa
from entidades.mercado import Mercado

# cada entidade terá uma classe dessa, implementação bem simples.
class MercadoDAO(DAO):
    def __init__(self):
        super().__init__("mercados.pkl")

    def add(self, mercado: Mercado):
        if (mercado is not None) and isinstance(mercado, Mercado):
            super().add(mercado.cnpj, mercado)

    def update(self, mercado: Mercado):
        if (mercado is not None) and isinstance(mercado, Mercado):
            super().update(mercado.cnpj, mercado)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
