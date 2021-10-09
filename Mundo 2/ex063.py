#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros números da sequência de Fibonacci.
n = int(input('Quantos elementos quer mostrar? '))
n1 = 1
n2 = 1
c = 1
print(n1, end='- ')
while c <= n:
    print(n1, end='')
    print(' - ' if c < n else ' ', end='')
    n3 = n1 + n2
    n2 = n1
    n1 = n3
    c += 1
    