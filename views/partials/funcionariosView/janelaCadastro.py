import customtkinter as ctk
import center_tk_window
from controller.controllerFuncionário import ControllerFuncionario
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_cadastrar_funcionario(self):
    cadastro_window = ctk.CTkToplevel(self.root)
    cadastro_window.title("Cadastrar Funcionário")
    cadastro_window.geometry("900x600")

    center_tk_window.center_on_screen(cadastro_window)

    formulario_frame = ctk.CTkFrame(cadastro_window)
    formulario_frame.pack(padx=10, pady=10)

    nome_label = ctk.CTkLabel(formulario_frame, text="Nome:")
    nome_label.grid(row=0, column=0, pady=5)

    nome_entry = ctk.CTkEntry(formulario_frame)
    nome_entry.grid(row=0, column=1, pady=5)

    cpf_label = ctk.CTkLabel(formulario_frame, text="CPF:")
    cpf_label.grid(row=1, column=0, pady=5)

    cpf_entry = ctk.CTkEntry(formulario_frame)
    cpf_entry.grid(row=1, column=1, pady=5)

    telefone_label = ctk.CTkLabel(formulario_frame, text="Telefone:")
    telefone_label.grid(row=2, column=0, pady=5)

    telefone_entry = ctk.CTkEntry(formulario_frame)
    telefone_entry.grid(row=2, column=1, pady=5)

    endereco_label = ctk.CTkLabel(formulario_frame, text="endereco:")
    endereco_label.grid(row=3, column=0, pady=5)

    endereco_entry = ctk.CTkEntry(formulario_frame)
    endereco_entry.grid(row=3, column=1, pady=5)

    email_label = ctk.CTkLabel(formulario_frame, text="email:")
    email_label.grid(row=4, column=0, pady=5)

    email_entry = ctk.CTkEntry(formulario_frame)
    email_entry.grid(row=4, column=1, pady=5, padx=5)

    clt_label = ctk.CTkLabel(formulario_frame, text="CLT:")
    clt_label.grid(row=5, column=0, pady=5)

    clt_entry = ctk.CTkEntry(formulario_frame)
    clt_entry.grid(row=5, column=1, pady=5, padx=5)

    def atualizar_e_salvar_funcionario():
        nome = nome_entry.get()
        cpf = cpf_entry.get()
        telefone = telefone_entry.get()
        endereco = endereco_entry.get()
        email = email_entry.get()
        clt = clt_entry.get()
        controller = ControllerFuncionario()
        resultado, mensagem = controller.cadastrarFuncionario(
            nome, cpf, telefone, endereco, email, clt
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
            atualizar_lista(self, ControllerFuncionario)

    salvar_button = ctk.CTkButton(
        formulario_frame,
        text="Salvar",
        width=140,
        command=atualizar_e_salvar_funcionario,
    )
    salvar_button.grid(row=6, column=0, pady=5)

    cancelar_button = ctk.CTkButton(
        formulario_frame, text="Cancelar", command=cadastro_window.destroy, width=140
    )
    cancelar_button.grid(row=6, column=1, pady=5)
