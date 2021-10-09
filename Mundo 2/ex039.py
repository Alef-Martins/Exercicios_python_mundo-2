#Faça um programa que leia o ano de nascimento do usuário e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou da hora. O programa também deverá mostrar o tempo que falta ou quanto tempo se passou do prazo.
from datetime import date
sexo = int(input('Sexo: \n[1] Masculino \n[2] Feminino\n:'))
nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
if sexo == 1:
    if idade < 18:
        print(f'Faltam {18 - idade} ano(s) para você se alistar.\nSeu alistamento será no ano de {18 - idade + ano_atual}')
    elif idade > 18:
        print(f'Seu alistamento está atrasado em {idade - 18} ano(s)\nSeu alistamento deveria ter sido feito no ano de {ano_atual - (idade - 18)}')
    else:
        print('''Você tem 18 anos completos \nVocê deve se alistar ainda esse ano!''')
else:
    print('O alistamento para o sexo feminino não é obrigatório')
