#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exeder 30% do salário do comprador ou o empréstimo será negado.
valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
anos = int(input('Em quantos anos deseja pagar? '))
prestaçao = valor / anos / 12
if prestaçao <= salario * 30 / 100:
    print(f'Empréstimo aprovado! \nO valor das parcelas será de: {prestaçao:.2f}')
else:
    print('Empréstimo negado! \nO valor das parcela é maior que 30% do salário informado')
print(f'{prestaçao:.2f}')
