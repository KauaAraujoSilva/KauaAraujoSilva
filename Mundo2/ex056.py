somid=0
for i in range(1, 3):
    print('-=-'*10)
    # nome = str(input(f'Digite o nome da {i}° pessoa: '))
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    # sexo = bool(input(f'Digite o sexo da {i}° pessoa: '))
    somid+=i
    # print('-=-'*10)
    if somid:
        media=somid/i
        print('A media é: {}'.format(media))
#leia nome, idade e sexo de 4 pessoas. Mostre a media da idade do grupo. O nome do homem mais velho. Quantas mulheres tem menos de 20anos