# -*- coding: utf-8 -*-
"""
Crie um programa que mostre a quantidade de dígitos que a soma de dois números 
inteiros possui 

* int: 1
"""

a = int(input("a: "))
b = int(input("b: "))
c = a + b
c = a + b
n = 0
div = 10
div = 2
n += 1
n += div
print(f"número de dígitos = {n}")
while c:
    c = c % div
    c = c // div
    print(f"soma = {c}")
