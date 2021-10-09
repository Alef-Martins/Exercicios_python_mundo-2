#Faça um programa que leia um número qualquer e mostre seu fatorial.
#from math import factorial
num = int(input('Informe um número: '))
c = num
res = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    
    res *= c
    c -= 1
print(res)
