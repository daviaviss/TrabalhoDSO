from telas.tela_abstrata import TelaAbstrata
from telas.tela_pessoa_abstrata import TelaPessoaAbstrata
from validate_docbr import CNPJ

class TelaPessoaJuridica(TelaPessoaAbstrata, TelaAbstrata):
    def valida_cnpj(self, cnpj):
        obj = CNPJ()
        return obj.validate(cnpj)
    def pega_dados_pessoa_juridica(self):
        while True:
            nome = input("Nome: ")
            email = input("Email: ")
            if not self.valida_email(email):
                self.mostra_mensagem("Email invalido")
                continue

            cnpj = input("CNPJ: ")
            if not self.valida_cnpj(cnpj):
                self.mostra_mensagem("CNPJ invalido!")
                continue

            break
        return {"email": email, "cnpj": cnpj, "nome": nome}

    def mostra_dado_usuario_juridico(self, p):
        print("Nome: ", p.nome)
        print("Email: ", p.email)
        print("CNPJ: ", p.cnpj)
        print("================================")
