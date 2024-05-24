from database.dao import DaoEstoque, DaoCategoria
from models.Models import Produtos


class ControllerEstoque:
    def __init__(self):
        self.categorias = DaoCategoria.ler()
        self.estoque = DaoEstoque.ler()

    def atualizarArquivoEstoque(self):
        with open("./database/data/estoque.txt", "w") as arq:
            for item in self.estoque:
                arq.writelines(
                    f"{item.produto.id}|"
                    f"{item.produto.nome}|"
                    f"{item.produto.preco}|"
                    f"{item.produto.categoria}|"
                    f"{item.quantidade}\n"
                )

    def cadastrarProduto(self, id, nome, preco, categoria, quantidade):
        categoria_existente = any(cat.categoria == categoria for cat in self.categorias)
        produto_existente = any(item.produto.nome == nome for item in self.estoque)

        if not categoria_existente:
            mensagem = "Categoria inexistente!"
            print(mensagem)
            return False, mensagem

        if produto_existente:
            mensagem = "Produto já existente em estoque"
            print(mensagem)
            return False, mensagem

        produto = Produtos(id, nome, float(preco), categoria)
        DaoEstoque.salvar(produto, int(quantidade))
        mensagem = "Produto cadastrado com sucesso!"
        print(mensagem)
        return True, mensagem

    def removerProduto(self, id):
        id_existe = any(item.produto.id == id for item in self.estoque)
        if not id_existe:
            mensagem = "Produto não cadastrado!"
            print(mensagem)
            return False, mensagem

        for i in range(len(self.estoque)):
            if self.estoque[i].produto.id == id:
                del self.estoque[i]
                mensagem = "Produto removido com sucesso!"
                print(mensagem)
                break
        self.atualizarArquivoEstoque()
        return True, mensagem

    def buscaProdutoPorId(self, id):
        for item in self.estoque:
            if item.produto.id == id:
                return item
        return None

    def buscarNomeProdutoPorCodigo(self, id):
        for item in self.estoque:
            if item.produto.id == id:
                return item
        return None

    def alterarProduto(self, id, novoNome, novoPreco, novaCategoria, novaQuantidade):
        categoria_existente = any(
            cat.categoria == novaCategoria for cat in self.categorias
        )
        if not categoria_existente:
            mensagem = "Categoria inexistente!"
            print(mensagem)
            return False, mensagem

        produto_existente = any(item.produto.id == id for item in self.estoque)
        if not produto_existente:
            mensagem = "O produto que deseja alterar não existe"
            print(mensagem)
            return False, mensagem

        for item in self.estoque:
            if item.produto.id == id:
                item.produto.nome = novoNome
                item.produto.preco = float(novoPreco)
                item.produto.categoria = novaCategoria
                item.quantidade = int(novaQuantidade)

        self.atualizarArquivoEstoque()
        mensagem = "Produto alterado com secesso!"
        print(mensagem)
        return True, mensagem

    def exibirLista(self):
        if not self.estoque:
            mensagem = "Estoque vazio"
            print(mensagem)
            return False, mensagem

        else:
            lista_texbox = (
                f'{"=" * 60}\n' f'{"********Estoque********":^60}\n' f'{"=" * 60}\n'
            )

            for item in self.estoque:
                lista_texbox += (
                    f"ID: {item.produto.id}\n"
                    f"Nome: {item.produto.nome}\n"
                    f"Preço: {item.produto.preco}\n"
                    f"Categoria: {item.produto.categoria}\n"
                    f"Quantidade: {item.quantidade}\n"
                    f'{"-" * 60}\n'
                )

            print(lista_texbox)
            return True, lista_texbox
