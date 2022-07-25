from abc import ABC
from errno import ECANCELED
import PySimpleGUI as sg

class TelaAbstrata(ABC):
    def __init__(self):
        self.__window = None

    def mostra_tela_confirmacao(self):
        l = [
            [sg.Text("TEM CERTEZA QUE DESEJA REALIZAR ESSA ACAO")],
            [sg.Button("SIM", key=0), sg.Button("NAO", key=1)]
        ]
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
    
    def pega_qualificador(self):
        l = [
            [sg.Text("Titulo Qualificador"), sg.Input("titulo")],
           [sg.Text("Descricao Qualificador"), sg.Input("descricao")], 
           [sg.Button("Adicionar", key="adicionar"), sg.Button("Voltar")]
        ]
        while True:
            self.__window = sg.Window("Dados Qualificador", l)
            event, values = self.__window.read()
            if event == "adicionar":
                if not values["titulo"] or not values["descricao"]:
                    self.mostra_mensagem("Todos os dados devem ser preenchidos!")
                    continue
                self.__window.close()
                return values
            else:
                self.__window.close()
                return

    def pega_dado_generico(self, msg):
        l = [
            sg.Text("")
        ]

    def valida_float(self, valor):
        try:
            valor = float("{:.2f}".format(float(valor)))
            if valor < 0:
                return False
            return valor

        except:
            return False
    
