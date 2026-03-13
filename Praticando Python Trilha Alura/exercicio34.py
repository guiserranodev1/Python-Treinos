lista_atual = ['Pedro', 'Ana', 'Carlos']

print(lista_atual)

nome = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição que quer colocar ele na lista: '))

lista_atual.insert(posicao, nome)

print(lista_atual)