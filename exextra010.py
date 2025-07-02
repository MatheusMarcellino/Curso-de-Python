nomeH = str(input('Qual é o nome dele? '))
nomeM = str(input('Qual é o nome dela? '))
idadeH = int(input('Qual é a idade do homem? '))
print('\033[1;33mA idade do {} é de {} anos '.format(nomeH, idadeH))
idadeM = int(input('Qual é a idade da mulher? '))
print('\033[1;33mA idade da {} é de {} anos'.format(nomeM, idadeM))
if idadeH >= 65:
    print('\033[1;30;41mEle está apto a se aposentar!')
else:
    print('\033[1;30;41mEle não está apto a se aposentar!')
if idadeM >= 60:
    print('Ela está apta a se aposentar!')
else:
    print('Ela não está apta a se aposentar!')

