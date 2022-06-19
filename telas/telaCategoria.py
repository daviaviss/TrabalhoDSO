class TelaCategoria:
    
    def mostra_categoria(self, categoria):
        print(f'CATEGORIA: {categoria.nome}')

    def pega_nome_categoria(self):
        nome = input("Nome da categoria: ")
        return nome