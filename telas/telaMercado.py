class TelaMercado:
    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def pega_dados_mercado(self):
        while True:
            dados = {}
            print("---- DADOS DO MERCADO ----")
            dados["nome"] = input("Nome do mercado: ")
            dados["cep"] = input("CEP do mercado: ")
            dados["numero"] = input("Numero do endereço do mercado: ")
            dados["cnpj"] = input("CNPJ do mercado: ")

            if not self.verifica_integridade_dados():
                self.mostra_mensagem("Dados inválidos, tente novamente!")
                continue
            return dados

    def mostra_dados_mercado(self, dados):
        print("Nome do mercado: ", dados["nome"])
        print("CEP do mercado: ", dados["cep"])
        print("CNPJ do mercado: ", dados["cnpj"])
