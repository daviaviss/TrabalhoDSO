from entidades.endereco import Endereco
from entidades.mercado import Mercado
from telas.tela_mercado import TelaMercado


class ControladorMercado:
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__mercados = []
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
                    dados["numero"] == mercado.endereco.numero,
                    dados["cnpj"] == mercado.cnpj,
                ]
            ):
                return True
        for pf in self.controlador_cessao.controlador_pessoa_juridica.pessoas_juridicas:
            if pf.cnpj == dados["cnpj"]:
                return True

        return False

    def cadastra_mercado(self) -> None:
        dados = self.tela_mercado.pega_dados_mercado()
        if self.verifica_dados_duplicados(dados):
            self.tela_mercado.mostra_mensagem("Esse CNPJ ja foi cadastrado!")
            return

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
        if not self.mercados:
            self.tela_mercado.mostra_mensagem("Nao existe mercado para ser listado!")
            return
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

    def altera_cep_mercado(self):
        dados_mercado = self.pega_mercado_por_cnpj()
        if not dados_mercado:
            self.tela_mercado.mostra_mensagem("Um mercado com esse CNPJ nao existe!")
            return

    def pega_mercado_por_cnpj(self):
        while True:
            cnpj = self.tela_mercado.seleciona_mercado()
            for index, mercado in enumerate(self.mercados):
                if mercado.cnpj == cnpj:
                    return {"mercado": mercado, "index": index}
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")
            opcao = self.tela_mercado.mostra_pergunta()
            if opcao == 1:
                return False
            continue

    def altera_mercado(self) -> None:
        dados_mercado = self.pega_mercado_por_cnpj()
        if not dados_mercado.get("mercado", False):
            self.tela_mercado.mostra_mensagem("Um mercado com esse CNPJ nao existe!")
            return
        if (
            dados_mercado["mercado"].proprietario
            != self.controlador_cessao.usuario_atual
        ):
            self.tela_mercado.mostra_mensagem(
                "Voce nao pode alterar um mercado que voce nao eh o proprietario!"
            )
            return
        dados_usuario = self.tela_mercado.pega_dados_mercado(
            cnpj=False, permitir_vazio=True
        )
        dados_mercado["mercado"].nome = (
            dados_usuario.get("nome", False) or dados_mercado["mercado"].nome
        )
        dados_mercado["mercado"].endereco.cep = (
            dados_usuario.get("cep") or dados_mercado["mercado"].endereco.cep
        )
        dados_mercado["mercado"].numero = (
            dados_usuario.get("numero") or dados_mercado["mercado"].endereco.numero
        )

        self.tela_mercado.mostra_mensagem("Mercado alterado com sucesso!")

    def edita_nome_mercado(self):
        mercado = self.pega_mercado_por_cnpj()
        if mercado:
            novo_nome = self.tela_mercado.pega_dado_generico("Novo nome do mercado: ")
            mercado["mercado"].nome = novo_nome
            self.tela_mercado.mostra_mensagem("Nome atualizado com sucesso!")
        else:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")

    def edita_endereco_mercado(self):
        mercado = self.pega_mercado_por_cnpj()
        if mercado:
            dados = self.controlador_cessao.controlador_endereco.cadastra_endereco()
            mercado["mercado"].endereco = Endereco(dados["cep"], dados["numero"])
            self.tela_mercado.mostra_mensagem("Endereco atualizado com sucesso!")
        else:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")

    def exlui_produto_mercado(self):
        mercado = self.pega_mercado_por_cnpj()
        if mercado:
            id_produto = self.tela_mercado.pega_dado_generico("ID do produto: ")
            produto = self.controlador_cessao.controlador_produto.pega_produto(
                id_produto
            )
            if produto:
                for index, p in enumerate(mercado["mercado"].produtos):
                    if str(p.id) == id_produto:
                        del mercado["mercado"].produtos[index]
                        self.tela_mercado.mostra_mensagem(
                            "Produto deletado com sucesso!"
                        )
                        return
                self.tela_mercado.mostra_mensagem(
                    "Nao existe um produto com esse id no mercado elecionado!"
                )
            else:
                self.tela_mercado.mostra_mensagem("Nao existe um produto com esse ID!")
        else:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")

    def lista_produtos_mercado(self):
        mercado = self.pega_mercado_por_cnpj()
        if mercado:
            self.controlador_cessao.controlador_produto.lista_produtos(
                mercado["mercado"].produtos, montar_dados=True
            )
        elif not mercado:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")
            return

        if not mercado["mercado"].produtos:
            self.tela_mercado.mostra_mensagem("Esse mercado nao contem produtos!")

    def verifica_produto_mercado(self, produto):
        mercados = []
        for m in self.mercados:
            if m.proprietario == self.controlador_cessao.usuario_atual:
                mercados.append(m)
        for mercado_usuario in mercados:
            for p in mercado_usuario.produtos:
                if p == produto:
                    return True

        return False

    def ordena_precos_por_data(self, precos):
        return precos.sort(key=lambda p: p.data_postagem, reverse=True)

    def pega_maior_menor_preco_produto(self, produto):
        precos_produtos = produto.precos
        maior_preco = max(precos_produtos, key=lambda p: p.valor)
        menor_preco = min(precos_produtos, key=lambda p: p.valor)
        return menor_preco, maior_preco

    def pega_evolucao_precos(self, precos):
        precos_ordenados = self.ordena_precos_por_data(precos)
        try:
            if precos_ordenados[-1].valor == 0:
                diferenca = precos_ordenados[0] * 100
                return diferenca
            elif precos_ordenados[0].valor == 0:
                diferenca = (precos_ordenados[-1].valor * 100) * -1
                return diferenca

            elif precos_ordenados[0].valor < precos_ordenados[-1].valor:
                diferenca = (
                    (precos_ordenados[0].valor / precos_ordenados[-1]) * 100
                ) * -1
            else:
                diferenca = (precos_ordenados[0].valor / precos_ordenados[-1]) * 100
            return diferenca
        except:
            return "Nao foi possivel calcular"

    def gera_relatorio_mercado(self):
        if not self.mercados:
            self.tela_mercado.mostra_mensagem(
                "Nao existe mercado para gerar relatorio!"
            )
            return
        mercado = self.pega_mercado_por_cnpj()
        if not mercado:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")
            return
        dados = []

        for p in mercado["mercado"].produtos:
            menor_preco, maior_preco = self.pega_maior_menor_preco_produto(p)

            dados.append(
                {
                    "id_produto": str(p.id),
                    "maior_preco": maior_preco.valor,
                    "menor_preco": menor_preco.valor,
                    "diferenca_precos": self.pega_evolucao_precos(p.precos),
                }
            )
        self.controlador_cessao.controlador_produto.lista_relatorio_produto(dados)

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
            5: self.lista_produtos_mercado,
            6: self.edita_endereco_mercado,
            7: self.edita_nome_mercado,
            8: self.exlui_produto_mercado,
            9: self.gera_relatorio_mercado,
        }
        while True:
            if tipo_usuario == "fisico":
                opcao = self.tela_mercado.menu_mercado_pessoa_fisica()
            else:
                opcao = self.tela_mercado.menu_mercado_pessoa_juridica()
            if opcao == 0:
                break
            opcoes[opcao]()
