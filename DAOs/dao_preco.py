from DAOs.dao import DAO
from entidades.preco import Preco

#cada entidade terá uma classe dessa, implementação bem simples.
class PrecoDAO(DAO):
    def __init__(self):
        super().__init__('precos.pkl')

    def add(self, preco: Preco):
        if(preco is not None) and isinstance(preco, Preco):
            super().add(str(preco.id), preco)

    def update(self, preco: Preco):
        if((preco is not None) and isinstance(preco, Preco)):
            super().update(str(preco.id), preco)

    def get(self, key:int):
        return super().get(key)

    def remove(self, key:int):
        return super().remove(key)