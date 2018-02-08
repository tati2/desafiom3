numero1 = input('Digite seu número: \n ')
numero2 = input('Confirme seu número: \n')

while numero1 != numero2:
	print('Erro! \n Tente novamente!')
	numero1 = input('Digite seu número: \n ')
	numero2 = input('Confirme seu número: \n')

else:
	print('Recarga Completa!')
