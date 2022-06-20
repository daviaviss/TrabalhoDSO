from abc import ABC, abstractmethod
from telas.tela_pessoa_fisica import TelaPessoaFisica
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata


class ControladorPessoaAbstrato(ABC):
    @abstractmethod
    def __init__(self, controlador_sessao):
        self.__tela_pessoa_abstrata = TelaPessoaFisica()
        self.__controlador_sessao = controlador_sessao

    def pega_dados_usuario(self):
        dados = self.__tela_pessoa_abstrata.pega_nome_email_usuario()
        return dados
