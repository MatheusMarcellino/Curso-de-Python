from random import choice
m1 = str(input('Qual o nome da sua primeira banda favorita? '))
m2 = str(input('Qual o nome da sua segunda banda favorita? '))
m3 = str(input('Qual o nome da sua terceira banda favorita? '))
m4 = str(input('Qual o nome da sua quarta banda favorita? '))
lista = [m1, m2, m3, m4]
choice(lista)
print('\033[1;33mO nome das minhas bandas favoritas são: ')
print(lista)


