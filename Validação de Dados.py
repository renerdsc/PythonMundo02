sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo= str(input('Erro opção inválida. tente novamente:')).strip().upper()[0]
print('Sexo {} registrado com sucesso:'.format(sexo))