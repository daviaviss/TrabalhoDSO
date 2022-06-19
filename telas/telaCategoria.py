from telas.tela_abstrata import TelaAbstrata


class TelaCategoria(TelaAbstrata):
    CATEGORIAS = [
        "carne",
        "higiene",
        "limpeza",
        "bebida",
        "hortfruti",
    ]

    def mostra_categoria(self, categoria):
        print(f"CATEGORIA: {categoria.nome}")

    def pega_nome_categoria(self):
        nome = input("Nome da categoria: ")
        return nome

    def mostra_categorias(self):
        print("[0] - CARNE")
        print("[1] - HIGIENE")
        print("[2] - LIMPEZA")
        print("[3] - BEBIDA")
        print("[4] - HORTFRUTI")
        return self.le_numero_inteiro(
            "Selecione uma das categorias acima: ", [0, 1, 2, 3, 4]
        )
