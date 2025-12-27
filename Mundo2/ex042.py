v1 = float(input('Digite o valor do primeiro segmento: '))
v2 = float(input('Digite o valor do segundo segmento: '))
v3 = float(input('Digite o valor do terceiro segmento: '))
if v1<v2+v3 and v2<v1+v3 and v3<v2+v1:
    #antes tava dando erro por que eu deixei OR ao inves de AND,
    #se deixar assim, qualquer valor maior é contado.
    print('Pode formar um triangulo')
    print('='*25)
    if v1==v2==v3:
        print('Esse triangulo é Equilatero.')
    elif v1!=v2!=v3!=v1:
        print('Esse triangulo é Escaleno.')
    else:
        print('Esse triangulo é Isosceles.')
    print('='*25)
    
else:
    print('NÃO podem formar um triangulo')