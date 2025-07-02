produto = float(input('Qual o valor do produto? R$'))
novo = produto + (produto * 30/100)
reajuste = produto - (produto * 10/100)
print('\033[1;36;40mO produto que custava R$', produto,', com aumento de 30% passou a custar R$',novo, ', mas com desconto de 10%, o valor final ficou em R$', reajuste)