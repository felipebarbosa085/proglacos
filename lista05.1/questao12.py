"""Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menorr número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menorr, e nem na contagem da média"""


maior = float('-inf')
menor = float('inf')
soma = 0
quantidade = 0

numero = float(input("Digite um número: (-1 para encerrar):"))

while numero != -1:

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

    soma += numero
    quantidade += 1

    numero = float(input("Digite um número: (-1 para encerrar):"))

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
print(f"A média dos números digitados é: {media:.2f}")
