print("<Exercício 1>")
# 1- Faça um programa em Python que leia o nome do usuário e o imprima na
# vertical, em forma de escada, usando apenas letras maiúsculas.
# Exemplo:
# Entrada: nome = Diego
# Resultado:
# D
# DI
# DIE
# DIEG
# DIEGO

nome = input("Qual seu nome? ")
nome = nome.upper()

for i in range(len(nome)+1):
    print(nome[0:i])
