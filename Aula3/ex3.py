print("<Exercício 3>")
# 3 -Faça um programa em Python que recebe uma string que representa uma
# cadeia de DNA e gera a cadeia complementar.
# Exemplo:
# Entrada: AATCTGCAC
# Saída:   TTAGACGTG

complemento = {'A': 'T',
               'T': 'A',
               'C': 'G',
               'G': 'C'}

cadeiaDNA = input("Entre com a cadeia de DNA: ")
cadeiaComp = ""

for base in cadeiaDNA:
    cadeiaComp += complemento[base]

print("Cadeia complementar:", cadeiaComp)
