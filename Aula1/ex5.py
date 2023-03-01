print("<Exercício 5>")
# Uma livraria está fazendo uma promoção para pagamento à vista em que o
# comprador pode escolher entre dois critérios de desconto:
# Critério A: R$ 0,25 por livro + R$ 7,50
# Critério B: R$ 0,50 por livro + R$ 2,50
# Faça um programa em que o usuário digita a quantidade de livros que deseja
# comprar e o programa calcula qual seria o valor do pagamento em ambos
# critérios. O programa deve afirma quais dos critérios é maior vantajoso.

qtdLivros = float(input("Quantos livros você deseja comprar? "))

valA = (qtdLivros*0.25) + 7.50
valB = (qtdLivros*0.50) + 2.50

print("Valor do critério A:", valA)
print("Valor do critério B:", valB)
if valA > valB:
    print("O critério B é o mais vantajoso para a sua compra. Você pagará", (valA - valB), "reais a menos!")
elif valB < valA:
    print("O critério A é o mais vantojoso para a sua compra. Você pagará", (valB - valA), "reais a menos!")
else:
    print("O preço da sua compra será o mesmo em ambos os critérios!")
