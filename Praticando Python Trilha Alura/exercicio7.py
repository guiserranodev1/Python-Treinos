nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))
nota3 = float(input('Digite a nota da prova 3: '))

media = (nota1 + nota2 + nota3) / (3)

if media >= 7:
    print("Aprovado!")
elif 5 <= media < 7:
    print('Recuperação.')
else:
    print('Reprovado.')

print(f'Media: {media:.2f}')