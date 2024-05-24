from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, id, nome, preco, categoria):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(
        self,
        itensVendidos: Produtos,
        vendedor,
        comprador,
        quantidadeVendida,
        valorTotal,
        data=None,
    ):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.valorTotal = valorTotal
        if data is not None:
            self.data = data
        else:
            self.data = datetime.now().strftime("%d/%m/%Y")


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, email, clt):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, endereco, email)
