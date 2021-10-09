#Crie uma programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Informe o peso: '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O maior peso digitado foi {maior}')
print(f'O menor peso digitado foi {menor}')
