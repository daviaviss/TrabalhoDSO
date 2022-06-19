from telas.telaPessoaFisica import TelaPessoaFisica
from entidades.pessoaFisica import PessoaFisica
class ControladorPessoaFisica:

    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__pessoas_fisicas = []
        self.__tela_pessoa_fisica = TelaPessoaFisica()

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao
    
    @property
    def pessoas_fisicas(self):
        return self.__pessoas_fisicas
    
    @property
    def tela_pessoa_fisica(self):
        return self.__tela_pessoa_fisica
    
    def verifica_pessoa_fisica_existente(self, email, cpf):
        for p in self.pessoas_fisicas:
            if p.cpf == cpf or p.email == email:
                return True
        return False
    
    def cadastra_pessoa_fisica(self):
        while True:
            dados = self.tela.pega_dados_pessoa_fisica()
            if self.verifica_pessoa_fisica_existente(dados["email"], dados["cpf"]):
                self.tela_pessoa_fisica.mostra_mensagem("Usuario ja cadastrado!")
                continue
            user = PessoaFisica(dados["cpf"], dados["nome"], dados["email"])
            self.pessoas_fisicas.append(user)
            self.tela_pessoa_fisica.mostra_mensagem("Usuario cadastrado com sucesso!")
            break
    
    