import customtkinter as ctk
import center_tk_window
from controller.controllerFornecedor import ControllerFornecedor
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_busca_cnpj(self):

    def buscar_e_abrir_janela_alterar():
        cnpj_busca = cnpj_entry.get()
        controller = ControllerFornecedor()
        fornecedor = controller.buscarFornecedorPorCNPJ(cnpj_busca)

        if fornecedor:
            busca_window.destroy()
            abrir_janela_alterar_cliente(self, fornecedor)
        else:
            mensagem_label.configure(text="CNPJ não encontrado!", fg_color="#FF0000")

    busca_window = ctk.CTkToplevel(self.root)
    busca_window.title("Buscar Fornecedor")
    busca_window.geometry("400x200")

    center_tk_window.center_on_screen(busca_window)

    cnpj_label = ctk.CTkLabel(busca_window, text="CNPJ do Fornecedor:")
    cnpj_label.pack(pady=10)

    cnpj_entry = ctk.CTkEntry(busca_window)
    cnpj_entry.pack(pady=10)

    buscar_button = ctk.CTkButton(
        busca_window, text="Buscar", command=buscar_e_abrir_janela_alterar
    )
    buscar_button.pack(pady=10)

    mensagem_label = ctk.CTkLabel(busca_window, text="")
    mensagem_label.pack(pady=10)


def abrir_janela_alterar_cliente(self, fornecedor):

    alterar_window = ctk.CTkToplevel(self.root)
    alterar_window.title("Alterar Fornecedor")
    alterar_window.geometry("900x600")

    center_tk_window.center_on_screen(alterar_window)

    formulario_frame = ctk.CTkFrame(alterar_window)
    formulario_frame.pack(padx=10, pady=10)

    cnpj_alterar_label = ctk.CTkLabel(
        formulario_frame, text="CNPJ do Fornecedor que deseja alterar"
    )
    cnpj_alterar_label.grid(row=0, column=0, pady=5)

    cnpj_alterar_entry = ctk.CTkEntry(formulario_frame)
    cnpj_alterar_entry.insert(0, fornecedor.cnpj)
    cnpj_alterar_entry.grid(row=0, column=1, pady=5)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome novo:")
    nome_label.grid(row=1, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.insert(0, fornecedor.nome)
    nome_entry.grid(row=1, column=1, pady=5)

    cnpj_label = ctk.CTkLabel(formulario_frame, text="CNPJ novo:")
    cnpj_label.grid(row=2, column=0, pady=5)

    cnpj_entry = ctk.CTkEntry(formulario_frame)
    cnpj_entry.insert(0, fornecedor.cnpj)
    cnpj_entry.grid(row=2, column=1, pady=5)

    telefone_label = ctk.CTkLabel(formulario_frame, text="Telefone novo:")
    telefone_label.grid(row=3, column=0, pady=5)

    telefone_entry = ctk.CTkEntry(formulario_frame)
    telefone_entry.insert(0, fornecedor.telefone)
    telefone_entry.grid(row=3, column=1, pady=5)

    categoria_label = ctk.CTkLabel(formulario_frame, text="Categoria nova:")
    categoria_label.grid(row=4, column=0, pady=5)

    categoria_entry = ctk.CTkEntry(formulario_frame)
    categoria_entry.insert(0, fornecedor.categoria)
    categoria_entry.grid(row=4, column=1, pady=5)

    def atualizar_e_salvar_fornecedor():
        cnpjAlterar = cnpj_alterar_entry.get()
        nomeNovo = nome_entry.get()
        cnpjNovo = cnpj_entry.get()
        telefoneNovo = telefone_entry.get()
        categoriaNova = categoria_entry.get()
        controller = ControllerFornecedor()
        resultado, mensagem = controller.alterarFornecedor(
            cnpjAlterar, nomeNovo, cnpjNovo, telefoneNovo, categoriaNova
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
        formulario_frame, text="Cancelar", command=alterar_window.destroy, width=140
    )
    cancelar_button.grid(row=5, column=1, pady=5)
