from re import M
from DAOs.dao_mercado import MercadoDAO
from entidades.endereco import Endereco
from entidades.mercado import Mercado
from telas.tela_mercado import TelaMercado


class ControladorMercado:
    def __init__(self, controlador_sessao):
        self.__controlador_sessao = controlador_sessao
        self.__mercados = []
        self.__mercados = []
        self.__tela_mercado = TelaMercado()
        self.__mercado_DAO = MercadoDAO()

    @property
    def mercado_DAO(self):
        return self.__mercado_DAO


    def remove(self, mercado):
        for p in mercado.produtos:
            self.controlador_sessao.controlador_produto.remove(p)
        self.mercado_DAO.remove(mercado.cnpj)
            

    @property
    def mercados(self):
        return self.mercado_DAO.get_all()

    @property
    def controlador_sessao(self):
        return self.__controlador_sessao

    @property
    def tela_mercado(self):
        return self.__tela_mercado
    
    def verifica_mercado_dupicado(self, cnpj):
        for m in self.mercados:
            if m.cnpj == cnpj:
                return m
            return False

    def cadastra_mercado(self) -> None:
        dados = self.tela_mercado.pega_dados_mercado()
        if self.verifica_mercado_dupicado(dados["cnpj"]):
            self.tela_mercado.mostra_mensagem("Esse CNPJ ja foi cadastrado!")
            return

        novo_mercado = Mercado(
            dados["nome"],
            dados["cep"],
            dados["numero"],
            dados["cnpj"],
            self.controlador_sessao.usuario_atual,
        )
        self.mercado_DAO.add(novo_mercado)
        self.tela_mercado.mostra_mensagem("Mercado criado com sucesso")

    def lista_mercados(self) -> None:
        if not self.mercados:
            self.tela_mercado.mostra_mensagem("Nao existe mercado para ser listado!")
            return
        dados = []
        for mercado in self.mercados:
            dados.append(
                [mercado.nome, mercado.cnpj, mercado.endereco.cep, mercado.proprietario.nome]
            )
        self.tela_mercado.mostra_dados_mercado(dados)

    def exclui_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        self.remove(mercado)

    
    def pega_mercado(self, cnpj):
        for m in self.mercados:
            if m.cnpj == cnpj:
                return m
        return False
    
    def edita_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        dados = {
            "nome": mercado.nome,
            "cnpj": mercado.cnpj,
            "cep": mercado.endereco.cep,
            "numero": mercado.endereco.numero
        }
        dados = self.tela_mercado.edita_mercado(default_data=dados)
        if not dados:
            return
        mercado.nome = dados["nome"]
        mercado.endereco.cep = dados["cep"]
        mercado.endereco.numero = dados["numero"]
        self.mercado_DAO.update(mercado)
        self.tela_mercado.mostra_mensagem("Mercado Editado com Sucesso!")


    def seleciona_mercado(self, todos=False):
        if not self.mercados:
            self.tela_mercado.mostra_mensagem("Nao existem mercados!")
            return False
        dados = {}
        for m in self.mercados:
            if not todos:
                if m.proprietario.cnpj == self.controlador_sessao.usuario_atual.cnpj:
                    dados[m.cnpj] = m.nome + " - " + m.cnpj
            else:
               dados[m.cnpj] = m.nome + " - " + m.cnpj 

        cnpj = self.tela_mercado.seleciona_mercado(dados)
        if not cnpj:
            return False
        mercado = self.pega_mercado(cnpj)
        if not mercado:
            self.tela_mercado.mostra_mensagem("Mercado Nao Existe")
            return 
        return mercado


    def exlui_produto_mercado(self):
        mercado = self.seleciona_mercado()
        if not mercado:
            return
        if not mercado.produtos:
            self.tela_mercado.mostra_mensagem("Mercado nao contem produtos!")
            return
        produtos = [self.controlador_sessao.controlador_produto.get(p) for p in mercado.produtos]
        produto = self.controlador_sessao.controlador_produto.seleciona_produto(produtos)
        self.controlador_sessao.controlador_produto.deleta_produto(produto)

    def lista_produtos_mercado(self):
        mercado = self.seleciona_mercado(todos=True)
        if not mercado:
            return
        if not mercado.produtos:
            self.tela_mercado.mostra_mensagem("Mercado Nao Contem Produtos!")
            return
        self.controlador_sessao.controlador_produto.lista_produtos(mercado.produtos)


    
    def volta_menu_mercado(self):
        self.__tela_mercado.mostra_menu_inical()

    def abre_menu_mercado(self):
        if hasattr(self.controlador_sessao.usuario_atual, "cnpj"):
            tipo_usuario = "juridico"
        else:
            tipo_usuario = "fisico"
        opcoes = {
            1: self.lista_mercados,
            2: self.cadastra_mercado,
            3: self.edita_mercado,
            4: self.exclui_mercado,
            5: self.lista_produtos_mercado,
        }
        while True:
            if tipo_usuario == "fisico":
                opcao = self.tela_mercado.menu_mercado_pessoa_fisica()
            else:
                opcao = self.tela_mercado.menu_mercado_pessoa_juridica()
            if opcao == 0:
                break
            opcoes[opcao]()
