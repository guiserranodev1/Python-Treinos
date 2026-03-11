renda = int(input('Digite o valor da sua renda: '))
parcela = int(input('Digite o valor da parcela desejada: '))

if renda > 2000 and parcela <= 0.3 * renda:
    print('Emprestimo aprovado.')
elif renda <= 2000:
    print('Rend1 insuficiente.')
else:
    print('Parcela acima de 30% da renda.') 