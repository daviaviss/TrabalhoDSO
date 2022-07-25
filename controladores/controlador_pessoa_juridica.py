from DAOs.dao_pessoas_juridicas import PessoaJuridicaDAO
from DAOs.pessoa_fisica_dao import PessoaFisicaDAO
from controladores.controlador_pessoa_abstrato import ControladorPessoaAbstrato
from entidades.pessoa_juridica import PessoaJuridica
from telas.tela_pessoa_juridica import TelaPessoaJuridica


class ControladorPessoaJuridica(ControladorPessoaAbstrato):
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__pessoas_juridicas = []
        self.__tela_pessoa_juridica = TelaPessoaJuridica()
        self.__pj_DAO = PessoaJuridicaDAO()

    @property
    def pj_DAO(self):
        return self.__pj_DAO

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    @property
    def tela_pessoa_juridica(self):
        return self.__tela_pessoa_juridica

    @property
    def pessoas_juridicas(self):
        return self.pj_DAO.get_all()

    @property
    def tela_pessoa_juridica(self):
        return self.__tela_pessoa_juridica

    def verifica_pessoa_juridica_existente(self, email, cnpj):
        pessoas_juridicas = self.pj_DAO.get_all()
        for p in pessoas_juridicas:
            if p.cnpj == cnpj or p.email == email:
                return True
        return False

    def pega_pessoa_por_email(self, email):
        pessoas_juridicas = self.pj_DAO.get_all()
        for p in pessoas_juridicas:
            if p.email == email:
                return p
        return False

    def cadastra_pessoa_juridica(self):
        dados = self.tela_pessoa_juridica.pega_dados_pessoa_juridica()
        if not dados:
            return None
        if self.verifica_pessoa_juridica_existente(dados["email"], dados["cnpj"]):
            self.tela_pessoa_juridica.mostra_mensagem("Usuario ja cadastrado!")
            return None
        user = PessoaJuridica(dados["cnpj"], dados["nome"], dados["email"])
        self.pj_DAO.add(user)
        self.tela_pessoa_juridica.mostra_mensagem("Usuario cadastrado com sucesso!")

    def lista_pessoas_juridicas(self):
        pessoas_juridicas = self.pj_DAO.get_all()
        dados = []
        for p in pessoas_juridicas:
            dados.append(p.nome, p.email, p.cnpj)
        self.tela_pessoa_juridica.mostra_dado_usuario_juridico(dados)

    def edita_usuario_juridico(self):
        user = self.controlador_sessao.usuario_atual
        dados = {"nome": user.nome, "email": user.email, "cnpj": user.cnpj}
        dados = self.tela_pessoa_juridica.edita_pessoa_juridica(dados)
        if not isinstance(dados, dict):
            return None
        if dados["email"] != user.email:
            if self.pega_pessoa_por_email(dados["email"]):
                self.tela_pessoa_juridica.mostra_mensagem("Email ja Cadastrado!")
                return None
        user.email = dados["email"]
        user.nome = dados["nome"]
        self.pj_DAO.update(user)
        self.tela_pessoa_juridica.mostra_mensagem("Edicao feita com sucesso")

    def exclui_usuario(self):
        opcao = self.tela_pessoa_juridica.mostra_tela_confirmacao()
        if opcao == 0:
            user = self.controlador_sessao.usuario_atual
            for mercado in self.controlador_sessao.controlador_mercado.mercados:
                import pdb

                pdb.set_trace()
                if mercado.proprietario is user:
                    self.controlador_sessao.controlador_mercado.remove(mercado)

            self.pj_DAO.remove(self.controlador_sessao.usuario_atual.cnpj)
            self.controlador_sessao.abre_menu()
        return None

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
