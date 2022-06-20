from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata


class TelaPessoaFisica(TelaPessoaAbstrata, TelaAbstrata):
    def pega_dados_pessoa_fisica(self):
        while True:
            nome = input("Nome: ")
            email = input("Email: ")
            cpf = input("CPF: ")
            break
        return {"email": email, "cpf": cpf, "nome": nome}

    def mostra_dado_usuario_fisico(self, p):
        print("Nome: ", p.nome)
        print("Email: ", p.email)
        print("CPF: ", p.cpf)
        print("================================")
