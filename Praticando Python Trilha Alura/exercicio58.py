desconto = int(input('Digite a porcentagem do desconto (%): '))
item = int(input("Digite o valor da compra: "))

desconto = item - (item * (desconto / 100))

print(f'Valor ficou: {desconto}')