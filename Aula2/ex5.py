print("<Exercício 5>")
# Crie um programa em Python que dê as opções para o usuário inserir um nome
# no fim de uma lista, em uma posição definida por ele, remover um item e
# imprimir todos os nomes da lista. Faça um menu com as opções disponíveis que
# permita que o usuário possa escolher as opções enquanto quiser e escolher uma
# opção para finalizar o programa.

lista = []
while True:
    print("Bem vindo ao seu gerenciador de lista. Escolha uma opção:")
    print("1 - Incluir novo nome")
    print("2 - Remover um nome")
    print("3 - Visualizar lista")
    print("9 - Finalizar programa")
    escolha = int(input())
    if escolha == 1:
        nome = input("Digite o nome a ser incluído: ")
        print("Onde deseja incluir o nome?\n1 - No fim da lista\n2 - Posição personalizada")
        escolhaLista = int(input())
        if escolhaLista == 1:
            lista.append(nome)
            print("Operação realizada!\n")
        else:
            pos = int(input("Qual posição deseja incluir o nome? "))
            lista.insert(pos, nome)
            print("Operação realizada!\n")
    elif escolha == 2:
        remover = input("Que nome deseja remover? ")
        lista.remove(remover)
        print("Operação realizada!\n")
    elif escolha == 3:
        print(lista)
    elif escolha == 9:
        break
