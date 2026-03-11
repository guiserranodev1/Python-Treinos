estoque = 20

while estoque > 0:
    compra = int(input('Digite a quantidade de livros que quer comprar: '))

    if compra <= estoque:
        estoque -= compra
        print(f'Compra realizada! Estoque atual: {estoque}')
    else: 
        print(f'Não temos essa quantidade em estoque ({estoque}).')

    if estoque == 0:
        print('Estoque esgotado.')