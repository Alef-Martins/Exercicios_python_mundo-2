#'''Escreva um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de págamento:
# [1] a vista em dinheiro: 10% de desconto
# [2] A vista no cartão: 5% de desconto
# [3] Em atŕ 2x no cartão: Preço normal
# [4] 3x ou mais: 20% de juros'''
preço = float(input('Valor da compra: '))
desconto = 0
pagamento = int(input('''Escolha a forma de pagamento: \n
[1] Dinheiro
[2] A vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais\n
Opção: '''))
if pagamento == 1:
    desconto = desconto - (preço * 10 / 100)
    print(f'Você receberá um desconto de R${desconto}')
    print(f'O valor total de sua compra será de R${preço + desconto:.2f}')
elif pagamento == 2:
    desconto = desconto - (preço * 5 / 100)
    print(f'Você receberá um desconto de: R${desconto}')
    print(f'O valor toal de sua compra será de: R${preço + desconto:.2f})')
elif pagamento == 3:
    print(f'O valor da sua compra será de: R${preço:.2f}')
elif pagamento == 4:
    desconto = desconto + (preço * 20 / 100)
    print(f'Os juros da sua compra serão de: R${desconto:.2f}')
    print(f'O valor total de sua compra será de: R${preço + desconto:.2f}')
else:
    print('Opção inválida!')
