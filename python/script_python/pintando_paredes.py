#entrada
largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da Parede em metros: '))

#processamento
area = largura * altura
qtd_tinta = area / 2

#saída
print('\n\t\t\tPintado Parede')
print('-' * 65)
print('A dimensão é {} X {} equivalente a {:.2f}m2\n'
      'para realizar a pintura será necessário {:.1f} litro(s) de Tinta(s) '
      .format(largura, altura, area, qtd_tinta))
print('-' * 65)
