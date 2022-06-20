from telas.tela_abstrata import TelaAbstrata


class TelaProduto(TelaAbstrata):
    def menu_produtos(self):
        print("--- MENU PRODUTOS ---")
        print("[1] - LISTAR PRODUTOS")
        print("[2] - CADASTRAR PRODUTO")
        print("[3] - ADICIONAR PRECO A UM PRODUTO")
        print("[4] - CONFIRMA PRECO DE UM PRODUTO")
        print("[5] - EDITAR NOME PRODUTO")
        print("[6] - EDITAR DESCRICAO PRODUTO")
        print("[7] - ADICIONAR QUALIFICADOR EM UM PRODUTO")
        print("[8] - EXCLUIR QUALIFICADOR DE UM PRODUTO")
        print("[9] - EXCLUIR UM PRODUTO")
        print("[10] - BUSCAR UM PRODUTO")
        print("[0] - VOLTAR")
        inteiros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        return self.le_numero_inteiro(
            "Escolha uma das opcoes acima: ", inteiros_validos
        )

    def pega_dados_produto(self):
        while True:
            dados = []
            nome = input("Nome do produto: ")
            descricao = input("Descricao do produto: ")
            dados.append(nome)
            dados.append(descricao)
            if not self.verifica_dados(dados):
                print("Dados invalidos!")
                continue
            return {"nome": nome, "descricao": descricao}

    def pega_valor_preco(self):
        while True:
            preco = input("Insira o preco: ")
            try:
                preco = float(preco)
            except ValueError:
                print("Insira um preco valido!")
                continue
            return preco

    def mostra_relatorio_produto(self, dados):
        print("----------------------------------------------------------")
        print("PRODUTO ID: ", dados["id_produto"])
        print("MAIOR VALOR REGISTRADO: R$", dados["maior_preco"])
        print("MENOR VALOR REGISTRADO: R$", dados["menor_preco"])
        print("DIFERENCE DE PRECO NO TEMPO: ", dados["diferenca_precos"], "%")

    def pega_modo_ordenacao(self, atributo_ordenacao):
        if atributo_ordenacao == "preco":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")
            print("[1] - MAIOR PRECO")
            print("[2] - MENOR PRECO")
            opcoes = {"1": "maior_preco", "2": "menor_preco"}
        if atributo_ordenacao == "numero_confirmacoes":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")
            print("[1] - MAIS CONFIRMACOES")
            print("[2] - MENOS CONFIRMACOES")
            opcoes = {"1": "mais_confirmacoes", "2": "menos_confirmacoes"}
        if atributo_ordenacao == "data_postagem":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")
            print("[1] - MAIS RECENTE")
            print("[2] - MENOS ANTIGO")
            opcoes = {"1": "maid_recente", "2": "mais_antigo"}
        modo_ordenacao = input("Insira o modo de ordencao: ")
        return opcoes[modo_ordenacao]

    def menu_busca(self):
        dados_busca = {}
        filtros = {}
        print("--- FILTROS DE BUSCA ---")
        nome_produto = input("Nome do produto:")
        qualificadores = input("Qualificadores: ")
        filtros["nome_produto"] = nome_produto
        filtros["qualificadores"] = qualificadores
        print("--- SELECIONE UM FILTRO DE BUSCA ---")
        print("[1] - PRECO")
        print("[2] - NUMERO DE CONFIRMACOES")
        print("[3] - DATA DE POSTAGEM")
        filtro_busca = input("Filtro de busca: ")
        opcoes = {"1": "preco", "2": "numero_confirmacoes", "3": "data_postagem"}
        modo_ordenacao = self.pega_modo_ordenacao(opcoes[filtro_busca])
        dados_busca["atributo_ordenacao"] = opcoes[filtro_busca]
        dados_busca["modo_ordenacao"] = modo_ordenacao
        dados_busca["filtros"] = filtros
        return dados_busca

    def cadastra_qualificador(self):
        print("--- CADASTRO DE QUALIFICADOR ----")
        qualificador = input("Qualificador: ")
        return qualificador

    def edita_produto(self, id_produto):
        print(f"--- EDICAO DO PRODUTO COM ID ({id_produto}) ---")
        preco = input("Preco: ")
        categoria = input("Categoria: ")
        nome = input("Nome: ")
        qualificadores = input("Qualificadores (separados por virgula): ")

    def exclui_produto(self):
        print("--- ESCLUSAO DE PRODUTO ---")
        id_produto = self.pega_id_produto()
        return id_produto

    def mostra_dado_produto(self, dados):
        print("======================================================")
        print("ID: ", dados["id"])
        print("NOME: ", dados["nome"])
        print("DESCRICAO: ", dados["descricao"])
        print("CATEGORIA: ", dados["categoria"])
        print("DATA DE POSTAGEM: ", dados["data_postagem"])
        print("QUALIFICADORES: ", dados["qualificadores"])

        for p in dados["precos"]:
            print("PRECO: R$", str(p.valor), "| CONTADOR: ", p.contador)

    def pega_inteiro(self, max, min, msg):
        while True:
            inteiro = input(msg)
            try:
                int(inteiro)
                if not inteiro >= min and not inteiro <= max:
                    print("Insira um valor valido!")
                    continue
            except:
                print("Insira um valor inteiro!")
                continue
            return inteiro

    def pega_nome_produto(self):
        return input("Insira o nome do produto: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
