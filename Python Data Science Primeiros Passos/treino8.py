var = True
na_area = False

if var and na_area:
    print("PENALIDADE MÁXIMA!")
elif var and not na_area:
    print("Falta fora da área!")
else:
    print("Não foi falta!")