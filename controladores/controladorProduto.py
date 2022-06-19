from json.encoder import py_encode_basestring_ascii
from xml.etree.ElementTree import TreeBuilder
from entidades.mercado import Mercado
from telas.telaProduto import TelaProduto
from entidades.produto import Produto
from entidades.preco import Preco
from datetime import datetime
from random import randint


class ControladorProduto:
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    @property
    def produtos(self):
        return self.__produtos

    @property
    def tela_produto(self):
        return self.__tela_produto

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao

    def pega_preco_ou_confirmacao_preco_produto(self, produto, atributo) -> Preco:
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
            return min(mais_confirmados_duplicados, key=lambda p: p.valor)

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
        for p in self.produtos:
            self.tela_produto.mostra_dado_produto(self.monta_dados_produto(p))

    def filtra_produtos(self, filtros: dict):
        produtos = []
        for p in self.produtos:
            if self.compara_dados_produto(p, filtros):
                produtos.append(p)
        return produtos

    def monta_dados_produto(self, produto):
        preco = self.pega_preco_ou_confirmacao_preco_produto(produto, "preco")
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
        for preco in self.controlador_cessao.controlador_preco.precos:
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
        for preco in self.controlador_cessao.controlador_preco.precos:
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

    def verifica_produto_duplicado(self, dados):
        for p in self.produtos:
            if all(
                [
                    p.nome == dados["nome"],
                    p.preco.valor == dados["preco"],
                    p.mercado == dados["mercado"],
                    p.categoria.nome == dados["categoria"],
                    self.verifica_qualificadores_iguais(p, dados["qualificadores"]),
                ]
            ):
                return p
        return False

    def verifica_qualificadores_iguais(self, produto, qualificadores):
        for q_pruduto in produto.qualificadores:
            for q in qualificadores:
                if not q_pruduto.titulo == q:
                    return False
        return True

    def verifica_existe_mercado(self):
        if self.controlador_cessao.controlador_mercado.mercados:
            return True
        return False

    def cadastra_qualificadores(self):
        dados_qualificadores = []
        while True:
            dados_qualificador = (
                self.controlador_cessao.controlador_qualificador.cadastra_qualificador()
            )
            dados_qualificadores.append(dados_qualificador)
            resposta = self.tela_produto.mostra_pergunta()
            if resposta == 1:
                break
        return dados_qualificadores

    def cadastra_produto(self):
        if not self.verifica_existe_mercado():
            self.tela_produto.mostra_mensagem(
                "Crie pelo menos um mercado para cadastrar um produto!"
            )
            return

        dados_produto = self.tela_produto.pega_dados_produto()
        mercado = self.controlador_cessao.controlador_mercado.pega_mercado_por_cnpj()
        categoria = self.controlador_cessao.controlador_categoria.pega_categoria()
        qualificadores = self.cadastra_qualificadores()

        dados = {}
        dados["nome"] = dados_produto["nome"]
        dados["preco"] = dados_produto["preco"]
        dados["mercado"] = mercado["mercado"]
        dados["categoria"] = categoria
        produto = self.verifica_produto_duplicado(dados)
        if produto:
            produto.preco.contador += 1
            self.tela_produto.mostra_mensagem(
                "Produto ja cadastro, o contador foi incrementado!"
            )
            return
        user = self.controlador_cessao.usuario_atual
        produto = Produto(
            dados_produto["nome"],
            dados_produto["descricao"],
            categoria,
            qualificadores,
            mercado["mercado"],
            user,
        )
        mercado["mercado"].produtos.append(produto)
        preco = Preco(dados["preco"], produto)
        # import pdb; pdb.set_trace()
        produto.precos.append(preco)
        self.produtos.append(produto)
        self.tela_produto.mostra_mensagem("Produto cadastrado com sucesso!")

    def pega_produto(self, id_produto):
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto
        return False

    def confirma_preco_produto(self, produto):
        while True:
            id_produto = self.tela_produto.confirma_preco()
            produto = self.pega_produto(id_produto)
            if not produto:
                self.tela_produto.mostra_mensagem(
                    "Nao existe um produto com esse ID. Tente novamente!"
                )
                continue

            produto.contador_preco += 1
            self.tela_produto.mostra_mensagem("Preco confirmado!")
            break

    def adicionar_preco_produto(self):
        while True:
            dados = self.tela_produto.adiciona_preco()
            produto = self.pega_produto(dados["id_produto"])
            if not produto:
                self.tela_produto.mostra_mensagem(
                    "Nao existe um produto com esse ID. Tente novamente!"
                )
                continue
            data_cadastro = datetime.now()
            # usuario = self.controlador_cessao.controlador_sessao.usuario_atual
            ja_cadastrado = False
            for preco in produto.precos:
                if preco.valor == dados["preco"]:
                    preco.contador += 1
                    ja_cadastrado = True
                    self.tela_produto.mostra_mensagem(
                        "Preco ja cadastrado, o contador foi incrementado."
                    )
                    break
            if not ja_cadastrado:
                # import pdb; pdb.set_trace()
                preco = Preco(dados["preco"], self.produtos[0])
                produto.precos.append(preco)
                # import pdb
                self.tela_produto.mostra_mensagem("Preco cadastrado com sucesso!")
            break

    def busca_produto(self):
        dados_busca = self.tela_produto.busca_produto()
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
            self.tela_produto.mostra_dado_produto(self.monta_dados_produto(produto))

    def abre_menu_inical(self):
        # lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
        #                 0: self.encerra_sistema}
        p = Produto("nome", "desc")
        preco = Preco(12.0, p)
        p.precos.append(preco)
        self.produtos.append(p)
        p.precos.append(preco)
        while True:
            opcao = self.tela_produto.menu_produtos()
            self.cadastra_produto()

    def abre_menu_produto(self):
        opcoes = {
            1: self.lista_produtos,
            2: self.cadastra_produto,
            # 3: self.cadastra_qualificador,
            4: self.adicionar_preco_produto,
            5: self.confirma_preco_produto,
            # 7: self.edita_produto,
            # 8: self.exclui_produto,
            9: self.busca_produto,
        }
        while True:
            opcao = self.tela_produto.menu_produtos()
            if opcao == 0:
                break
            opcoes[opcao]()
