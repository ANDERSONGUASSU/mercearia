import customtkinter as ctk
from views.mainView import MainView

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("assets/themes/redorange.json")

if __name__ == "__main__":
    app = ctk.CTk()
    main_view = MainView(app)
    app.mainloop()
