from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjcente: '))
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))