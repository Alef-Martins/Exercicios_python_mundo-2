#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o valor solicitado for 0
while True:
    cont = 1
    numero = int(input('Digite um número para exibir a tabuada: '))
    print('==='*10)
    if numero == 0:
        break
    while True:
        print(f'{numero} x {cont} = {numero * cont}')
        cont += 1
        if cont >= 11:
            break
