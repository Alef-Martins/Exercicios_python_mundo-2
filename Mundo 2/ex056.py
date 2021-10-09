#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
sexo = str()
idade = 0
nome = str()
media = 0
velhon = str()
velhoi = 0
mulher = 0
for p in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F] [M]: ')).strip().upper()
    media += idade / (p + 1)
    if sexo == 'M' and idade > 20:
        velhon = nome
        velhoi = idade
    if sexo == 'F' and idade < 20:
        mulher += 1
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho é o {velhon} com {velhoi} anos')
print(f'{mulher} mulheres abaixo dos 20 anos')