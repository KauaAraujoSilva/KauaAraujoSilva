dist = float(input('Digite qual será a distancia percorrida em kilometros: '))
if dist <= 200:
    print('Até a distancia {}, o valor será de {} reais.'.format(dist, dist*0.5 ))
else: 
    print('Até a distancia {}, o valor será de {}'.format(dist, dist*0.45))

#qual a distancia da viagem em km, calcule o preço da viagem po 0,5rs - km para viagens ate 200km
# \n e  para acima de 200km, se torna 0.45rs - km