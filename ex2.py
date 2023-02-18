print("<Exercício 2>")
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.
#
# Entrada
# Digite Algo: FHO O tipo primitivo desse valor é: <class 'str'>
#
# Saída
# Só tem espaços? False
# É um número? False
# É alfabético? True
# É alfanumérico? True
# Está em maiúsculas? True
# Está em minúsculas? False
# Está capitalizada? False

entrada = input("Digite algo: ")

print("O tipo primitivo desse valor é:", type(entrada))
print("Só tem espaços?", entrada.isspace())
print("É um número?", entrada.isnumeric())
print("É alfabético?", entrada.isalpha())
print("É alfanumérico?", entrada.isalnum())
print("Está em maiúsculas?", entrada.isupper())
print("Está em minúsculas?", entrada.islower())
print("Está capitalizada?", entrada.istitle())
