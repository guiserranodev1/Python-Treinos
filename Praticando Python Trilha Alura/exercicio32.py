voluntarios = []

while True:
    nome = input("Digite o nome do voluntario ou 'sair' para encerrar: ")

    if nome.lower() == 'sair':
        break
    else:
        voluntarios.append(nome)

print('Voluntarios registrados: ', voluntarios)
