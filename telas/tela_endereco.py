from telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaEndereco(TelaAbstrata):
    def valida_cep(self, cep):
        cep = cep.replace("-", "")
        if len(cep) == 8:
            return True

    def valida_numero(self, numero):
        try:
            int(numero)
        except ValueError:
            return False
        return True

    def pega_dados_endereco(self):

        layout = [
            [sg.Text("CEP"), sg.Input(key="cep")],
            [sg.Text("Numero"), sg.Input(key="numero")],
        ]
        self.__window = sg.Window(title="Endereço", layout=layout)
        while True:
            event, values = self.__window.read()
            dados = []
            dados.append(values["cep"])
            dados.append(values["numero"])
            if not self.valida_cep(dados[0]) and self.valida_numero(dados[1]):
                print("Dados invalidos!")
                continue
            self.__window.close()
            return {"cep": values["cep"], "numero": values["numero"]}
