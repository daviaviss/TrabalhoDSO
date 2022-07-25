from DAOs.dao_mercado import MercadoDAO
from entidades.endereco import Endereco
from entidades.mercado import Mercado
from telas.tela_mercado import TelaMercado


class ControladorMercado:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__mercados = []
        self.__mercados = []
        self.__tela_mercado = TelaMercado()
        self.__mercado_DAO = MercadoDAO()

    @property
    def mercado_DAO(self):
        return self.__mercado_DAO

    @property
    def mercados(self):
        return self.mercado_DAO.get_all()

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

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
        for pf in self.controlador_sessao.controlador_pessoa_juridica.pessoas_juridicas:
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
            self.controlador_sessao.usuario_atual,
        )
        self.mercado_DAO.add(novo_mercado)
        self.tela_mercado.mostra_mensagem("Mercado criado com sucesso")

    def lista_mercados(self) -> None:
        if not self.mercados:
            self.tela_mercado.mostra_mensagem("Nao existe mercado para ser listado!")
            return
        dados = []
        for mercado in self.mercados:
            dados.append(
                [mercado.nome, mercado.cnpj, mercado.endereco.cep, mercado.proprietario.nome]
            )
        self.tela_mercado.mostra_dados_mercado(dados)

    def exclui_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        self.mercado_DAO.remove(mercado.cnpj)
        self.tela_mercado.mostra_mensagem("Mercado Removido com Sucesso!")

    def altera_cep_mercado(self):
        dados_mercado = self.pega_mercado_por_cnpj()
        if not dados_mercado:
            self.tela_mercado.mostra_mensagem("Um mercado com esse CNPJ nao existe!")
            return
    
    def pega_mercado(self, cnpj):
        for m in self.mercados:
            if m.cnpj == cnpj:
                return m
        return False
    
    def edita_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        dados = {
            "nome": mercado.nome,
            "cnpj": mercado.cnpj,
            "cep": mercado.endereco.cep,
            "numero": mercado.endereco.numero
        }
        dados = self.tela_mercado.edita_mercado(default_data=dados)
        if not dados:
            return
        mercado.nome = dados["nome"]
        mercado.endereco.cep = dados["cep"]
        mercado.endereco.numero = dados["numero"]
        self.mercado_DAO.update(mercado)
        self.tela_mercado.mostra_mensagem("Mercado Editado com Sucesso!")


    def seleciona_mercado(self, todos=False):
        if not self.mercados:
            self.tela_mercado.mostra_mensagem("Nao existem mercados!")
            return False
        dados = {}
        for m in self.mercados:
            if not todos:
                if m.proprietario.cnpj == self.controlador_sessao.usuario_atual.cnpj:
                    dados[m.cnpj] = m.nome + " - " + m.cnpj
            else:
               dados[m.cnpj] = m.nome + " - " + m.cnpj 

        cnpj = self.tela_mercado.seleciona_mercado(dados)
        if not cnpj:
            return False
        mercado = self.pega_mercado(cnpj)
        if not mercado:
            self.tela_mercado.mostra_mensagem("Mercado Nao Existe")
            return 
        return mercado


    def altera_mercado(self) -> None:
        dados_mercado = self.pega_mercado_por_cnpj()
        if not dados_mercado.get("mercado", False):
            self.tela_mercado.mostra_mensagem("Um mercado com esse CNPJ nao existe!")
            return
        if (
            dados_mercado["mercado"].proprietario
            != self.controlador_sessao.usuario_atual
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
            dados = self.controlador_sessao.controlador_endereco.cadastra_endereco()
            mercado["mercado"].endereco = Endereco(dados["cep"], dados["numero"])
            self.tela_mercado.mostra_mensagem("Endereco atualizado com sucesso!")
        else:
            self.tela_mercado.mostra_mensagem("Nao existe um mercado com esse CNPJ!")

    def exlui_produto_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        if not mercado.produtos:
            self.tela_mercado.mostra_mensagem("Mercado nao contem produtos!")
            return 
        produto = self.controlador_sessao.controlador_produto.seleciona_produto(mercado.produtos)
        self.controlador_sessao.controlador_produto.deleta_produto(produto)

    def lista_produtos_mercado(self):
        mercado = self.seleciona_mercado(todos=True)
        if not mercado:
            return
        if not mercado.produtos:
            self.tela_mercado.mostra_mensagem("Mercado Nao Contem Produtos!")
            return
        produtos = [self.controlador_sessao.controlador_produto.get(produto) for produto in mercado.produtos]
        self.controlador_sessao.controlador_produto.lista_produtos(produtos)


    def verifica_produto_mercado(self, produto):
        mercados = []
        for m in self.mercados:
            if m.proprietario == self.controlador_sessao.usuario_atual:
                mercados.append(m)
        if not mercados:
            self.tela_mercado.mostra_mensagem("Voce nao tem mercados para editar")
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
        self.controlador_sessao.controlador_produto.lista_relatorio_produto(dados)

    def volta_menu_mercado(self):
        self.__tela_mercado.mostra_menu_inical()

    def abre_menu_mercado(self):
        if hasattr(self.controlador_sessao.usuario_atual, "cnpj"):
            tipo_usuario = "juridico"
        else:
            tipo_usuario = "fisico"
        opcoes = {
            1: self.lista_mercados,
            2: self.cadastra_mercado,
            3: self.edita_mercado,
            4: self.exclui_mercado,
            5: self.lista_produtos_mercado,
            6: self.gera_relatorio_mercado,
        }
        while True:
            if tipo_usuario == "fisico":
                opcao = self.tela_mercado.menu_mercado_pessoa_fisica()
            else:
                opcao = self.tela_mercado.menu_mercado_pessoa_juridica()
            if opcao == 0:
                break
            opcoes[opcao]()
