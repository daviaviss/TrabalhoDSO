from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
import PySimpleGUI as sg

class TelaPessoaFisica(TelaPessoaAbstrata, TelaAbstrata):
    def __init__(self):
        self.__window = None

    def pega_dados_pessoa_fisica(self):
        layout = [[sg.Text('Cadastro Pessoa Fisica')],           
                    [sg.Text("Nome"), sg.Input(key="nome")],
                    [sg.Text("Email"), sg.Input(key="email")],
                    [sg.Text("CPF",), sg.Input(key="cpf")],
                    [sg.Button("Cadastrar", key="cadastrar"), sg.Cancel("Cancelar")]
                    ]
        self.__window = sg.Window('Menu Principal', layout)
        while True:
            event, values = self.__window.read()
            if event == "cadastrar":
                self.__window.close()
                break
        return {"email": values["email"], "cpf": values["cpf"], "nome": values["nome"]}

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