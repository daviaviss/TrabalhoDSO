from controladores.controlador_pessoa_abstrato import ControladorPessoaAbstrato
from entidades.pessoaJuridica import PessoaJuridica
from telas.telaPessoaJuridica import TelaPessoaJuridica

class ControladorPessoaJuridica(ControladorPessoaAbstrato):
    def __init__(self, controlador_cessao):
        self.__controlador_cessao = controlador_cessao
        self.__pessoas_juridicas = []
        self.__tela_pessoa_juridica = TelaPessoaJuridica()

    @property
    def controlador_cessao(self):
        return self.__controlador_cessao

    @property
    def tela_pessoa_juridica(self):
        return self.__tela_pessoa_juridica

    @property
    def pessoas_juridicas(self):
        return self.__pessoas_juridicas

    @property
    def tela_pessoa_juridica(self):
        return self.__tela_pessoa_juridica

    def verifica_pessoa_juridica_existente(self, email, cnpj):
        for p in self.pessoas_juridicas:
            if p.cnpj == cnpj or p.email == email:
                return True
        return False
    
    def pega_pessoa_por_email(self, email):
        for p in self.pessoas_juridicas:
            if p.email == email:
                return p
        return False


    def cadastra_pessoa_juridica(self):
        while True:
            dados = self.tela_pessoa_juridica.pega_dados_pessoa_juridica()
            if self.verifica_pessoa_juridica_existente(dados["email"], dados["cnpj"]):
                self.tela_pessoa_juridica.mostra_mensagem("Usuario ja cadastrado!")
                continue
            user = PessoaJuridica(dados["cnpj"], dados["nome"], dados["email"])
            self.pessoas_juridicas.append(user)
            self.tela_pessoa_juridica.mostra_mensagem("Usuario cadastrado com sucesso!")
            break

    def lista_pessoas_juridicas(self):
        for p in self.pessoas_juridicas:
            self.tela_pessoa_juridica.mostra_dado_usuario_juridico(p)

    def edita_usuario_juridico(self):
        dados = self.tela_pessoa_juridica.pega_nome_email_usuario()
        user = self.controlador_cessao.usuario_atual
        if dados.get("nome"):
            editado = True
            user.nome = dados["nome"]
        if dados.get("email"):
            editado = True
            user.email = dados["email"]
        if not editado:
            self.tela_pessoa_juridica.mostra_mensagem("Nenhum dado feio modificado!")
        self.tela_pessoa_juridica.mostra_mensagem("Edicao feita com sucesso")

    def exclui_usuario(self):
        opcao = self.tela_pessoa_juridica.mostra_tela_confirmacao()
        self.pessoas_juridicas.remove(self.controlador_cessao.usuario_atual)
        self.controlador_cessao.abre_menu()
    

    def abre_tela(self):
        opcoes = {
            1: self.edita_usuario_juridico,
            2: self.exclui_usuario,
        }
        while True:
           opcao = self.tela_pessoa_juridica.menu_usuario()
           if opcao == 0:
               break
           opcoes[opcao]()