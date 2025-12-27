from math import radians, sin, cos, tan
an = float(input('digite o valor do angulo: '))
sen = sin(radians(an))
print('O SENO de do angulo {} é: {:.2f}'.format(an, sen))
cos = cos(radians(an))
print('O valor do COSSENO do angulo de {} é de: {:.2f}'.format(an,cos))
tan = tan(radians(an))
print("o valor da TANGENTE do angulo {} é de: {:.2f}".format(an, tan))