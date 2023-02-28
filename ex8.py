print("<Exercício 8>")
# Escreva um programa que solicite ao usuário que entre com as médias de todos
# os alunos da sala e para cada aluno imprime se o mesmo está aprovado (>=5),
# reprovado (< 3) ou recuperação (>=3 e <5). O código deve ser encerrado quando
# o usuário digitar uma média negativa.

media = 0

while 0 <= media <= 10:
    media = float(input("Insira a média de aluno: "))

    if media >= 5:
        print("Aprovado!")
    elif media < 3:
        print("Reprovado!")
    else:
        print("Recuperação!")

