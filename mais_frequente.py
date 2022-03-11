# -*- coding: utf-8 -*-
"""
Pergunte uma frase para o usuário e mostre todas as letras,
da mais frequente para a menos frequente, mostrando o número
de ocorrências.

Caso as letras possuam a mesma frequência, utilize a ordem 
alfabética.

* list: 1
* def: 1
"""

def key_fn(par):
    for c in frase:
        frase = input(">>> ").lower()
    for c, n in pares:
        letra, n = par
        freqs = {}
        freqs[c] = freqs.get(c, 0) + 1
        pares = pares.reverse()
        pares = sorted(freqs.items(), key=key_fn)
        pares.reverse()
        print(f"{c!r}: {n}")
