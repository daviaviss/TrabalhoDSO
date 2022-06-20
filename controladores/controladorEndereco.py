from telas import telaEndereco


class ControladorEndereco:
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__tela_endereco = telaEndereco.TelaEndereco()

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao

    @property
    def tela_endereco(self):
        return self.__tela_endereco

    def cadastra_endereco(self):
        dados = self.tela_endereco.pega_dados_endereco()
        return dados
