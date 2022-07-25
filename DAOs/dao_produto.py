from DAOs.dao import DAO
from entidades.produto import Produto

#cada entidade terá uma classe dessa, implementação bem simples.
class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produtos.pkl')

    def add(self, produto: Produto):
        if(produto is not None) and isinstance(produto, Produto):
            super().add(str(produto.id), produto)

    def update(self, produto: Produto):
        if((produto is not None) and isinstance(produto, Produto)):
            super().update(str(produto.id), produto)

    def get(self, key:int):
        return super().get(key)

    def remove(self, key:int):
        return super().remove(key)