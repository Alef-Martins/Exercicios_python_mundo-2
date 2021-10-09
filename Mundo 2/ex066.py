#Reescreva o exercpicio 64 desconsiderando o flag.
soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    quantidade += 1
    soma += numero
print(f'Foram digitados {quantidade} números, a soma entre eles é {soma}')