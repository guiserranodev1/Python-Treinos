guilherme = 9
gabriele = 10

print('Olá, seja bem-vindo ao sistema de notas.')
nome = input('Qual o seu nome? ')
if nome.lower() == 'guilherme':
    print('Olá Guilherme, sua nota está em {}' .format(guilherme))
elif nome.lower() == 'gabriele':
    print('Olá Gabriele, sua nota está em {}' .format(gabriele))
else:
    print('Nome não encontrado no sistema de notas.')

