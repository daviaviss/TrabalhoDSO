from telas.tela_abstrata import TelaAbstrata
from validate_docbr import CPF, CNPJ
from email_validator import validate_email


class TelaCessao(TelaAbstrata):
    def mostra_menu_principal(self):
        print("--- MENU PRINCIPAL ---")
        print("[1] - ENTRAR")
        print("[2] - CADASTRAR USUARIO FISICO")
        print("[3] - CADASTRAR USUARIO JURIDICO")
        print("[4] - LISTAS USUARIOS")
        print("[0] - ENCERRAR PROGRAMA")
        msg = "Insira uma das opcoes acima: "
        opcao = self.le_numero_inteiro(msg, [1, 2, 3, 4, 0])
        return opcao

    def valida_cpf(self, cpf):
        obj = CPF()
        return obj.validate(cpf)

    def valida_cnpj(self, cnpj):
        obj = CNPJ()
        return obj.validate(cnpj)
    
    def valida_email(self, email):
        try:
            validate_email(email)
        except Exception:
            return False
        return True
    
    def pega_email(self):
        while True:
            email = input("Email: ")
            if self.valida_email(email):
                break
            self.mostra_mensagem("Email invalido!")
        return email



    def mostra_dados_usuario(self, usuario, tipo):
        print(f"NOME {usuario.nome}")
        print(f"EMAIL: {usuario.email}")
        if tipo == "fisico":
            print(f"CPJ: {usuario.cpf}")
        elif tipo == "juridico":
            print(f"CNPJ: {usuario.cnpj}")