lista1 = [42, 7, 91, 13, 65, 28, 34, 76, 59, 2,
88, 47, 19, 63, 5, 72, 14, 99, 31, 8,
56, 24, 83, 60, 17, 45, 92, 10, 38, 70,
4, 67, 21, 54, 80, 33, 6, 95, 12, 73,
26, 58, 41, 3, 84, 69, 16, 50, 77, 29]

somaLista1 = sum(lista1) #.sum() soma geral dos itens na lista

print(f'A soma dos numeros na lista 1 é {somaLista1}')

print(f'Quantidade de numeros na lista: {len(lista1)}')

par = []
impar = []

for n in lista1:
    if n % 2 == 0:
        par.append(n) #.append() inclui na lista
    else:
        impar.append(n)

print(f'Numero par: {par} e impar: {impar}.')

# mostrar o valor da lista em especifico = lista[14]