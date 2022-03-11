# -*- coding: utf-8 -*-
"""
Crie um programa que leia um número n e retorne a sequência de Fizz-Buzz até este número.

A sequência Fizz-Buzz é feita imprimindo cada número natural, mas trocando os múltiplos 
de 3 por "fizz", os múltiplos de 5 por "buzz" e os múltiplos de ambos por "fizzbuzz".

* for: 1
* if: 1
"""

n = int(input(("n: ")))
for i in range(n):
    if n <= 0:
        print(i)
else:
        print("número inválido")

for i in range(n + 1):
        print("fizzbuzz")
   
for i in range(1, n + 1):
        print("fizz")
