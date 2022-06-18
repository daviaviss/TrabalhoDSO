from entidades.mercado import Mercado
from telas.telaMercado import TelaMercado


class ControladorMercado:
    def __init__(self, controlador_sistema):
        self.__controlado_sistema = controlador_sistema
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
        mensagem = "Dados inválidos, tente novamente!"
        novo_nome = dados.get("nome", False)
        if novo_nome and isinstance(novo_nome, str):
            for mercado in self.__mercados:
                if novo_nome == mercado.nome:
                    self.__tela_mercado.mostra_mensagem(mensagem)
                    self.te
                    break
        else:
            self.__tela_mercado.mostra_mensagem(mensagem)

    def exclui_supermercado(self, cnpj):
        self.__tela_mercado.mostra_mensagem("DIGITE O CNPJ DO MERCADO DE DESEJA EXLUIR")
        cnpj = self.__tela_mercado.seleciona_mercado()
        for mercado in self.__mercados:
            pass
            # TODO: implementar login para saber o mercado que o usuario pode excluir
        self.__tela_mercado.mostra_mensagem("NÃO FOI POSSÍVEL EXLUIR ESSE MERCADO!")
        self.__tela_mercado.seleciona_mercado()

    def pega_mercado_por_cnpj(self, cnpj):
        for mercado in self.__mercados:
            if mercado.cnpj == cnpj:
                return mercado
        return False

    def lista_produtos_mercado(self, cnpj):
        mercado = self.pega_mercado_por_cnpj(cnpj)
        if mercado:
            produtos = []
            for cadastro in mercado.cadastros:
                produtos.append(cadastro.produto)
            self.__controlado_sistema.__controlador_produto.lista_produtos(produtos)
        else:
            self.__tela_mercado.mostra_mensagem("Não existe um mercado com esse CNPJ.")
            # TODO: mandar usuario para tela inicala novamente

    def volta_menu_mercado(self):
        self.__tela_mercado.mostra_menu_inical()
