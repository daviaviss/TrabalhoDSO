from entidades.preco import Preco
from telas.tela_abstrata import TelaAbstrata


class TelaPreco(TelaAbstrata):
    def pega_valor_preco(self):
        while True:
            preco = input("Insira o preco do produto: ")
            try:
                preco = float(preco)
                if preco < 0:
                    print("Insira um valor valido!")
                    continue
                preco = "{:.2f}".format(preco)
            except ValueError:
                print("Insira um valor valido!")
                continue
            return preco

    def mostra_dado_preco(self, preco: Preco):
        print("-----------------------------------------")
        print("ID: ", str(preco.id))
        print("PRODUTO: ", preco.produto)
        print("VALOR: ", preco.valor)
        print("CONTADOR: ", preco.contador)
        print("DATA POSTAGEM: ", preco.data_postagem)
