nome = str(input("Qual é o seu nome? "))
print(f'Tenha um bom dia \033[31m {nome}. \033[m')
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem comum')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')

