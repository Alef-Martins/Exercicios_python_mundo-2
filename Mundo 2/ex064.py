#Crie um programa que leia vários valores inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
numero = int(input('Informe um número [999 para parar]: '))
quantidade = 0
soma = 0
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input('Informe um número [999 para parar]: '))
print(f'Foram digitados {quantidade} números e a soma entre eles é: {soma}')