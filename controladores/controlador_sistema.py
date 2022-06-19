from controladores import controladorProduto, controladorPreco, controladorMercado


class ControladorSistema:
    def __init__(self):
        self.__controlador_produto = controladorProduto.ControladorProduto(self)
        self.__controlador_preco = controladorPreco.ControladorPreco(self)
        self.__controlador_mercado = controladorMercado.ControladorMercado(self)
    
    @property
    def controlador_produto(self):
        return self.__controlador_produto
    
    @property
    def controlador_mercado(self):
        return self.__controlador_mercado

    @property
    def controlador_preco(self):
        return self.__controlador_preco

    def inicializa_sistema(self):
        self.controlador_produto.abre_menu_inicial()
