peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura**2)
print('Seu IMC está em {:.2f}'.format(imc))
if imc <18.5:
    print('Você esta abaixo do peso.')
elif imc<=25:
    print('Você esta no seu peso ideal.')
elif imc<=30:
    print('Você esta no sobrepeso.')
elif imc<=40:
    print('Você está na obesidade.')
elif imc>40:
    print('Você tem Obesidade Mórbida!')