import PySimpleGUI as sg
from telas.tela_abstrata import TelaAbstrata

class TelaCategoria(TelaAbstrata):
    CATEGORIAS = [
        "carne",
        "higiene",
        "limpeza",
        "bebida",
        "hortfruti",
    ]

    def mostra_categoria(self, categoria):
        sg.theme('SandyBeach') 
        sg.Print({categoria.nome}, do_not_reroute_stdout=False)

    def pega_nome_categoria(self):
        sg.theme('SandyBeach') 
        layout = [
            [sg.Text('Digite o nome da categoria')],
            [sg.Text('Nome da categoria', size =(15, 1)), sg.InputText()],
            [sg.Enviar(), sg.Cancelar()]
        ]

        window = sg.Window('Categoria', layout)
        nome = window.read()
        window.close()
        return nome

    def mostra_categorias(self):
        sg.theme('SandyBeach')
        layout = [
            [sg.Radio('Carne', '0', default=True)],
            [sg.Radio('Higiene', '1'),]
            [sg.Radio('Limpeza', '2'),]
            [sg.Radio('Bebida', '3')]
            [sg.Radio('Hortfruti' '4')],
            [sg.Button('Enviar'), sg.Cancelar()]
        ]

        window = sg.Window('Categoria', layout)
        window.close()
        return window.read()