from telas import tela_endereco


class ControladorEndereco:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__tela_endereco = tela_endereco.TelaEndereco()

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    @property
    def tela_endereco(self):
        return self.__tela_endereco

    def cadastra_endereco(self):
        dados = self.tela_endereco.pega_dados_endereco()
        return dados
