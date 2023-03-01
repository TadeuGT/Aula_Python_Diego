print("<Exercício 6>")
# Crie um programa em Python semelhante ao exercício 5, para que o usuário crie
# uma lista telefônica (Nome e Telefone). Permita também que o usuário
# verifique se o telefone está na lista. Utilize dicionários.

listaTelefonica = {}
while True:
    print("Bem vindo à sua lista telefônica. Escolha uma opção: ")
    print("1 - Adicionar contatos")
    print("2 - Verificar telefone")
    print("3 - Visualizar lista")
    print("9 - Encerrar programa")
    escolha = int(input())

    if escolha == 1:
        nome = input("Entre com nome do contato: ")
        tel = int(input("Entre com telefone do contato: "))
        listaTelefonica[nome] = tel
        print("Operação realizada com sucesso!\n")
    elif escolha == 2:
        numero = int(input("Entre com número de telefone: "))
        for nome, tel in listaTelefonica.items():
            if tel == numero:
                print(f"O número {numero} está associado ao contato {nome}!\n")
            else:
                print("O número não existe na lista telefônica.\n")
    elif escolha == 3:
        print(listaTelefonica)
    elif escolha == 9:
        break

