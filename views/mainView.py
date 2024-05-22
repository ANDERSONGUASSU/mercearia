import customtkinter as ctk
from views.fornecedorView import FornecedorView
from views.caixaView import CaixaView
from views.vendasView import VendasView
from views.clientesView import ClientesView
from views.funcionariosView import FuncionarioView
from views.estoqueView import EstoqueView


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Mercearia")
        root.geometry("1024x1600")
        root.minsize(1024, 1600)
        root.maxsize(1920, 1920)

        self.tabview = ctk.CTkTabview(root)
        self.tabview.pack(expand=1, fill="both")

        self.caixa_tab = self.tabview.add("Caixa")
        self.vendas_tab = self.tabview.add("Vendas")
        self.clientes_tab = self.tabview.add("Clientes")
        self.funcionarios_tab = self.tabview.add("Funcionários")
        self.fornecedores_tab = self.tabview.add("Fornecedores")
        self.estoque_tab = self.tabview.add("Estoque")

        self.init_caixa_tab()
        self.init_vendas_tab()
        self.init_clientes_tab()
        self.init_funcionarios_tab()
        self.init_fornecedores_tab()
        self.init_estoque_tab()

    def init_caixa_tab(self):
        CaixaView(self.caixa_tab)

    def init_vendas_tab(self):
        VendasView(self.vendas_tab)

    def init_clientes_tab(self):
        ClientesView(self.clientes_tab)

    def init_funcionarios_tab(self):
        FuncionarioView(self.funcionarios_tab)

    def init_fornecedores_tab(self):
        FornecedorView(self.fornecedores_tab)

    def init_estoque_tab(self):
        EstoqueView(self.estoque_tab)
