print("<Exercício 1>")
# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da
# hipotenusa. (Não utilize nenhuma biblioteca para a realização desse código).
# Fórmula do cálculo da hipotenusa:
# hi = √co2 + ca2

catetoOpt = float(input("Informe cateto oposto: "))
catetoAdj = float(input("Informe cateto adjacente: "))

hipotenusa = (catetoOpt**2 + catetoAdj**2)**0.5

print("Valor da hipotenusa: ", hipotenusa)
