print('Calculadora de IMC')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está abaixo do peso. IMC de: {imc:.1f}.')
elif imc < 25:
    print(f'Seu peso está normal. IMC de: {imc:.1f}.')
else: 
    print(f'Você está acima do peso. IMC de {imc:.1f}.')



