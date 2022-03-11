# -*- coding: utf-8 -*-
"""
Crie um programa que mostre uma lista com todos os primos de 1 até n, onde
n é um valor fornecido pelo usuário.

O exercício possui algumas dicas de implementação na forma de comentários.

* for: 2
"""

# Acrescentamos os novos primos a lista de primos.
# Assumimos que o numero e primo e tentamos encontrar o divisor.
# Um numero nao pode ser primo se for divisivel por outro primo.
import math


N = int(input("N: "))
A = list(range(2, N))
for i in range(2, int(math.sqrt(N)+1)):
  if i in A:
    for j in range(i**2, N, i):
      if j in A: A.remove(j)
print(A)
