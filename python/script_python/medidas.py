#Dados de Entrda:
medida = float(input('Informe uma distância em metros: '))

#processamento
dm = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10

#saída
print('\n--------Conversor de Medidas-----------\n'
      'A medida {} metros equivale:\n'
      'DM:\t{:0f}\nCM:\t{:0f}\nMM:\t{:0f}\nKM:\t{:.3f}\nHM:\t{:.2f}\nDAM\t{:.1f}'
      '\n---------------------------------------'
      ''.format(medida, dm, cm, mm, km, hm, dam))

