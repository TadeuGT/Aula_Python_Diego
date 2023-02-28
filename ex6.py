print("<Exercício 6>")
# A cidade A possui 90.000 habitantes e a cidade B 50.000. A população da
# cidade A cresce 0,9 % ao ano enquanto que a da cidade B cresce 1,5% ao ano.
# Faça um programa que leia o número de anos e calcule qual será o número da
# população de cada cidade. O programa deve verificar se o tamanho da cidade A
# é maior que a cidade B, ou se o tamanho da cidade B é maior que a cidade A.

anos = int(input("Número de anos: "))

popA = 90000
popB = 50000

for i in range(anos):
    popA += popA * 0.009
    popB += popB * 0.015

print("Tamanho da cidade A:", int(popA))
print("Tamanho da cidade B:", int(popB))

if popA > popB:
    print("Daqui", anos, "anos a cidade A continuará maior que a cidade B!")
else:
    print("Daqui", anos, "anos a cidade B será maior que a cidade A!")
