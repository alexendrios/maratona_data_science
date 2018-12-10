from random import shuffle
#entrada
lista = input('Entre com os nomes para Ser realizado a Ordem: ').split()

#processamento
sorteio = lista
shuffle(sorteio)

#saída
print('\n--------------------- Sorteio de Ordem-------------------')
for i in range(len(lista)):
    print(i + 1, sorteio[i])

print('-' * 57)
