class TelaQualificador:
    
    def mostra_dados_qualificador(self, qualidicador):
        print("TITULO: ", qualidicador.nome)
        print("DESCRICAO: ", qualidicador.descricao)
    
    def pega_titulo_qualificador(self):
        titulo = input("Titulo do qualificador: ")
        return titulo
    
    def pega_dados_qualificador(self):
        titulo = self.pega_titulo_qualificador
        descriacao = input("Descricao do qualificador: ")
        return {"titulo": titulo, "descricao": descriacao}
    
    def mostra_mensagem(self, msg):
        print(msg)