#Crie um programa que faça o computador jogar jokempo com o usuário
from time import sleep
from random import randint
opçao = int(input('''Escolha a sua opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA
Sua escolha: '''))
comp = randint(1,3)
print('=-=-=-=-=-=-=-=-=-=-')
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO')
sleep(0.5)
print('=-=-=-=-=-=-=-=-=-=-')
if opçao == 1:
    if comp == 1:
        print('Jogador jogou PEDRA \nComputador jogou PEDRA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('EMPATE')
    elif comp == 2:
        print('Jogador jogou PEDRA \nComputador jogou PAPEL')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('DERROTA')
    elif comp == 3:
        print('Jogador jogou PEDRA \nComputador jogou TESOURA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('VITÓRIA')
elif opçao == 2:
    if comp == 1:
        print('Jogador jogou PAPEL \nComputador jogou PEDRA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('VITÓRIA')
    elif comp == 2:
        print('Jogador jogou PAPEL \nComputador jogou PAPEL')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('EMPATE')
    elif comp == 3:
        print('Jogador jogou PAPEL \nComputador jogou TESOURA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('DERROTA')
elif opçao == 3:
    if comp == 1:
        print('Joagdor jogou TESOURA \nComputador jogou PEDRA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('DERROTA')
    elif comp == 2:
        print('Joagdor jogou TESOURA \nComputador jogou PAPEL')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('VITÓRIA')
    elif comp == 3:
        print('Jogador jogou TESOURA \nComputador jogou TESOURA')
        print('=-=-=-=-=-=-=-=-=-=-')
        print('EMPATE')
else:
    print('Opção inválida')
        