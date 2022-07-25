from datetime import datetime
from entidades.qualificador import Qualificador
import uuid


class Produto:
    def __init__(
        self,
        nome: str,
        descricao: str,
        categoria,
        dados_qualificadores,
        mercado,
        criador,
    ):
        self.__id = uuid.uuid4()
        self.__nome = nome
        self.__descricao = descricao
        self.__precos = []
        self.__categoria = categoria
        self.__qualificadores = [
            Qualificador(q["titulo"], q["descricao"]) for q in dados_qualificadores
        ]
        self.__data_criacao = datetime.now()
        self.__mercado = mercado
        self.__criador = criador

    @property
    def precos(self):
        return self.__precos

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def criador(self):
        return self.__criador

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

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria