lista1 = [42, 7, 91, 13, 65, 28, 34, 76, 59, 2,
88, 47, 19, 63, 5, 72, 14, 99, 31, 8,
56, 24, 83, 60, 17, 45, 92, 10, 38, 70,
4, 67, 21, 54, 80, 33, 6, 95, 12, 73,
26, 58, 41, 3, 84, 69, 16, 50, 77, 29, 'REMOVA']

lista2 = [10, 23, 100]

print(len(lista1))

lista1.extend(lista2)  # .extend() junta listas

print(lista1[1:11])   # partição [inicio:fim]

lista1.remove('REMOVA')

print(lista1)