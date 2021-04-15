n = soma = 0
di = 0
menor = 0
maior = 0
while True:
    n = int(input('Dgite uma valor:'))
    if n == 999:
        break
    soma += n
    di += 1
    if n < 5:
        menor = 0
        menor += n
    if n > 10:
        maior = 0
        maior += n
print('A soma de todos os números é {}'.format(soma))
print('Foram digitado {} números'.format(di))


