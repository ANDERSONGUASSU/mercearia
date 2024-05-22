from database.dao import DaoFuncionario
from models.Models import Funcionario


class ControllerFuncionario:
    def __init__(self) -> None:
        self.funcionarios = DaoFuncionario.ler()

    def atualizarArquivoFuncionario(self):
        with open("./database/data/funcionarios.txt", "w") as arq:
            for item in self.funcionarios:
                arq.writelines(
                    f"{item.nome}|"
                    f"{item.cpf}|"
                    f"{item.telefone}|"
                    f"{item.endereco}|"
                    f"{item.email}|"
                    f"{item.clt}\n"
                )

    def cadastrarFuncionario(self, nome, cpf, telefone, endereco, email, clt):
        if len(cpf) != 11:
            mensagem = "Digite um CPF válido"
            print(mensagem)
            return False, mensagem
        cpf_existe = any(funcionario.cpf == cpf for funcionario in self.funcionarios)
        if cpf_existe:
            mensagem = "CPF já cadastrado no sistema"
            print(mensagem)
            return False, mensagem

        email_existe = any(
            funcionario.email == email for funcionario in self.funcionarios
        )
        if email_existe:
            mensagem = "E-mail já cadastrado no sistema"
            print(mensagem)
            return False, mensagem

        novo_funcionário = Funcionario(nome, cpf, telefone, endereco, email, clt)
        DaoFuncionario.salvar(novo_funcionário, clt)
        mensagem = "Funcionário cadastrado com sucesso!"
        print(mensagem)
        return True, mensagem

    def removerFuncionario(self, cpf):
        cpf_existe = any(funcionario.cpf == cpf for funcionario in self.funcionarios)
        if not cpf_existe:
            mensagem = "CPF não cadastrado no sistema."
            print(mensagem)
            return False, mensagem

        for i in range(len(self.funcionarios)):
            if self.funcionarios[i].cpf == cpf:
                del self.funcionarios[i]
                mensagem = "Funcionário removido com sucesso!"
                print(mensagem)
                break
        self.atualizarArquivoFuncionario()
        return True, mensagem

    def buscaFuncionarioPorCpf(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def alterarFuncionario(
        self,
        cpfAlterar,
        nomeNovo,
        cpfNovo,
        telefoneNovo,
        enderecoNovo,
        emailNovo,
        cltNova,
    ):
        cpf_novo_existe = any(
            funcionario.cpf == cpfNovo
            for funcionario in self.funcionarios
            if funcionario.cpf != cpfAlterar
        )
        if cpf_novo_existe:
            mensagem = "O CPF novo informado já existe no sistema!"
            print(mensagem)
            return False, mensagem

        cpf_existe = any(
            funcionario.cpf == cpfAlterar for funcionario in self.funcionarios
        )

        if not cpf_existe:
            mensagem = "CPF não existe no sistema"
            print(mensagem)
            return False, mensagem

        for item in self.funcionarios:
            if item.cpf == cpfAlterar:
                item.nome = nomeNovo
                item.cpf = cpfNovo
                item.telefone = telefoneNovo
                item.endereco = enderecoNovo
                item.email = emailNovo
                item.clt = cltNova
        self.atualizarArquivoFuncionario()
        mensagem = "Funcionário alterado com sucesso!"
        print(mensagem)
        return True, mensagem

    def exibirLista(self):
        if not self.funcionarios:
            mensagem = "Não há funcionários para exibir"
            print(mensagem)
            return False, mensagem

        else:
            lista_texbox = (
                f'{"=" * 60}\n'
                f'{"********Funcionários********":^60}\n'
                f'{"=" * 60}\n'
            )

            for item in self.funcionarios:
                lista_texbox += (
                    f"Nome: {item.nome}\n"
                    f"CPF: {item.cpf}\n"
                    f"Telefone: {item.telefone}\n"
                    f"Endereço: {item.endereco}\n"
                    f"E-mail: {item.email}\n"
                    f"CLT: {item.clt}\n"
                    f'{"-" * 60}\n'
                )

            print(lista_texbox)
            return True, lista_texbox
