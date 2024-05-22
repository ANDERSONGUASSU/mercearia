from controller.controllerFornecedor import ControllerFornecedor
from views.partials.utils.setup_ui import setup_ui
from views.partials.utils.atualizar_lista import atualizar_lista
from views.partials.fornecedoresView.janelaCadastro import (
    abrir_janela_cadastrar_fornecedor,
)
from views.partials.fornecedoresView.janelaAlterar import abrir_janela_busca_cnpj
from views.partials.fornecedoresView.janelaExcluir import (
    abrir_janela_excluir_fornecedor,
)


class FornecedorView:
    cadastrar = abrir_janela_cadastrar_fornecedor
    alterar = abrir_janela_busca_cnpj
    excluir = abrir_janela_excluir_fornecedor

    def __init__(self, root):
        self.root = root
        self.lista_clientes = []
        self.controller = ControllerFornecedor()

        setup_ui(self, "Clientes")
        atualizar_lista(self, ControllerFornecedor)
