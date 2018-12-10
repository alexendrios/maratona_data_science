import random
#entrada
lista = input('Entre com os nomes para Ser realizado o sorteio: ').split()

#processamento
sorteio = random.choice(lista)

#saída
print('\n--------------------- Sorteio ----------------------')
print('O nome escolhido foi: ***** {} ******'.format(sorteio))
print('-' * 52)
