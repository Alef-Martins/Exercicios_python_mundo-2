#'''Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais'''
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
if valor1 > valor2:
    print('O \033[31mprimeiro\033[m valor é maior')
elif valor2 > valor1:
    print('O \033[31msegundo\033[m valor é maior')
else:
    print('\033[33mOs dois valores são iguais')
