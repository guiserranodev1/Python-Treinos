class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Nome da pessoa: {self.nome}, idade: {self.idade}'
    


p1 = Pessoa('Guilherme', 21)
p2 = Pessoa('Bruno', 22)


print(p1)
