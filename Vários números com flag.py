n = soma = 0
di = 0
while True:
    n = int(input('Dgite uma valor:'))
    if n == 999:
        break
    soma += n
    di += 1
print('A soma de todos os números é {}'.format(soma))
print('Foram digitado {} números'.format(di))


