#Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número entre 1 e 10. Só que agora o jogador vai tentar até acertar, mostrando no final quantos palpites foram nescessários para vencer.
from random import randint
numero = randint(0, 10)
tentativas = 1
resposta = int
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
while resposta != numero:
    resposta = int(input('Qual é o seu palpite? '))
    if resposta > numero:
        print('Menos... Tente  outra vez')
        tentativas += 1
    elif resposta < numero:
        print('Mais... Tente outra vez')
        tentativas += 1
    else:
        print(f'Você acertou com {tentativas} tentativas, parabéns')
