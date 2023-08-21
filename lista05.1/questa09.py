"""Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2"""

soma = 0

num = 0

while num <= 500:

    if num % 2 == 0:
        soma += num

    num += 2

print("A soma dos valores pares é:", soma)
