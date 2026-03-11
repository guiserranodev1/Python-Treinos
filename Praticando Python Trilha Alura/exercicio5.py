despesas = int(input('Digite o total de despesas do mês (R$): '))

negativo = 3000 - despesas

if despesas > 3000:
    print(f'Atenção! Você ultrapassou o limite do orçamento: {negativo}.')
else:
    print('Dinheiro gasto dentro do orçamento.')