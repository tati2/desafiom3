#crie um programa que sorteia um valor entre 1 e 20

import random 

numero_sorteado = random.randint(1, 20)

total_de_tentativas = 0

while total_de_tentativas <3:

	print('Digite um numero: ')

	tentativa = int(input())

	total_de_tentativas = total_de_tentativas +1

	if tentativa > numero_sorteado:
		print('Digite um número menor: ')
		break

	else:
		print('Digite um número maior: ')

if tentativa == numero_sorteado:
	print('Você acertou!!')

else:
	print('Você errou!' + 'o número sorteado foi: ' + str(numero_sorteado))
	
