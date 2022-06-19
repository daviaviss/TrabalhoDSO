from controladores import (
    controladorProduto,
    controladorPreco,
    controladorMercado,
    controlador_menu_principal,
    controladorEndereco,
    controladorCategoria,
    controladorPessoaFisica,
    controladorPessoaJuridica,
    controladorQualificador,
)
from telas.tela_cessao import TelaCessao


class ControladorCessao:
    def __init__(self):
        self.__controlador_produto = controladorProduto.ControladorProduto(self)
        self.__controlador_preco = controladorPreco.ControladorPreco(self)
        self.__controlador_mercado = controladorMercado.ControladorMercado(self)
        self.__controlador_menu_principal = (
            controlador_menu_principal.ControladorMenuPrincipal(self)
        )
        self.__controlador_endereco = controladorEndereco.ControladorEndereco(self)
        self.__controlador_categoria = controladorCategoria.ControladorCategoria(self)
        self.__controlador_pessoa_fisica = (
            controladorPessoaFisica.ControladorPessoaFisica(self)
        )
        self.__controlador_pessoa_juridica = (
            controladorPessoaJuridica.ControladorPessoaJuridica(self)
        )
        self.__tela_cessao = TelaCessao()
        self.__usuarios = []

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_menu_principal(self):
        return self.__controlador_menu_principal

    @property
    def tela_cessao(self):
        return self.__tela_cessao

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

    @property
    def usuarios(self):
        return self.__usuarios

    def inicializa_sistema(self):
        self.abre_menu()

    def encerra_programa(self):
        self.tela_cessao.mostra_mensagem("=== PROGRAMA ENCERRADO! ===")
        exit(0)

    def pega_usuario_por_email(self, email):
        for u in self.usuarios:
            if u.email == email:
                return u
        return False

    def abre_menu_opcoes(self):
        self.controlador_menu_principal.abre_menu_principal()

    def entrar(self):
        email = self.tela_cessao.pega_email()
        if not self.pega_usuario_por_email(email):
            self.tela_cessao.mostra_mensagem("Nao existe um usuario com esse email!")
            return
        self.controlador_menu_principal.abre_menu_principal()

    def verifica_usuario(self, dados, tipo):
        if tipo == "fisico":
            usuarios = self.controlador_pessoa_fisica.pessoas
            for u in usuarios:
                if u.cpf == dados["identificador"] and dados["email"] == u.email:
                    return True
        elif tipo == "juridico":
            usuarios = self.controlador_pessoa_juridica.pessoas
            for u in usuarios:
                if u.cnpj == dados["identificador"] and dados["email"] == u.email:
                    return True
        return False

    def cadastra_usuario_fisico(self):
        while True:
            dados = self.tela_cessao.pega_dados_usuario("fisico")
            if self.verifica_usuario(dados["identificador"], dados["email"]):
                self.tela_cessao.mostra_mensagem("Usuario ja cadastrado!")
                continue
            user = self.controlador_pessoa_fisica.cadastra_pessoa_fisica()
            break

    def cadastra_usuario_jurifico(self):
        dados = self.tela_cessao.pega_dados_usuario("juridico")

    def lista_usuarios(self):
        for u in self.usuarios:
            self.__tela_cessao.mostra_dados_usuario(u, u.tipo)

    def abre_menu(self):
        opcoes = {
            0: self.encerra_programa,
            1: self.entrar,
            2: self.cadastra_usuario_fisico,
            3: self.cadastra_usuario_jurifico,
            4: self.lista_usuarios,
        }
        while True:
            opcao_escolhida = self.tela_cessao.mostra_menu_principal()
            opcoes[opcao_escolhida]()
