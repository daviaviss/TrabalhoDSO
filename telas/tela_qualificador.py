from code import interact
from multiprocessing.sharedctypes import Value
from entidades.qualificador import Qualificador
from telas.tela_abstrata import TelaAbstrata


class TelaQualificador(TelaAbstrata):
    def mostra_dados_qualificador(self, qualificador: Qualificador):

        print("---------------------------------------------------")
        print("ID: ", str(qualificador.id))
        print("TITULO: ", qualificador.titulo)
        print("DESCRICAO: ", qualificador.descricao)
        print("-----------------------------------------------------")

    def pega_titulo_qualificador(self):
        titulo = input("Titulo do qualificador: ")
        return titulo

    def pega_dados_qualificador(self):
        titulo = self.pega_titulo_qualificador()
        descricao = input("Descricao do qualificador: ")
        return {"titulo": titulo, "descricao": descricao}
