from math import sqrt as raiz

print("<Exercício 2>")
# Refaça o exercício 1 utilizando a biblioteca math. Importe somente os itens
# necessários dessa biblioteca.

catetoOpt = float(input("Informe cateto oposto: "))
catetoAdj = float(input("Informe cateto adjacente: "))

hipotenusa = raiz(catetoOpt**2 + catetoAdj**2)

print("Valor da hipotenusa: ", hipotenusa)
