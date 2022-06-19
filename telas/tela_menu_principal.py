from telas.tela_abstrata import TelaAbstrata

class TelaMenuPrincipal(TelaAbstrata):
    
    def abre_menu_principal(self):
        print("--- MENU PRINCIPAL ---")
        print("[1] - OPCOES USUARIO")
        print("[2] - OPCOES MERCADO")
        print("[3] - OPCOES PRODUTOS")
        print("[0] - DESLOGAR")
        
        opcao = self.le_numero_inteiro("Selecione uma das opcoes acima: ", [0, 1, 2, 3])
        return opcao