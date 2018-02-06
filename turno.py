turno = input('Digite M-matutino, V-vespertino ou N-noturno: ')

if turno.lower() == 'm':
	print('Bom dia!')

elif turno.lower() == 'v':
	print('Boa Tarde! ')

elif turno.lower() == 'n':
	print('Boa Noite!')

else:
	print('Valor Inválido!')
