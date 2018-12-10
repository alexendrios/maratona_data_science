import math

#entrada
angulo = float(input('Digite o ângulo que Deseja: '))

#processamento
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#saída
print('O angulo de {}º tem:\n\nSeno\t\t{:.2f}\nCosseno\t\t{:.2f}\nTangente\t{:.2f}'
      .format(angulo, seno, cosseno, tangente))