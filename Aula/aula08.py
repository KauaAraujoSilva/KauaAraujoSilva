import math
n = float(input('Digite um numero: '))
raiz = math.sqrt(n)
print("A raiz de {} é igual ao numero: {:.2f} ".format(n, raiz))
#ao usar o math.ceil, ele aproxima para cima

from math import sqrt, ceil
n = float(input("numero: "))
raiz = sqrt(n)
print("a raiz de {} é {}".format(n, ceil(raiz)))

#ambos sao "os mesmos"