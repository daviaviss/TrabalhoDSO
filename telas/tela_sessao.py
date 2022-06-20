from telas.tela_abstrata import TelaAbstrata
from validate_docbr import CPF, CNPJ


class TelaSessao(TelaAbstrata):
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

    def pega_email(self):
        email = input("Email: ")
        return email
