import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.controllerVenda import ControllerVenda


def abri_janela_dash(self):
    dash_window = ctk.CTkToplevel(self.root, fg_color="#ADD8E6")
    dash_window.title("Dashboard Vendas")
    dash_window.geometry("1200x750")
    dash_window.resizable(width=False, height=False)
    dash_window.minsize(1200, 750)
    dash_window.maxsize(1200, 750)
    vendas, clientes, produtos, fig, fig_1, fig_2 = ControllerVenda.criar_grafico(dash_window)

    canvas = tk.Canvas(
        dash_window,
        height=750,  # Aumentei a altura do canvas
        width=1200,  # Ajustei a largura do canvas
        bd=0,
        highlightthickness=0,
        relief="ridge",
        bg="#ADD8E6",
    )
    canvas.place(x=0, y=0)

    canvas.create_rectangle(
        0.0,
        0.0,
        1200.0,
        72.0,
        fill="#FF3E36",
        outline="",
    )

    canvas.create_text(
        83.0,
        16.0,
        anchor="nw",
        text="Relatório de Vendas",
        fill="#000000",
        font=("Inter Bold", 30 * -1),
    )

    # Carrega a imagem usando PIL
    image1 = Image.open("assets/img/image_1.png")
    image2 = Image.open("assets/img/image_2.png")
    image3 = Image.open("assets/img/image_3.png")
    image4 = Image.open("assets/img/image_4.png")
    image5 = Image.open("assets/img/image_5.png")
    image6 = Image.open("assets/img/image_6.png")
    image7 = Image.open("assets/img/image_7.png")
    image8 = Image.open("assets/img/image_8.png")
    image9 = Image.open("assets/img/image_9.png")
    image10 = Image.open("assets/img/image_10.png")

    # Redimenciona a imagem
    image1_resized = image1.resize((400, 100), Image.LANCZOS)
    image2_resized = image2.resize((400, 100), Image.LANCZOS)
    image3_resized = image3.resize((400, 100), Image.LANCZOS)
    image4_resized = image4.resize((400, 500), Image.LANCZOS)
    image5_resized = image5.resize((400, 500), Image.LANCZOS)
    image6_resized = image6.resize((400, 500), Image.LANCZOS)
    image7_resized = image7.resize((25, 25), Image.LANCZOS)
    image8_resized = image8.resize((25, 25), Image.LANCZOS)
    image9_resized = image9.resize((25, 25), Image.LANCZOS)
    image10_resized = image10.resize((30, 30), Image.LANCZOS)

    # cria a variável para guardar a imagem
    canvas.image1 = ImageTk.PhotoImage(image1_resized)
    canvas.image2 = ImageTk.PhotoImage(image2_resized)
    canvas.image3 = ImageTk.PhotoImage(image3_resized)
    canvas.image4 = ImageTk.PhotoImage(image4_resized)
    canvas.image5 = ImageTk.PhotoImage(image5_resized)
    canvas.image6 = ImageTk.PhotoImage(image6_resized)
    canvas.image7 = ImageTk.PhotoImage(image7_resized)
    canvas.image8 = ImageTk.PhotoImage(image8_resized)
    canvas.image9 = ImageTk.PhotoImage(image9_resized)
    canvas.image10 = ImageTk.PhotoImage(image10_resized)

    canvas.create_image(200.0, 150.0, image=canvas.image1)

    canvas.create_image(600.0, 150.0, image=canvas.image2)

    canvas.create_image(1000.0, 150.0, image=canvas.image3)
    canvas.create_image(200.0, 500.0, image=canvas.image4)

    canvas.create_image(600.0, 500.0, image=canvas.image5)

    canvas.create_image(1000.0, 500.0, image=canvas.image6)
    canvas.create_image(60.0, 120.0, image=canvas.image7)
    canvas.create_image(460.0, 120.0, image=canvas.image8)
    canvas.create_image(860.0, 120.0, image=canvas.image9)
    canvas.create_image(56.0, 32.0, image=canvas.image10)
    canvas.create_text(
        70.0,
        110.0,
        anchor="nw",
        text="Receita do Mês",
        fill="#FFFFFF",
        font=("Inter Bold", 16),
    )

    canvas.create_text(
        475.0,
        110.0,
        anchor="nw",
        text="Clientes",
        fill="#FFFFFF",
        font=("Inter Bold", 16),
    )
    canvas.create_text(
        875.0,
        110.0,
        anchor="nw",
        text="Produtos Vendidos",
        fill="#FFFFFF",
        font=("Inter Bold", 16),
    )
    canvas.create_text(
        50.0,
        135.0,
        anchor="nw",
        text=f"R$ {vendas}",
        fill="#FFFFFF",
        font=("Inter Bold", 28),
    )

    canvas.create_text(
        450.0,
        135.0,
        anchor="nw",
        text=f"{clientes}",
        fill="#FFFFFF",
        font=("Inter Bold", 28),
    )
    canvas.create_text(
        850.0,
        135.0,
        anchor="nw",
        text=f"{produtos}",
        fill="#FFFFFF",
        font=("Inter Bold", 28),
    )

    canvas = FigureCanvasTkAgg(fig, master=dash_window)
    canvas.draw()
    canvas.get_tk_widget().place(x=10, y=320)

    canvas = FigureCanvasTkAgg(fig_1, master=dash_window)
    canvas.draw()
    canvas.get_tk_widget().place(x=410, y=320)

    canvas = FigureCanvasTkAgg(figure=fig_2, master=dash_window)
    canvas.draw()
    canvas.get_tk_widget().place(x=810, y=320)
