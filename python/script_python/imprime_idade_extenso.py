# entrada
idade = int(input('Informe sua idade: '))

numeros_unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
numeros_dezenas = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
numeros_centenas = 'cento'
numeros_irregulares = ['onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

# processamento
u = idade // 1 % 10
d = idade // 10 % 10
c = idade // 100 % 10

unidade = ''
dezena = ''
centena = ''
conectivo = ''

if idade <= 122:
    if c == 0 and d == 0 and u == 0:
        unidade = numeros_unidades[0]
        status = True
    elif c == 0 and d == 0 and u == 1:
        unidade = numeros_unidades[1]
        status = True
    elif c == 0 and d == 0 and u == 2:
        unidade = numeros_unidades[2]
        status = True
    elif c == 0 and d == 0 and u == 3:
        unidade = numeros_unidades[3]
        status = True
    elif c == 0 and d == 0 and u == 4:
        unidade = numeros_unidades[4]
        status = True
    elif c == 0 and d == 0 and u == 5:
        unidade = numeros_unidades[5]
        status = True
    elif c == 0 and d == 0 and u == 6:
        unidade = numeros_unidades[6]
        status = True
    elif c == 0 and d == 0 and u == 7:
        unidade = numeros_unidades[7]
        status = True
    elif c == 0 and d == 0 and u == 8:
        unidade = numeros_unidades[8]
        status = True
    elif c == 0 and d == 0 and u == 9:
        unidade = numeros_unidades[9]
        status = True

    elif c == 0 and d == 1 and u == 0:
        dezena = numeros_dezenas[0]
        status = True
    elif c == 0 and d == 1 and u == 1:
        unidade = numeros_irregulares[0]
        status = True
    elif c == 0 and d == 1 and u == 2:
        unidade = numeros_irregulares[1]
        status = True
    elif c == 0 and d == 1 and u == 3:
        unidade = numeros_irregulares[2]
        status = True
    elif c == 0 and d == 1 and u == 4:
        unidade = numeros_irregulares[3]
        status = True
    elif c == 0 and d == 1 and u == 5:
        unidade = numeros_irregulares[4]
        status = True
    elif c == 0 and d == 1 and u == 6:
        unidade = numeros_irregulares[5]
        status = True
    elif c == 0 and d == 1 and u == 7:
        unidade = numeros_irregulares[6]
        status = True
    elif c == 0 and d == 1 and u == 8:
        unidade = numeros_irregulares[7]
        status = True
    elif c == 0 and d == 1 and u == 9:
        unidade = numeros_irregulares[8]
        status = True

    elif c == 0 and d == 2 and u == 0:
        dezena = numeros_dezenas[1]
        status = True
    elif c == 0 and d == 2 and u == 1:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 2:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 3:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 4:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 5:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 6:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 7:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 8:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 2 and u == 9:
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 3 and u == 0:
        dezena = numeros_dezenas[2]
        status = True
    elif c == 0 and d == 3 and u == 1:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 2:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 3:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 4:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 5:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 6:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 7:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 8:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 3 and u == 9:
        dezena = numeros_dezenas[2]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 4 and u == 0:
        dezena = numeros_dezenas[3]
        status = True
    elif c == 0 and d == 4 and u == 1:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 2:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 3:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 4:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 5:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 6:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 7:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 8:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 4 and u == 9:
        dezena = numeros_dezenas[3]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 5 and u == 0:
        dezena = numeros_dezenas[4]
        status = True
    elif c == 0 and d == 5 and u == 1:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 2:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 3:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 4:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 5:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 6:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 7:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 8:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 5 and u == 9:
        dezena = numeros_dezenas[4]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 6 and u == 0:
        dezena = numeros_dezenas[5]
        status = True
    elif c == 0 and d == 6 and u == 1:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 2:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 3:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 4:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 5:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 6:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 7:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 8:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 6 and u == 9:
        dezena = numeros_dezenas[5]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 7 and u == 0:
        dezena = numeros_dezenas[6]
        status = True
    elif c == 0 and d == 7 and u == 1:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 2:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 3:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 4:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 5:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 6:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 7:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 8:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 7 and u == 9:
        dezena = numeros_dezenas[6]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 8 and u == 0:
        dezena = numeros_dezenas[7]
        status = True
    elif c == 0 and d == 8 and u == 1:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 2:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 3:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 4:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 5:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 6:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 7:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 8:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 8 and u == 9:
        dezena = numeros_dezenas[7]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 0 and d == 9 and u == 0:
        dezena = numeros_dezenas[8]
        status = True
    elif c == 0 and d == 9 and u == 1:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 2:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 3:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 4:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 5:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 6:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[6]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 7:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 8:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 0 and d == 9 and u == 9:
        dezena = numeros_dezenas[8]
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 1 and d == 0 and u == 0:
        centena = numeros_centenas
        status = True
    elif c == 1 and d == 0 and u == 1:
        centena = numeros_centenas
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 2:
        centena = numeros_centenas
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 3:
        centena = numeros_centenas
        unidade = numeros_unidades[3]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 4:
        centena = numeros_centenas
        unidade = numeros_unidades[4]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 5:
        centena = numeros_centenas
        unidade = numeros_unidades[5]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 6:
        unidade = numeros_unidades[6]
        centena = numeros_centenas
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 7:
        centena = numeros_centenas
        unidade = numeros_unidades[7]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 8:
        centena = numeros_centenas
        unidade = numeros_unidades[8]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 0 and u == 9:
        centena = numeros_centenas
        unidade = numeros_unidades[9]
        conectivo = 'e'
        status = True

    elif c == 1 and d == 1 and u == 0:
        centena = numeros_centenas
        dezena = numeros_dezenas[0]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 1:
        centena = numeros_centenas
        unidade = numeros_irregulares[0]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 2:
        centena = numeros_centenas
        unidade = numeros_irregulares[1]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 3:
        centena = numeros_centenas
        unidade = numeros_irregulares[2]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 4:
        centena = numeros_centenas
        unidade = numeros_irregulares[3]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 5:
        centena = numeros_centenas
        unidade = numeros_irregulares[4]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 6:
        centena = numeros_centenas
        unidade = numeros_irregulares[5]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 7:
        centena = numeros_centenas
        unidade = numeros_irregulares[6]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 8:
        centena = numeros_centenas
        unidade = numeros_irregulares[7]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 1 and u == 9:
        centena = numeros_centenas
        unidade = numeros_irregulares[8]
        conectivo = 'e'
        status = True

    elif c == 1 and d == 2 and u == 0:
        centena = numeros_centenas
        dezena = numeros_dezenas[1]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 2 and u == 1:
        centena = numeros_centenas
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[1]
        conectivo = 'e'
        status = True
    elif c == 1 and d == 2 and u == 2:
        centena = numeros_centenas
        dezena = numeros_dezenas[1]
        unidade = numeros_unidades[2]
        conectivo = 'e'
        status = True
else:
    status = False

# saída
print('')
print('-' * 30)
if status == True:
    if c == 0:
        print('Você tem {} {} {} anos'.format(dezena, conectivo, unidade))
    elif c == 1:
        print('Você tem {} {} {} {} anos.'.format(centena, conectivo, dezena, unidade))
else:
    print('''\n\tParabéns!!
    Você é mais velho(a) que:
    Jeanne-Louise Calment,
    Nasceu em 21 de fevereiro de 1875 e faleceu em  4 de agosto de 1997
    foi uma supercentenária francesa confirmada como a pessoa mais 
    velha já documentada da história, depois de alcançar a idade de:
    122 anos.
    ''')

print('-' * 30)
