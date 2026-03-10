# Solicita os valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operador = input("Digite o operador (+, -, *, /): ")
potencia = float(input("Digite a potência: "))

# Realiza a operação
if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        print("Erro: divisão por zero!")
        exit()
else:
    print("Operador inválido!")
    exit()

# Aplica a exponenciação
resultado_final = resultado ** potencia

print(f"Resultado da operação: {resultado}")
print(f"Resultado após elevar à potência {potencia}: {resultado_final}")

