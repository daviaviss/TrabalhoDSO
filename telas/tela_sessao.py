from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg
class TelaSessao(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def mostra_menu_principal(self):
        layout = [          
                    [sg.Button("Entrar", key=1)],
                    [sg.Button("Cadastrar Usuario Fisico", key=2)],
                    [sg.Button("Cadastrar Usuario Juridico", key=3)],
                    [sg.Button("Listar Usuarios", key=4)],
                    [sg.Button("Encerrar Programa", key=0)]
                    ] 
        self.__window = sg.Window('Menu Principal', layout=layout)
        event, values = self.__window.read()
        if event != None:
            self.__window.close()
            return event

    def pega_email(self):
        layout = [
            [sg.Text('Email'), sg.InputText(key='email')],
            [sg.Submit('Enviar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window("Email", layout=layout)
        event, values = self.__window.read()
        self.__window.close()
        return values["email"]