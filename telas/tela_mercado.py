from entidades.mercado import Mercado
from telas.tela_abstrata import TelaAbstrata
from validate_docbr import CNPJ
import PySimpleGUI as sg


class TelaMercado(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def pega_cnpj_mercado(self):
        layout = [
                [sg.Text('CNPJ'), sg.InputText(key='cnpj')],
                [sg.Submit('Enviar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window("Dados", layout=layout)
        event, values = self.__window.read()
        self.__window.close()
        return values["cnpj"]

    def valida_inteiro(self, inteiro):
        try:
            int(inteiro)
        except ValueError:
            return False
        return True

    def menu_mercado_pessoa_fisica(self):

        layout = [          
                [sg.Button("Listar Mercado", key=1)],
                [sg.Button("Listar Produtos Mercado", key=5)],
                [sg.Button("Editar Endereco Mercado", key=6)],
                [sg.Button("Editar Nome Mercado", key=7)],
                [sg.Button("Excluir Produto Mercado", key=8)],
                [sg.Button("Gerar Relatorio Mercado", key=9)],
                [sg.Button("Voltar", key=0)],
                ]  
        self.__window = sg.Window('Menu Mercado', layout=layout)

        event, values = self.__window.read()
        self.__window.close
        return event

    def menu_mercado_pessoa_juridica(self):
        layout = [          
                [sg.Button("Listar Mercados", key=1)],
                [sg.Button("Cadastrar Mercado", key=2)],
                [sg.Button("Editar Mercado", key=3)],
                [sg.Button("Excluir Mercado", key=4)],
                [sg.Button("Listar Produtos Mercado", key=5)],
                [sg.Button("Editar Endereço Mercado", key=6)],
                [sg.Button("Editar Nome Mercado", key=7)],
                [sg.Button("Editar Produto Mercado", key=8)],
                [sg.Button("Gerar Relatório Mercado", key=9)],                                
                [sg.Button("Voltar", key=0)],
                ]  
        self.__window = sg.Window('Menu Mercado', layout=layout)

        event, values = self.__window.read()
        self.__window.close
        return event

    def valida_cnpj(self, cnpj):
        obj = CNPJ()
        return obj.validate(cnpj)

    def pega_dados_mercado(self, cnpj=True, permitir_vazio=False):
        while True:
            cnpj_mercado = ""
            dados = {}
            print("---- DADOS DO MERCADO ----")
            nome = input("Nome do mercado: ")
            if not nome and not permitir_vazio:
                print("Esse campo nao pode ficar em branco!")
                continue
            cep = input("CEP do mercado: ")
            if not permitir_vazio and not cep:
                if not self.valida_cep(cep):
                    print("CEP invalido, tente novamente!")
                    continue
            numero = input("Numero do endereço do mercado: ")
            if not numero and not permitir_vazio:
                if not self.valida_inteiro(numero):
                    print("Numero nao valido, tente novamente!")
                    continue
            if cnpj:
                cnpj_mercado = input("CNPJ do mercado: ")
                if not self.valida_cnpj(cnpj_mercado):
                    print("CNPJ invalido! Tente novamente.")
                    continue

            return {"nome": nome, "cep": cep, "numero": numero, "cnpj": cnpj_mercado}

    def mostra_dados_mercado(self, mercado: Mercado):
        print("------------------------------------------")
        print("NOME: ", mercado.nome)
        print("CNPJ: ", mercado.cnpj)
        print("PROPRIETARIO: ", mercado.proprietario.nome)
        print("CEP: ", mercado.endereco.cep)

    def seleciona_mercado(self):
        while True:
            cnpj = input("CNPJ do mercado: ")
            if not self.valida_cnpj(cnpj):
                sg.Print('CPNJ invalido, tente novamente', do_not_reroute_stdout=False)
                #print("CNPJ invalido, tente novamente!")
                continue
            return cnpj
