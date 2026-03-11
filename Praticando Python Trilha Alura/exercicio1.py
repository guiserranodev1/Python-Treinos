banana = int(input('Quantidade de bananas vendidas: '))
macas = int(input('Quantidade de maças vendidas: '))

if banana > macas:
    print('Bananas venderam mais que maçãs!')
elif macas > banana:
    print('Maças venderam mais que bananas!')
else:
    print('As quantidades de vendas foram iguais!')

