from database.dao import DaoEstoque, DaoVenda
from models.Models import Venda
from datetime import datetime


class ControllerVenda:
    def __init__(self):
        self.estoque = DaoEstoque.ler()
        self.venda = DaoVenda.ler()

    def atualizarEstoque(self):
        with open("./database/data/estoque.txt", "w") as arq:
            for item in self.estoque:
                arq.writelines(
                    f"{item.produto.nome}|"
                    f"{item.produto.preco}|"
                    f"{item.produto.categoria}|"
                    f"{item.quantidade}\n"
                )

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        produto_encontrado = None

        # Verifica se o produto existe no estoque e se há quantidade suficiente
        for item in self.estoque:
            if item.produto.nome == nomeProduto:
                produto_encontrado = item
                if int(item.quantidade) >= quantidadeVendida:
                    item.quantidade = int(item.quantidade) - quantidadeVendida
                    break
                else:
                    print("Quantidade insuficiente no estoque.")
                    return

        if not produto_encontrado:
            print("Produto não encontrado no estoque.")
            return

        venda = Venda(
            produto_encontrado.produto,
            vendedor,
            comprador,
            quantidadeVendida,
            data=datetime.now().strftime("%d/%m/%Y"),
        )

        DaoVenda.salvar(venda)
        self.atualizarEstoque()

        print("Venda registrada com sucesso!")

    def relatorioProdutosMaisVendidos(self):
        produtos = []
        for item in self.venda:
            nome = item.itensVendidos.nome
            quantidade = item.quantidadeVendida
            tamanho = list(filter(lambda x: x["produto"] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(
                    map(
                        lambda x: (
                            {
                                "produto": nome,
                                "quantidade": x["quantidade"] + quantidade,
                            }
                            if (x["produto"] == nome)
                            else (x)
                        ),
                        produtos,
                    )
                )
            else:
                produtos.append({"produto": nome, "quantidade": quantidade})

        ordenado = sorted(produtos, key=lambda k: k["quantidade"], reverse=True)
        print("Esses são os produtos mais vendidos")
        a = 1
        for a, item in enumerate(ordenado, 1):
            print(
                f'{"=" * 10} Produto [{a}] {"=" * 10} \n'
                f"Produto: {item['produto']}\n"
                f"Quantidade: {item['quantidade']}\n"
            )

    def mostrarVendas(self, dataInicial, dataFinal):
        dataInicio = datetime.strptime(dataInicial, "%d/%m/%Y")
        dataTermino = datetime.strptime(dataFinal, "%d/%m/%Y")

        vendasSelecionadas = list(
            filter(
                lambda x: dataInicio
                <= datetime.strptime(x.data, "%d/%m/%Y")
                <= dataTermino,
                self.venda,
            )
        )

        cont = 1
        total = 0

        for item in vendasSelecionadas:
            print(
                f'{"="*10} Venda [{cont}]{"="*10} '
                f"Nome: {item.itensVendidos.nome}\n"
                f"Categoria: {item.itensVendidos.categoria}\n"
                f"Data: {item.data}\n"
                f"Quantidade: {item.quantidadeVendida}\n"
                f"Cliente: {item.comprador}\n"
                f"Vendedor: {item.vendedor}\n"
                f"Subtotal: {int(item.quantidadeVendida) * float(item.itensVendidos.preco)}\n"
            )
            total += float(item.itensVendidos.preco) * int(item.quantidadeVendida)
            cont += 1
        print(f"Total vendido: {total}")
