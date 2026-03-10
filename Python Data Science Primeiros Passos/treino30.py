gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

contador = 0

total = sum(gastos)

media = (total) / len(gastos)

print(f'Media de gastos: {media}')

for i in gastos:
    if i > 3000:
        print('Compra acima de 3000: ', i)
        contador += 1

porcentagem = (contador / len(gastos)) * 100

print("Quantidade de compras acima de 3000:", contador)
print(f"Porcentagem: {porcentagem:.2f}%")