dia = int(input('Digite seu dia de nascimento: '))
mes = int(input('Digite seu mês de nascimento: '))
ano = int(input('Digite seu ano de nascimento: '))

if ano < 1950 or ano > 2026:
    print('Ano invalido para analise.')
else:
    print(f'Data valida para analise. Você nasceu em {dia} do {mes} de {ano}')