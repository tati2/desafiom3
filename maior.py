x = input('Digite um número: ')
y = input('Digite um número:')
z = input('Digite um número:')

def maior():
	if x > y and x > z:
		print(x)
	elif y > x and y > z:
		print(y) 
	else:
		print(z)
def menor():
	if x < y and x < z:
		print(x)
	elif y < x and y < z:
		print(y)
	else:
		print(z)

maior()
menor()