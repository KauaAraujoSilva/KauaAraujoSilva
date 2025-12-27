casa = float(input('Digite o valor do imovel: '))
salario = float(input('Digite o valor do seu salario: '))
ano = float(input('Quanto anos de financiamento: '))
prest = casa / (ano*12)
min = salario*30/100
print('Para pagar um imovel de R$ {} em {:.0f} anos,'. format(casa, ano), end = '')
print(' o valor da prestação será de: R$ {:.1f}'.format(prest))
if prest<=min:
    print('EMPRESTIMO CONCEDIDO')
else:
    print('EMPERSTIMO NEGADO')
'''calcule o valor mensal da prestação, e que nao pode exceder mais 
do que 30% do salario da pessoa ou entao sera negado o emprestimo'''