from DAOs.pessoa_dao import PessoaDAO
from telas.tela_pessoa_fisica import TelaPessoaFisica
from entidades.pessoa_fisica import PessoaFisica
from DAOs.pessoa_fisica_dao import PessoaFisicaDAO

class ControladorPessoaFisica:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__pessoas_fisicas = []
        self.__tela_pessoa_fisica = TelaPessoaFisica()
        self.__pf_DAO = PessoaFisicaDAO()
        self.__pessoas_DAO = PessoaDAO()
    
    @property
    def pf_DAO(self):
        return self.__pf_DAO
    
    @property
    def pessoas_DAO(self):
        return self.__pessoas_DAO

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    @property
    def pessoas_fisicas(self):
        return self.pf_DAO.get_all()

    @property
    def tela_pessoa_fisica(self):
        return self.__tela_pessoa_fisica

    def pega_pessoa_por_email(self, email):
        pessoas_fisicas = self.__pf_DAO.get_all()
        for p in pessoas_fisicas:
            if p.email == email:
                return p
        return False

    def verifica_pessoa_fisica_existente(self, email, cpf):
        pessoas_fisicas = self.pf_DAO.get_all()
        for p in pessoas_fisicas:
            if p.cpf == cpf or p.email == email:
                return True
        return False

    def cadastra_pessoa_fisica(self):
        while True:
            dados = self.tela_pessoa_fisica.pega_dados_pessoa_fisica()
            if not isinstance(dados, dict):
                return None
            if self.verifica_pessoa_fisica_existente(dados["email"], dados["cpf"]):
                self.tela_pessoa_fisica.mostra_mensagem("Usuario ja cadastrado!")
                return None
            user = PessoaFisica(dados["cpf"], dados["nome"], dados["email"])
            self.pf_DAO.add(user)
            self.tela_pessoa_fisica.mostra_mensagem("Usuario cadastrado com sucesso!")
            break

    def lista_pesoas_fisicas(self):
        dados = []
        pessoas_fisicas = self.pf_DAO.get_all()
        for p in pessoas_fisicas:
            dados.append(
                [p.nome, p.email, p.cpf]
            )
        self.tela_pessoa_fisica.mostra_dado_usuario_fisico(dados)
    

    def edita_usuario_fisico(self):
        user = self.controlador_sessao.usuario_atual
        dados = {
            "nome": user.nome,
            "email": user.email,
            "cpf": user.cpf
        }
        dados = self.tela_pessoa_fisica.edita_pessoa_fisica(default_data=dados)
        if not isinstance(dados, dict):
            return None
        if dados["email"] != user.email:
            if self.pega_pessoa_por_email(dados["email"]):
                self.tela_pessoa_fisica.mostra_mensagem("Email ja Cadastrado!")
                return None
        user.email = dados["email"]
        user.nome = dados["nome"]
        self.pf_DAO.update(user)
        self.tela_pessoa_fisica.mostra_mensagem("Edicao feita com sucesso")

    def exclui_usuario(self):
        opcao = self.tela_pessoa_fisica.mostra_tela_confirmacao()
        if opcao == 0:
            user = self.controlador_sessao.usuario_atual
            produtos = self.controlador_sessao.controlador_produto.produtos
            for p in produtos:
                if p.criador is user:
                    mercado = p.mercado
                    mercado.produtos.remove(p)
                    self.controlador_sessao.controlador.mercado.update(mercado)
                    self.controlador_sessao.controlador_produto.remove(p)

            self.pf_DAO.remove(user.cpf)
            self.controlador_sessao.abre_menu()
        return None

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
