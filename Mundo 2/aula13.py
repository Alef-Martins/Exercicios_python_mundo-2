from time import sleep
i = int(input('Início'))
f = int(input('Fim:'))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
    sleep(1)
print('fim')