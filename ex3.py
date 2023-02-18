print("<Exercício 3>")
# Crie uma agenda eletrônica capaz de realizar a leitura dos dados de uma
# pessoa física (Nome completo, RG, CPF, celular, e-mail). Para cada dado, exiba
# uma frase autoexplicativa no console. Após realizar a leitura dos dados, imprima
# todos no console, logo após, peça ao usuário que confirme a ação, digitando
# SIM ou NÃO.

while True:
    nome = input("Inclua seu nome: ")
    RG = input("Inclua seu RG: ")
    CPF = input("Inclua seu CPF: ")
    cel = input("Inclua seu celular: ")
    email = input("Inclua seu e-mail: ")
    confirma = input("Confirmar criação de conta? SIM/NAO: ")
    if confirma == "SIM":
        print("Conta registrada com sucesso!")
        break
    else:
        print("Operação Cancelada")
        break
