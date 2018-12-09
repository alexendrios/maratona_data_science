#Entrada de Dados
tabuada = int(input('Digite um Número para ver a Tabuada: '))
resultado = 0

#Processamento
print('-' * 12)

for i in range(1, 11):
    resultado = tabuada * i
#Saída
    print('{:2} X {:2} = {:2}'.format(tabuada, i, resultado))

print('-' * 12)
