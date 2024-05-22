import customtkinter as ctk
import center_tk_window
from controller.controllerCliente import ControllerCliente
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_busca_cpf(self):

    def buscar_e_abrir_janela_alterar():
        cpf_busca = cpf_entry.get()
        controller = ControllerCliente()
        cliente = controller.buscarClientePorCPF(cpf_busca)

        if cliente:
            busca_window.destroy()
            abrir_janela_alterar_cliente(self, cliente)
        else:
            mensagem_label.configure(text="CPF não encontrado!", fg_color="#FF0000")

    busca_window = ctk.CTkToplevel(self.root)
    busca_window.title("Buscar Cliente")
    busca_window.geometry("400x200")

    center_tk_window.center_on_screen(busca_window)

    cpf_label = ctk.CTkLabel(busca_window, text="CPF do cliente:")
    cpf_label.pack(pady=10)

    cpf_entry = ctk.CTkEntry(busca_window)
    cpf_entry.pack(pady=10)

    buscar_button = ctk.CTkButton(
        busca_window, text="Buscar", command=buscar_e_abrir_janela_alterar
    )
    buscar_button.pack(pady=10)

    mensagem_label = ctk.CTkLabel(busca_window, text="")
    mensagem_label.pack(pady=10)


def abrir_janela_alterar_cliente(self, cliente):

    alterar_window = ctk.CTkToplevel(self.root)
    alterar_window.title("Alterar Cliente")
    alterar_window.geometry("900x600")

    center_tk_window.center_on_screen(alterar_window)

    formulario_frame = ctk.CTkFrame(alterar_window)
    formulario_frame.pack(padx=10, pady=10)

    cpf_alterar_label = ctk.CTkLabel(
        formulario_frame, text="CPF do cliente que deseja alterar"
    )
    cpf_alterar_label.grid(row=0, column=0, pady=5)

    cpf_alterar_entry = ctk.CTkEntry(formulario_frame)
    cpf_alterar_entry.insert(0, cliente.cpf)
    cpf_alterar_entry.grid(row=0, column=1, pady=5)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome novo:")
    nome_label.grid(row=1, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.insert(0, cliente.nome)
    nome_entry.grid(row=1, column=1, pady=5)

    cpf_label = ctk.CTkLabel(formulario_frame, text="CPF novo:")
    cpf_label.grid(row=2, column=0, pady=5)

    cpf_entry = ctk.CTkEntry(formulario_frame)
    cpf_entry.insert(0, cliente.cpf)
    cpf_entry.grid(row=2, column=1, pady=5)

    telefone_label = ctk.CTkLabel(formulario_frame, text="Telefone novo:")
    telefone_label.grid(row=3, column=0, pady=5)

    telefone_entry = ctk.CTkEntry(formulario_frame)
    telefone_entry.insert(0, cliente.telefone)
    telefone_entry.grid(row=3, column=1, pady=5)

    endereco_label = ctk.CTkLabel(formulario_frame, text="Endereco novo:")
    endereco_label.grid(row=4, column=0, pady=5)

    endereco_entry = ctk.CTkEntry(formulario_frame)
    endereco_entry.insert(0, cliente.endereco)
    endereco_entry.grid(row=4, column=1, pady=5)

    email_label = ctk.CTkLabel(formulario_frame, text="E-mail novo:")
    email_label.grid(
        row=5,
        column=0,
        pady=5,
    )

    email_entry = ctk.CTkEntry(formulario_frame)
    email_entry.insert(0, cliente.email)
    email_entry.grid(row=5, column=1, pady=5, padx=5)

    def atualizar_e_salvar_cliente():
        cpfAlterar = cpf_alterar_entry.get()
        nomeNovo = nome_entry.get()
        cpfNovo = cpf_entry.get()
        telefoneNovo = telefone_entry.get()
        enderecoNovo = endereco_entry.get()
        emailNovo = email_entry.get()
        controller = ControllerCliente()
        resultado, mensagem = controller.alterarCliente(
            cpfAlterar, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, emailNovo
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
            atualizar_lista(self, ControllerCliente)

    salvar_button = ctk.CTkButton(
        formulario_frame, text="Salvar", width=140, command=atualizar_e_salvar_cliente
    )
    salvar_button.grid(row=6, column=0, pady=5)

    cancelar_button = ctk.CTkButton(
        formulario_frame, text="Cancelar", command=alterar_window.destroy, width=140
    )
    cancelar_button.grid(row=6, column=1, pady=5)
