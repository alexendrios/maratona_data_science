#Entrada
valor = float(input('Insira o valor da Compra R$ '))

#Processamento
desconto = valor * 0.05
valor_pagar = valor - desconto

#Saída
print('\n\t-----------\tDescontos\t----------')
print('Total da Compra\t\t{:.2f}\nDesconto de 5%\t\t{:.2f}\n'
      'Total a Pagar R$\t{:.2f}'.format(valor, desconto, valor_pagar))
print('-' * 39)
