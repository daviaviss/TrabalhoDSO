from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
class TelaSessao(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def mostra_menu_principal(self):
        
        # sg.popup('popup')

        layout = [          
                 [sg.Button("Entrar", key=1)],
                 [sg.Button("Cadastrar Usuario Fisico", key=2)],
                 [sg.Button("Cadastrar Usuario Juridico", key=3)],
                 [sg.Button("Listar Usuarios", key=4)],
                 [sg.Button("Ecerrar Programa", key=0)]
                 ]  
        self.__window = sg.Window('Menu Principal', layout=layout)

        opcao = self.le_numero_inteiro("", [1, 2, 3, 4, 0], self.__window)
        return opcao

    def pega_email(self):
        l = [
            [sg.Text("Email"), sg.Input(key="email")]
        ]
        self.__window = sg.Window("Email", layout=l)
        event, values = self.__window.read()
        self.__window.close()
        # email = input("Email: ")
        return values["email"]