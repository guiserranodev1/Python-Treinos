dia1 = int(input('Informe os dias para a atividade A: '))
dia2 = int(input('Informe os dias para a atividade B: '))
dia3 = int(input('Informe os dias para a atividade C: '))

total = dia1 + dia2 + dia3


if dia1 < 0:
    print("Os dias não podem ser negativos.")
elif dia2 < 0:
    print('Os dias não podem ser negativos.')
elif dia3 < 0:
    print("Os dias não podem ser negativos.")
else:
    print(f'As atividades demorarão {total} dias para serem concluidas.')


