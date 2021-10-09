#Desenvolva um programa que leia o primeiro termo e razão de uma PA. No final mostre os 10 primeiros termos.
print('=='*10)
print('10 termos de uma PA')
print('=='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range (1, 11):
    print(termo)
    termo += razao