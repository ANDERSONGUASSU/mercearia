import customtkinter as ctk
import center_tk_window
from controller.controllerFuncionário import ControllerFuncionario
from views.partials.utils.atualizar_lista import atualizar_lista


def abrir_janela_excluir_funcionario(self):

    excluir_window = ctk.CTkToplevel(self.root)
    excluir_window.title("Excluir Funcionario")
    excluir_window.geometry("900x600")

    center_tk_window.center_on_screen(excluir_window)

    formulario_frame = ctk.CTkFrame(excluir_window)
    formulario_frame.pack(padx=10, pady=10)

    cpf_excluir_label = ctk.CTkLabel(
        formulario_frame, text="CPF do funcionário que deseja Excluir"
    )
    cpf_excluir_label.grid(row=0, column=0, pady=5)

    cpf_excluir_entry = ctk.CTkEntry(formulario_frame)
    cpf_excluir_entry.grid(row=0, column=1, pady=5)

    def atualizar_e_salvar_funcionario():
        cpfExcluir = cpf_excluir_entry.get()
        controller = ControllerFuncionario()
        resultado, mensagem = controller.removerFuncionario(cpfExcluir)

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
        formulario_frame, text="Cancelar", command=excluir_window.destroy, width=140
    )
    cancelar_button.grid(row=6, column=1, pady=5)
