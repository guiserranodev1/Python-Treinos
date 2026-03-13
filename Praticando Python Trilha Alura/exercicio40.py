convidados = set() #set cria um conjunto e remove duplicados
  
while True: 
    nome = input("Digite o nome do convidado ou 'sair' para encerrar: ") 

    if nome.lower() == "sair": 
        break 

    convidados.add(nome) 

print(f"Convidados confirmados: {', '.join(convidados)}")  #.join é o separados do input