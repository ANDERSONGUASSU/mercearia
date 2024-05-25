import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from database.dao import DaoEstoque, DaoVenda, DaoPessoas
from models.Models import Venda, Produtos
from datetime import datetime
from matplotlib.figure import Figure


def gerador_cores(n):
    cores = plt.get_cmap('hsv', n)
    return [cores(i) for i in range(n)]


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

    def cadastrarVenda(
        self,
        id,
        nome,
        preco,
        categoria,
        vendedor,
        comprador,
        quantidadeVendida,
        valorTotal,
    ):
        itens_vendidos = Produtos(id, nome, preco, categoria)
        venda = Venda(
            itensVendidos=itens_vendidos,
            vendedor=vendedor,
            comprador=comprador,
            quantidadeVendida=quantidadeVendida,
            valorTotal=valorTotal,
            data=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        )

        DaoVenda.salvar(venda)
        mensagem = "Venda registrada com sucesso!"
        print(mensagem)

    def criar_grafico(dash_window):
        vendas = DaoVenda.ler()
        clientes = DaoPessoas.ler()
        estoque = DaoEstoque.ler()

        data_venda = []
        data_clientes = []
        data_estoque = []

        for venda in vendas:
            data_venda.append(
                [
                    venda.itensVendidos.id,
                    venda.itensVendidos.nome,
                    venda.itensVendidos.preco,
                    venda.itensVendidos.categoria,
                    venda.vendedor,
                    venda.comprador,
                    venda.quantidadeVendida,
                    venda.valorTotal,
                    datetime.strptime(venda.data, "%d/%m/%Y %H:%M:%S"),
                ]
            )

        for cliente in clientes:
            data_clientes.append([cliente.nome, cliente.cpf])

        for item in estoque:
            data_estoque.append([item.produto.nome, item.quantidade])

        df_vendas = pd.DataFrame(
            data_venda,
            columns=[
                "id",
                "produto",
                "preco_unitario",
                "categoria",
                "vendedor",
                "comprador",
                "quantidade",
                "total_venda",
                "data_venda",
            ],
        )
        df_cliente = pd.DataFrame(data_clientes, columns=["nome", "cpf"])

        df_estoque = pd.DataFrame(data_estoque, columns=["produto", "quantidade"])
        df_estoque = df_estoque.groupby("produto")["quantidade"].sum().reset_index()
        df_estoque = df_estoque.sort_values(by="quantidade")
        df_estoque = df_estoque.head(20)

        current_month = datetime.now().month
        total_vendas_mes = df_vendas[df_vendas["data_venda"].dt.month == current_month][
            "total_venda"
        ].sum()

        total_clientes = len(df_cliente)

        total_vendas_produtos = df_vendas[
            df_vendas["data_venda"].dt.month == current_month
        ]["quantidade"].sum()

        total_vendas_por_dia = (
            df_vendas.groupby(df_vendas["data_venda"].dt.date)["total_venda"]
            .sum()
            .reset_index()
        )
        total_vendas_por_dia.columns = ["data", "total_venda"]

        produtos_quantidade_vendida = (
            df_vendas.groupby("produto")["quantidade"].sum().reset_index()
        )
        produtos_quantidade_vendida.columns = ["produto", "quantidade"]

        fig = Figure(figsize=(3.8, 3), facecolor="#917FB3")
        ax = fig.add_subplot()
        ax.set_facecolor("#917FB3")
        ax.fill_between(
            x=total_vendas_por_dia["data"],
            y1=total_vendas_por_dia["total_venda"],
            alpha=0.7,
        )
        ax.tick_params(labelsize=10, colors="white")
        fig.autofmt_xdate()
        ax.plot(
            total_vendas_por_dia["data"],
            total_vendas_por_dia["total_venda"],
            color="deepskyblue",
        )
        ax.grid(visible=True)

        fig_1 = Figure(figsize=(3.8, 3), facecolor="#917FB3")
        ax_1 = fig_1.add_subplot()
        ax_1.set_facecolor("#917FB3")
        ax_1.barh(df_estoque["produto"], df_estoque["quantidade"], color="skyblue")
        fig_1.tight_layout()
        ax_1.grid(visible=True)

        # Preparar dados para o gráfico polar
        produtos_quantidade_vendida["angle"] = np.linspace(
            0, 2 * np.pi, len(produtos_quantidade_vendida), endpoint=False
        )

        num_cores = len(produtos_quantidade_vendida)
        produtos_quantidade_vendida["color"] = gerador_cores(num_cores)

        # gráfico polar
        fig_2 = Figure(figsize=(3.8, 3), facecolor="#917FB3")
        ax_2 = fig_2.add_subplot(projection="polar")
        ax_2.set_facecolor("#917FB3")
        ax_2.bar(
            x=produtos_quantidade_vendida["angle"],
            height=produtos_quantidade_vendida["quantidade"],
            color=produtos_quantidade_vendida["color"],
        )
        ax_2.set_frame_on(False)
        ax_2.set_xticks([])
        ax_2.tick_params(labelsize=2, colors="white")
        ax_2.grid(alpha=0.7)

        for angle, label, rotation in zip(
            produtos_quantidade_vendida["angle"],
            produtos_quantidade_vendida["produto"],
            range(0, len(produtos_quantidade_vendida)),
        ):
            ax_2.text(
                x=angle,
                y=max(produtos_quantidade_vendida["quantidade"]) + 30,
                s=label,
                rotation=rotation * (360 / len(produtos_quantidade_vendida)),
                ha="center",
                va="center",
                color="white",
                fontsize=8,
            )

        return total_vendas_mes, total_clientes, total_vendas_produtos, fig, fig_1, fig_2
