a = int(input('Qual é a altura do triângulo? '))
b = int(input('Qual é a base do triângulo? '))
area = (b * a) / 2
print('\033[1;34;40mA área do triângulo é',area)
print('---')
a = int(input('Qual é a altura do retângulo? '))
b = int(input('Qual é a base do retângulo? '))
area = (b * a)
print('\033[4;31;40mA área do retângulo é', area)
print('---')
l = int(input('Qual é o comprimento do lado do quadrado?' ))
area = l * l
print('\033[0;35;47mA área do quadrado é', area)