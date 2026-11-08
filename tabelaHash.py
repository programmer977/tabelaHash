# CONSTANTES
M = 11
tabela = [[] for _ in range(M)]
def hash_func(matricula):
    return matricula % M

def inserir_aluno(matricula, nome, idade):
    indice = hash_func(matricula)
    for aluno in tabela[indice]:
        if aluno["matricula"] == matricula:
            print("\nErro: matrícula já cadastrada!")
            return
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "idade": idade
    }
    tabela[indice].append(aluno)
    print(f"\nAluno cadastrado na posição {indice}!")

def buscar_aluno(matricula):
    indice = hash_func(matricula)
    for aluno in tabela[indice]:
        if aluno["matricula"] == matricula:
            print("\nAluno encontrado!")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Posição Hash: {indice}")
            return
    print("\nAluno não encontrado!")

def exibir_tabela():
    print("\n========== TABELA HASH ==========")
    for indice in range(M):
        print(f"[{indice}]", end=" -> ")
        if not tabela[indice]:
            print("VAZIO")
            continue
        for aluno in tabela[indice]:
            print(
                f"({aluno['matricula']}, "
                f"{aluno['nome']}, "
                f"{aluno['idade']})",
                end=" -> "
            )
        print("None")
def menu():
    while True:
        print("\n========== MENU ==========")
        print("1 - Cadastrar aluno")
        print("2 - Buscar aluno")
        print("3 - Exibir tabela hash")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            try:
                matricula = int(input("Matrícula: "))
                nome = input("Nome: ").strip()
                idade = int(input("Idade: "))
                if matricula < 0 or idade < 0 or not nome:
                    print("\nDados inválidos!")
                    continue
                inserir_aluno(matricula, nome, idade)
            except ValueError:
                print("\nErro: matrícula e idade devem ser inteiros!")
        elif opcao == "2":
            try:
                matricula = int(input("Digite a matrícula: "))
                buscar_aluno(matricula)
            except ValueError:
                print("\nErro: matrícula deve ser um inteiro!")
        elif opcao == "3":
            exibir_tabela()
        elif opcao == "0":
            print("\nEncerrando sistema...")
            break
        else:
            print("\nOpção inválida!")
if __name__ == "__main__":
    menu()