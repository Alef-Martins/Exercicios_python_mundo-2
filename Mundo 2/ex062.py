#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerará quando o usuário disser que quer mostrar 0 itens.
print('╔════════════•ೋೋ•═══════════╗ ')
print(' Progressão aritimética v3.0')
print('╚════════════•ೋೋ•═══════════╝')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(termo, end='')
        print(' - ' if c < 10 else ' ', end='')
        termo += razao
        c += 1
    mais = int(input('\nQuantos termos deseja adicionar? '))
print(f'Foram mostrados {total} termos no total')
