# Exercício 3
# Faça uma aplicação que apresente em tela a tabuada de qualquer número.
# O usuário fornece o número desejado e a aplicação apresenta a relação de todos os cálculos de 1 a 10. 
 
num1 = float(input("Informe o numero para a tabuada: "))
for i in range(1,11):
    print("%d x %d = %d" %(num1,i,num1*i))