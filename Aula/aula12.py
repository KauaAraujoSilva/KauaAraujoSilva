nome = input('Digite o seu nome: ')
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome =='Pedro' or nome =='Rafael':
    print('Seu nome é bem popular no brasil.')
elif nome in 'Ana Maria de Souza':
    print('Que belo nome feminino!')
else:
    print('Seu nome é comum.')
print('Ola {}, tudo bem?'.format(nome))