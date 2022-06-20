from telas.tela_menu_principal import TelaMenuPrincipal


class ControladorMenuPrincipal:
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__tela_menu_principal = TelaMenuPrincipal()

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao

    @property
    def tela_menu_principal(self):
        return self.__tela_menu_principal

    def abre_opcoes_usuario(self):
        if hasattr(self.controlador_cessao.usuario_atual, "cnpj"):
            self.controlador_cessao.controlador_pessoa_juridica.abre_tela()
        else:
            self.controlador_cessao.controlador_pessoa_fisica.abre_tela()

    def abre_opcoes_mercado(self):
        self.controlador_cessao.controlador_mercado.abre_menu_mercado()

    def abre_opcoes_produto(self):
        self.controlador_cessao.controlador_produto.abre_menu_produto()

    def abre_menu_principal(self):
        self.tela_menu_principal.abre_menu_principal()

    def desloga(self):
        self.controlador_cessao.usuario_atual = None

    def abre_menu_principal(self):
        opcoes = {
            1: self.abre_opcoes_usuario,
            2: self.abre_opcoes_mercado,
            3: self.abre_opcoes_produto,
        }
        while True:
            opcao = self.tela_menu_principal.abre_menu_principal()
            if opcao == 0:
                self.desloga()
                break
            opcoes[opcao]()
