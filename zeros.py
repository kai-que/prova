# -*- coding: utf-8 -*-
"""
Crie um programa que peça um número no terminal e conte a quantidade de 
zeros à esquerda do mesmo.

* while: 1
* str: 1
"""

n = 0
while number == "0":
    print(f"número de zeros = {n}")
    while number[0] == "0":
        number = input("n: ")
        n += 1
        while number.startswith("0"):
            number = number[1:]
