#Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
valor = int(input('Qual o valor do saque? R$\033[32m'))
total = valor
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        if cedula == 20:
            cedula == 10
        if cedula == 10:
            cedula = 1
        if total == 0:
            break

