from controller.controllerCategoria import ControllerCategoria
from controller.controllerEstoque import ControllerEstoque
from views.partials.utils.setup_ui import setup_ui
from views.partials.utils.atualizar_lista import atualizar_lista
from views.partials.estoqueView.janelaCadastro import abrir_janela_cadastrar_estoque
from views.partials.estoqueView.janelaAlterar import abrir_janela_busca_id
from views.partials.estoqueView.janelaExcluir import abrir_janela_excluir_estoque


class EstoqueView:
    cadastrar = abrir_janela_cadastrar_estoque
    alterar = abrir_janela_busca_id
    excluir = abrir_janela_excluir_estoque

    def __init__(self, root):
        self.root = root
        self.lista_estoque = []
        ""
        self.controllerCat = ControllerCategoria()
        self.controller = ControllerEstoque()

        setup_ui(self, "Categoria")
        atualizar_lista(self, ControllerCategoria)

        setup_ui(self, "Estoque")
        atualizar_lista(self, ControllerEstoque)
