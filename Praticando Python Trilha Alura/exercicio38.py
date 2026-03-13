notas = input('Digite as notas da turma separadas por vírgula: ').split(', ')

notas = [float(nota) for nota in notas]

media = sum(notas) / len(notas)

print(f'A média da turma é: {media:.2f}')