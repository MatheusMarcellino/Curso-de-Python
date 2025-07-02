aluno = str(input('Qual o nome do aluno?'))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('\033[0;33mA media do aluno(a) foi de {}'.format(media))
if media >= 6:
    print('\033[1;35mAluno(a) {} teve uma boa média. Foi APROVADO(A)!'.format(aluno, media))
else:
    print('\033[1;35mAluno(a) {} não teve uma boa média. Foi REPROVADO(A)!'.format(aluno, media))