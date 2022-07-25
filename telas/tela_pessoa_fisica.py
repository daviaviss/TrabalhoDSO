from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
import PySimpleGUI as sg

class TelaPessoaFisica(TelaPessoaAbstrata, TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def edita_pessoa_fisica(self, default_data):
        layout = [[sg.Text('Edicao Pessoa Fisica')],           
                    [sg.Text("Nome"), sg.Input(key="nome", default_text=default_data["nome"])],
                    [sg.Text("Email"), sg.Input(key="email", default_text=default_data["email"])],
                    [sg.Text("CPF",), sg.Input(key="cpf", default_text=default_data["cpf"], disabled=True, readonly=True)],
                    [sg.Button("Editar", key="editar"), sg.Button("Cancelar")]
                    ]
        self.__window = sg.Window("Editar Usuario Fisica", layout=layout)
        # while True:
        event, values = self.__window.read()
        if event == "editar":
            self.__window.close()
            return {"email": values["email"], "nome": values["nome"]}
        if event != "editar":
            self.__window.close()
            return event


    def pega_dados_pessoa_fisica(self):
        layout = [[sg.Text('Cadastro Pessoa Fisica')],           
                    [sg.Text("Nome"), sg.Input(key="nome")],
                    [sg.Text("Email"), sg.Input(key="email")],
                    [sg.Text("CPF",), sg.Input(key="cpf")],
                    [sg.Button("Cadastrar", key="cadastrar"), sg.Button("Cancelar", key="cancelar")]
                    ]
        self.__window = sg.Window('Menu Principal', layout)
        while True:
            event, values = self.__window.read()
            if event == "cadastrar":
                self.__window.close()
                return {"email": values["email"], "cpf": values["cpf"], "nome": values["nome"]}
            elif event == "cancelar":
                self.__window.close()
                return event


    def mostra_dado_usuario_fisico(self, data):
        h = ["Nome", "Email", "CPF"]
        layout = [
            [sg.Table(values=data, headings=h)],
            [sg.Button("Fechar")]
        ]
        self.__window = sg.Window("Dados Usuario Fisico", layout)
        while True:
            event, values = self.__window.read()
            if event == "Fechar":
                self.__window.close()
                break