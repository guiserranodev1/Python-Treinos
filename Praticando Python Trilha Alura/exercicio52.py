def calculadora(num1, num2, operacao):
    if operacao == '*':
        return (num1 * num2)
    elif operacao == '/':
        return (num1 / num2)
    elif operacao == '+':
        return (num1 + num2)
    elif operacao == '-':
        return (num1 - num2)
    else:
        print('Operação invalida.')
    
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
operacao = input('Digite a operação (+ - * /): ')
    

print(calculadora(num1, num2, operacao))