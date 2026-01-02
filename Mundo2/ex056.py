quant = 0
for i in range(4):
    print('-=-'*10)
    sexo = str(input('Digite o seu sexo(M/F): '))
    x = sexo.upper()
    
    print(x)
    if x=='M':
        print('diferente de m', x)
    elif x!='F':
        print('diferente de f', x)
    else:
        print('what is', x)
    quant+=x
print(f'A media da idade do grupo é igual à: {quant/(i+1)}')
        
#leia nome, idade e sexo de 4 pessoas. Mostre a media da idade do grupo. O nome do homem mais velho. Quantas mulheres tem menos de 20anos