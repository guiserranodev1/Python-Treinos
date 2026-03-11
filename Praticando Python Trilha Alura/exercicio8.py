distancia = int(input('Digite a distancia percorrida em KM: '))

if distancia < 100:
    print('R$10,00 em pedagios.')
elif 100 < distancia <= 200:
    print('R$20,00 em pedagios.')
else:
    print('R$30,00 em pedagios.')