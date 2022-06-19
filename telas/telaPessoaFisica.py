from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
from validate_docbr import CPF


class TelaPessoaFisica(TelaPessoaAbstrata, TelaAbstrata):
    def valida_cpf(self, cpf):
        obj = CPF()
        return obj.validate(cpf)

    def pega_dados_pessoa_fisica(self):
        while True:
            nome = input("Nome: ")
            email = input("Email: ")
            if not self.valida_email(email):
                self.mostra_mensagem("Email invalido")
                continue

            cpf = input("CPF: ")
            if not self.valida_cpf(cpf):
                self.mostra_mensagem("CPF invalido!")
                continue

            break
        return {"email": email, "cpf": cpf, "nome": nome}

    def mostra_dado_usuario_fisico(self, p):
        print("Nome: ", p.nome)
        print("Email: ", p.email)
        print("CPF: ", p.cpf)
        print("================================")
