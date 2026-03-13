ana = set(input('Produtos de Ana: ').split(', '))
laura = set(input('Produtos de Laura: ').split(', '))

comuns = ana.intersection(laura)

print(f'Produtos em comum nas listas: {', '.join(comuns)}')

exclaura = laura.difference(ana)
excana = ana.difference(laura)

print(f'Produtos exclusivos da Laura: {', '.join(exclaura)}')
print(f'Produtos exclusivos da Ana: {', '.join(excana)}')