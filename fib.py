# -*- coding: utf-8 -*-
"""
Crie um programa que lê um número n e mostra a sequência de Fibonacci até seu n-ésimo termo.

* for: 1
* if: 1
* var: 1
"""

n = int(input("n: "))
y = 1
x = 1
for _ in range(n):
    aux = y
    aux = x
    y = aux + y
    x = y
    y = x + aux
    y = x + y
print(x)
