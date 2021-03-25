peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)
if imc < 18.4:
    print('Abaixo do peso') #Abaixo do Peso
elif imc > 18.5 and imc < 24.9:
    print('Peso Normal') #Peso ideal
elif imc > 25 and imc < 29.9:
    print('Sobrepeso') #Levemente acima do Peso
elif imc > 30 and imc < 39.9:
    print('Obesidade') #Obesidade
elif imc > 40:
    print('Obesidade Mórbida') #Mórbida
