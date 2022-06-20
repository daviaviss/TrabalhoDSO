from abc import ABC


class TelaAbstrata(ABC):
    def mostra_tela_confirmacao(self):
        print("== TEM CERTEZA QUE DESEJA REALIZAR ESSA ACAO? ==")
        print("[0] - SIM")
        print("[1] - NAO")
        opcao = self.le_numero_inteiro("Escolhe uma das opcoes acima: ", [0, 1])

    def mostra_mensagem(self, msg):
        print(msg)

    def le_numero_inteiro(self, msg, inteiros_validos):
        while True:
            opcao = input(msg)
            try:
                opcao = int(opcao)
                if not opcao in inteiros_validos:
                    self.mostra_mensagem("Selecione um dos valores acima!")
                    continue
            except ValueError:
                self.mostra_mensagem("Insira um valor inteiro!")
                continue
            return opcao

    def verifica_tipo_dados(self, dados, tipo):
        tipos_dados = {"int": int, "float": float, "dict": dict, "list": list}

        for d in dados:
            try:
                tipos_dados[tipo](d)
            except ValueError:
                return False
        return True

    def mostra_pergunta(self):
        print("== DESEJA CONTINUAR? ==")
        print("[0] - SIM")
        print("[1] - NAO")
        return self.le_numero_inteiro("Selecione uma das alternativas: ", [0, 1])

    def verifica_dados(self, dados):
        if all(dados):
            return True
        return False

    def pega_dado_generico(self, msg):
        while True:
            dado = input(msg)
            if not self.verifica_dados([dado]):
                continue
            return dado
