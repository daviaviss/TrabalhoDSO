from telas.tela_abstrata import TelaAbstrata
from email_validator import validate_email
import PySimpleGUI as sg


class TelaPessoaAbstrata(TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def menu_usuario(self):
        layout = [          
            [sg.Button("Editar Usuário", key=1)],
            [sg.Button("Excluir Usuário", key=2)],
            [sg.Button("Voltar", key=0)]
            ]  
        self.__window = sg.Window('Menu Principal', layout=layout)

        event, values = self.__window.read()
        self.__window.close()
        return event


    def pega_nome_email_usuario(self):
        layout = [
                [sg.Text('Nome'), sg.InputText(key='nome')],
                [sg.Text('Email'), sg.InputText(key='email')],
                [sg.Submit('Enviar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window("Dados", layout=layout)
        event, values = self.__window.read()
        nome = values['nome']
        email = values['email']
        self.__window.close()
        return {"nome": nome, "email": email}

    def valida_email(self, email):
        try:
            validate_email(email)
        except Exception:
            return False
        return True
