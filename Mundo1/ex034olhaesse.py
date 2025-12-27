'''salario = int(input('Digite o valor do seu salario: '))
if salario >= 1250:
    print('O seu salário será de {}'.format(salario + (salario)*0.1))
else:
    print('O seu salário será de {}'.format(salario + (salario)*0.15))'''

salario = float(input('Digite o seu salario: '))
if  salario <=1250:
    novo = salario + salario*0.15
else:
    novo = salario + salario*0.10
print('O seu salario sera de: {:.2f} reais.'.format(novo))
#essa é outra maneira de fazer

'''print salario de um func. e calcule o valor de seu aumento
superiores á 1250 - 10%, inferior a 1250 - aumento de 15%'''