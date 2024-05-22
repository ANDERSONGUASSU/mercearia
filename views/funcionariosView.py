from controller.controllerFuncionário import ControllerFuncionario
from views.partials.utils.setup_ui import setup_ui
from views.partials.utils.atualizar_lista import atualizar_lista
from views.partials.funcionariosView.janelaCadastro import (
    abrir_janela_cadastrar_funcionario,
)
from views.partials.funcionariosView.janelaAlterar import abri_janela_busca_cpf
from views.partials.funcionariosView.janelaExcluir import (
    abrir_janela_excluir_funcionario,
)


class FuncionarioView:
    cadastrar = abrir_janela_cadastrar_funcionario
    alterar = abri_janela_busca_cpf
    excluir = abrir_janela_excluir_funcionario

    def __init__(self, root):

        self.root = root
        self.lista_funcionarios = []
        self.controller = ControllerFuncionario()

        setup_ui(self, "Funcionários")
        atualizar_lista(self, ControllerFuncionario)
