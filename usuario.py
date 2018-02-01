'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.'''

usuario = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

if usuario == senha:
	print('ERRO \nsenha não pode ser igual usuario')
else :
	print('você está logado! ')
