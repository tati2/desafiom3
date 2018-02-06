a = int(input('insira um n°: '))
b = int(input('insira um n°: '))
c = int(input('insira um n°: '))

print(sorted((a, b, c), key=int, reverse=True))