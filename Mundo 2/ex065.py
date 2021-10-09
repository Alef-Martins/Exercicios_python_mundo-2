#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor número lido. O programa deve perguntar se o usuário quer o não continuar a digitar os valores.
numero = int(input('Digite um número: '))
quantidade = 1
maior = menor = numero
media = numero
while True:
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
    numero = int(input('Digite um número: '))
    quantidade += 1
    media += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
media /= quantidade
print(f'Você digitou {quantidade} números, a média entre eles é {media}, o maior valor digitado foi {maior} e o menor foi {menor}')
