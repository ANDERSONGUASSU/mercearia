import customtkinter as ctk
import center_tk_window
from controller.controllerFornecedor import ControllerFornecedor
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_cadastrar_fornecedor(self):

    cadastro_window = ctk.CTkToplevel(self.root)
    cadastro_window.title("Cadastrar Fornecedor")
    cadastro_window.geometry("900x600")

    center_tk_window.center_on_screen(cadastro_window)

    formulario_frame = ctk.CTkFrame(cadastro_window)
    formulario_frame.pack(padx=10, pady=10)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome:")
    nome_label.grid(row=0, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.grid(row=0, column=1, pady=5)

    cnpj_label = ctk.CTkLabel(formulario_frame, text="CNPJ:")
    cnpj_label.grid(row=1, column=0, pady=5)

    cnpj_entry = ctk.CTkEntry(formulario_frame)
    cnpj_entry.grid(row=1, column=1, pady=5)

    telefone_label = ctk.CTkLabel(formulario_frame, text="Telefone:")
    telefone_label.grid(row=2, column=0, pady=5)

    telefone_entry = ctk.CTkEntry(formulario_frame)
    telefone_entry.grid(row=2, column=1, pady=5)

    categoria_label = ctk.CTkLabel(formulario_frame, text="Categoria:")
    categoria_label.grid(row=3, column=0, pady=5)

    categoria_entry = ctk.CTkEntry(formulario_frame)
    categoria_entry.grid(row=3, column=1, pady=5)

    def atualizar_e_salvar_fornecedor():
        nome = nome_entry.get()
        cnpj = cnpj_entry.get()
        telefone = telefone_entry.get()
        categoria = categoria_entry.get()
        controller = ControllerFornecedor()
        resultado, mensagem = controller.cadastrarFornecedor(
            nome, cnpj, telefone, categoria
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
            atualizar_lista(self, ControllerFornecedor)

    salvar_button = ctk.CTkButton(
        formulario_frame,
        text="Salvar",
        width=140,
        command=atualizar_e_salvar_fornecedor,
    )
    salvar_button.grid(row=5, column=0, pady=5)

    cancelar_button = ctk.CTkButton(
        formulario_frame, text="Cancelar", command=cadastro_window.destroy, width=140
    )
    cancelar_button.grid(row=5, column=1, pady=5)
