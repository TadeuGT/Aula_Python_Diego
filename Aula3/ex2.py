from datetime import datetime
import locale

print("<Exercício 2>")
# 2 - Faça um programa em Python que leia uma data de nascimento no formato
# dd/mm/aaaa e imprima a data com o mês escrito por extenso.
# Exemplo:
# Entrada: data = 13/09/1989
# Resultado: Você nasceu em 13 de setembro de 1989

nascimento = input("Entre com sua data de nascimento no formato dd/mm/aaaa: ")

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
data = datetime.strptime(nascimento, "%d/%m/%Y")
mesNome = data.strftime('%B')

print(f"Você nasceu em {data.day} de {mesNome} de {data.year}")
