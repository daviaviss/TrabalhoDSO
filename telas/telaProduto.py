class TelaProduto:
    
    def menu_produtos(self):
        print("--- MENU PRODUTOS ---")
        print("[1] - LISTAR PRODUTOS")
        print("[2] - CADASTRAR PRODUTO")
        print("[3] - CADASTRAR QUALIFICADOR")
        print("[4] - ADICIONAR PRECO A UM PRODUTO")
        print("[5] - CONFIRMA PRECO DE UM PRODUTO")
        print("[6] - EDITAR UM PRODUTO")
        print("[7] - EXCLUIR UM PRODUTO")
        print("[8] - BUSCAR UM PRODUTO")
        print("[0] - VOLTAR")
        escolha = input("Insira uma das opcoes acima: ")
    def cadastra_produto(self, perecivel=False):
        print("---- CADASTRO DE PRODUTO ----")
        mercado = input("Mercado onde o produto sera cadastrado: ")
        preco = input("Preço do produto: ")
        categoria = input("Categoria do produto: ")
        nome = input("Nome do produto: ")
        tipo = input("Tipo do produto: ")
        qualificadores = input("Qualificadores (separados por virgula): ")
        if perecivel:
            validade = input("Validade do produto (ex: 19/10/2022: ")

    def confirma_preco(self):
        id_produto = input("ID do produto que deseja confirmar o preço: ")
        return id_produto

    def adiciona_preco(self):
        preco = input("Preço: ")
        id_produto = self.pega_id_produto()

    def pega_id_produto(self):
        id_pruduto = input("Insira o ID do produto: ")
        return id_pruduto
    
    def pega_modo_ordenacao(self, atributo_ordenacao):
        if atributo_ordenacao == "preco":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")            
            print("[1] - MAIOR PRECO")
            print("[2] - MENOR PRECO")
        if atributo_ordenacao == "numero_confirmacoes":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")            
            print("[1] - MAIS CONFIRMCOES")
            print("[2] - MENOS CONFIRMACOS")
        if atributo_ordenacao == "data_postagem":
            print("--- SELECIONE O TIPO DE ORDENACAO ---")            
            print("[1] - MAIS RECENTE")
            print("[2] - MENOS ANTIGO")
        modo_ordenacao = input("Insira o modo de ordencao: ")
        return modo_ordenacao
    def busca_produto(self):
        opcoes = {"1": "preco", "2": "numero_confirmacoes", "3": "data_postagem"}
        dados_busca = {}
        print("--- BUSCAS DE PRODUTO ---")
        nome_produto = input("Nome do produto:")
        qualificadores = input("Qualificadores (ou deixe em branco): ")
        dados_busca["nome_produto"] = nome_produto
        dados_busca["qualificadores"] = qualificadores
        print("--- SELECIONE UM FILTRO DE BUSCA ---")
        print("[1] - PRECO")
        print("[2] - NUMERO DE CONFIRMACOES")
        print("[3] - DATA DE POSTAGEM")
        filtro_busca = input("Filtro de busca: ")
        modo_ordenacao = self.pega_modo_ordenacao(opcoes[filtro_busca])
        dados_busca["atributo_ordenacao"] = filtro_busca,
        dados_busca["modo_ordenacao"] = modo_ordenacao
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
        print("NOME & QUALIFICADORES | LOCAL | PRECO")
        print(
            f'{dados["nome"]} {dados["qualificadores"]} | {dados["local"]} | R$ {dados["preco"]}'
        )

    def mostra_mensagem(self, mensagem):
        print(mensagem)