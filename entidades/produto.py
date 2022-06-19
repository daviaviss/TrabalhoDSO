from abc import ABC, abstractmethod
from datetime import datetime
from entidades.qualificador import Qualificador
from entidades.preco import Preco


class Produto:
    def __init__(self, nome: str, descricao: str, categoria, dados_qualificadores):
        super().__init__()
        self.__id = "1"
        self.__nome = nome
        self.__descricao = descricao
        self.__precos = []
        self.__categoria = categoria
        self.__qualificadores = [Qualificador(q["titulo"], q["descricao"]) for q in dados_qualificadores]
        self.__data_criacao = datetime.now()
        self.__mercado = None

    @property
    def precos(self):
        return self.__precos
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao
    
    @property
    def mercado(self):
        return self.__mercado
    
    @property
    def data_criacao(self):
        return self.__data_criacao
    
    @property
    def preco(self):
        return self.__precos
    
    @property
    def id(self):
        return self.__id
    
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    