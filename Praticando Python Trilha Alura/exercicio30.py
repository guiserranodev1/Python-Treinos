while True:

    lista = ['arroz', 'massa', 'peixe']

    item = input('Digite o item que quer verificar: ')

    if item in lista:
        print('Item ja em lista de compras.')
    else:
        print('Item ainda não adicionado na lista de compras.')