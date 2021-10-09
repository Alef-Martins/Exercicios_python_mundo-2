#Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final mostre: 1-Qual o gasto total, 2- Quantos produtos custam mais de R$1000, 3- Qual o produto mais barato.
total = caro = 0
produto_barato = 'str'
barato = cont = 0
while True:
    produto = str(input('\033[mNome do produto:\033[32m '))
    preço = float(input('\033[mPreço:\033[32m '))
    flag = str(input('\033[mQuer continuar? [S/N]\033[32m ')).strip().upper()[0]
    total += preço
    cont +=1
    if cont == 1:
        barato = preço
    else:
        if preço < barato:
            barato = preço
            produto_barato = produto
    if preço > 1000:
        caro += 1
    if flag == 'N':
        break
print('\033[m')
print(f'O total da compra foi de: R${total:.2f}')
print(f'Temos {caro} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${barato:.2f}')