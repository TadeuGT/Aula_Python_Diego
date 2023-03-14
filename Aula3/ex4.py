print("<Exercício 4>")
# 4 - Um anagrama é uma palavra que é feita a partir da transposição das letras de
# outra palavra ou frase. Por exemplo, “Iracema” é um anagrama de “América”.
# Escreva um programa em Python que decida se uma string é um anagrama de
# outra string, ignorando os espaços em branco. O programa deve considerar
# maiúsculas e minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.

frase1 = input("Entre com a primeira palavra: ")
frase2 = input("Entre com a segunda palavra: ")

frase1 = frase1.upper()
frase2 = frase2.upper()
f1sort = sorted(frase1)
f2sort = sorted(frase2)

# print(frase1, f1sort)
# print(frase2, f2sort)

if f1sort == f2sort:
    print(frase1, "é um anagrama de", frase2)
else:
    print(frase1, "não é um anagrama de", frase2)
