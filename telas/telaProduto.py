class TelaProduto:
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

    def busca_produto(self):
        print("--- BUSCAS DE PRODUTO ---")
        nome_produto = input("Nome do produto:")
        qualificadores = input("Qualificadores (ou deixe em branco): ")
        print("--- SELECIONE O TIPO DE ORDENACAO ---")
        print("[1] - DECRESCENTE")
        print("[2] - CRESCENTE")
        tipo_listagem = input("Tipo de ordenacao: ")
        print("--- SELECIONE UM FILTRO DE BUSCA ---")
        print("[1] - PRECO")
        print("[2] - NUMERO DE CONFIRMACOES")
        print("[3] - DATA DE POSTAGEM")
        filtro_busca = input("Filtro de busca: ")

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
