from math import sin, cos, tan, radians

print("<Exercício 3>")
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo. Utiliza a biblioteca math, importando apenas
# os itens que serão necessários dessa biblioteca. (Em caso de dúvidas do
# funcionamento das funções utilizadas, pesquise sua documentação no site
# oficial).

angulo = float(input("Insira o ângulo: "))
anguloRad = radians(angulo)

print("Valor do seno:", sin(anguloRad))
print("Valor do cosseno", cos(anguloRad))
print("Valor da tangente", tan(anguloRad))
