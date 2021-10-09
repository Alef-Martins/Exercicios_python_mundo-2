#'''Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# EQUILÀTERO = todos os lados iguais
# ISÒSCELES = dois lados iguais, um diferente
# ESCALENO = todos os lados diferentes'''
segmento1 = float(input('Segmento 1: '))
segmento2 = float(input('Segmento 2: '))
segmento3 = float(input('Segmento 3: '))
if segmento3 < segmento1 + segmento2 and segmento2 < segmento1 + segmento3 and segmento1 < segmento2 + segmento3:
    print('Os segmentos podem formar um triângulo ', end='')
    if segmento1 == segmento2 and segmento1 == segmento3:
        print('\033[31mEQUILÁTERO\033[m')
    elif segmento1 != segmento2 and segmento1 != segmento3 and segmento3 != segmento2:
        print('\033[31mESCALENO\033[m')
    else:
        print('\033[31mISÓSCELES\033[m')
else:
    print('As retas não podem formar um triângulo')