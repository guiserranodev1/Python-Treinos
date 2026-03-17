conta = float(input('Valor da conta: '))
gorjeta = float(input('Gorjeta em %: '))

gorjeta2 = (gorjeta / 100) * conta

total = conta + gorjeta

print(f'Valor da gorjeta: R${gorjeta2:.2f}')
print(f'Total a pagar: R${total:.2f}')