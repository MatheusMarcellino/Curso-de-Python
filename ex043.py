peso = int(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO do peso NORMAL!')
elif imc  < 25:
    print('Parabéns! Você está com o peso NORMAL!')
elif imc < 30:
    print('Você está com SOBREPESO!')
elif imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA. Cuidado!')