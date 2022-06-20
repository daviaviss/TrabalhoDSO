from entidades.categoria import Categoria
from entidades.mercado import Mercado
from entidades.pessoa_fisica import PessoaFisica
from entidades.qualificador import Qualificador
from telas.tela_produto import TelaProduto
from entidades.produto import Produto
from entidades.preco import Preco
from datetime import datetime


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

    def compara_dados_produto(self, produto, dados_comparar):
        # import pdb; pdb.set_trace()
        if produto.nome == dados_comparar["nome_produto"]:
            return True
        for qualificador in produto.qualificadores:
            if qualificador.titulo in dados_comparar["qualificadores"].split():
                return True
        return False

    def monta_dados(self, produto):
        dados = {
            "id": str(produto.id),
            "precos": produto.precos,
            "contador": produto.precos,
            "nome": produto.nome,
            "descricao": produto.descricao,
            "data_postagem": produto.data_criacao,
            "criador": produto.criador.nome,
            "categoria": produto.categoria.nome,
            "qualificadores": self.concatena_qualificadores(produto.qualificadores),
        }
        return dados

    def lista_produtos(self, dados, montar_dados=False):
        for dado in dados:
            if montar_dados:
                dado = self.monta_dados(dado)

            self.tela_produto.mostra_dado_produto(dado)

    def filtra_produtos(self, filtros: dict):
        produtos_filtrados = []
        for i, p in enumerate(self.produtos):
            print(i)
            if self.compara_dados_produto(p, filtros):
                produtos_filtrados.append(p)
        return produtos_filtrados

    def concatena_qualificadores(self, qualificadores: list) -> str:
        dados = ""
        for qualificador in qualificadores:
            if not isinstance(qualificador, str):
                dados += qualificador.titulo + qualificador.descricao
        return dados

    def monta_dados_produto(self, produto):
        dados = {
            "nome": produto.nome,
            "mercado": produto.mercado.nome,
            "data_cricao": produto.data_criacao,
            "criador": produto.criador.nome,
            "preco": produto.precos,
            "contagem_confirmacoes": produto.precos,
            "qualificadores": self.concatena_qualificadores(produto.qualificadores),
            "id": produto.id,
        }
        return dados

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
        metodo = modos[atributo_ordenacao]
        metodo(produtos, modo_ordenacao)

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
        preco = self.controlador_cessao.controlador_preco.cadastra_preco()
        mercado = self.controlador_cessao.controlador_mercado.pega_mercado_por_cnpj()
        if not mercado:
            self.tela_produto.mostra_mensagem("Mercado nao encontrado!")
            return
        categoria = self.controlador_cessao.controlador_categoria.pega_categoria()
        qualificadores = self.cadastra_qualificadores()

        dados = {}
        dados["nome"] = dados_produto["nome"]
        dados["preco"] = preco
        dados["mercado"] = mercado["mercado"]
        dados["categoria"] = categoria

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
        preco = Preco(preco, produto)
        produto.precos.append(preco)
        self.produtos.append(produto)
        self.tela_produto.mostra_mensagem("Produto cadastrado com sucesso!")

    def lista_relatorio_produto(self, dados):
        for d in dados:
            self.tela_produto.mostra_relatorio_produto(d)

    def pega_produto(self, id_produto):
        for produto in self.produtos:
            if str(produto.id) == id_produto:
                return produto
        return False

    def confirma_preco_produto(self):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID produto: ")
            valor_preco = self.tela_produto.pega_valor_preco()
            produto = self.pega_produto(id_produto)
            if not produto:
                self.tela_produto.mostra_mensagem("Nao existe um produto com esse ID!")
                opcao = self.tela_produto.mostra_pergunta()
                if opcao == 1:
                    return
                continue
            valores = [p.valor for p in produto.precos]

            if not valor_preco in valores:
                self.tela_produto.mostra_mensagem(
                    "Essa preco nao existe nesse produto!"
                )
                return

            for preco in produto.precos:
                if preco.valor == valor_preco:
                    preco.contador += 1
                    break
            self.tela_produto.mostra_mensagem("Preco confirmado!")
            break

    def verifica_permissao(self, produto):
        permissao = (
            self.controlador_cessao.controlador_mercado.verifica_produto_mercado(
                produto
            )
        )
        return permissao

    def adicionar_preco_produto(self):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID do produto")
            produto = self.pega_produto(id_produto)
            if not produto:
                self.tela_produto.mostra_mensagem("Nao existe um produto com esse ID!")
                if self.tela_produto.mostra_pergunta() == 1:
                    return
                continue
            permissao = self.verifica_permissao(produto)
            if not permissao:
                self.tela_produto.mostra_mensagem(
                    "Voce nao tem permissao para alterar o preco desse produto"
                )
                return
            valor_preco = self.tela_produto.pega_valor_preco()
            for preco in produto.precos:
                if preco.valor == valor_preco:
                    preco.contador += 1
                    self.tela_produto.mostra_mensagem(
                        "Preco ja cadastrado, o contador foi incrementado."
                    )
                    return

            preco = Preco(valor_preco, produto)
            produto.precos.append(preco)
            self.controlador_cessao.controlador_preco.precos.append(preco)
            self.tela_produto.mostra_mensagem("Preco cadastrado com sucesso!")
            break

    def busca_produto(self):
        dados_busca = self.tela_produto.menu_busca()
        filtros = {
            "nome": dados_busca["nome_produto"],
            "qualificadores": dados_busca["qualificadores"],
        }
        produtos = self.filtra_produtos(filtros)
        produtos = self.ordena_produtos(
            produtos, dados_busca["modo_ordenacao"], dados_busca["atributo_ordenacao"]
        )
        for produto in produtos:
            self.tela_produto.mostra_dado_produto(self.monta_dados_produto(produto))

    def adiciona_qualificador_produto(self):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID produto: ")
            produto = self.pega_produto(id_produto)
            if not produto:
                print("Produto nao encontrado!")
                opcao = self.tela_produto.mostra_pergunta()
                if opcao == 1:
                    return
                else:
                    continue
            dados_qualificadores = (
                self.controlador_cessao.controlador_qualificador.cadastra_qualificador()
            )
            produto.qualificadores.append(
                Qualificador(
                    dados_qualificadores["titulo"], dados_qualificadores["descricao"]
                )
            )
            self.tela_produto.mostra_mensagem("Qualificador adicionado com sucesso!")
            break

    def remove_qualificador_produto(self):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID do produto: ")
            produto = self.pega_produto(id_produto)
            if not produto:
                print("Produto nao encontrado")
                opcao = self.tela_produto.mostra_pergunta()
                if opcao == 1:
                    return
                else:
                    continue
            for p in self.produtos:
                for qualificador in p.qualificadores:
                    self.controlador_cessao.controlador_qualificador.lista_qualificadores(
                        qualificador
                    )
            id_qualificador = self.tela_produto.pega_dado_generico(
                "ID do qualificador: "
            )
            for p in self.produtos:
                for index, q in enumerate(p.qualificadores):
                    if str(q.id) == id_qualificador:
                        del p.qualificadores[index]
                        self.tela_produto.mostra_mensagem("Qualificador Deletado!")
                        return
            self.tela_produto.mostra_mensagem(
                "Nenhum qualficador com esse id foi achado no produto informado!"
            )

    def modifica_nome_descricao_produto(self, atributo):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID do produto: ")
            produto = self.pega_produto(id_produto)
            if not produto:
                print("Produto nao encontrado")
                opcao = self.tela_produto.mostra_pergunta()
                if opcao == 1:
                    return
                else:
                    continue
            msg = "Insira o novo valor de " + atributo + " :"
            dado = self.tela_produto.pega_dado_generico(msg)
            if atributo == "nome":
                produto.nome = dado
                self.tela_produto.mostra_mensagem("Nome atualizado!")
            elif atributo == "descricao":
                produto.descricao = dado
                self.tela_produto.mostra_mensagem("Descricao atualiada!")
            return

    def exclui_produto(self):
        while True:
            id_produto = self.tela_produto.pega_dado_generico("ID do produto: ")
            produto = self.pega_produto(id_produto)
            if not produto:
                print("Produto nao encontrado")
                opcao = self.tela_produto.mostra_pergunta()
                if opcao == 1:
                    return
                else:
                    continue
            for index, p in enumerate(self.produtos):
                if p == produto:
                    del self.produtos[index]
                    self.tela_produto.mostra_mensagem("Produto deletado!")
                    return

    def abre_menu_busca(self):
        opcoes_usuario = self.tela_produto.menu_busca()
        opcoes_busca = {
            "numero_confirmacoes": self.ordena_por_confirmacoes_preco,
            "data_postagem": self.ordena_produto_por_data,
            "preco": self.ordena_produto_por_preco,
        }
        func = opcoes_busca[opcoes_usuario["atributo_ordenacao"]]
        produtos = self.filtra_produtos(opcoes_usuario["filtros"])
        items = func(produtos, opcoes_usuario["modo_ordenacao"])

        dados = []
        if isinstance(items[0], Preco):
            for item in items:
                dados.append(
                    {
                        "id": str(item.produto.id),
                        "precos": [item],
                        "nome": item.produto.nome,
                        "descricao": item.produto.descricao,
                        "data_postagem": item.produto.data_criacao,
                        "criador": item.produto.criador.nome,
                        "categoria": item.produto.categoria.nome,
                        "qualificadores": self.concatena_qualificadores(
                            item.produto.qualificadores
                        ),
                    }
                )
        else:
            for item in items:
                dados.append(
                    {
                        "id": str(item.id),
                        "precos": item.precos,
                        "nome": item.nome,
                        "descricao": item.descricao,
                        "data_postagem": item.data_criacao,
                        "criador": item.criador.nome,
                        "categoria": item.categoria.nome,
                        "qualificadores": self.concatena_qualificadores(
                            item.qualificadores
                        ),
                    }
                )
        self.lista_produtos(dados)
        self.abre_menu_produto()

    def abre_menu_produto(self):

        opcoes = {
            1: self.lista_produtos,
            2: self.cadastra_produto,
            3: self.adicionar_preco_produto,
            4: self.confirma_preco_produto,
            5: self.modifica_nome_descricao_produto,
            6: self.modifica_nome_descricao_produto,
            7: self.adiciona_qualificador_produto,
            8: self.remove_qualificador_produto,
            9: self.exclui_produto,
        }

        dados_edicao = {5: "nome", 6: "descricao"}

        while True:
            opcao = self.tela_produto.menu_produtos()
            if opcao == 0:
                break
            elif opcao in dados_edicao:
                opcoes[opcao](dados_edicao[opcao])
            elif opcao == 10:
                self.abre_menu_busca()

            elif opcao == 1:
                opcoes[opcao](self.produtos, montar_dados=True)
            else:
                opcoes[opcao]()
