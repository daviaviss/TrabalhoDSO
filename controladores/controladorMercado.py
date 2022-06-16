from entidades.mercado import Mercado
from telas.telaMercado import TelaMercado


class ControladorMercado:
    def __init__(self):
        self.__mercados = []
        self.__tela_mercado = TelaMercado()

    def verifica_dados_duplicados(self, dados: dict) -> bool:
        for mercado in self.__mercados:
            if any(
                [
                    dados["nome"] == mercado.nome,
                    dados["numero"] == mercado.numero,
                    dados["cnpj"] == mercado.cnpj,
                ]
            ):
                return True
        return False

    def cadastra_mercado(self, dados: dict) -> None:
        if self.verifica_dados_duplicados(dados):
            pass
            # TODO: MOSTRAR MENSAGEM
        if not self.verifica_integridade_dados(dados):
            pass
            # TODO: MOSTRAR MENSAGEM
        novo_mercado = Mercado(
            dados["nome"], dados["cep"], dados["nome_rua"], dados["numero"]
        )
        self.__mercados.append(novo_mercado)

    def lista_mercados(self) -> None:
        for mercado in self.__mercados:
            pass
            # TODO: mostrar mensagem com dados do mercado

    def exclui_mercado(self, usuario, cnpj):
        pass
        # TODO: chhamar controlador pessoa juridica para verificar se o mercado que ela quer exluir eh dela

    def altera_mercado(self, dados: dict) -> None:
        novo_nome = dados.get("nome", False)
        if novo_nome and isinstance(novo_nome, str):
            for mercado in self.__mercados:
                if novo_nome == mercado.nome:
                    pass
                    # TODO: retornar mensagem que o nome ja existe
        else:
            pass
        # TODO: retornar mensagem de dados invalidos
