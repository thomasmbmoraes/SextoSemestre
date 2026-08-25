# FUNDAMENTOS DA PROGRAMAÇÃO EM PYTHON

#exemplo de indexação e fatiamento de strings
s = "João da Silva"
print(s[0])
print(s[1])
print(s[:4])
print(s[5:7])

#exemplo de entrada de dados e formatação de saída
num1 = float(input("Informe o primero número: "))
num2 = float(input("Informe o segundo número: "))
soma = num1 + num2

print("Soma = %.2f" % soma)

print("{0} + {1} = {2}".format(num1,num2,soma))

#exemplo de laços de repetição
nome ="João da Silva"

for letra in nome:
    print(letra)

for i in range(5):
    print(i)

for i in range(5,10,2):
    print(i)

soma = 0
for i in range(10):
    soma = soma + i
else:
    print("Soma = %d" %soma)
