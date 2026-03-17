class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome da pessoa: {self.nome}, idade: {self.idade}'

banco_pessoas = []

while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade: "))

    pessoa = Pessoa(nome, idade)
    banco_pessoas.append(pessoa)

    continuar = input("Deseja adicionar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break


print("\nPessoas cadastradas:")
for p in banco_pessoas:
    print(p)