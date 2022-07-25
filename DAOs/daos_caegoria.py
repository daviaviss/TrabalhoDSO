from DAOs.dao import DAO
from DAOs.pessoa_dao import PessoaDAO
from entidades.categoria import Categoria
from entidades.pessoa import Pessoa
from entidades.mercado import Mercado

# cada entidade terá uma classe dessa, implementação bem simples.
class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__("categorias.pkl")

    def add(self, categoria: Categoria):
        if (categoria is not None) and isinstance(categoria, Categoria):
            super().add(categoria.nome.lower(), categoria)

    def get(self, key: int):
        return super().get(key)
