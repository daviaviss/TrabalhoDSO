from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata


class TelaPessoaJuridica(TelaPessoaAbstrata, TelaAbstrata):
    def pega_dados_pessoa_juridica(self):
        while True:
            nome = input("Nome: ")
            email = input("Email: ")

            cnpj = input("CNPJ: ")

            break
        return {"email": email, "cnpj": cnpj, "nome": nome}

    def mostra_dado_usuario_juridico(self, p):
        print("Nome: ", p.nome)
        print("Email: ", p.email)
        print("CNPJ: ", p.cnpj)
        print("================================")
