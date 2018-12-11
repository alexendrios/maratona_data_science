#entrada
numero = int(input('Informe o numero a ser analisado de 0 a 9999: '))

#processamento
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

#milhar
print('\nAnalisando o Número {}'.format(numero))
print('Unidade:\t{}'.format(u))
print('Dezena:\t\t{}'.format(d))
print('Centena:\t{}'.format(c))
print('Milhara:\t{}'.format(m))
