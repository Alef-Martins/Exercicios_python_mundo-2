#Refaça o exercício 51, lendo o primeiro termo e a razão de um PA mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Progressão aritimética')
print('=-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(f'{termo} ', end='')
    print('- ' if c < 10 else '', end='')
    termo += razao
    c += 1
    
