palavra = input('Digite uma palavra com cinco letras: \n')
qtd_de_letras = len(palavra)

if qtd_de_letras > 5:
	print('Digite novamente: \n')
	letra = palavra[0:2]
	resultado = letra + str('gato')
	print(resultado)

else:
	print('Sua palavra não tem a quantidade sulficiente.')