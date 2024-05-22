from database.dao import DaoPessoas
from models.Models import Pessoa


class ControllerCliente:
    def __init__(self):
        self.clientes = DaoPessoas.ler()

    def atualizarArquivoCliente(self):
        with open("./database/data/clientes.txt", "w") as arq:
            for item in self.clientes:
                arq.writelines(
                    f"{item.nome}|"
                    f"{item.cpf}|"
                    f"{item.telefone}|"
                    f"{item.endereco}|"
                    f"{item.email}\n"
                )

    def cadastrarCliente(self, nome, cpf, telefone, endereco, email):

        if len(cpf) != 11:
            mensagem = "Digite um CPF válido"
            print(mensagem)
            return False, mensagem

        cpf_existe = any(cliente.cpf == cpf for cliente in self.clientes)
        if cpf_existe:
            mensagem = "CPF já cadastrado no sistema!"
            print(mensagem)
            return False, mensagem

        email_existe = any(cliente.email == email for cliente in self.clientes)
        if email_existe:
            mensagem
            print(mensagem)
            return False, mensagem

        novo_cliente = Pessoa(nome, cpf, telefone, endereco, email)
        DaoPessoas.salvar(novo_cliente)
        mensagem = "Cliente cadastrado com sucesso!"
        self.atualizarArquivoCliente()
        print(mensagem)
        return True, mensagem

    def removerCliente(self, cpf):
        cpf_existe = any(cliente.cpf == cpf for cliente in self.clientes)
        if not cpf_existe:
            mensagem = "CPF não cadastrado no sistema."
            return False, mensagem

        for i in range(len(self.clientes)):
            if self.clientes[i].cpf == cpf:
                del self.clientes[i]
                mensagem = "Cliente removido com sucesso!"
                print(mensagem)
                break

        self.atualizarArquivoCliente()
        return True, mensagem

    def buscarClientePorCPF(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def alterarCliente(
        self, cpfAlterar, nomeNovo, cpfNovo, telefoneNovo, enderecoNovo, emailNovo
    ):
        cpf_novo_existe = any(
            cliente.cpf == cpfNovo
            for cliente in self.clientes
            if cliente.cpf != cpfAlterar
        )
        if cpf_novo_existe:
            mensagem = "O CPF novo informado já existe no sistema!"
            print(mensagem)
            return False, mensagem

        cpf_existe = any(cliente.cpf == cpfAlterar for cliente in self.clientes)

        if not cpf_existe:
            mensagem = "CPF não existe no sistema!"
            print(mensagem)
            return False, mensagem

        for item in self.clientes:
            if item.cpf == cpfAlterar:
                item.nome = nomeNovo
                item.cpf = cpfNovo
                item.telefone = telefoneNovo
                item.endereco = enderecoNovo
                item.email = emailNovo

        self.atualizarArquivoCliente()
        mensagem = "Cliente alterado com sucesso!"
        print(mensagem)
        return True, mensagem

    def exibirLista(self):

        if not self.clientes:
            mensagem = "Não há clientes para exibir"

            print(mensagem)
            return False, mensagem

        else:
            lista_texbox = (
                f'{"=" * 60}\n' f'{"********Clientes********":^60}\n' f'{"=" * 60}\n'
            )

            for item in self.clientes:
                lista_texbox += (
                    f"Nome: {item.nome}\n"
                    f"CPF: {item.cpf}\n"
                    f"Telefone: {item.telefone}\n"
                    f"Endereço: {item.endereco}\n"
                    f"E-mail: {item.email}\n"
                    f'{"-" * 60}\n'
                )

            print(lista_texbox)
            return True, lista_texbox
