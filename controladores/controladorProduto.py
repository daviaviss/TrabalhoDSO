from json.encoder import py_encode_basestring_ascii
from telas.telaProduto import TelaProduto
from entidades.produto import Produto
from entidades.preco import Preco
from datetime import datetime
from random import randint


class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    def pega_preco_ou_confirmacao_preco_produto(
        self, produto, atributo, modo="mais_confirmado"
    ) -> Preco:
        """
        Como um produto pode ter mais de um preco, caso tenha, pega o preco com mais confirmacoes,
        caso haja confirmacoes com a mesma quantidade, pega, dos precos com mais confirmacoes, o de menor preco
        """

        infos = {}
        if len(produto.precos) == 1:
            return produto.precos[0]

        for preco in produto.precos:
            infos[preco] = preco.contador
        existe_duplicado = len(infos.values()) != len(set(infos.values()))
        if existe_duplicado:
            mais_confirmados_duplicados = []
            maior_contagem = max(infos.values())
            for preco, contagem in infos.items():
                if contagem == maior_contagem:
                    if atributo == "preco":
                        mais_confirmados_duplicados.append(preco)
                    elif atributo == "confirmacoes":
                        mais_confirmados_duplicados.append(contagem)
            return min(mais_confirmados_duplicados)

        return max(infos, key=infos.get)

    def compara_dados_produto(self, produto, dados_comparar):
        if any(
            [
                produto.nome == dados_comparar["nome"],
                any(
                    x in str(produto.qualificadores)
                    for x in dados_comparar["qualificadores"]
                ),
            ]
        ):
            return True
        return False

    def lista_produtos(self):
        for p in self.__produtos:
            self.__tela_produto.mostra_dado_produto(self.monta_dados_produto(p))

    def filtra_produtos(self, filtros: dict):
        produtos = []
        for p in self.__produtos:
            if self.compara_dados_produto(p, filtros):
                produtos.append(p)
        return produtos

    def monta_dados_produto(self, produto):
        preco = self.pega_preco_produto(produto)
        dados = {
            "nome": produto.nome,
            "mercado": produto.mercado,
            "data_cricao": produto.data_criacao,
            "criador": produto.criador,
            "preco": preco.valor,
            "contagem_confirmacoes": preco.contador,
        }
        return dados

    def get_atributo_ordenacao(self, produto, ordenacao):
        tipos_ordenacoes = {
            "data": produto.data_criacao,
            "preco": self.pega_preco_ou_confirmacao_preco_produto(
                produto, "preco"
            ).valor,
            "confirmacoes_preco": self.pega_preco_ou_confirmacao_preco_produto(
                produto, "confirmacoes"
            ),
        }

    def get_preco_produto(self, produto, opcao):
        ondenacoes = {
            "data": produto.data,
            "menor_preco": self.get_menor_preco_produto,
            "maior_preco": self.get_maior_preco_produto,
            "confirmacoes_preco": self.get_confirmacao_preco_produto,
        }

        if opcao == "maior_preco":
            return max(produto.precos, key=lambda produto: produto.valor.preco)
        elif opcao == "menor_preco":
            return max(produto.precos, key=lambda produto: produto.valor.preco)

    def ordena_produto_por_preco(self, produtos, modo):
        precos = []
        for preco in self.__controlador_sistema.controlador_preco.precos:
            for produto in produtos:
                if preco in produto.precos:
                    precos.append(preco)

        if modo == "maior_preco":
            precos.sort(key=lambda preco: preco.valor, reverse=True)
        else:
            precos.sort(key=lambda preco: preco.valor)
        return precos

    def ordena_produto_por_data(self, produtos, modo):
        if modo == "mais_recente":
            produtos.sort(key=lambda produto: produto.data_criacao)
        else:
            produtos.sort(key=lambda produto: produto.data_criacao, reverse=True)

        return produtos

    def ordena_por_confirmacoes_preco(self, produtos, modo):
        precos = []
        for preco in self.__controlador_sistema.controlador_preco.precos:
            for produto in produtos:
                if preco in produto.precos:
                    precos.append(preco)
        if modo == "mais_confirmacoes":
            precos.sort(key=lambda preco: preco.contador, reverse=True)

        else:
            precos.sort(key=lambda preco: preco.contador)

        return precos

    def ordena_produtos(self, produtos: dict, modo_ordenacao, atributo_ordenacao):
        modos = {
            "data": self.ordena_produto_por_data,
            "preco": self.ordena_produto_por_preco,
            "numero_confirmacoes": self.ordena_por_confirmacoes_preco,
        }
        # import pdb; pdb.set_trace()
        metodo = modos[atributo_ordenacao]
        metodo(produtos, modo_ordenacao)

    def cadastra_produto(self):
        dados = self.__tela_produto.cadastra_produto()
        for produto in self.__produtos:
            if all(
                [
                    dados["preco"] == produto.preco,
                    dados["nome"] == produto.nome,
                    dados["categoria"] == produto.categoria.nome,
                    dados["qualificador"] == produto,
                ]
            ) and all(x in produto.qualificadores for x in dados["qualificadores"]):
                produto.contador_preco += 1
                self.__tela_produto.mostra_mensagem("Produto ja cadastrado, o contador foi incrementado!")
                # TODO: retornar para menu principal
        data_criacao = datetime.now()
        preco = Preco(dados["preco"])
        produto = Produto(
            dados["nome"],
            dados["descricao"]
        )
        produto.precos.append(preco)
        preco.produto = produto


        self.__produtos.append(produto)
        self.__tela_produto.mostra_mensagem("Produto cadastrado!")
        self.__tela_produto.menu_produtos()
        return

    def pega_produto(self, id_produto):
        for produto in self.__produtos:
            if produto.id == id_produto:
                return produto
        return False

    def confirma_preco_produto(self, produto):
        while True:
            id_produto = self.__tela_produto.confirma_preco()
            produto = self.pega_produto(id_produto)
            if not produto:
                self.__tela_produto.mostra_mensagem(
                    "Nao existe um produto com esse ID. Tente novamente!"
                )
                continue

            produto.contador_preco += 1
            self.__tela_produto.mostra_mensagem("Preco confirmado!")

            # TODO: retornar para menu principal

    def adicionar_preco_produto(self):
        while True:
            dados = self.__tela_produto.adiciona_preco()
            produto = self.pega_produto(dados["id_produto"])
            if not produto:
                self.__tela_produto.mostra_mensagem(
                    "Nao existe um produto com esse ID. Tente novamente!"
                )
                continue
            data_cadastro = datetime.now()
            # usuario = self.__controlador_sistema.controlador_sessao.usuario_atual
            ja_cadastrado = False
            for preco in produto.precos:
                if preco.valor == dados["preco"]:
                    preco.contador += 1
                    ja_cadastrado = True
                    self.__tela_produto.mostra_mensagem(
                        "Preco ja cadastrado, o contador foi incrementado."
                    )
                    break
            if not ja_cadastrado:
                # import pdb; pdb.set_trace()
                preco = Preco(dados["preco"], self.__produtos[0])
                produto.precos.append(preco)
                # import pdb
                self.__tela_produto.mostra_mensagem("Preco cadastrado com sucesso!")
            break
        self.__tela_produto.menu_produtos()

    def busca_produto(self):
        dados_busca = self.__tela_produto.busca_produto()
        # import pdb
        # pdb.set_trace()
        filtros = {
            "nome": dados_busca["nome_produto"],
            "qualificadores": dados_busca["qualificadores"],
        }
        produtos = self.filtra_produtos(filtros)
        # import pdb; pdb.set_trace()
        produtos = self.ordena_produtos(
            produtos, dados_busca["modo_ordenacao"], dados_busca["atributo_ordenacao"]
        )
        for produto in produtos:
            self.__tela_produto.mostra_dado_produto(self.monta_dados_produto(produto))

    def abre_menu_inical(self):
        # lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
        #                 0: self.encerra_sistema}
        p = Produto("nome", "desc")
        preco = Preco(12.0, p)
        p.precos.append(preco)
        self.__produtos.append(p)
        p.precos.append(preco)
        while True:
            opcao = self.__tela_produto.menu_produtos()
            self.cadastra_produto()
