valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores))   #map converte valores digitados em numeros
print(f"O total de vendas foi: {total}") 