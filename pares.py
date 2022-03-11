# -*- coding: utf-8 -*-
"""
Crie um programa que leia uma lista de strings separadas por vírgulas e
mostre uma lista de pares. Caso a lista possua um número ímpar de 
elementos, inclua a string vazia como segundo elemento do par final

* while: 1
* lst: 1
"""

pares = []
strings = input("lst: ").split(",")
n = len(pares)
n = len(strings)
for i in range(0, n, 2):
    if i == n - 1:
        print(x, y)
    else:
        for x, y in pares:
            pares.append([x, y])
            x = strings[i]
            y = strings[i + 1]
