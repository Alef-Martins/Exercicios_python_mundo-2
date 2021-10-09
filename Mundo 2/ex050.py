#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas entre aqueles que forem pares, se o resultado da soma for ímpar desconsidere-o.
soma = 0
for c in range (1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
if soma % 2 == 0:
    print(f'A soma entre os números pares é {soma}')
elif soma < 2 or soma % 2 != 0:
    print('O resultado da soma é ímpar.')