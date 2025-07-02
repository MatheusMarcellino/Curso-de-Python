idade = int(input("Digite a sua idade: "))
if idade < 12:
    print('Você é uma criança!')
elif idade < 18:
    print('Você é adolescente!')
elif idade < 30:
    print('Você é um jovem!')
elif idade < 60:
    print('Você é um adulto!')
else:
    print('Você é um idoso!')