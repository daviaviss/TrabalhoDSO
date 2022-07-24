from cgitb import text
from multiprocessing import _JoinableQueueType
from typing import Text
from webbrowser import WindowsDefault
from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaProduto(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def menu_produtos(self):
        l = [
            [sg.Button(text="Listar Produtos", key=1)],
            [sg.Button(text="Cadastrar Produto", key=2)],
            [sg.Button(text="Adicionar preco a um produto", key=3)],
            [sg.Button(text="Confirmar preco de um produto", key=4)],
            [sg.Button(text="Editar nome de um produto", key=5)],
            [sg.Button(text="Editar descricao de um produto", key=6)],
            [sg.Button(text="Adicionar qualificador em um produto", key=7)],
            [sg.Button(text="Excluir qualificador em um produto", key=8)],
            [sg.Button(text="Excluir um produto", key=9)],
            [sg.Button(text="Buscar um produto", key=10)],
            [sg.Button(text="Voltar", key=0)]
        ]
        self.__window = sg.Window(title="Menu Produtos", layout=l)
        inteiros_validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
        return self.le_numero_inteiro(
            "Escolha uma das opcoes acima: ", inteiros_validos, self.__window
        )

    def pega_dados_produto(self):
        l = [
            [sg.Text("Nome do produto"), sg.Input(key="nome")],
            [sg.Text("Descricao do produto"), sg.Input(key="descricao")],
        ]
        self.__window = sg.Window(title="Dados Produto", layout=l)
        while True:
            event, values = self.__window.read()
            dados = []
            dados.append(values["nome"])
            dados.append(values["descricao"])
            if not self.verifica_dados(dados):
                print("Dados invalidos!")
                continue
            self.__window.close()
            return {"nome": values["nome"], "descricao": values["descricao"]}

    def pega_valor_preco(self):
        l = [
            [sg.Text("Preco"), sg.Input(key="preco")]
        ]
        self.__window = sg.Window("Preco", layout=l)
        while True:
            event, values = self.__window.read()
            try:
                preco = float(values["preco"])
                preco = "{:.2f}".format(preco)
            except ValueError:
                print("Insira um preco valido!")
                continue
            self.__window.close()
            return preco

    def mostra_relatorio_produto(self, dados):
        h = ["ID PRODUTO", "MAIOR VALOR REGISTRADO", "MENOR VALOR REGISTRADO", "DIFERENCA DE PRECO NO TEMPO"]
        l = [
            [sg.Table(values=dados, headings=h)],
            [sg.Button(text="Fechar", key="fechar")]
        ]
        while True:
            event, values = sg.Window(self.__window, l)
            if event:
                self.__window.close()
                break


    def pega_modo_ordenacao(self, atributo_ordenacao):
        while True:
            if atributo_ordenacao == "preco":
                print("--- SELECIONE O TIPO DE ORDENACAO ---")
                l = [
                [sg.Checkbox(text="Maior Preco", key="1")],
                [sg.Checkbox(text="Menor Preco", key="2")], 
                ]   
                opcoes = {"1": "maior_preco", "2": "menor_preco"}
            elif atributo_ordenacao == "numero_confirmacoes":
                l = [
                [sg.Checkbox(text="Mais Confirmacoes", key="1")],
                [sg.Checkbox(text="Menos Confirmacoes", key="2")], 
                ]
                opcoes = {"1": "mais_confirmacoes", "2": "menos_confirmacoes"}
            elif atributo_ordenacao == "data_postagem":
                l = [
                [sg.Checkbox(text="Mais recente", key="1")],
                [sg.Checkbox(text="Mais Antigo", key="2")], 
                ]  
                opcoes = {"1": "maid_recente", "2": "mais_antigo"}
            l.append([sg.Button(text="Escolher", key="escolha")])
            event, values = sg.Window(title="Modo Ordencacao", layout=l)
            if event == "escolha" and values:
                self.__window.close()
                break
        # modo_ordenacao = input("Insira o modo de ordencao: ")
        self.__window.close()
        return opcoes[values]
    
    def menu_busca(self):
        # l = [
        #         [sg.Text("Nome do produto"), sg.Input(key="nome_produto")],
        #         [sg.Text("Qualificadores"), sg.Input(key="qualificadores")]
        #     ]
        l= [
                [sg.Text("Nome do produto"), sg.Input(key="nome_produto")],
                [sg.Text("Qualificadores"), sg.Input(key="qualificadores")],
                [sg.Text("Selecione um dos filtros de busca abaixo:")],
                [sg.Checkbox("Preco", key="preco")],
                [sg.Checkbox("Numero de confirmacoes", key="numero_confirmacoes")],
                [sg.Checkbox("Data de postagem", key="data_postagem")]
            ]
        while True:
            dados_busca = {}
            filtros = {}
            self.__window = sg.Window("Menu Busca", l)
            event, values = self.__window.read()
            filtros["nome_produto"] = values["nome_produto"]
            filtros["qualificadores"] = values["qualificadores"]
            # print("--- SELECIONE UM FILTRO DE BUSCA ---")
            # print("[1] - PRECO")
            # print("[2] - NUMERO DE CONFIRMACOES")
            # print("[3] - DATA DE POSTAGEM")
            # self.__window = sg.Window("Menu Busca", l)
            # event, values = self.__window.read()
            # filtro_busca = input("Filtro de busca: ")
            opcoes = {"1": "preco", "2": "numero_confirmacoes", "3": "data_postagem"}
            modo_ordenacao = self.pega_modo_ordenacao(opcoes[values])
            dados_busca["atributo_ordenacao"] = opcoes[values]
            dados_busca["modo_ordenacao"] = modo_ordenacao
            dados_busca["filtros"] = filtros
            self.__window.close()
            break
        return dados_busca

    def cadastra_qualificador(self):
        l = [
            [sg.Text("Qualificador"), sg.Input(key=qualificador)]
        ]
        self.__window = sg.Window("Qualificador", l)
        event, values = self.__window.read()
        print("--- CADASTRO DE QUALIFICADOR ----")
        qualificador = input("Qualificador: ")
        return values["qualificador"]

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

    def mostra_dado_produto(self, dados, dados_preco):
        print("======================================================")
        print("ID: ", dados["id"])
        print("NOME: ", dados["nome"])
        print("DESCRICAO: ", dados["descricao"])
        print("CATEGORIA: ", dados["categoria"])
        print("DATA DE POSTAGEM: ", dados["data_postagem"])
        print("QUALIFICADORES: ", dados["qualificadores"])
        # REFORMATAR DADOS RECEBER DADOS COMO MATRIZ
        h_produto = ["ID", "NOME", "DESCRICAO", "CATEGORIA", "DATA DE POSTAGEM", "QUALIFICADORES", "PRECO", "CONTADOR"]
        l = [
            [sg.Table(values=dados, headings=h_produto)],
        ]


        # for p in dados["precos"]:
        #     print("PRECO: R$", str(p.valor), "| CONTADOR: ", p.contador)

    def pega_inteiro(self, max, min, msg):
        l = [
            [sg.Text(msg), sg.Input(key="inteiro")]
        ]
        self.__window = sg.Window("Pega dado", l)
        while True:
            event, values = self.__window.read()
            inteiro = input(msg)
            try:
                int(values["inteiro"])
                if not inteiro >= min and not inteiro <= max:
                    print("Insira um valor valido!")
                    continue
            except:
                print("Insira um valor inteiro!")
                continue
            return inteiro

    def pega_nome_produto(self):
        l = [
            [sg.Text("Nome do produto"), sg.Input(key="nome")]
        ]
        self.__window = sg.Window("Nome do Produto", l)
        event, values = self.__window.read()
        return values
        return input("Insira o nome do produto: ")

    def mostra_mensagem(self, mensagem):
        l = [
            [sg.Text(mensagem)],
            [sg.Button(text="Fechar", key="fechar")]
        ]
        self.__window = sg.Window("Mensagem", l)
        event, values = self.__window.read()
        if event == "fehcar":
            self.__window.close()

        # print(mensagem)
