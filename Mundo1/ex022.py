nome = input('Digite o seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
pnome = nome.split() #split tira os espaços vazios
print(pnome[0])