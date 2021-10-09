#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
cont = vitorias = soma = 0
flag = bool
print('༺═─────────────═༻')
print('   Par ou ímpar')
print('༺═─────────────═༻')
while True:
    opçao = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    if opçao == 'P':
        numero1 = int(input('Digite um valor: '))
        numero2 = randint(0, 10)
        print('❢◥ ▬▬▬▬▬▬▬▬▬▬▬▬▬ ◆ ▬▬▬▬▬▬▬▬▬▬▬▬▬ ◤❢')
        print(f'Você jogou \033[34m{numero1}\033[m e o computador jogou \033[31m{numero2}\033[m')
        print('❢◥ ▬▬▬▬▬▬▬▬▬▬▬▬▬ ◆ ▬▬▬▬▬▬▬▬▬▬▬▬▬ ◤❢')
        soma = numero1 + numero2
        print(f'O total é {soma}')
        if soma % 2 != 0:
            print('Você perdeu')
            print(f'Você venceu o total de {vitorias} vezes')
            flag = False
            break
        else:
            print('Você venceu')
            vitorias += 1
            flag = True
    if opçao == 'I':
        numero1 = int(input('Digite um valor: '))
        numero2 = randint(1, 10)
        print('❢◥ ▬▬▬▬▬▬▬▬▬ ◆ ▬▬▬▬▬▬▬▬▬ ◤❢')
        print(f'Você jogou {numero1} e o computador jogou {numero2}')
        print('❢◥ ▬▬▬▬▬▬▬▬▬ ◆ ▬▬▬▬▬▬▬▬▬ ◤❢')
        soma = numero1 + numero2
        print(f'O total é {soma}')
        if soma % 2 == 0:
            print('você perdeu')
            print(f'Você venceu o total de {vitorias} vezes')
            flag = False
            break
        else:
            print('Você venceu')
            vitorias += 1
            flag = True
    if flag == False:
        print(f'Você venceu o total de {vitorias} vezes')
        break        
          