from entidades.qualificador import Qualificador
from telas.telaQualificador import TelaQualificador


class ControladorQualificador:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_qualificador = TelaQualificador()
        self.__qualificadores = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def tela_qualificador(self):
        return self.__tela_qualificador

    @property
    def qualificadores(self):
        return self.__qualificadores

    def cadastra_qualificador(self, produto):
        while True:
            dados = self.tela_qualificador.pega_dados_qualificador()
            if not self.pega_qualificador_por_titulo(dados["titulo"]):
                produto.qualificadores.append(
                    Qualificador(dados["titulo"], dados["descricao"])
                )
                for q in produto.qualificadores:
                    if q.titulo == dados["titulo"]:
                        self.qualificadores.append(q)
                        break
                self.tela_qualificador.mostra_mensagem(
                    "Qualificador cadastrado com sucesso!"
                )
                
                break
            else:
                self.tela_qualificador.mostra_mensagem(
                    "Um qualificador com esse titulo ja existe, tente novamente!"
                )

    def pega_qualificador_por_titulo(self):
        titulo = self.tela_sistema.pega_nome_qualificador()
        for q in self.qualificadores:
            if q.titulo == titulo:
                return q
        return False

    def lista_qualificadores(self):
        for q in self.qualificadores:
            self.tela_sistema.mostra_dados_qualificador(q)
