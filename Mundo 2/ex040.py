#'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida.
# Média abaixo de 5.0 = REPROVADO
# Média entre 5.0 e 6.9 = RECUPERAÇÃO
# Media 7.0 ou superior = APROVADO'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi de {media} \nREPROVADO!')
elif media <= 6.9:
    print(f'Sua média foi de {media} \nRECUPERAÇÂO!')
elif media >= 7.0:
    print(f'Sua média foi de {media} \nAPROVADO!')

