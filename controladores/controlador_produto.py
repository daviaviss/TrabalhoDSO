from DAOs.dao_produto import ProdutoDAO
from entidades.categoria import Categoria
from entidades.mercado import Mercado
from entidades.pessoa_fisica import PessoaFisica
from entidades.qualificador import Qualificador
from telas.tela_produto import TelaProduto
from entidades.produto import Produto
from entidades.preco import Preco


class ControladorProduto:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__produtos = []
        self.__tela_produto = TelaProduto()
        self.__produto_DAO = ProdutoDAO()
    
    def get(self, produto):
        return self.__produto_DAO.get(str(produto.id))

    @property
    def produto_DAO(self):
        return self.__produto_DAO

    @property
    def produtos(self):
        return self.__produto_DAO.get_all()

    @property
    def tela_produto(self):
        return self.__tela_produto

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    def compara_dados_produto(self, produto, dados_comparar):
        # import pdb; pdb.set_trace()
        if produto.nome == dados_comparar["nome_produto"]:
            return True
        for qualificador in produto.qualificadores:
            if qualificador.titulo in dados_comparar["qualificadores"].split():
                return True
        return False
    
    def deleta_produt(self, produto):
        self.produto_DAO.remove(produto)
        self.tela_produto.mostra_mensagem("Produto Deletado com Sucesso")

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
    
    def seleciona_produto(self, produtos):
        dados = {}
        for p in produtos:
            try:
                nome = p.nome
                info = "Nome: {} | Descricao:  {} | Categoria: {} | ".format(nome, p.descricao, p.categoria.nome)
                dados[str(p.id)] = info
            except:
                continue
        id_produto = self.tela_produto.seleciona_produto(dados)
        if not id_produto:
            return
        produto = self.pega_produto(id_produto)
        return produto

    def lista_produtos(self, produtos, montar_dados=False):
        dados = []
        for produto in produtos:
            dados.append(
                [produto.nome, produto.descricao, produto.categoria.nome, "", ""]
            )
            for preco in produto.precos:
                dados.append(
                    ["xxxxxxx", "xxxxxxx", "xxxxxxx", preco.valor, preco.contador]
                )
            if produto.precos:
                dados.append(
                    ["-------","-------","-------","-------","-------"]
                )
        self.tela_produto.mostra_dados_produtos(dados)

    def filtra_produtos(self, nome, categoria):
        produtos_filtrados = []
        for produto in self.produtos:
            if produto.nome == nome or produto.categoria.nome.lower() == categoria:
                produtos_filtrados.append(produto)
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
        for preco in self.controlador_sessao.controlador_preco.precos:
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
        for preco in self.controlador_sessao.controlador_preco.precos:
            for produto in produtos:
                if preco in produto.precos:
                    precos.append(preco)
        if modo == "mais_confirmacoes":
            precos.sort(key=lambda preco: preco.contador, reverse=True)

        else:
            precos.sort(key=lambda preco: preco.contador)

        return precos
    
    def ordena_produto_por_mais_antigo(self, produtos):
        produtos_ordenados = []
        produtos.sort(key=lambda produto: produto.data_criacao, reverse=True)
        for p in produtos:
            produtos_ordenados.append([p.nome, p.descricao, p.categoria.nome, p.precos[0].valor if p.precos else "Sem Preco", p.precos[0].contador if p.precos else 0, self.formata_data(p.data_criacao)])
        return produtos_ordenados
    
    def ordena_produto_por_mais_recente(self, produtos):
        produtos_ordenados = []
        produtos.sort(key=lambda produto: produto.data_criacao)
        for p in produtos:
            produtos_ordenados.append([p.nome, p.descricao, p.categoria.nome, p.precos[0] if p.precos else "Sem Preco", p.precos[0] if p.precos else 0, self.formata_data(p.data_criacao)])
        return produtos_ordenados

    
    def ordena_por_mais_confirmacoes(self, produtos):
        precos = []
        for p in produtos:
            for preco in p.precos:
                precos.append(preco)
        precos.sort(key=lambda preco: preco.contador, reverse=True)
        dados = []
        for preco in precos:
            dados.append([preco.produto.nome, preco.produto.descricao, preco.produto.categoria.nome, preco.valor, preco.contador, self.formata_data(preco.produto.data_criacao)])
        return dados
    
    def ordena_por_menos_confirmacoes(self, produtos):
        precos = []
        for p in produtos:
            for preco in p.precos:
                precos.append(preco)
        precos.sort(key=lambda preco: preco.contador)
        dados = []
        for preco in precos:
            dados.append([preco.produto.nome, preco.produto.descricao, preco.produto.categoria.nome, preco.valor, preco.contador, self.formata_data(preco.produto.data_criacao)])
        return dados
    
    def ordena_por_mais_caro(self, produtos):
        precos = []
        for p in produtos:
            for preco in p.precos:
                precos.append(preco)
        precos.sort(key=lambda preco: preco.valor, reverse=True)
        dados = []
        for preco in precos:
            import pdb;pdb.set_trace()
            dados.append([preco.produto.nome, preco.produto.descricao, preco.produto.categoria.nome, preco.valor, preco.contador, self.formata_data(preco.produto.data_criacao)])
        return dados
    
    def ordena_por_mais_barato(self, produtos):
        precos = []
        for p in produtos:
            for preco in p.precos:
                precos.append(preco)
        precos.sort(key=lambda preco: preco.valor)
        dados = []
        for preco in precos:
            dados.append([preco.produto.nome, preco.produto.descricao, preco.produto.categoria.nome, preco.valor, preco.contador, self.formata_data(preco.produto.data_criacao)])
        return dados
    
    def formata_data(self, data):
        return data.strftime("%d/%m/%Y - %H:%M")

    def ordena_produtos(self, produtos: dict, modo_ordenacao):
        modos = {
            "mais_antigo": self.ordena_produto_por_mais_antigo,
            "mais_recente": self.ordena_produto_por_mais_recente,
            "mais_confirmacoes": self.ordena_por_mais_confirmacoes,
            "menos_confirmacoes": self.ordena_por_menos_confirmacoes,
            "maior_preco": self.ordena_por_mais_caro,
            "menor_preco": self.ordena_por_mais_barato
        }
        metodo = modos[modo_ordenacao]
        dados = metodo(produtos)
        return dados
    

    def verifica_qualificadores_iguais(self, produto, qualificadores):
        for q_pruduto in produto.qualificadores:
            for q in qualificadores:
                if not q_pruduto.titulo == q:
                    return False
        return True

    def verifica_existe_mercado(self):
        if self.controlador_sessao.controlador_mercado.mercados:
            return True
        return False

    def cadastra_qualificadores(self):
        dados_qualificadores = []
        while True:
            dados_qualificador = (
                self.controlador_sessao.controlador_qualificador.cadastra_qualificador()
            )
            dados_qualificadores.append(dados_qualificador)
            resposta = self.tela_produto.mostra_pergunta()
            if resposta == 1:
                break
        return dados_qualificadores
    
    def verifica_produto_duplicado(self, nome, categoria, preco):
        produtos = self.produtos
        for p in produtos:
            if p.nome == nome and p.categoria == categoria and p.preco.valor == preco:
                return p
        return False
    

    def get_preco_produto(self, produto, valor_preco):
        for preco in produto.precos:
            if preco.valor == valor_preco:
                return preco

    def cadastra_produto(self):
        if not self.verifica_existe_mercado():
            self.tela_produto.mostra_mensagem(
                "Crie pelo menos um mercado para cadastrar um produto!"
            )
            return
        dados = self.tela_produto.pega_dados_produto([c.nome for c in self.controlador_sessao.controlador_categoria.categorias])
        if not dados:
            return
        mercado = self.controlador_sessao.controlador_mercado.seleciona_mercado()
        if not mercado:
            return
        produto_duplicado = self.verifica_produto_duplicado(dados["nome"], dados["categoria"], dados["preco"])
        if produto_duplicado:
            preco = self.get_preco_produto(produto_duplicado, dados["preco"])
            preco.contador += 1
            self.controlador_sessao.controlador_preco.preco_DAO.update(preco)
            self.tela_produto.mostra_mensagem("Preco ja cadastrado, o contador foi incrementado!")
            return
        categoria = self.controlador_sessao.controlador_categoria.get_categoria(dados["categoria"])

        novo_produto = Produto(
            nome= dados["nome"],
            descricao=dados["descricao"],
            categoria = categoria,
            dados_qualificadores= dados["qualificadores"],
            mercado=mercado,
            criador= self.controlador_sessao.usuario_atual
        )
        preco = Preco(valor=dados["preco"], produto=novo_produto)
        novo_produto.precos.append(preco)
        self.produto_DAO.add(novo_produto)
        mercado.produtos.append(novo_produto)
        self.controlador_sessao.controlador_mercado.mercado_DAO.update(mercado)
        self.controlador_sessao.controlador_preco.preco_DAO.add(preco)
        self.tela_produto.mostra_mensagem("Produto Criado com Sucesso!")

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
            self.controlador_sessao.controlador_mercado.verifica_produto_mercado(
                produto
            )
        )
        return permissao
    
    def verica_produtos_permitidos(self):
        user = self.controlador_sessao.usuario_atual
        produtos = []
        for m in self.controlador_sessao.controlador_mercado.mercados:
            if m.proprietario.cnpj == user.cnpj:
                for p in m.produtos:
                    p = self.produto_DAO.get(str(p.id))
                    produtos.append(p)
        return produtos
    
    def verifica_preco_duplicado(self, produto, preco):
        for preco_produto in produto.precos:
            if preco_produto.valor == preco:
                return preco_produto
        return False

    def adicionar_preco_produto(self):
        if not self.produtos:
            self.tela_produto.mostra_mensagem("Nenhum Produto Cadastrado!")
            return

        if hasattr(self.controlador_sessao.usuario_atual, "cnpj"):
            produtos = self.verica_produtos_permitidos()
            if not produtos:
                self.tela_produto.mostra_mensagem("Nenhum Produto Cadastrado!")
                return
        else:
            produtos = self.produtos
        
        produto = self.seleciona_produto(produtos)
        if not produto:
            return
        precos = [p.valor for p in produto.precos]
        valor_preco = self.tela_produto.pega_valor_preco(precos)
        if not valor_preco:
            return
        preco = self.verifica_preco_duplicado(produto, valor_preco)
        if preco:
            preco.contador += 1
            self.controlador_sessao.controlador_preco.preco_DAO.update(preco)
            self.controlador_sessao.controlador_produto.produto_DAO.update(preco.produto)
            self.tela_produto.mostra_mensagem("preco ja existe, contador incrementado!")
            return
        novo_preco = Preco(valor=valor_preco, produto=produto)
        produto.precos.append(novo_preco)
        self.controlador_sessao.controlador_produto.produto_DAO.update(produto)
        self.controlador_sessao.controlador_preco.preco_DAO.add(novo_preco)
    
    def edita_produto(self):
        if not self.produtos:
            self.tela_produto.mostra_mensagem("Nenhum Produto Cadastrado!")
            return

        if hasattr(self.controlador_sessao.usuario_atual, "cnpj"):
            produtos = self.verica_produtos_permitidos()
            if not produtos:
                self.tela_produto.mostra_mensagem("Nenhum Produto Cadastrado!")
                return
        else:
            produtos = self.produtos
        produto = self.seleciona_produto(produtos)
        if not produto:
            return
        dados = {
            "nome": produto.nome,
            "descricao": produto.descricao,
            "categoria": produto.categoria.nome
        }
        categorias = [c.nome for c in self.controlador_sessao.controlador_categoria.categorias]
        dados = self.tela_produto.edita_produto(dados, categorias)
        if not dados:
            return
        produto.nome = dados["nome"]
        produto.descricao = dados["descricao"]
        categoria = self.controlador_sessao.controlador_categoria.get_categoria(dados["categoria"])
        import pdb;pdb.set_trace()
        produto.categoria = categoria
        self.produto_DAO.update(produto)
        self.tela_produto.mostra_mensagem("Produto Editado com Sucesso!")

    def busca_produto(self):
        
        categorias = [c.nome for c in self.controlador_sessao.controlador_categoria.categorias]
        dados_busca = self.tela_produto.menu_busca(categorias)
        if not dados_busca:
            return
        produtos_filtrados = self.filtra_produtos(dados_busca["nome_produto"], dados_busca["categoria"])
        if not produtos_filtrados:
            self.tela_produto.mostra_mensagem("Nenhum Produto Encontrado")
            return
        dados = self.ordena_produtos(
            produtos_filtrados, dados_busca["modo"]
        )
        self.tela_produto.mostra_dados_produtos(dados, additional_header="DATA PUBLICACAO")
            
    def adiciona_qualificador_produto(self):
        user = self.controlador_sessao.usuario_atual
        if hasattr(user, "cpf"):
            produtos = self.verifica_permitidos_pf()
        else:
            produtos = self.verica_produtos_permitidos()
        if not produtos:
            self.tela_produto.mostra_mensagem("Nenhum produto para modificar")
        produto = self.seleciona_produto(produtos)
        if not produto:
            return
        dados = self.tela_produto.pega_dados_qualificadores()
        if not dados:
            return
        for dado in dados:
            qualificador = Qualificador(dado["titulo"], dado["descricao"])
            self.controlador_sessao.controlador_qualificador.add(qualificador)
            produto.qualificadores.append(qualificador)
        self.produto_DAO.update(produto)
        self.tela_produto.mostra_mensagem("Qualificador adicionado com sucesso!")
            

    def remove_qualificador_produto(self):
        user = self.controlador_sessao.usuario_atual
        if hasattr(user, "cpf"):
            produtos = self.verifica_permitidos_pf()
        else:
            produtos = self.verica_produtos_permitidos()
        if not produtos:
            self.tela_produto.mostra_mensagem("Nenhum produto para ")
        produto = self.seleciona_produto(produtos)
        if not produto:
            return
        dados = {}
        for q in produto.qualificadores:
            dados[str(q.id)] = q.titulo + " - " + q.descricao
        id_qualificador = self.controlador_sessao.controlador_qualificador.pega_qualificador(dados)
        if not id_qualificador:
            return
        for index, q in enumerate(produto.qualificadores):
            if str(q.id) == id_qualificador:
                del produto.qualificadores[index]
                self.controlador_sessao.controlador_qualificador.remove(id_qualificador)
                self.produto_DAO.update(produto)
                self.tela_produto.mostra_mensagem("Qualificador Removido!")
                break
    def verifica_permitidos_pf(self):
        permitidos = []
        produtos = self.produto_DAO.get_all()
        for p in produtos:
            if p.criador.cnpj == self.controlador_sessao.usuario_atual.cnpj:
                permitidos.append(p)
        return permitidos

    def exclui_produto(self):
        user = self.controlador_sessao.usuario_atual
        if hasattr(user, "cpf"):
            produtos = self.verifica_permitidos_pf()
        else:
            produtos = self.verica_produtos_permitidos()
        if not produtos:
            self.tela_produto.mostra_mensagem("Nenhum produto para ")
        produto = self.seleciona_produto(produtos)
        if not produto:
            return
        self.produto_DAO.remove(str(produto.id))
        self.tela_produto.mostra_mensagem("Produto Delete com Sucesso!")

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
            4: self.adicionar_preco_produto,
            5: self.edita_produto,
            6: self.adiciona_qualificador_produto,
            7: self.remove_qualificador_produto,
            8: self.exclui_produto,
            9: self.busca_produto
        }

        while True:
            opcao = self.tela_produto.menu_produtos()
            if opcao == "voltar":
                break
            elif opcao == 1:
                opcoes[opcao](self.produtos, montar_dados=True)
            else:
                print(opcao)
                opcoes[opcao]()
