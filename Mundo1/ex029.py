vel = float(input('Digite em qual velocidade você estava: '))
if vel > 80:
    print('Você estava {:.1f}km acima da velocidade permitida!'.format(vel - 80))
    print('Você será multado em: {:.1f} reais'.format((vel - 80)*7))
else:
    print('Você estava não será multado.')

#calcule quantos km ele andou a mais e acrescente 7,00 para cada