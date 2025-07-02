número = int(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1
for i in range (1, número + 1):
        fatorial *= i
print("O fatorial de determinado número é:" , fatorial)