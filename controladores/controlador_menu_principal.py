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
        self.controlador_cessao.controlador_usuario.abre_menu_usuario()
    
    def abre_opcoes_mercado(self):
        self.controlador_cessao.controlador_mercado.abre_menu_mercado()
    
    def abre_opcoes_produto(self):
        self.controlador_cessao.controlador_produto.abre_menu_produtos()
        
    def abre_menu_principal(self):
        self.tela_menu_principal.abre_menu_principal()
    
    def desloga(self):
        self.controlador_cessao.desloga()
    
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