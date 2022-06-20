from telas.tela_abstrata import TelaAbstrata


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
        while True:
            cep = input("Insira o CEP: ")
            if not self.valida_cep(cep):
                print("CEP invalido!")
                continue

            numero = input("Insira o numero: ")
            if not self.valida_numero(numero):
                print("Numero invalido!")
                continue
            return {"cep": cep, "numero": numero}
