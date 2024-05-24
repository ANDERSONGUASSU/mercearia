from models.Models import (
    Categoria,
    Venda,
    Produtos,
    Estoque,
    Fornecedor,
    Pessoa,
    Funcionario,
)


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open("./database/data/categoria.txt", "a") as arq:
            arq.writelines(f"{categoria}\n")

    @classmethod
    def ler(cls):
        with open("./database/data/categoria.txt", "r") as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace("\n", ""), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("./database/data/venda.txt", "a") as arq:
            arq.writelines(
                f"{venda.itensVendidos.id}|"
                f"{venda.itensVendidos.nome}|"
                f"{venda.itensVendidos.preco}|"
                f"{venda.itensVendidos.categoria}|"
                f"{venda.vendedor}|"
                f"{venda.comprador}|"
                f"{venda.quantidadeVendida}|"
                f"{venda.valorTotal}|"
                f"{venda.data}\n"
            )

    @classmethod
    def ler(cls):
        with open("./database/data/venda.txt", "r") as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace("\n", ""), cls.venda))
        cls.venda = list(map(lambda x: x.split("|"), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(
                Venda(
                    Produtos(i[0], i[1], float(i[2]), i[3]),
                    i[4],
                    i[5],
                    int(i[6]),
                    float(i[7]),
                    i[8],
                )
            )
        return vend


class DaoEstoque:
    @classmethod
    def gerar_novo_id(cls):
        try:
            with open("./database/data/estoque.txt", "r") as arq:
                linhas = arq.readlines()
                if not linhas:
                    return 1
                ultimo_id = max(int(linha.split("|")[0]) for linha in linhas)
                return ultimo_id + 1
        except FileNotFoundError:
            return 1

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open("./database/data/estoque.txt", "a") as arq:
            arq.writelines(
                f"{produto.id}|"
                f"{produto.nome}|"
                f"{float(produto.preco):.2f}|"
                f"{produto.categoria}|"
                f"{int(quantidade)}\n"
            )

    @classmethod
    def ler(cls):
        with open("./database/data/estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()
            cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
            cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))
            est = []
            if len(cls.estoque) > 0:
                for i in cls.estoque:
                    est.append(
                        Estoque(Produtos(i[0], i[1], float(i[2]), i[3]), int(i[4]))
                    )
            return est


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("./database/data/fornecedores.txt", "a") as arq:
            arq.writelines(
                f"{fornecedor.nome}|"
                f"{fornecedor.cnpj}|"
                f"{fornecedor.telefone}|"
                f"{fornecedor.categoria}\n"
            )

    @classmethod
    def ler(cls):
        with open("./database/data/fornecedores.txt", "r") as arq:
            cls.fornecedores = arq.readlines()
            cls.fornecedores = list(
                map(lambda x: x.replace("\n", ""), cls.fornecedores)
            )
            cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))
            forn = []
            if len(cls.fornecedores) > 0:
                for i in cls.fornecedores:
                    forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
            return forn


class DaoPessoas:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open("./database/data/clientes.txt", "a") as arq:
            arq.writelines(
                f"{pessoas.nome}|"
                f"{pessoas.cpf}|"
                f"{pessoas.telefone}|"
                f"{pessoas.endereco}|"
                f"{pessoas.email}\n"
            )

    @classmethod
    def ler(cls):
        with open("./database/data/clientes.txt", "r") as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))
        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Pessoa, clt):
        with open("./database/data/funcionarios.txt", "a") as arq:
            arq.writelines(
                f"{funcionario.nome}|"
                f"{funcionario.cpf}|"
                f"{funcionario.telefone}|"
                f"{funcionario.email}|"
                f"{funcionario.endereco}|"
                f"{clt}\n"
            )

    @classmethod
    def ler(cls):
        with open("./database/data/funcionarios.txt", "r") as arq:
            cls.funcionarios = arq.readlines()
        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))
        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionario
