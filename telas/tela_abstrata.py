from abc import ABC
import PySimpleGUI as sg

class TelaAbstrata(ABC):
    def __init__(self):
        self.__window = None

    def mostra_tela_confirmacao(self):
        l = [
            [sg.Text("TEM CERTEZA QUE DESEJA REALIZAR ESSA ACAO")],
            [sg.Button("SIM", key=0), sg.Button("NAO", key=1)]
        ]
        # print("== TEM CERTEZA QUE DESEJA REALIZAR ESSA ACAO? ==")
        # print("[0] - SIM")
        # print("[1] - NAO")
        self.__window = sg.Window("Tela Confirmacao", l)
        event, values = self.__window.read()
        if event != None:
            self.__window.close()
            return event

    def mostra_mensagem(self, msg):
        sg.Popup(msg)

    def verifica_tipo_dados(self, dados, tipo):
        tipos_dados = {"int": int, "float": float, "dict": dict, "list": list}

        for d in dados:
            try:
                tipos_dados[tipo](d)
            except ValueError:
                return False
        return True

    def mostra_pergunta(self):
        layout = [          
                [sg.Text("Deseja continuar?")],
                [sg.Button("Sim", key=0)],
                [sg.Button("Não", key=1)],
                ]  
        self.__window = sg.Window('Pergunta', layout=layout)

        event, values = self.__window.read()
        return event

    def verifica_dados(self, dados):
        if all(dados):
            return True
        return False

    def pega_dado_generico(self, msg):
        while True:
            dado = input(msg)
            if not self.verifica_dados([dado]):
                continue
            return dado
