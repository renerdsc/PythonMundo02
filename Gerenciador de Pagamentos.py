print('{:=^40}'.format('LOJASRENER.COM.BR'))
compra = float(input('Preço das compras R$ '))
print(''''
Formas de pagamento
[1] ávista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = compra - (compra * 10 / 100) #desconto, total da compra multiplicado por 10% é dividido por 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, total))
elif opção == 2:
    total = compra - (compra * 5 / 100) # desconto, total da compra multiplicado por 5% é dividido por 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra, total))
elif opção == 3:
    total = compra
    parcela = total / 2 # parcela o total da compra dividido por 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = compra + (compra * 20 / 100) # total da compra parcelado + que 3x no cartão é acrescentado 20% de juros
    totalparcela = int(input('Quantas parcelas?'))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcela, parcela))
else:
    total = 0
    total = compra
    print('OPÇÃO INVÁLIDA  de pagamento. Tente novamente!') # se digitado opção inexistente erro opção inválida
