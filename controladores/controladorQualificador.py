from telas.telaQualificador import TelaQualificador
class ControladorQualificador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_sistema = TelaQualificador()
        self.__qualificadores = []
        
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_sistema(self):
        return self.__tela_sistema
    
    @property
    def qualificadores(self):
        return self.__qualificadores
    
    def pega_qualificador_por_titulo(self):
        titulo = self.tela_sistema.pega_nome_qualificador()
        for q in self.qualificadores:
            if q.titulo == titulo:
                return q
        return False
    
    def lista_qualificadores(self):
        for q in self.qualificadores:
            self.tela_sistema.mostra_dados_qualificador(q)