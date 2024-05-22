def atualizar_lista(self, controllerClass):
    controller = controllerClass()
    sucesso, dados = controller.exibirLista()

    self.lista_texbox.configure(state="normal")
    self.lista_texbox.delete(0.0, "end")
    self.lista_texbox.insert(0.0, dados)
    self.lista_texbox.configure(state="disabled")
