# -*- coding: utf-8 -*-

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(f"Lista original: {letras}")

primeiros_4 = letras[:4]
print(f"Os 4 primeiros elementos: {primeiros_4}")

do_3o_ao_7o = letras[2:7]
print(f"Do 3º ao 7º elemento: {do_3o_ao_7o}")

ultimos_3 = letras[-3:]
print(f"Os 3 últimos elementos: {ultimos_3}")

lista_invertida = letras[::-1]
print(f"Lista invertida: {lista_invertida}")

elementos_pares = letras[::2]
print(f"Elementos de índice par: {elementos_pares}")
