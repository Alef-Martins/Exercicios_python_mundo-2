#Crie um programa que leia uma fraze qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = str(input('Digite um frase: ')).replace(' ', '').lower().strip()
inverter = frase[::-1]
print(frase)
print(f'A frase digitada ao contrário é: \033[31m{inverter}\033[m')
if inverter == frase:
    print('Temos um palíndromo!')
else:   
    print('Não é um palíndromo')
