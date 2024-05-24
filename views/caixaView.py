import customtkinter as ctk
from controller.controlerCaixa import ControllerCaixa
from controller.controllerVenda import ControllerVenda
from controller.controllerEstoque import ControllerEstoque
from database.dao import DaoPessoas, DaoFuncionario, DaoEstoque


class CaixaView:
    def __init__(self, root):
        self.root = root
        self.controller_caixa = ControllerCaixa()
        self.controller_venda = ControllerVenda()
        self.controller_estoque = ControllerEstoque()
        self.dao_estoque = DaoEstoque.ler()
        self.dao_cliente = DaoPessoas.ler()
        self.dao_funcionario = DaoFuncionario.ler()
        self.setup_ui()
        self.itens_registrados = []

    def setup_ui(self):
        # Caixa de texto no topo para mostrar o nome do produto
        self.produto_nome_label = ctk.CTkLabel(
            self.root,
            text="Nome do Produto",
            font=("Arial", 30),
            justify="center",
            height=100,
            fg_color="#F9F9FA",
            corner_radius=10,
        )
        self.produto_nome_label.grid(
            row=0, column=0, columnspan=2, padx=10, pady=50, sticky="ew"
        )

        self.frame1 = ctk.CTkFrame(self.root)
        self.frame2 = ctk.CTkFrame(self.root)

        self.frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)

        self.setup_frame1()
        self.setup_frame2()

    def setup_frame1(self):
        self.frame1.grid_columnconfigure(0, weight=1)
        self.frame1.grid_columnconfigure(1, weight=1)

        # Estilos de fonte e tamanho do texto
        estilo_fonte = ("Arial", 30)
        self.color = "#E84A5F"
        self.color_button = "#FF3E36"

        # TODO implemantar foto

        # Dropdown para selecionar funcionário
        self.funcionarios = ["Selecionar Funcionário"]
        ControllerCaixa.lista_funcionarios(self)

        # Exemplo de lista de funcionários
        self.funcionario_dropdown = ctk.CTkOptionMenu(
            self.frame1, values=self.funcionarios
        )
        self.funcionario_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Dropdown para selecionar comprador
        self.compradores = ["Comprador"]
        ControllerCaixa.lista_clientes(self)
        self.comprador_dropdown = ctk.CTkOptionMenu(
            self.frame1, values=self.compradores, state="disabled"
        )
        self.comprador_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # entradas de dados
        self.cod_produto_label = ctk.CTkLabel(
            self.frame1, text="Código do Produto", font=estilo_fonte
        )
        self.cod_produto_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.cod_produto_entry = ctk.CTkEntry(
            self.frame1,
            placeholder_text="Cod. Produto",
            font=estilo_fonte,
            state="disabled",
        )
        self.cod_produto_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.cod_produto_entry.bind("<KeyRelease>", self.ao_alterar_cod_produto)
        self.cod_produto_entry.bind("<Return>", self.registre_produto)

        self.quantidade_label = ctk.CTkLabel(
            self.frame1, text="Quantidade", font=estilo_fonte
        )
        self.quantidade_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.quantidade_entry = ctk.CTkEntry(
            self.frame1, placeholder_text="0", font=estilo_fonte, state="disabled"
        )
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.quantidade_entry.bind("<KeyRelease>", self.atualizar_valor_total)
        self.quantidade_entry.bind("<Return>", self.registre_produto)

        self.preco_label = ctk.CTkLabel(
            self.frame1, text="Valor Unitário", font=estilo_fonte, state="disabled"
        )
        self.preco_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.preco_entry = ctk.CTkEntry(
            self.frame1, placeholder_text="0.00", font=estilo_fonte, state="disabled"
        )
        self.preco_entry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        self.total_label = ctk.CTkLabel(
            self.frame1,
            text="Valor Total",
            font=estilo_fonte,
        )
        self.total_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.total_entry = ctk.CTkEntry(
            self.frame1, placeholder_text="0.00", font=estilo_fonte, state="disabled"
        )
        self.total_entry.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        self.status_label = ctk.CTkLabel(
            self.frame1,
            text="Status do Caixa",
            font=estilo_fonte,
            fg_color="#F9F9FA",
            corner_radius=10,
        )
        self.status_label.grid(
            row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew"
        )

        # Botões para iniciar e finalizar venda
        self.iniciar_venda_button = ctk.CTkButton(
            self.frame1,
            text="Iniciar Venda",
            font=estilo_fonte,
            command=self.iniciar_venda,
        )
        self.iniciar_venda_button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")

        self.finalizar_venda_button = ctk.CTkButton(
            self.frame1,
            text="Finalizar Venda",
            font=estilo_fonte,
            state="disbled",
            fg_color=self.color,
            command=self.finalizar_venda,
        )
        self.finalizar_venda_button.grid(
            row=6, column=1, padx=10, pady=10, sticky="nsew"
        )

        # Garantir que as linhas também se expandam verticalmente
        for i in range(8):
            self.frame1.grid_rowconfigure(i, weight=1)

    def setup_frame2(self):
        # Estilos de fonte e tamanho do texto
        estilo_fonte = ("Arial", 30)

        # Caixa de texto para o cupom fiscal
        self.recipiente_texbox = ctk.CTkTextbox(self.frame2, height=15)
        self.recipiente_texbox.pack(padx=10, pady=10, fill="both", expand=True)

        # Caixa de texto para o subtotal da compra
        self.total_compra_label = ctk.CTkLabel(
            self.frame2,
            text="Subtotal: R$ 0,00",
            font=estilo_fonte,
            fg_color="#F9F9FA",
            corner_radius=10,
        )
        self.total_compra_label.pack(padx=10, pady=10, fill="x")

    def ao_alterar_cod_produto(self, event):
        cod_produto = self.cod_produto_entry.get()
        produto = self.controller_estoque.buscarNomeProdutoPorCodigo(cod_produto)
        if produto:
            self.produto_nome_label.configure(text=produto.produto.nome)

            self.quantidade_entry.delete(0, "end")
            self.quantidade_entry.insert(0, 1)

            self.preco_entry.delete(0, "end")
            self.preco_entry.insert(0, f"{produto.produto.preco:.2f}")
            self.atualizar_valor_total()
        else:
            self.produto_nome_label.configure(text="Produto não encontrado")

            self.quantidade_entry.delete(0, "end")
            self.quantidade_entry.insert(0, 0)

            self.preco_entry.delete(0, "end")
            self.preco_entry.insert(0, 0)

            self.total_entry.delete(0, "end")
            self.total_entry.insert(0, 0)

    def atualizar_valor_total(self, event=None):
        quantity = (
            int(self.quantidade_entry.get()) if self.quantidade_entry.get() else 0
        )
        unit_price = float(self.preco_entry.get()) if self.preco_entry.get() else 0.0
        total_value = quantity * unit_price
        self.total_entry.delete(0, "end")
        self.total_entry.insert(0, f"{total_value:.2f}")

    def iniciar_venda(self):
        self.iniciar_venda_button.configure(state="disabled")
        self.iniciar_venda_button.configure(fg_color=self.color)
        self.finalizar_venda_button.configure(state="normal")
        self.comprador_dropdown.configure(state="normal")
        self.cod_produto_entry.configure(state="normal")
        self.quantidade_entry.configure(state="normal")
        self.preco_entry.configure(state="normal")
        self.total_entry.configure(state="normal")
        self.finalizar_venda_button.configure(fg_color=self.color_button)

    def finalizar_venda(self):
        # Desabilita os campos e botão de finalizar venda
        self.finalizar_venda_button.configure(state="disabled")
        self.cod_produto_entry.delete(0, "end")
        self.cod_produto_entry.configure(state="disabled")
        self.quantidade_entry.delete(0, "end")
        self.quantidade_entry.configure(state="disabled")
        self.preco_entry.delete(0, "end")
        self.preco_entry.configure(state="disabled")
        self.total_entry.delete(0, "end")
        self.total_entry.configure(state="disabled")
        self.finalizar_venda_button.configure(fg_color=self.color)
        self.iniciar_venda_button.configure(state="normal")
        self.iniciar_venda_button.configure(fg_color=self.color_button)
        self.recipiente_texbox.delete("1.0", ctk.END)

        for item in self.itens_registrados:
            ControllerVenda.cadastrarVenda(
                self,
                id=item["id"],
                nome=item["nome"],
                preco=item["preco"],
                categoria=item["categoria"],
                vendedor=item["vendedor"],
                comprador=item["comprador"],
                quantidadeVendida=item["quantidadeVendida"],
                valorTotal=item["valorTotal"],
            )
        self.itens_registrados.clear()
        self.comprador_dropdown.set(self.compradores[0])
        self.comprador_dropdown.configure(state="disabled")
        self.status_label.configure(
            text="Venda finalizada com sucesso", fg_color="#5cb85c"
        )

    def registre_produto(self, event):
        cod_produto = self.cod_produto_entry.get()
        produto_nome = self.produto_nome_label.cget("text")
        quantidade = int(self.quantidade_entry.get())
        preco = float(self.preco_entry.get())
        total = float(self.total_entry.get())
        vendedor = self.funcionario_dropdown.get()
        comprador = self.comprador_dropdown.get()

        estoque = DaoEstoque.ler()
        produto = next(
            (item for item in estoque if item.produto.id == cod_produto), None
        )

        if produto:
            if produto.quantidade < quantidade:
                self.status_label.configure(
                    text="Quantidade insuficiente no estoque", fg_color="#FF3E36"
                )
            else:
                produto.quantidade -= quantidade

                self.itens_registrados.append(
                    {
                        "id": cod_produto,
                        "nome": produto_nome,
                        "preco": preco,
                        "categoria": produto.produto.categoria,
                        "vendedor": vendedor,
                        "comprador": comprador,
                        "quantidadeVendida": quantidade,
                        "valorTotal": total,
                    }
                )
                self.status_label.configure(
                    text="Produto registrado com sucesso", fg_color="#5cb85c"
                )
                self.atualiza_recipiente()

                ControllerCaixa.atualizarEstoque(self, estoque)
        else:
            self.status_label.configure(
                text="Produto não encontrado no estoque", fg_color="#FF3E36"
            )

    def atualiza_recipiente(self):
        self.recipiente_texbox.delete("1.0", ctk.END)

        header = f'{"="*10} Cupom fiscal {"="*10}\n'
        self.recipiente_texbox.insert(ctk.END, header)
        for item in self.itens_registrados:
            formatted_item = (
                f"Código: {item['id']} | Nome: {item['nome']} | Quantidade: {item['quantidadeVendida']} | "
                f"Preço: R${item['preco']} | Total: R${item['valorTotal']}\n"
            )
            self.recipiente_texbox.insert(ctk.END, formatted_item)

        # Calcula e adiciona o total
        total = sum(float(item["valorTotal"]) for item in self.itens_registrados)
        total_text = f"\n\n{'='*40}\nTotal: R${total:.2f}\n"
        self.recipiente_texbox.insert(ctk.END, total_text)
        subtotal = f"Subtotal: R${total:.2f}"
        self.total_compra_label.configure(text=subtotal)

        # Move o cursor para o início da caixa de texto
        self.recipiente_texbox.see(ctk.END)
