from telas import telaPreco
class ControladorPreco:
    def __init__(self, controlador_sitema):
        self.__controlador_sistema = controlador_sitema
        self.__precos = []

    def busca_preco(self, preco, produto):
        for p in self.__precos:
            if p.valor == preco and p.produto == produto:
                return p
        return False



