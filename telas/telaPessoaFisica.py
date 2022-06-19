from telas.tela_abstrata import TelaAbstrata

class TelaPessoaFisica(TelaAbstrata):
    
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