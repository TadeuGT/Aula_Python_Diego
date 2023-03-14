def calculador(ma1: float, mb1: float, p1: float, ma2: float, mb2: float, p2: float):
    a1 = 0.7*p1 + 0.1*ma1 + 0.2*mb1
    a2 = 0.7*p2 + 0.1*ma2 + 0.2*mb2
    final = (a1 + (2*a2))/3
    return final


print("<Exercício 6>")
# 6- Faça uma nova versão do exercício 5 que permita que o usuário escolha a
# opção de escrever os nomes e notas de alunos no arquivo “notas.txt” (esse
# arquivo possui a mesma estrutura do arquivo do exercício 5). O usuário também
# deve ter a opção de realizar os cálculos das médias conforme regras do exercício 5.


while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar dados")
    print("2 - Calcular médias")
    print("9 - Encerrar programa")
    escolha = input()

    if escolha == "1":
        arquivo = open('notas.txt', 'a')
        print("Escreva os dados que deseja adicionar. Respeite o formato:")
        print("Nome do Aluno, Ma1, Mb1, P1, Ma2, Mb2, P2")
        entrada = input()
        arquivo.write("\n" + entrada)

    elif escolha == "2":
        arquivo = open('notas.txt', 'r')
        conteudo = arquivo.readlines()
        notas = []

        for linha in conteudo:
            valor = linha.strip().split(',')
            notas.append(valor)
        arquivo.close()

        for nota in notas:
            media = calculador(float(nota[1]), float(nota[2]), float(nota[3]), float(nota[4]), float(nota[5]),
                               float(nota[6]))
            print(nota[0], "obteve média {:.2f}".format(media))
    elif escolha == "9":
        break
    else:
        print("Opção inválida.")
