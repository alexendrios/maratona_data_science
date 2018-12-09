#Entrada
valor = float(input('Informe o valor \tR$: '))

#processamento
dolar = valor / 3.8950
euro = valor / 4.44
libra = valor / 4.75
guarani = 1512.47 * valor
pesos = 9.5662 * valor
yuan = 1.7667006799477405 * valor

#saída
print()
print('-' * 5, 'Converão de Moedas', '-' * 5)
print('Dolar:\t\t{:.2f}\nEuro:\t\t{:.2f}\nLibras:\t\t{:.2f}\n'
      'Guarani:\t{:.2f}\nPesos:\t\t{:.2f}\nYuan:\t\t{:.2f}'
      .format(dolar, euro, libra, guarani, pesos, yuan))
print('-' * 30)
