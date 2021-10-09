#'''Escreva um programa que leia o peso e altura do usuário, calcule seu índice de massa corporal (IMC) e mostre o resultado de acordo com a tabela: 
# Abaixo de 18,5 = Abaixo do peso
# Entre 18,5 e 25 = Peso ideal
# 25 até 30 = Sobrepeso
# 30 até 40 = Obesidade
# Acima de 40 = Obesidade mórbida'''
peso = float(input('Informe o peso: Kg '))
altura = float(input('Informe a altura: m '))
imc = peso / (altura**2)
print(f'seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <=imc < 25:
    print('Você está na faixa de peso ideal')
elif 25 <= imc < 30:
    print('Você está acima do peso')
elif 30 <= imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')
