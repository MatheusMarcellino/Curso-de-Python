from time import sleep
nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual é a sua idade? '))
print('\033[1;31mVamos verificar se você pode ingerir bebida alcoólica na festa!')
print('VERIFICANDO...')
sleep(5)
if idade >= 18:
    print('\033[1;35mVocê PODE ingerir bebida alcoólica na festa!'.format(idade))
else:
    print('\033[1;35mVocê NÃO PODE ingerir bebida alcoólica na festa!'.format(idade))

