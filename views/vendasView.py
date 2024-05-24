from controller.controllerVenda import ControllerVenda
from views.partials.utils.setup_ui import setup_ui_vendas
from views.partials.vendasView.janelaDash import abri_janela_dash


class VendasView:
    dash = abri_janela_dash

    def __init__(self, root):
        self.root = root

        setup_ui_vendas(self, "DashBoard Vendas")
