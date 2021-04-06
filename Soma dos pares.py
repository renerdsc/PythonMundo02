soma = 0
cont = 0
for i in range(1, 6, ):
    num = int(input('Digite o {} valor:'.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('voce informou {} números e a soma foi {}'.format(cont, soma))


