from entidades.mercado import Mercado
from telas.tela_abstrata import TelaAbstrata
from validate_docbr import CNPJ
import PySimpleGUI as sg


class TelaMercado(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def pega_cnpj_mercado(self):
        layout = [
                [sg.Text('CNPJ'), sg.InputText(key='cnpj')],
                [sg.Submit('Enviar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window("Dados", layout=layout)
        event, values = self.__window.read()
        self.__window.close()
        return values["cnpj"]

    def valida_inteiro(self, inteiro):
        try:
            int(inteiro)
        except ValueError:
            return False
        return True

    def menu_mercado_pessoa_fisica(self):

        layout = [          
                [sg.Button("Listar Mercado", key=1)],
                [sg.Button("Listar Produtos Mercado", key=5)],
                [sg.Button("Voltar", key=0)],
                ]  
        self.__window = sg.Window('Menu Mercado', layout=layout)

        event, values = self.__window.read()
        self.__window.close()
        return event

    def menu_mercado_pessoa_juridica(self):
        layout = [          
                [sg.Button("Listar Mercados", key=1)],
                [sg.Button("Cadastrar Mercado", key=2)],
                [sg.Button("Editar Mercado", key=3)],
                [sg.Button("Excluir Mercado", key=4)],
                [sg.Button("Listar Produtos Mercado", key=5)],
                [sg.Button("Voltar", key=0)],
                ]  
        self.__window = sg.Window('Menu Mercado', layout=layout)

        event, values = self.__window.read()
        self.__window.close()
        return event

    def valida_cnpj(self, cnpj):
        obj = CNPJ()
        return obj.validate(cnpj)

    def pega_dados_mercado(self, cnpj=True, permitir_vazio=False):
        l = [
            [sg.Text("Nome do mercado"), sg.Input(key="nome")],
            [sg.Text("CEP do mercado"), sg.Input(key="cep")],
            [sg.Text("Numero do endereço do mercado"), sg.Input(key="numero")],
            [sg.Text("CNPJ do mercado"), sg.Input(key="cnpj")],
            [sg.Button("Cadastrar", key="cadastrar")],
        ]
        self.__window = sg.Window("Cadastar Mercado", l)
        while True:
            event, values = self.__window.read()
            if event == "cadastrar":
                if not all(
                    [bool(v) for k, v in values.items()]
                ):
                    self.mostra_mensagem("Nenhum campo pode ficar em branco!")
                    continue
                else:
                    self.__window.close()
                    return values
            else:
                self.__window.close()
                return event



    def mostra_dados_mercado(self, dados):
        h = ["NOME", "CNPJ", "CEP", "PROPRIETARIO"]
        l = [
            [sg.Table(dados, headings=h, justification="center")],
            [sg.Button("Voltar")]
        ]
        self.__window = sg.Window("Dados Mercados", l)
        event, values = self.__window.read()
        if event:
            self.__window.close()
            return
    def seleciona_mercado(self, dados):
        l = [
            [sg.Text("SELECIONE UM DOS MERCADOS ABAIXO")]
        ]
        for id, dado in dados.items():
            l.append(
                [sg.Radio(text=dado, key=id, group_id="")]
            )
        l.append([sg.Button("Selecionar Mercado", key="selecionado"), sg.Button("Voltar", key="voltar")])
        self.__window = sg.Window("Selecionar Mercado", l)
        while True:
            event, values = self.__window.read()
            if event == "selecionado" and not values:
                self.mostra_mensagem("Selecione um mercado!") 
                continue
            elif event == "selecionado" and values:
                for k, v in values.items():
                    if v == True:
                        self.__window.close()
                        return k
            elif event != "selecionado":
                self.__window.close()
                return False

    def edita_mercado(self, default_data):
        layout = [[sg.Text('Edicao Mercado')],           
                    [sg.Text("Nome"), sg.Input(key="nome", default_text=default_data["nome"])],
                    [sg.Text("CNPJ"), sg.Input(key="cnpj", default_text=default_data["cnpj"], disabled=True, readonly=True)],
                    [sg.Text("CEP",), sg.Input(key="cep", default_text=default_data["cep"])],
                    [sg.Text("NUMERO"), sg.Input(key="numero", default_text=default_data["numero"])],
                    [sg.Button("Editar", key="editar"), sg.Button("Cancelar")]
                    ]
        self.__window = sg.Window("Editar Usuario Fisica", layout=layout)
        while True:
            event, values = self.__window.read()
            if event == "editar":
                if any(
                    [v == "" for k, v in values.items()]
                ):
                    self.mostra_mensagem("Nenhum Dado pode ficar em branco")
                    continue
                self.__window.close()
                return {"nome": values["nome"], "cnpj": values["cnpj"], "cep": values["cep"], "numero": values["numero"]}
            if event != "editar":
                self.__window.close()
                return False