from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
import PySimpleGUI as sg
from PySimpleGUI import Table
class TelaPessoaJuridica(TelaPessoaAbstrata, TelaAbstrata):
    def __init__(self):
        self.__window = None

    def pega_dados_pessoa_juridica(self):
        layout = [[sg.Text('Cadastro Pessoa Juridica')],           
                    [sg.Text("Nome"), sg.Input(key="nome")],
                    [sg.Text("Email"), sg.Input(key="email")],
                    [sg.Text("CNPJ",), sg.Input(key="cnpj")],
                    [sg.Button("Cadastrar", key="cadastrar")]
                    ]
        self.__window = sg.Window('Menu Principal', layout)
        while True:
            event, values = self.__window.read()
            if event == "cadastrar":
                self.__window.close()
                break
        return {"email": values["nome"], "cnpj": values["cnpj"], "nome": values["nome"]}

    def mostra_dado_usuario_juridico(self, p):
        h = ["Nome", "Email", "CNPJ"]
        l = [
            [sg.Table(values=p, headings=h, auto_size_columns=True)],
            [sg.Button(button_text="Fechar")]
        ]
        self.__window = sg.Window("Dados Usuario Juridico", l)
        event, values = self.__window.read()
        while True:
            if event == "Fechar":
                self.__window.close()
                break