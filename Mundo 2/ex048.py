#Crie um programa que some todos os números múltiplos de 3 no intervalo de 1 a 500
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(soma)