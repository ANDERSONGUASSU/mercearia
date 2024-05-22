import customtkinter as ctk


def setup_ui(self, titulo):
    self.titulo_label = ctk.CTkLabel(
        self.root,
        text=titulo,
        font=("Arial", 30),
        justify="center",
        height=1,
        fg_color="#F9F9FA",
        corner_radius=10,
    )
    self.titulo_label.pack(pady=10)

    self.frame_botoes = ctk.CTkFrame(self.root)
    self.frame_lista = ctk.CTkFrame(self.root)
    self.root.grid_rowconfigure(0, weight=0)
    self.root.grid_rowconfigure(1, weight=1)
    self.frame_botoes.pack(pady=20)
    self.frame_lista.pack(fill="both", expand=True)

    # Título da aba "Clientes"

    # Criar botões "Cadastrar", "Alterar" e "Excluir"
    self.cadastrar_button = ctk.CTkButton(
        self.frame_botoes, text="Cadastrar", command=self.cadastrar
    )
    self.cadastrar_button.pack(side=ctk.LEFT, padx=10)

    self.alterar_button = ctk.CTkButton(
        self.frame_botoes, text="Alterar", command=self.alterar
    )
    self.alterar_button.pack(side=ctk.LEFT, padx=10)

    self.excluir_button = ctk.CTkButton(
        self.frame_botoes, text="Excluir", command=self.excluir
    )
    self.excluir_button.pack(side=ctk.LEFT)

    # Área para exibir lista de clientes (vazia inicialmente)
    self.lista_label = ctk.CTkLabel(
        self.frame_lista,
        text=f"Lista de {titulo}",
        font=("Arial", 30),
        justify="center",
        fg_color="#F9F9FA",
        corner_radius=10,
    )
    self.lista_label.pack()

    self.lista_texbox = ctk.CTkTextbox(
        self.frame_lista,
        width=900,
        height=600,
        border_width=2,
        activate_scrollbars=True,
        state="disabled",
        font=("Consolas", 22),
    )
    self.lista_texbox.pack()
