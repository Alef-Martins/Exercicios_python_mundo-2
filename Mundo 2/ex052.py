#Fça um programa que leia um número inteiro e diga se ele é primo ou não
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')