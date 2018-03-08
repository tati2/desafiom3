palavra = input('Digite uma palavra com cinco letras: \n')
qtd_de_letras = len(palavra)

final = qtd_de_letras - 4 
'''essa variavel serve para contar quantas letras quero tirar'''

if qtd_de_letras >= 6:
	letra = palavra[0:final]
'''essa variavel divide a palavra'''
	resultado = letra + str('gato')
	print(resultado)

else:
	print('Digite uma palavra maior: ')