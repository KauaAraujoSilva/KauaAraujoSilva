print('{:=^40}'.format(' LOJAS KAUÃ '))
prod = float(input('Digite o valor dos produto: '))
print('Avista = 1''\nCartão = 2')
v = int(input('Selecione uma das opções acima: '))
if v==1:
    print('Você escolheu a opção AVISTA, seu produto de {}R$, sairá por {}R$.'.format(prod, prod*90/100))
if v==2:
    print('Você escolheu a opção CARTÃO.')
    print('Irá pagar avista(1) ou parcelar?(2)')
    val=int(input('Selecione uma das opções acima: '))
    if val==1:
        print('Você escolheu a opção AVISTA NO CARTÃO, seu produto de {:.0f}R$,sairá por {:.0f}R$.'.format(prod, prod*95/100))
    if val==2:
        parc = int(input('Digite o valor das parcelas: '))
        if parc == 2:
            print('Você escolheu a opção PARCELADO NO CARTÃO, seu produto de {}, sairá por {}'.format(prod, prod))
        elif parc>=3:
            print('Você escolheu a opção PARCELADO NO CARTÃO, seu produto de {}, sairá por {}'.format(prod, prod*120/100))
            print('O valor da parcela será de: {:.2f}R$.'.format((prod*120/100)/parc))
else:
    print('Escolha somente uma das opções acima!')
