def calculadora(num1,num2,operacao):

    if operacao == 'soma':
        return num1 + num2
    if operacao == 'menos':
        return num1 - num2
    if operacao == 'vezes':
        return num1 * num2
    if operacao == 'dividir':
        return num1 / num2


print(calculadora(4,5,'soma'))