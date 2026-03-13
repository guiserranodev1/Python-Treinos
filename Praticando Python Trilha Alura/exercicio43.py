nomes = input("Digite os nomes separados por vírgula: ")

lista_nomes = nomes.split(",")

lista_nomes = [nome.strip() for nome in lista_nomes]

resultado = " | ".join(lista_nomes)

print(resultado)
print(f"Foram digitados {len(lista_nomes)} nomes")