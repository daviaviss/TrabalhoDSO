from DAOs.dao import DAO
from DAOs.pessoa_dao import PessoaDAO
from entidades.qualificador import Qualificador
from entidades.pessoa import Pessoa
from entidades.mercado import Mercado

#cada entidade terá uma classe dessa, implementação bem simples.
class QualificadorDAO(DAO):
    def __init__(self):
        super().__init__('qualificadores.pkl')

    def add(self, qualificador: Qualificador):
        if(qualificador is not None) and isinstance(qualificador, Qualificador):
            super().add(str(qualificador.id), qualificador)

    def get(self, key:int):
        return super().get(key)

    def update(self, qualificador: Qualificador):
        if((qualificador is not None) and isinstance(qualificador, Qualificador)):
            super().update(str(qualificador.id), qualificador)