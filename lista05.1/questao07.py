"""Desenvolver um programa que apresente todos os números divisíveis por 4 que sejam menores que 200. Para
saber se o número é divisível por 4 será necessário verificar a lógica desta condição com o comando if. Sendo
divisível, mostre-o; não sendo, passe para o próximo passo. A variável que controla o cont deve ser iniciada
com valor 1."""

n = int(input("Informe um número: "))
if (n %3 ):
    while (n < 200):
        print(n)
        n = n * 4


else:
    print(f"{n} é invalido!")