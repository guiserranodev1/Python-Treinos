prod26 = float(input('Informe o crescimento da produção da empresa em 2026 (%): '))
prod25 = 27.0

if prod26 > prod25:
    print(f'A produção cresceu positivamente em um ano, de {prod25}% em 2025 para {prod26}% em 2026!')
elif prod26 < prod25:
    print(f'A produção diminuiu negativamente em um ano, de {prod25}% em 2025 para {prod26}% em 2026. ')
else:
    print('A produção permaneceu a mesma nos dois anos.')