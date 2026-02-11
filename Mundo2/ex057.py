sexo = 'M' or 'F'
n = str(input('Digite o seu sexo(M/F): ')).upper()
while n!=sexo:
    print('Digite um sexo correspondente!')
    if n == 'M' or 'F':
        print('ola')
    break