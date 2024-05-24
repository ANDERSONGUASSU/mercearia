from database.dao import DaoFuncionario, DaoPessoas


class ControllerCaixa:
    def __init__(self):
        self.dao_funcionario = DaoFuncionario.ler()
        self.dao_cliente = DaoPessoas.ler()

    def lista_funcionarios(self):
        for func in self.dao_funcionario:
            funcionario = f"{func.nome}"
            self.funcionarios.append(funcionario)
        return

    def lista_clientes(self):
        for pessoa in self.dao_cliente:
            cliente = f"{pessoa.cpf}"
            self.compradores.append(cliente)
        return

    def atualizarEstoque(self, estoque):
        with open("./database/data/estoque.txt", "w") as arq:
            for item in estoque:
                arq.writelines(
                    f"{item.produto.id}|"
                    f"{item.produto.nome}|"
                    f"{item.produto.preco}|"
                    f"{item.produto.categoria}|"
                    f"{item.quantidade}\n"
                )
