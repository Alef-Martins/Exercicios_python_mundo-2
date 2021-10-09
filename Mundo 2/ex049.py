#Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora usando um laço for
tabuada = int(input('Digite um número para exibir a tabuada: '))
for c in range (1, 11):
    print(f'{tabuada} x {c} = {tabuada * c}')
