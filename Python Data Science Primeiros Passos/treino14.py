n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort()
 #caso quisesse fazer em decrescente: numeros.sort(reverse=True)

print("Ordem crescente:", numeros)


nomes = ["banana", "abacaxi", "laranja"]
nomes.sort()
print(nomes)