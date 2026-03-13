def calcular_idade(ano1, ano2):
    return ano2 - ano1

nascimento = int(input('Digite seu ano de nascimento: '))
anoatual = int(input('Digite o ano atual: '))
idade = calcular_idade(nascimento, anoatual)

print(f'Você tem ou faz {idade} anos.')
