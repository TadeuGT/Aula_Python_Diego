from random import choice as aleatoriezar

print("<Exercício 4>")
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
# um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o
# nome do escolhido.

qtdAlunos = int(input("Insira quantidade de alunos: "))
alunos = []

for i in range(qtdAlunos):
    nome = input(f"Insira nome do aluno {i}: ")
    alunos.append(nome)

print("SORTEIO: O aluno", aleatoriezar(alunos), "vai apagar o quadro hoje.")
