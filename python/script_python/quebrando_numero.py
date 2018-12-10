import math

#entrada
numero = float(input('Entre com o número Flutuante: '))

#processamento
inteira = math.trunc(numero)

#saida
print('O valor digitado foi {} e sua porção inteira é: {}'.format(numero, inteira))
