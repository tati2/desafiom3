usuario = input('usuario: ')
senha = input('senha:')
animal = input('animal de estimação: ')
niver = input('data de nascimento: ')

qtd_de_letras = len(senha)



if qtd_de_letras > 6:
	print(' Senha maior que 6 digitos!')
elif senha == usuario or senha == animal or senha == niver:
	print('tente novamente')
else:
	print('Senha Invalida!')