for segundos in range(10, 0, -1):   # significado (começa em 10, vai até 1, diminuindo de 1 em 1)
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")