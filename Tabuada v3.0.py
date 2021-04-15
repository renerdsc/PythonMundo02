while True:
    num = int(input('Digite um número para ver a tabbuada:'))
    print('-'*30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('PROGRAMA ENCERRADO. volte sempre!')
