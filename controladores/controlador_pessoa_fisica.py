from click import edit
from telas.tela_pessoa_fisica import TelaPessoaFisica
from entidades.pessoa_fisica import PessoaFisica


class ControladorPessoaFisica:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__pessoas_fisicas = []
        self.__tela_pessoa_fisica = TelaPessoaFisica()

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    @property
    def pessoas_fisicas(self):
        return self.__pessoas_fisicas

    @property
    def tela_pessoa_fisica(self):
        return self.__tela_pessoa_fisica

    def pega_pessoa_por_email(self, email):
        for p in self.pessoas_fisicas:
            if p.email == email:
                return p
        return False

    def verifica_pessoa_fisica_existente(self, email, cpf):
        for p in self.pessoas_fisicas:
            if p.cpf == cpf or p.email == email:
                return True
        return False

    def cadastra_pessoa_fisica(self):
        while True:
            print("=========================================")
            dados = self.tela_pessoa_fisica.pega_dados_pessoa_fisica()
            if self.verifica_pessoa_fisica_existente(dados["email"], dados["cpf"]):
                self.tela_pessoa_fisica.mostra_mensagem("Usuario ja cadastrado!")
                continue
            user = PessoaFisica(dados["cpf"], dados["nome"], dados["email"])
            self.pessoas_fisicas.append(user)
            self.tela_pessoa_fisica.mostra_mensagem("Usuario cadastrado com sucesso!")
            break

    def lista_pesoas_fisicas(self):
        for p in self.pessoas_fisicas:
            self.tela_pessoa_fisica.mostra_dado_usuario_fisico(p)

    def edita_usuario_fisico(self):
        dados = self.tela_pessoa_fisica.pega_nome_email_usuario()
        user = self.controlador_sessao.usuario_atual
        editado = False
        if dados.get("nome"):
            editado = True
            user.nome = dados["nome"]
        if dados.get("email"):
            editado = True
            user.email = dados["email"]
        if not editado:
            self.tela_pessoa_fisica.mostra_mensagem("Nenhum dado feio modificado!")
        else:
            self.tela_pessoa_fisica.mostra_mensagem("Edicao feita com sucesso")

    def exclui_usuario(self):
        opcao = self.tela_pessoa_fisica.mostra_tela_confirmacao()
        self.pessoas_fisicas.remove(self.controlador_sessao.usuario_atual)
        self.controlador_sessao.abre_menu()

    def abre_tela(self):
        opcoes = {
            1: self.edita_usuario_fisico,
            2: self.exclui_usuario,
        }
        while True:
            opcao = self.tela_pessoa_fisica.menu_usuario()
            if opcao == 0:
                break
            opcoes[opcao]()
