num1 = float(input("Digite um número:"))
num2 = float(input("Digite outro número:"))
operação =  str(input("Escolha uma operação: '+', '-', '*', '/': "))
if operação == '+':
        resultado = num1 + num2
elif operação == '-':
        resultado = num1 - num2
elif operação == '*':
        resultado = num1 * num2
elif operação == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão inválida!"
else:
        resultado = "Operação inválida!"
print("Resultado", resultado)



