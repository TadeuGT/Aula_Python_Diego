print("<Exercício 4 (2)>")
# Suponha que você desenvolverá um sistema para gerenciar suas notas. Seu
# programa deve conter variáveis para guardar RA, notas N1 e N2, e média. Deve
# ser capaz de realizar a leitura desses valores via teclado e, após isso, você deve
# fazer as conversões necessárias dos tipos de dados. Imprima os valores finais no
# console.w

ra = input("Insira RA: ")
n1 = input("Insira Nota 1: ")
n2 = input("Insira Nota 2: ")
media = (float(n1)+float(n2))/2

print("-------------\nAluno RA", ra)
print("Nota 1:", n1)
print("Nota 2:", n2)
print("Media:", media)
