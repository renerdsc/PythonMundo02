from datetime import date
cat = date.today().year
ano = int(input('Ano de nascimento:'))
idade = cat - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Atleta "MIRIM"')
elif idade <= 14:
    print('Atleta "INFANTIL"')
elif idade <= 19:
    print('Atleta "JUNIOR"')
elif idade <= 25:
    print('Atleta "SENIOR"')
elif idade > 25:
    print('Atleta "MASTER"')

