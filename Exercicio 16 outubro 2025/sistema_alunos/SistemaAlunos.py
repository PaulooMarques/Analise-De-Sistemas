def adicionarAluno():
    nome = input("Nome do aluno: ").strip().lower()
    while True:
        nota = input("Nota final: ")
        if nota.isdigit() or is_float(nota):
            nota = float(nota)
            break
        print("nota inválida, tente novamente")
        continue
    notas[nome] = nota
    listaNomes.append(nome)
    print("Aluno cadastrado com sucesso!")

def listarAlunos():
    if not listaNomes:
        print("Nenhum aluno cadastrado.")
    print("\nLista de alunos:")
    for nome in listaNomes:
        print(f"- {nome} | Nota: {notas[nome]}")

def buscarNota():
    nome = input("Nome do aluno: ").strip().lower()
    if nome in listaNomes:
        print(f"Nota de {nome}: {notas[nome]}")
    else:
        print("Aluno não encontrado.")

def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

notas = {}
listaNomes = []

opcao = None

while opcao != 0:
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Adicionar alunos")
    print("2 - Listar alunos")
    print("3 - Buscar nota")
    print("0 - Sair")
    opcao = input("Opção: ")
    if  not opcao.isdigit():
        print("opção inválida")
        continue
    opcao = int(opcao)
    if opcao == 1:
        adicionarAluno()
    elif opcao == 2:
        listarAlunos()
    elif opcao == 3:
        buscarNota()
    elif opcao == 0:
        print('Encerrando...')
        break
    else:
        print("Opção inválida")
    continue