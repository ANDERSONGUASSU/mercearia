from database.dao import DaoFornecedor
from models.Models import Fornecedor


class ControllerFornecedor:
    def __init__(self):
        self.fornecedores = DaoFornecedor.ler()

    def atualizarArquivoFornecedor(self):
        with open("./database/data/fornecedores.txt", "w") as arq:
            for item in self.fornecedores:
                arq.writelines(
                    f"{item.nome}|"
                    f"{item.cnpj}|"
                    f"{item.telefone}|"
                    f"{item.categoria}\n"
                )

    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        if len(cnpj) != 14:
            mensagem = "Digite um CNPJ válido"
            print(mensagem)
            return False, mensagem

        cnpj_existente = any(forn.cnpj == cnpj for forn in self.fornecedores)
        if cnpj_existente:
            mensagem = "CNPJ já existe no sistema!"
            print(mensagem)
            return False, mensagem

        if not (10 <= len(telefone) <= 11):
            mensagem = "Digite um telefone válido"
            print(mensagem)
            return False, mensagem

        telefone_existente = any(
            forn.telefone == telefone for forn in self.fornecedores
        )
        if telefone_existente:
            mensagem = "Telefone já existe no sistema!"
            print(mensagem)
            return False, mensagem

        novo_fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
        DaoFornecedor.salvar(novo_fornecedor)
        mensagem = "Fornecedor cadastrado com sucesso!"
        print(mensagem)
        return True, mensagem

    def removerFornecedor(self, cnpj):
        cnpj_existente = any(forn.cnpj == cnpj for forn in self.fornecedores)

        if not cnpj_existente:
            mensagem = "CNPJ não cadastrado no sistema"
            print(mensagem)
            return False, mensagem

        for i in range(len(self.fornecedores)):
            if self.fornecedores[i].cnpj == cnpj:
                del self.fornecedores[i]
                mensagem = "Fornecedor removido com sucesso!"
                print(mensagem)
                break

        self.atualizarArquivoFornecedor()
        return True, mensagem

    def buscarFornecedorPorCNPJ(self, cnpj):
        for fornecedor in self.fornecedores:
            if fornecedor.cnpj == cnpj:
                return fornecedor
        return None

    def alterarFornecedor(
        self, cnpjAlterar, nomeNovo, cnpjNovo, telefoneNovo, categoriaNova
    ):
        cnpj_novo_existe = any(
            forn.cnpj == cnpjNovo
            for forn in self.fornecedores
            if forn.cnpj != cnpjAlterar
        )

        if cnpj_novo_existe:
            mensagem = "O CNPJ novo informado já existe no sistema!"
            print(mensagem)
            return False, mensagem

        cnpj_existente = any(forn.cnpj == cnpjAlterar for forn in self.fornecedores)
        if not cnpj_existente:
            mensagem = "CNPJ não existe no sistema!"
            print(mensagem)
            return False, mensagem

        for item in self.fornecedores:
            if item.cnpj == cnpjAlterar:
                item.nome = nomeNovo
                item.cnpj = cnpjNovo
                item.telefone = telefoneNovo
                item.categoria = categoriaNova
        self.atualizarArquivoFornecedor()
        mensagem = "Fornecedor alterado com sucesso!"
        print(mensagem)
        return True, mensagem

    def exibirLista(self):
        if not self.fornecedores:
            mensagem = "Não há fornecedores para exibir"
            print(mensagem)
            return False, mensagem
        else:
            lista_texbox = (
                f'{"=" * 60}\n'
                f'{"********Fornecedores********":^60}\n'
                f'{"=" * 60}\n'
            )

            for item in self.fornecedores:
                lista_texbox += (
                    f"Nome: {item.nome}\n"
                    f"CNPJ: {item.cnpj}\n"
                    f"Telefone: {item.telefone}\n"
                    f"Categoria: {item.categoria}\n"
                    f'{"-" * 60}\n'
                )

            print(lista_texbox)
            return True, lista_texbox
