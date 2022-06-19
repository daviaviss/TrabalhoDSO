class TelaQualificador:
    
    def mostra_dados_qualificador(self, qualidicador):
        print("TITULO: ", qualidicador.nome)
        print("DESCRICAO: ", qualidicador.descricao)
    
    def pega_titulo_qualificador(self):
        titulo = input("Titulo do qualificador: ")
        return titulo