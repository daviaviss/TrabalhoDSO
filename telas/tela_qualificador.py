from code import interact
from multiprocessing.sharedctypes import Value
from entidades.qualificador import Qualificador
from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaQualificador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def mostra_dados_qualificador(self, qualificador: Qualificador):
        h = ["ID", "TITULO", "DESCRICAO"]
        l = [
            [sg.Table(values=qualificador, headings=h)],
            [sg.Button("Fechar", key="fechar")]
        ]
        self.__window = sg.Window(title="Dados Qualificador", layout=l)
        event, values = self.__window.read()
        # print("---------------------------------------------------")
        # print("ID: ", str(qualificador.id))
        # print("TITULO: ", qualificador.titulo)
        # print("DESCRICAO: ", qualificador.descricao)
        # print("-----------------------------------------------------")
        self.__window.close

    def pega_titulo_qualificador(self):
        l = [
            [sg.Text("Titulo do qualificador"), sg.Input(key="titulo")]
        ]
        self.__window = sg.Window("Titulo Qualificador", layout=l)
        event, values = self.__window.read()
        self.__window.close()
        return values["titulo"]

    def pega_dados_qualificador(self):
        l = [
            [sg.Text("Descricao do qualificador"), sg.Input(key="titulo")]
        ]
        titulo = self.pega_titulo_qualificador()
        self.__window = sg.Window("Dados Qualificador", layout=l)
        event, values = self.__window.read()
        # descricao = input("Descricao do qualificador: ")
        return {"titulo": titulo, "descricao": values["descricao"]}

    def seleciona_qualificador(self, dados):
        l = [
            [sg.Radio(text=dado, group_id="qualificadores", key=id) for id, dado in dados.items()],
            [sg.Button("Cconfirmar", key="confirmar"), sg.Button("Voltar")]
        ]
        while True:
            self.__window = sg.Window("Dados Qualificador", l)
            event, values = self.__window.read()
            if event == "confirmar":
                for k, v in values.items():
                    if v == True:
                        self.__window.close()
                        return k
                self.mostra_mensagem("Selecione Um Qualificador!")
                continue
            else:
                self.__window.close()
                return 