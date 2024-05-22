import customtkinter as ctk
import center_tk_window
from controller.controllerEstoque import ControllerEstoque
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_busca_id(self):

    def buscar_e_abrir_janela_alterar():
        id_busca = id_entry.get()
        controller = ControllerEstoque()
        produto = controller.buscaProdutoPorId(id_busca)

        if produto:
            busca_window.destroy()
            abrir_janela_alterar_produto(self, produto)
        else:
            mensagem_label.configure(text="CPF não encontrado!", fg_color="#FF0000")

    busca_window = ctk.CTkToplevel(self.root)
    busca_window.title("Buscar Produto")
    busca_window.geometry("400x200")

    center_tk_window.center_on_screen(busca_window)

    id_label = ctk.CTkLabel(busca_window, text="ID do produto:")
    id_label.pack(pady=10)

    id_entry = ctk.CTkEntry(busca_window)
    id_entry.pack(pady=10)

    buscar_button = ctk.CTkButton(
        busca_window, text="Buscar", command=buscar_e_abrir_janela_alterar
    )
    buscar_button.pack(pady=10)

    mensagem_label = ctk.CTkLabel(busca_window, text="")
    mensagem_label.pack(pady=10)


def abrir_janela_alterar_produto(self, produto):

    alterar_window = ctk.CTkToplevel(self.root)
    alterar_window.title("Alterar Produto")
    alterar_window.geometry("900x600")

    center_tk_window.center_on_screen(alterar_window)

    formulario_frame = ctk.CTkFrame(alterar_window)
    formulario_frame.pack(padx=10, pady=10)

    id_label = ctk.CTkLabel(formulario_frame, text="ID do produto que deseja alterar")
    id_label.grid(row=0, column=0, pady=5)

    id_entry = ctk.CTkEntry(formulario_frame)
    id_entry.insert(0, produto.produto.id)
    id_entry.grid(row=0, column=1, pady=5)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome novo:")
    nome_label.grid(row=1, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.insert(0, produto.produto.nome)
    nome_entry.grid(row=1, column=1, pady=5)

    preco_label = ctk.CTkLabel(formulario_frame, text="Preço novo:")
    preco_label.grid(row=3, column=0, pady=5)

    preco_entry = ctk.CTkEntry(formulario_frame)
    preco_entry.insert(0, produto.produto.preco)
    preco_entry.grid(row=3, column=1, pady=5)

    categoria_label = ctk.CTkLabel(formulario_frame, text="Categoria novo:")
    categoria_label.grid(row=4, column=0, pady=5)

    categoria_entry = ctk.CTkEntry(formulario_frame)
    categoria_entry.insert(0, produto.produto.categoria)
    categoria_entry.grid(row=4, column=1, pady=5)

    quantidade_label = ctk.CTkLabel(formulario_frame, text="Quantidade novo:")
    quantidade_label.grid(
        row=5,
        column=0,
        pady=5,
    )

    quantidade_entry = ctk.CTkEntry(formulario_frame)
    quantidade_entry.insert(0, produto.quantidade)
    quantidade_entry.grid(row=5, column=1, pady=5, padx=5)

    def atualizar_e_salvar_produto():
        idAlterar = id_entry.get()
        nomeNovo = nome_entry.get()
        precoNovo = preco_entry.get()
        categoriaNovo = categoria_entry.get()
        quantidadeNovo = quantidade_entry.get()
        controller = ControllerEstoque()
        resultado, mensagem = controller.alterarProduto(
            idAlterar, nomeNovo, precoNovo, categoriaNovo, quantidadeNovo
        )

        if not resultado:
            mensagem_label = ctk.CTkLabel(
                formulario_frame, text=mensagem, fg_color="#FF0000"
            )
            mensagem_label.grid(row=7, column=0, columnspan=2, pady=5)
        else:
            mensagem_label = ctk.CTkLabel(
                formulario_frame, text=mensagem, fg_color="#008000"
            )
            mensagem_label.grid(row=7, column=0, columnspan=2, pady=5)
            atualizar_lista(self, ControllerEstoque)

    salvar_button = ctk.CTkButton(
        formulario_frame, text="Salvar", width=140, command=atualizar_e_salvar_produto
    )
    salvar_button.grid(row=6, column=0, pady=5)

    cancelar_button = ctk.CTkButton(
        formulario_frame, text="Cancelar", command=alterar_window.destroy, width=140
    )
    cancelar_button.grid(row=6, column=1, pady=5)
