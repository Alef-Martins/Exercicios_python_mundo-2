#'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
# Até 9 anos = MIRIM
# Até 14 anos = INFANTIL
# Até 19 anos = JUNIOR
# Até 25 anos = SÊNIOR
# Acima de 25 = MASTER '''
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Categoria \033[31mMIRIM\033[m')
elif idade > 9 and idade <= 14:
    print('Categoria \033[31mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Categoria \033[31mJÚNIOR\033[m')
elif idade > 19 and idade <= 25:
    print('Categoria \033[31mSÊNIOR\033[m')
elif idade > 25:
    print('Categoria \033[31mMASTER\033[m')
