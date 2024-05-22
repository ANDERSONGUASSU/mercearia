from controller.controllerCliente import ControllerCliente
from views.partials.utils.setup_ui import setup_ui
from views.partials.utils.atualizar_lista import atualizar_lista
from views.partials.clientesView.janelaCadastro import abrir_janela_cadastrar_cliente
from views.partials.clientesView.janelaAlterar import abrir_janela_busca_cpf
from views.partials.clientesView.janelaExcluir import abrir_janela_excluir_cliente


class ClientesView:
    cadastrar = abrir_janela_cadastrar_cliente
    alterar = abrir_janela_busca_cpf
    excluir = abrir_janela_excluir_cliente

    def __init__(self, root):
        self.root = root
        self.lista_clientes = []
        self.controller = ControllerCliente()

        setup_ui(self, "Clientes")
        atualizar_lista(self, ControllerCliente)
