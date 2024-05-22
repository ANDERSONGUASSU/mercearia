from database.dao import DaoCategoria
from models.Models import Categoria


class ControllerCategoria:
    def __init__(self):
        self.categorias = DaoCategoria.ler()

    def atualizarArquivoCategoria(self):
        with open("./database/data/categoria.txt", "w") as arq:
            for item in self.categorias:
                arq.write(item.categoria + "\n")

    def cadastraCategoria(self, novaCategoria):
        categoria_existe = any(
            cat.categoria == novaCategoria for cat in self.categorias
        )
        if categoria_existe:
            mensagem = "Categoria já cadastrada no sistema"
            print(mensagem)
            return False, mensagem
        categoria = Categoria(novaCategoria)
        DaoCategoria.salvar(categoria)
        self.atualizarArquivoCategoria()
        mensagem = "Categoria cadastrada com sucesso!"
        print(mensagem)
        return True, mensagem

    def removerCategoria(self, categoriaRemover):
        categoria_existe = any(
            cat.categoria == categoriaRemover for cat in self.categorias
        )

        if not categoria_existe:
            mensagem = "A categoria que deseja remover não existe"
            print(mensagem)
            return False, mensagem

        for i in range(len(self.categorias)):
            if self.categorias[i].categoria == categoria_existe:
                del self.categorias[i]
                mensagem = "Categoria removida com sucesso!"

        self.atualizarArquivoCategoria()
        return True, mensagem

        # TODO: alterar a categoria no estoque

    def buscarCatPorCat(self, categoria):
        for cat in self.categorias:
            if cat.categoria == categoria:
                return cat
        return None

    def alterarCategoria(self, categoriaAlterar, categoriaNova):
        categoria_nova_existe = any(
            cat.categoria == categoriaNova
            for cat in self.categorias
            if cat.categoria != categoriaAlterar
        )
        if categoria_nova_existe:
            mensagem = "Essa categoria já existe!"
            print(mensagem)
            return False, mensagem

        categoria_existe = any(
            cat.categoria == categoriaAlterar for cat in self.categorias
        )
        if categoria_existe:
            mensagem = "A categoria que deseja alterar não existe"

            for item in self.categorias:
                if item.categoria == categoriaAlterar:
                    item.categoria = categoriaNova

            self.atualizarArquivoCategoria()
            mensagem = "Categoria alterada com sucesso"
            print(mensagem)
            return True, mensagem
            # TODO: alterar a categoria no estoque

    def exibirLista(self):
        if not self.categorias:
            mensagem = "Não ha categorias para exibir"
            print(mensagem)
            return False, mensagem

        else:
            lista_texbox = (
                f'{"=" * 60}\n' f'{"********Categorias********":^60}\n' f'{"=" * 60}\n'
            )

            for item in self.categorias:
                lista_texbox += f"Categoria: {item.categoria}\n" f'{"-" * 60}\n'
            print(lista_texbox)
            return True, lista_texbox
