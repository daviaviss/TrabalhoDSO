from DAOs.pessoa_dao import PessoaDAO
from controladores import (
    controlador_categoria,
    controlador_endereco,
    controlador_mercado,
    controlador_pessoa_fisica,
    controlador_pessoa_juridica,
    controlador_preco,
    controlador_produto,
    controlador_menu_principal,
    controlador_qualificador,
)
from entidades.pessoa_fisica import PessoaFisica
from entidades.pessoa_juridica import PessoaJuridica
from telas.tela_sessao import TelaSessao


class ControladorSessao:
    def __init__(self):
        self.__controlador_produto = controlador_produto.ControladorProduto(self)
        self.__controlador_qualificador = (
            controlador_qualificador.ControladorQualificador(self)
        )
        self.__controlador_preco = controlador_preco.ControladorPreco(self)
        self.__controlador_mercado = controlador_mercado.ControladorMercado(self)
        self.__controlador_menu_principal = (
            controlador_menu_principal.ControladorMenuPrincipal(self)
        )
        self.__controlador_endereco = controlador_endereco.ControladorEndereco(self)
        self.__controlador_categoria = controlador_categoria.ControladorCategoria(self)
        self.__controlador_pessoa_fisica = (
            controlador_pessoa_fisica.ControladorPessoaFisica(self)
        )
        self.__controlador_pessoa_juridica = (
            controlador_pessoa_juridica.ControladorPessoaJuridica(self)
        )
        self.__tela_sessao = TelaSessao()
        self.__usuario_atual = None

    @property
    def usuario_atual(self):
        return self.__usuario_atual

    @usuario_atual.setter
    def usuario_atual(self, valor):
        self.__usuario_atual = valor

    @property
    def controlador_qualificador(self):
        return self.__controlador_qualificador

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_menu_principal(self):
        return self.__controlador_menu_principal

    @property
    def tela_sessao(self):
        return self.__tela_sessao

    @property
    def controlador_mercado(self):
        return self.__controlador_mercado

    @property
    def controlador_preco(self):
        return self.__controlador_preco

    @property
    def controlador_endereco(self):
        return self.__controlador_endereco

    @property
    def controlador_categoria(self):
        return self.__controlador_categoria

    @property
    def controlador_pessoa_fisica(self):
        return self.__controlador_pessoa_fisica

    @property
    def controlador_pessoa_juridica(self):
        return self.__controlador_pessoa_juridica

    def inicializa_sistema(self):
        self.abre_menu()

    def encerra_programa(self):
        self.tela_sessao.mostra_mensagem("=== PROGRAMA ENCERRADO! ===")
        exit(0)

    def abre_menu_opcoes(self):
        self.controlador_menu_principal.abre_menu_principal()

    def entrar(self):
        email = self.tela_sessao.pega_email()
        pf = self.controlador_pessoa_fisica.pega_pessoa_por_email(email)
        pj = self.controlador_pessoa_juridica.pega_pessoa_por_email(email)
        if not pj and not pf:
            self.tela_sessao.mostra_mensagem("Nao existe um usuario com esse email!")
            return
        self.usuario_atual = pf or pj
        self.controlador_menu_principal.abre_menu_principal()

    def cadastra_usuario_fisico(self):
        self.controlador_pessoa_fisica.cadastra_pessoa_fisica()

    def cadastra_usuario_jurifico(self):
        self.controlador_pessoa_juridica.cadastra_pessoa_juridica()

    def lista_usuarios(self):
        dados = []
        pessoas_j = self.controlador_pessoa_juridica.pessoas_juridicas
        for pj in pessoas_j:
            dados.append([pj.nome, pj.email, pj.cnpj, "Juridica"])
        pessoas_f = self.controlador_pessoa_fisica.pessoas_fisicas
        for pf in pessoas_f:
            dados.append([pf.nome, pf.email, pf.cpf, "Fisica"])
        self.tela_sessao.lista_usuarios(dados)

    def abre_menu(self):
        opcoes = {
            0: self.encerra_programa,
            1: self.entrar,
            2: self.cadastra_usuario_fisico,
            3: self.cadastra_usuario_jurifico,
            4: self.lista_usuarios,
        }
        while True:
            opcao_escolhida = self.tela_sessao.mostra_menu_principal()
            opcoes[opcao_escolhida]()
