import math

print("<Exercício 4>")
# Crie um programa que leia dois valores inteiros do teclado e escreva na tela:
# a. O dobro do primeiro número
# b. A multiplicação entre o primeiro e o segundo número
# c. O resto da divisão entre o primeiro e o segundo número;
# d. A divisão inteira entre o primeiro e o segundo número;
# e. A potência entre o primeiro e o segundo número;
# f. A raiz quadrada do segundo número;


valor1 = input("Registre o primeiro valor: ")
valor2 = input("Registre o segundo valor: ")

valor1 = float(valor1)
valor2 = float(valor2)

print("Dobro do primeiro número: ", valor1 * 2)
print("Multiplicação entre o primeiro e o segundo número: ", valor1 * valor2)
print("Resto da divisão entre o primeiro e o segundo número: ", valor1 % valor2)
print("Divisão inteira entre o primeiro e o segundo número: ", valor1 // valor2)
print("Potência entre o primeiro e o segundo número: ", valor1 ** valor2)
print("Raiz quadrada do segundo número: ", math.sqrt(valor1))
