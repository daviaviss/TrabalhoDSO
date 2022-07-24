from entidades.preco import Preco
from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPreco(TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def pega_valor_preco(self):
        layout = [
                [sg.Text("Preco:"), sg.Input(key="preco")],
                [sg.Button("Cadastrar preco", key="cadastrar_preco")]
            ]
        self.__window = sg.Window("Preco", layout)
        while True:
            event, values = self.__window.read()
            try:
                preco = float(values["preco"])
                if preco < 0:
                    print("Insira um valor valido!")
                    continue
                preco = "{:.2f}".format(preco)
            except ValueError:
                print("Insira um valor valido!")
                continue
            self.__window.close()
            return preco

    # def mostra_dado_preco(self, preco: Preco):
    #     h = ["ID", "PRODUTO", "VALOR", "CONTADOR", "DATA POSTAGEM"]
    #     layout = [
    #         [sg.Table(values=data, headings=h)],
    #         [sg.Button("Fechar")]
    #     ]
    #     while True:
    #         event, values = self.__window.read()
    #         if event == "Fechar":
    #             self.__window.close()
    #             break
    #     print("-----------------------------------------")
    #     print("ID: ", str(preco.id))
    #     print("PRODUTO: ", preco.produto)
    #     print("VALOR: ", preco.valor)
    #     print("CONTADOR: ", preco.contador)
    #     print("DATA POSTAGEM: ", preco.data_postagem)
