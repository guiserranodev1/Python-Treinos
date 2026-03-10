ano1 = float(input('Digite o valor do carro no primeiro ano: '))
ano2 = float(input('Digite o valor do carro no segundo ano: '))
ano3 = float(input('Digite o valor do carro no terceiro ano: '))

media = (ano1 + ano2 + ano3) / (3)
print(f'{media:.3f} é a media de preços do carro nesses 3 anos.') 
# usei o .3f pra limitar os decimais do float

if ano1 > ano2 and ano1 > ano3:
    print('O primeiro ano foi o maior valor do carro.')
elif ano2 > ano1 and ano2 > ano3:
    print('O segundo ano foi o maior valor do carro.')
else:
    print('O terceiro ano foi o maior valor do carro.')