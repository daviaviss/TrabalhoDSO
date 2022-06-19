from ossaudiodev import control_labels
from entidades.mercado import Mercado
from telas.telaMercado import TelaMercado


class ControladorMercado:
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__mercados = []
        self.__tela_mercado = TelaMercado()

    @property
    def mercados(self):
        return self.__mercados

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao

    @property
    def tela_mercado(self):
        return self.__tela_mercado

    def verifica_dados_duplicados(self, dados: dict) -> bool:
        for mercado in self.mercados:
            if any(
                [
                    dados["nome"] == mercado.nome,
                    dados["numero"] == mercado.numero,
                    dados["cnpj"] == mercado.cnpj,
                ]
            ):
                return True
        return False

    def cadastra_mercado(self) -> None:
        dados = self.tela_mercado.pega_dados_mercado()
        if self.verifica_dados_duplicados(dados):
            self.tela_mercado.mostra_mensagem(
                "Um mercado com um dos dos dados inseridos ja existe!"
            )

        novo_mercado = Mercado(
            dados["nome"],
            dados["cep"],
            dados["numero"],
            dados["cnpj"],
            self.controlador_cessao.usuario_atual,
        )
        self.mercados.append(novo_mercado)
        self.tela_mercado.mostra_mensagem("Mercado criado com sucesso")

    def lista_mercados(self) -> None:
        for mercado in self.mercados:
            self.tela_mercado.mostra_dados_mercado(mercado)

    def exclui_mercado(self):
        mercado, index = self.pega_mercado_por_cnpj()
        if not mercado:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ")
            return
        if mercado.proprietario == self.controlador_cessao.usuario_atual:
            del self.mercados[index]
            self.tela_mercado.mostra_mensagem("Mercado deletado com sucesso!")
        else:
            self.tela_mercado.mostra_mensagem(
                "Voce nao pode deletar um mercado que voce nao eh o proprietario!"
            )

    def pega_mercado_por_cnpj(self):
        cnpj = self.tela_mercado.seleciona_mercado()
        for index, mercado in enumerate(self.mercados):
            if mercado.cnpj == cnpj:
                return {"mercado": mercado, "index": index}
        return {}

    def altera_mercado(self) -> None:
        dados_mercado = self.pega_mercado_por_cnpj()
        if not dados_mercado.get("mercado", False):
            self.tela_mercado.mostra_mensagem("Um mercado com esse CNPJ nao existe!")
            return
        if dados_mercado["mercado"].proprietario != self.controlador_cessao.usuario_atual:
            self.tela_mercado.mostra_mensagem(
                "Voce nao pode alterar um mercado que voce nao eh o proprietario!"
            )
            return
        dados_usuario = self.tela_mercado.pega_dados_mercado(cnpj=False, permitir_vazio=True)
        dados_mercado["mercado"].nome = dados_usuario.get("nome", False) or dados_mercado["mercado"].nome
        dados_mercado["mercado"].endereco.cep = (
            dados_usuario.get("cep") or dados_mercado["mercado"].endereco.cep
        )
        dados_mercado["mercado"].numero = (
            dados_usuario.get("numero") or dados_mercado["mercado"].endereco.numero
        )

        self.tela_mercado.mostra_mensagem("Mercado alterado com sucesso!")

    def lista_produtos_mercado(self, cnpj):
        mercado, _ = self.pega_mercado_por_cnpj(cnpj)
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

    def abre_menu_mercado(self):
        if hasattr(self.controlador_cessao.usuario_atual, "cnpj"):
            tipo_usuario = "juridico"
        else:
            tipo_usuario = "fisico"
        opcoes = {
            1: self.lista_mercados,
            2: self.cadastra_mercado,
            3: self.altera_mercado,
            4: self.exclui_mercado,
        }
        while True:
            opcao = self.tela_mercado.menu_mercado(tipo_usuario)
            if opcao == 0:
                break
            opcoes[opcao]()
