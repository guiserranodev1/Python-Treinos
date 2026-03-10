turno = (input("Qual turno tu estuda? ")).strip().lower()

if turno == 'manha':
    print('Bom dia!')
elif turno == 'dia':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else: 
    print('Turno invalido.')

