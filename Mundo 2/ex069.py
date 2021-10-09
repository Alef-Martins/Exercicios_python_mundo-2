#Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre: Quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos.
homens = 0
mulheres = 0
meninas = 0
maior = 0
while True:
    sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()
    idade = int(input('Qual a idade? '))
    if sexo == 'F':
        if idade <= 20:
            meninas += 1
        else:
            mulheres += 1
        if idade > 18:
            maior += 1
    elif sexo == 'M':
        homens += 1
        if idade > 18:
            maior += 1
    flag = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if flag == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {meninas}')
