#Entrada
print('\t\t\tAlugel de Carros')
print('-' * 50)
km = float(input('Informe a Quantidade de KM rodado: '))
dias = int(input('Informe a Quantidade de Dias que ficou com o veículo: '))

#Processamento
valor_aluguel = (km * 0.15) + (dias * 60)

#Saída
print('-' * 50)
print('\t\t\tValor a pagar')
print('Dias com Veículo\t{}\nKM Rodados\t\t{}\nValor a pagar R$\t{:.2f}'
      .format(dias, km, valor_aluguel))
