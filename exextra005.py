from random import choice
escola = str(input('Qual o nome da escola? '))
qtd = int(input('Quantos professores há na escola?'))
print('\033[0;35;40mO nome da escola é {}'.format(escola))
prof1 = str(input('Qual o nome do primeiro professor? '))
prof2 = str(input('Qual o nome do segundo professor? '))
prof3 = str(input('Qual o nome do terceiro professor? '))
prof4 = str(input('Qual onome do quarto professor? '))
profs = [prof1, prof2, prof3, prof4]
sorteado = choice(profs)
print('\033[0;33mO nome do professor(a) que irá trabalhar aos sábados desse mês será {}'.format(sorteado))








