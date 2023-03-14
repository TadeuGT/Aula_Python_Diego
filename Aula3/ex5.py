def calculador(ma1: float, mb1: float, p1: float, ma2: float, mb2: float, p2: float):
    a1 = 0.7*p1 + 0.1*ma1 + 0.2*mb1
    a2 = 0.7*p2 + 0.1*ma2 + 0.2*mb2
    final = (a1 + (2*a2))/3
    return final


print("<Exercício 5>")
# 5 - Crie um arquivo chamado “notas.txt” que contenha os nomes de alunos, e 6
# notas (Ma1, Mb1, P1, Ma2, Mb2 e P2), com todos os dados separados por ‘,’ (vírgula).
# Posteriormente, escreva um programa em Python que faça a leitura desse arquivo e
# exiba na tela o nome do aluno e a média final, calculada a partir da fórmula a seguir:
# Nota final = (A1 + (2 x A2) ) / 3
# em que:
# A1 = 70% por uma prova individual (P1), 10% por avaliação continuada (Ma1)
# e 20% Atividade em grupo (Mb1).
# A2 = 70% por uma prova individual (P2), 10% por avaliação continuada (Ma2)
# e 20% Atividade em grupo (Mb2).

arquivo = open('notas.txt')
conteudo = arquivo.readlines()
notas = []

for linha in conteudo:
    valor = linha.strip().split(',')
    notas.append(valor)
arquivo.close()

for nota in notas:
    media = calculador(float(nota[1]), float(nota[2]), float(nota[3]), float(nota[4]), float(nota[5]), float(nota[6]))
    print(nota[0], "obteve média {:.2f}".format(media))
