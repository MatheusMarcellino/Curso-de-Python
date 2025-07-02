print('\033[1;31;40mDois números de 1 a 50 são escolhidos de uma rifa! ')
print('Qual a probabilidade desses números escolhidos serem ímpares e primos? ')
p = 50 / 14
print('\033[1;35;40mA probabilidade dos números escolhidos serem ímpares e primos é {:.2f}'.format(p))
from random import choice
lista = 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
escolhidos = choice(lista)
print('\033[1;33;47mUm dos números escolhidos é {}'.format(escolhidos))




