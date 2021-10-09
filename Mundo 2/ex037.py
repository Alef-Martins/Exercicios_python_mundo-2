#Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão: 1 = binário, 2 = octal e 3 = hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
opçao = int(input('Sua opcção: '))
if opçao == 1:
    print(f'{num} convertido para BINÁRIO é igual a: {bin(num)[2:]}')
elif opçao == 2:
    print(f'{num} convertido para OCTAL é igual a: {oct(num)[2:]}')
elif opçao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a: {hex(num)[2:]}')
else:
    print('Opação inválida')
