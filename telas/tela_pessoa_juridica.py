from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
import PySimpleGUI as sg
from PySimpleGUI import Table
class TelaPessoaJuridica(TelaPessoaAbstrata, TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def edita_pessoa_juridica(self, default_data):
        layout = [[sg.Text('Edicao Pessoa Fisica')],           
                    [sg.Text("Nome"), sg.Input(key="nome", default_text=default_data["nome"])],
                    [sg.Text("Email"), sg.Input(key="email", default_text=default_data["email"])],
                    [sg.Text("CNPJ",), sg.Input(key="cnpj", default_text=default_data["cnpj"], disabled=True, readonly=True)],
                    [sg.Button("Editar", key="editar"), sg.Button("Cancelar")]
                    ]
        self.__window = sg.Window("Editar Usuario Juridica", layout=layout)
        event, values = self.__window.read()
        if event == "editar":
            self.__window.close()
            return {"email": values["email"], "nome": values["nome"]}
        if event != "editar":
            self.__window.close()
            return event

    def pega_dados_pessoa_juridica(self):
        layout = [[sg.Text('Cadastro Pessoa Juridica')],           
                    [sg.Text("Nome"), sg.Input(key="nome")],
                    [sg.Text("Email"), sg.Input(key="email")],
                    [sg.Text("CNPJ",), sg.Input(key="cnpj")],
                    [sg.Button("Cadastrar", key="cadastrar")]
                    ]
        self.__window = sg.Window('Menu Principal', layout)
        event, values = self.__window.read()
        if event == "cadastrar":
            self.__window.close()
            return {"email": values["email"], "cnpj": values["cnpj"], "nome": values["nome"]}
        else:
            return None
    def mostra_dado_usuario_juridico(self, p):
        h = ["Nome", "Email", "CNPJ"]
        l = [
            [sg.Table(values=p, headings=h, auto_size_columns=True)],
            [sg.Button(button_text="Fechar")]
        ]
        self.__window = sg.Window("Dados Usuario Juridico", l)
        event, values = self.__window.read()
        if event:
            self.__window.close()
