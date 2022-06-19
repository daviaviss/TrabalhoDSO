from entidades.mercado import Mercado
from telas.tela_abstrata import TelaAbstrata
from validate_docbr import CNPJ


class TelaMercado(TelaAbstrata):
    def pega_cnpj_mercado(self):
        cnpj = input("CNPJ do mercado: ")
        return cnpj

    def valida_cep(self, cep):
        cep = cep.replace("-", "")
        if len(cep) == 8:
            return True

        return False

    def valida_inteiro(self, inteiro):
        try:
            int(inteiro)
        except ValueError:
            return False
        return True

    def menu_mercado_pessoa_fisica(self):
        
        print("--- MENU MERCADO ---")
        print("[1] - LISTAR MERCADOS")
        print("[0] - VOLTAR")
        return self.le_numero_inteiro("Insira uma das opcoes acima: ", [0, 1])

    
    
    def menu_mercado_pessoa_juridica(self):
        print("--- MENU MERCADO ---")
        print("[1] - LISTAR MERCADOS")
        print("[2] - CADASTRAR MERCADO")
        print("[3] - EDITAR MERCADO")
        print("[4] - EXCLUIR MERCADO")
        print("[0] - VOLTAR")
        return self.le_numero_inteiro("Insira uma das opcoes acima: ", [0, 1, 2, 3, 4])

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
        print("=========================================")
        print("Nome do mercado: ", mercado.nome)
        print("CEP do mercado: ", mercado.endereco.cep)
        print("Numero do mercado: ", mercado.endereco.numero)
        print("CNPJ do mercado: ", mercado.cnpj)
        print("Proprietario: ", mercado.proprietario.nome)

    def seleciona_mercado(self):
        while True:
            cnpj = input("CNPJ do mercado: ")
            if not self.valida_cnpj(cnpj):
                print("CNPJ invalido, tente novamente!")
                continue
            return cnpj
