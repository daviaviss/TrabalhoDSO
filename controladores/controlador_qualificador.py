from DAOs.dao_qualificador import QualificadorDAO
from telas.tela_qualificador import TelaQualificador


class ControladorQualificador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_qualificador = TelaQualificador()
        self.__qualificadores = []
        self.__qualificador_DAO = QualificadorDAO()
    
    @property
    def qualificador_DAO(self):
        return self.__qualificador_DAO
    
    def add(self, qualificador):
        self.qualificador_DAO.add(qualificador)

    def get(self, id_qualificador):
        return self.qualificador_DAO.get(id_qualificador)
    
    def remove(self, id_qualificador):
        return self.qualificador_DAO.remove(id_qualificador)

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def tela_qualificador(self):
        return self.__tela_qualificador

    @property
    def qualificadores(self):
        return self.__qualificadores

    def cadastra_qualificador(self):
        return self.tela_qualificador.pega_dados_qualificador()

    def pega_qualificador_por_titulo(self):
        titulo = self.tela_qualificador.pega_nome_qualificador()
        for q in self.qualificadores:
            if q.titulo == titulo:
                return q
        return False

    def lista_qualificadores(self, qualificador):
        self.tela_qualificador.mostra_dados_qualificador(qualificador)

    def pega_qualificador(self, qualificadores):
        return self.tela_qualificador.seleciona_qualificador(qualificadores)
