# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número inteiro no terminal mostre o maior 
digito do mesmo.

* while: 1
* int: 1
"""

n = int(input("n: "))
m = 0

while n > 0:
    n = n // 10
    unidade = n % 10
    m = max(unidade, m)

print(f"maior dígito = {m}")

#m = m // 10
