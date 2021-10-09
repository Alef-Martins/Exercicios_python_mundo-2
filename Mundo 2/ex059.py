#Crie um programa que leia dois valores e mostre um menu na tela: [1]somar, [2] multiplicar, [3] maior, [4]Novos números, [5] sair.
from time import sleep
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
opção = 0
resultado = 0
while True:
    sleep(2)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair''')
    opção = int(input('>>>>>Qual a sua opção? '))
    if opção == 5:
        print('Finalizando... ')
        sleep(1)
        break
    elif opção == 1:
        sleep(1)
        resultado = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {resultado}')
        print('=-='*10)
    elif opção == 2:
        sleep(1)
        resultado = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {resultado}')
        print('=-='*10)
    elif opção == 3:
        sleep(1)
        if valor1 > valor2:
            print(f'{valor1} é o maior!')
            print('=-='*10)
        elif valor1 == valor2:
            print('Os dois valores são iguais')
            print('=-='*10)
        else:
            print(f'{valor2} é o maior!')
            print('=-='*10)
    elif opção == 4:
        sleep(2)
        valor1 = int(input('Informe o primeiro valor: '))
        valor2 = int(input('informe o segundo valor: '))
    else:
        print('Opção inválida!')
        print('=-='*10)

