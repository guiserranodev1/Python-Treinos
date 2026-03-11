import re

receita = input("Digite a descrição da receita: ")

resultado = re.search(r"\d+", receita)

if resultado:
    print(f"O número da receita é: {resultado.group()}")
else:
    print("Nenhum número de receita encontrado.")