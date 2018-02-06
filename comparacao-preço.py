'''
faça um programa que pergunte o preço de tres produtos e diga qual dos tres é o mais barato
'''
bala = float(input('Quanto é uma bala? '))
pirulito = float(input('Quanto é um pirulito? '))
goiabinha = float(input('Quanto é uma goiabinha? '))

barato = min(bala, pirulito, goiabinha)

print('O doce mais barato custa R$%.2f' % barato  )