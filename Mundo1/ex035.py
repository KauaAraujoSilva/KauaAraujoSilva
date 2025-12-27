v1 = float(input('Digite o valor do  primeiro segmento: ')) 
v2 = float(input('Digite o valor do segundo segmento: '))
v3 = float(input('Digite o valor do terceiro segmento: '))
if v1<v2+v3 and v2<v1+v3 and v3<v1+v2:
    print('Podem formar um triangulo!')
else:
    print('Não podem formar um triangulo')
#leia o comprimento de 3 retas e diga se elas podem ou não formar um triangulo
#pesquisar o principio matematico que faz possivel isso acontecer
#.sort = organiza em ordem crescente. fazer em lista   