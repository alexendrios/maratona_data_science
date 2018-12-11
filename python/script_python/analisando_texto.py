#entrada
nome = input('Informe o nome para Analizar: ').strip()

#saída
print('\nSeu nome analisado é ')
print('-' * 70)
print('Nome em Maíscula {}'.format(nome.upper()))
print('Nome em minúsculo {}'.format(nome.lower()))
print('seu nome Tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
es = nome.find(' ')
primeiro_nome = nome[:es].upper()
print('Seu primeiro nome é {} e tem {} letras'.format(primeiro_nome, len(primeiro_nome)))
print('-' * 70)

