def media_turma(alunos):
    media = 0
    for i in alunos.values():
        media += i
    return media/len(alunos)

def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

alunos = {}

for i in range(1, 6):
    nome = input(f"Digite o nome do aluno {i}:\n")
    nota = input(f"Digite a nota de {nome}:\n")

    if nota.isdigit() or is_float(nota):
        nota = float(nota)
    else:
        nota = 0.0
    alunos[nome] = nota

media = media_turma(alunos)
print("\n=== Lista de alunos ===")
for nome, nota in alunos.items():
    print(f"{nome} {" "*(10-len(nome))}| Nota: {nota:.2f}")
print(f"Média da turma: {media:.2f}")