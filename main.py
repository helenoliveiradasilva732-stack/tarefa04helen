# Tarefa 02 - Sistema de Cadastro de Alunos
# Disciplina: Introdução à Ciência da Computação
# Aluno(s): [preencher nome (matrícula)]
# Data: 17/11/2026

from datetime import datetime


alunos = {}


def ler_obrigatorio(prompt):
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Erro: este campo é obrigatório.")


def ler_data_nascimento(prompt="Data de Nascimento: "):
    while True:
        data = ler_obrigatorio(prompt)
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: informe uma data válida no formato dd/mm/aaaa.")


def cadastrar_aluno():
    print("\n=== Cadastrar Aluno ===")
    matricula = ler_obrigatorio("Matrícula: ")
    if matricula in alunos:
        print("Erro: já existe um aluno com essa matrícula.")
        return

    aluno = {
        "nome": ler_obrigatorio("Nome: "),
        "endereco": ler_obrigatorio("Endereço: "),
        "data_nasc": ler_data_nascimento(),
    }
    alunos[matricula] = aluno
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n=== Alunos Cadastrados ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for matricula, aluno in alunos.items():
        exibir_aluno(matricula, aluno)


def exibir_aluno(matricula, aluno):
    print(f"\nMatrícula: {matricula}")
    print(f"Nome: {aluno['nome']}")
    print(f"Endereço: {aluno['endereco']}")
    print(f"Data de Nascimento: {aluno['data_nasc']}")


def buscar_aluno():
    print("\n=== Buscar Aluno ===")
    termo = ler_obrigatorio("Digite o nome ou a matrícula: ")

    if termo in alunos:
        exibir_aluno(termo, alunos[termo])
        return

    encontrados = [
        (matricula, aluno)
        for matricula, aluno in alunos.items()
        if termo.casefold() in aluno["nome"].casefold()
    ]
    if encontrados:
        for matricula, aluno in encontrados:
            exibir_aluno(matricula, aluno)
    else:
        print("Nenhum aluno encontrado.")


def alterar_aluno():
    print("\n=== Alterar Aluno ===")
    matricula = ler_obrigatorio("Matrícula do aluno: ")
    aluno = alunos.get(matricula)
    if aluno is None:
        print("Erro: matrícula não encontrada.")
        return

    exibir_aluno(matricula, aluno)
    print("Deixe o campo vazio para manter o valor atual.")
    for campo, rotulo in (
        ("nome", "Nome"),
        ("endereco", "Endereço"),
    ):
        valor = input(f"{rotulo} [{aluno[campo]}]: ").strip()
        if valor:
            aluno[campo] = valor

    while True:
        data = input(f"Data de Nascimento [{aluno['data_nasc']}]: ").strip()
        if not data:
            break
        try:
            datetime.strptime(data, "%d/%m/%Y")
            aluno["data_nasc"] = data
            break
        except ValueError:
            print("Erro: informe uma data válida no formato dd/mm/aaaa.")

    print("Dados do aluno alterados com sucesso!")


def excluir_aluno():
    print("\n=== Excluir Aluno ===")
    matricula = ler_obrigatorio("Matrícula do aluno: ")
    aluno = alunos.get(matricula)
    if aluno is None:
        print("Erro: matrícula não encontrada.")
        return

    exibir_aluno(matricula, aluno)
    confirmacao = input("Confirma a exclusão? (s/n): ").strip().casefold()
    if confirmacao == "s":
        del alunos[matricula]
        print("Aluno excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def exibir_menu():
    print("\n=== Sistema de Cadastro de Alunos ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar")
    print("4 - Alterar")
    print("5 - Excluir")
    print("0 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            alterar_aluno()
        elif opcao == "5":
            excluir_aluno()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Digite um número de 0 a 5.")


if __name__ == "__main__":
    main()
