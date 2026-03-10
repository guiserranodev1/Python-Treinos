gabarito = ['D','A','C','B','A','D','C','C','A','B']

nota = 0

for i in range(10):
    resposta = input(f"Resposta da questão {i+1}: ").upper()
    
    if resposta == gabarito[i]:
        nota += 1

print("Nota final:", nota)