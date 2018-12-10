from math import hypot

#entrada
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Adjacente: '))

#processamento

#calculando a Hipotenusa sem a utilização da Biblioteca math
#hi = (co ** 2 + ca ** 2) ** (1/2)

#utilizando a biblioteca math
hi = hypot(co, ca)

#saída
print('A hipotenusa vai medir: {:.2f}'.format(hi))

