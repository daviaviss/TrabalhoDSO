from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaMenuPrincipal(TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def abre_menu_principal(self):
        layout = [          
                [sg.Button("Opções Usuário", key=1)],
                [sg.Button("Opções Mercado", key=2)],
                [sg.Button("Opções Produtos", key=3)],
                [sg.Button("Deslogar", key=0)]
                ]  
        self.__window = sg.Window('Menu Principal', layout=layout)

        event, values = self.__window.read()
        if event != None:
            self.__window.close()
            return event