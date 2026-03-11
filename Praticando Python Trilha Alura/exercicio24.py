url = input('Digite a URL para revisão: ')

if url.startswith('https://') and url.endswith('.com'):
    print('URL Válida!')
else:
    print('URL Invalida!')
