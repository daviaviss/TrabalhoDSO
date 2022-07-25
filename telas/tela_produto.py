from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg


class TelaProduto(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def menu_produtos(self):
        opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        l = [
            [sg.Button(button_text="Listar Produtos", key=1)],
            [sg.Button(button_text="Cadastrar Produto", key=2)],
            [sg.Button(button_text="Adicionar preco a um produto", key=3)],
            [sg.Button(button_text="Confirmar preco de um produto", key=4)],
            [sg.Button(button_text="Editar Produto", key=5)],
            [sg.Button(button_text="Adicionar qualificador em um produto", key=6)],
            [sg.Button(button_text="Excluir qualificador em um produto", key=7)],
            [sg.Button(button_text="Excluir um produto", key=8)],
            [sg.Button(button_text="Buscar um produto", key=9)],
            [sg.Button(button_text="Voltar", key="voltar")]
        ]
        self.__window = sg.Window(title="Menu Produtos", layout=l)
        event, values = self.__window.read()
        if not event in opcoes:
            self.__window.close()
            return "voltar"
        self.__window.close()
        return event
    
    # def edita_produto(self, default_data, categorias):

    #     layout = [[sg.Text('Edicao Produto')],           
    #                 [sg.Text("Nome"), sg.Input(key="nome", default_text=default_data["nome"])],
    #                 [sg.Text("Descricao"), sg.Input(key="descricao", default_text=default_data["descricao"])],
    #                 [sg.Button("Editar", key="editar"), sg.Button("Cancelar")]
    #     ]
    #     for c in categorias:
    #         layout.append(
    #             [sg.Radio(text=c.nome, group_id="categorias", default=True if c.nome.lower() == default_data["categorias"].lower() else False)]
    #         )
    #     self.__window = sg.Window("Editar Usuario Fisica", layout=layout)
    #     # while True:
    #     while True:
    #         event, values = self.__window.read()
    #         if event == "editar":
    #             if any(
    #                 [v == "" for k, v in values.items()]
    #             ):
    #                 self.mostra_mensagem("Nenhum valor pode ficar em branco!")
    #                 continue
    #             self.__window.close()
    #             dados = {"nome": values["nome"], "descricao": values["descricao"]}
    #             import pdb;pdb.set_trace()
    #         if event != "editar":
    #             self.__window.close()
    #             return event
        
    
    def seleciona_produto(self, dados):
        l = []
        for id, dado in dados.items():
            l.append(
                [sg.Radio(text=dado, key=id, group_id="")]
            )
        l.append([sg.Button("Selecionar Produto", key="selecionado"), sg.Button("Voltar", key="voltar")])
        self.__window = sg.Window("Selecionar Produto", l)
        while True:
            event, values = self.__window.read()
            if event == "selecionado" and not values:
                self.mostra_mensagem("Selecione um produto!") 
                continue
            elif event == "selecionado" and values:
                for k, v in values.items():
                    if v == True:
                        self.__window.close()
                        return k
            elif event != "selecionado":
                self.__window.close()
                return False
    
    def valida_dados_produto(self, dados):
        preco = self.valida_float(dados["preco"])
        if not preco:
            self.mostra_mensagem("Preco Invalido!")
            return False
    def seleciona_produto(self, dados):
        l = []
        for id, dado in dados.items():
            l.append(
                [sg.Radio(text=dado, key=id, group_id="")]
            )
        l.append([sg.Button("Selecionar Produto", key="selecionado"), sg.Button("Voltar", key="voltar")])
        self.__window = sg.Window("Selecionar Produto", l)
        while True:
            event, values = self.__window.read()
            if event == "selecionado" and not values:
                self.mostra_mensagem("Selecione um produto!") 
                continue
            elif event == "selecionado" and values:
                for k, v in values.items():
                    if v == True:
                        self.__window.close()
                        return k
            elif event != "selecionado":
                self.__window.close()
                return False
    

    def pega_dados_produto(self, categorias):
        l = [
            [sg.Text("Nome do produto"), sg.Input(key="nome")],
            [sg.Text("Descricao do produto"), sg.Input(key="descricao")],
            [sg.Text("Preco"), sg.Input(key="preco")]
        ]
        l.append([sg.Radio(text=nome, group_id="categorias", key=nome) for nome in categorias])
        l.append([sg.Button("Continuar Cadastro", key="cadastrar"), sg.Button("Voltar")])
        self.__window = sg.Window(title="Dados Produto", layout=l)
        while True:
            event, values = self.__window.read()
            if event != "cadastrar":
                self.__window.close()
                return 
            preco = self.valida_float(values["preco"])
            if not preco:
                self.mostra_mensagem("Preco Invalido")
                continue
            dados = {}
            for k, v in values.items():
                if v == True:
                    dados["categoria"] = k
                    break
            dados["nome"] = values["nome"]
            dados["descricao"] = values["descricao"]
            dados["preco"] = preco
            self.__window.close()
            qualidicadores = self.pega_dados_qualificadores()
            dados["qualificadores"] = qualidicadores
            return dados
    
    def pega_dados_qualificadores(self):
        qualificadores = []
        while True:
            l = [
            [sg.Text("Titulo Qualificador"), sg.Input(key="titulo")],
            [sg.Text("Descricao Qualificador"), sg.Input(key="descricao")],
            [sg.Button("Salvar", key="salvar"), sg.Button("Salvar e Adicionar Outro", key="continuar"), sg.Button("Voltar")]
            ]
            self.__window = sg.Window("Dados Qualificador", l)
            event, values = self.__window.read()
            em_branco = False
            if event in ["salvar", "continuar"]:
                for k, v in values.items():
                    if v == "":
                        self.mostra_mensagem("Dados nao pode ficar em branco")
                        em_branco = True
                        self.__window.close()
                        break
                if em_branco:
                    self.__window.close()
                    continue
                elif event == "continuar":
                    qualificadores.append(values)
                    self.__window.close()
                    continue
                if event == "salvar":
                    self.__window.close()

                    qualificadores.append(values)
                    return qualificadores
            else:
                self.__window.close()
                return

            
            # if event == "salvar" and not values and not qualificadores:
            #     self.mostra_mensagem("Adicione pelo menor uma qualificador")
            #     continue
            # elif event in ["salvar", "contisnuar"] and not values and qualificadores:
            #     self.mostra_mensagem("Dados nao pode ficar em branco")
            #     continue
            # if event in ["salvar", "continuar"]:
            #     for k, v in values.items():
            #         if v == "":
            #             self.mostra_mensagem("Dados nao pode ficar em branco")
            #             self.__window.close()
            #             break
            #         continue
            #     if event == "continuar":
            #         qualificadores.append(values)
            #         self.__window.close()
            #         continue
            #     elif event == "salvar":
            #         qualificadores.append(values)
            #         self.__window.close()
            #         return qualificadores
            # if not event in ["salvar", "continuar"]:
            #     self.__window.close()
            #     return qualificadores



    def pega_valor_preco(self, precos):
        l = [
            [sg.Text("Preco"), sg.Input(key="preco")],
        ]
        for p in precos:
            l.append([sg.Text("Preco: R$" + str(p))])
        l.append([sg.Button("Adicionar Preco", key="adicionar")])
        self.__window = sg.Window("Preco", layout=l)
        while True:
            event, values = self.__window.read()
            if event == "adicionar":
                preco = self.valida_float(values["preco"])
                if not preco or not values:
                    self.mostra_mensagem("Preco Invalido!")
                    continue
                self.__window.close()
                return preco
            else:
                self.__window.close()
                return
    

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
    
    def menu_busca(self, categorias):
        l= [
                [sg.Text("Nome do produto"), sg.Input(key="nome_produto")],
                [sg.Radio(text=nome, key=nome, group_id="categorias", default=True if nome == "carne" else False) for nome in categorias],
                [sg.Text("Selecione um dos filtros de busca abaixo:")],
                [sg.Radio("Maior Preco", key="maior_preco", group_id="filtros", default=True), sg.Radio("Menor Preco", key="menor_preco", group_id="filtros")],
                [sg.Radio("Mais confirmacoes", key="mais_confirmacoes", group_id="filtros"), sg.Radio("Menos confirmacoes", key="menos_confirmacoes", group_id="filtros")],
                [sg.Radio("Mais antigo", key="mais_antigo", group_id="filtros"), sg.Radio("Mais recente", key="mais_recente", group_id="filtros")],
                [sg.Button("Buscar", key="buscar"), sg.Button("Voltar")]
            ]
        while True:
            dados_busca = {}
            self.__window = sg.Window("Menu Busca", l)
            event, values = self.__window.read()
            if event == "buscar":
                dados_busca["nome_produto"] = values["nome_produto"]
                for k, v in values.items():
                    if v == True:
                        if k in categorias:
                            dados_busca["categoria"] = k
                        else:
                            dados_busca["modo"] = k
                self.__window.close()
                return dados_busca
            else:
                self.__window.close()
                return

    def cadastra_qualificador(self):
        l = [
            [sg.Text("Qualificador"), sg.Input(key=qualificador)]
        ]
        self.__window = sg.Window("Qualificador", l)
        event, values = self.__window.read()
        print("--- CADASTRO DE QUALIFICADOR ----")
        qualificador = input("Qualificador: ")
        return values["qualificador"]

    def edita_produto(self, default_data, categorias):
        l = [
            [sg.Text("Nome"), sg.Input(default_text=default_data["nome"], key="nome")],
            [sg.Text("Descricao"), sg.Input(default_text=default_data["descricao"], key="descricao")],
            [sg.Radio(text=nome, group_id="categorias", key=nome, default=True if nome == default_data["categoria"] else False) for nome in categorias],
            [sg.Button("Editar", key="editar"), sg.Button("Voltar", key="voltar")]
        ]
        while True:
            self.__window = sg.Window("Editar Produto", l)
            event, values = self.__window.read()
            if event == "editar":
                em_branco = False
                for k, v in values.items():
                    if v == "":
                        self.mostra_mensagem("Todos os dados devem ser preenchidos!")
                        em_branco = True
                        break
                if em_branco:
                    continue
                dados = {
                    "nome": values["nome"],
                    "descricao": values["descricao"],
                }
                for k, v in values.items():
                    if v == True:
                        dados["categoria"] = k
                self.__window.close()
                return dados
            else:
                self.__window.close()
                return 
        
    def exclui_produto(self):
        print("--- ESCLUSAO DE PRODUTO ---")
        id_produto = self.pega_id_produto()
        return id_produto

    def mostra_dados_produtos(self, dados, additional_header=False):
        h = ["NOME", "DESCRICAO", "CATEGORIA", "PRECO", "CONTADOR"]
        if additional_header:
            h.append(additional_header)
        l = [
            [sg.Table(values=dados, headings=h, auto_size_columns=True)],
            [sg.Button("Voltar", key="voltar")]
        ]
        self.__window = sg.Window("Dados Produtos", l)
        event, values = self.__window.read()
        if event:
            self.__window.close()
            return
        
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

    # def mostra_mensagem(self, mensagem):
    #     l = [
    #         [sg.Text(mensagem)],
    #         [sg.Button(button_text="Fechar", key="fechar")]
    #     ]
    #     self.__window = sg.Window("Mensagem", l)
    #     event, values = self.__window.read()
    #     if event == "fehcar":
    #         self.__window.close()

        # print(mensagem)
