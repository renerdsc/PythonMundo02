'''cont = 1
while cont <= 10:
    print(cont, '>', end='')
    cont += 1
print('ACABOU')'''
#######################
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 9999:
        break
    s += n
print('A soma vale {}'.format(s))
######################
'''nome = 'jose'
idade = 28
salario = 1152.40
print(f'O {nome:<5} tem {idade} anos e ganha {salario:.2f} ')
print('O {} tem {} anos e ganha {:.2f}'.format(nome, idade, salario))'''
