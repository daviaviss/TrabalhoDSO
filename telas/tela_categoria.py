import PySimpleGUI as sg
from telas.tela_abstrata import TelaAbstrata

class TelaCategoria(TelaAbstrata):
    def __init__(self):
        self.__window = None

    CATEGORIAS = [
        "carne",
        "higiene",
        "limpeza",
        "bebida",
        "hortfruti",
    ]

    def mostra_categoria(self, categoria):
        sg.Popup({categoria.nome})

    def pega_nome_categoria(self):
        layout = [
            [sg.Text('Digite o nome da categoria')],
            [sg.Text('Nome da categoria', size =(15, 1)), sg.InputText(key='nome')],
            [sg.Submit('Enviar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('Categoria', layout)
        event, values = self.__window.read()
        window.close()
        return values['nome']

    def mostra_categorias(self):
        layout = [         
                [sg.Text('Escolha uma categoria')],             
                [sg.Button("Carne", key=0)],
                [sg.Button("Higiene", key=1)],
                [sg.Button("Limpeza", key=2)],
                [sg.Button("Bebida", key=3)],
                [sg.Button("Hortfruti", key=4)],
                ]

        self.__window = sg.Window('Categorias', layout=layout)
        event, values = self.__window.read()
        self.__window.close
        return event