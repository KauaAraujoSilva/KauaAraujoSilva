import math
c1 = float(input("Digite o valor do Cateto Oposto: "))
c2 = float(input("Digite o valor do Cateto Adjacente: "))
hip = math.hypot(c1,c2)
print('o valor da hipotenusa é: {}'. format(hip))