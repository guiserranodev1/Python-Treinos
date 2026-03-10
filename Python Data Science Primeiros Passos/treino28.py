matricula_gui = {'matricula':1200016793,
              'dia_cadastro':25,
              'mes_cadastro': 10,
              'turma': '2E'}

matricula_gui['turma'] = '2G'
matricula_gui['modalidade'] = 'EAD'

print(matricula_gui['turma'], matricula_gui['modalidade'])
print(matricula_gui.items())
print(matricula_gui.keys())
print(matricula_gui.values())

for chaves, valores in matricula_gui.items():
    print(chaves, valores)