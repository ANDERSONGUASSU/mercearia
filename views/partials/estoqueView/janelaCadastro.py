import customtkinter as ctk
import center_tk_window
from controller.controllerEstoque import ControllerEstoque
from views.partials.utils.atualizar_lista import atualizar_lista
from database.dao import DaoEstoque


def abrir_janela_cadastrar_estoque(self):
    id = DaoEstoque.gerar_novo_id()

    cadastro_window = ctk.CTkToplevel(self.root)
    cadastro_window.title("Cadastrar Produto")
    cadastro_window.geometry("900x600")

    center_tk_window.center_on_screen(cadastro_window)

    formulario_frame = ctk.CTkFrame(cadastro_window)
    formulario_frame.pack(padx=10, pady=10)

    id_label = ctk.CTkLabel(formulario_frame, text="ID:")
    id_label.grid(row=0, column=0, pady=5)

    id_entry = ctk.CTkEntry(formulario_frame)
    id_entry.insert(0, id)
    id_entry.configure(state="disabled")
    id_entry.grid(row=0, column=1, pady=5)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome:")
    nome_label.grid(row=1, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.grid(row=1, column=1, pady=5)

    preco_label = ctk.CTkLabel(formulario_frame, text="Preço:")
    preco_label.grid(row=2, column=0, pady=5)

    preco_entry = ctk.CTkEntry(formulario_frame)
    preco_entry.grid(row=2, column=1, pady=5)

    categoria_label = ctk.CTkLabel(formulario_frame, text="Categoria:")
    categoria_label.grid(row=3, column=0, pady=5)

    categoria_entry = ctk.CTkEntry(formulario_frame)
    categoria_entry.grid(row=3, column=1, pady=5)

    quantidade_label = ctk.CTkLabel(formulario_frame, text="Quantidade:")
    quantidade_label.grid(row=4, column=0, pady=5)

    quantidade_entry = ctk.CTkEntry(formulario_frame)
    quantidade_entry.grid(row=4, column=1, pady=5, padx=5)

    def atualizar_e_salvar_estoque():
        nome = nome_entry.get()
        id = id_entry.get()
        preco = preco_entry.get()
        categoria = categoria_entry.get()
        quantidade = quantidade_entry.get()
        controller = ControllerEstoque()
        resultado, mensagem = controller.cadastrarProduto(
            id, nome, preco, categoria, quantidade
        )

        if not resultado:
            mensagem_label = ctk.CTkLabel(
                formulario_frame, text=mensagem, fg_color="#FF0000"
            )
            mensagem_label.grid(row=6, column=0, columnspan=2, pady=5)
        else:
            mensagem_label = ctk.CTkLabel(
                formulario_frame, text=mensagem, fg_color="#008000"
            )
            mensagem_label.grid(row=6, column=0, columnspan=2, pady=5)
            atualizar_lista(self, ControllerEstoque)
            id_entry.configure(state="normal")
            id_entry.delete(0, "end")
            id_entry.insert(0, str(int(id) + 1))
            id_entry.configure(state="disabled")

    salvar_button = ctk.CTkButton(
        formulario_frame, text="Salvar", width=140, command=atualizar_e_salvar_estoque
    )
    salvar_button.grid(row=5, column=0, pady=5)

    cancelar_button = ctk.CTkButton(
        formulario_frame, text="Cancelar", command=cadastro_window.destroy, width=140
    )
    cancelar_button.grid(row=5, column=1, pady=5)
