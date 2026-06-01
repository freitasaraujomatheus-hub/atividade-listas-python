# -*- coding: utf-8 -*-

frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]

print("Listas iniciais:")
print(f"Frutas: {frutas}")
print(f"Numeros: {numeros}")


primeira_fruta_sem_negativo = frutas[0]
ultima_fruta_sem_negativo = frutas[len(frutas) - 1]
print(f"Primeira fruta (sem índice negativo): {primeira_fruta_sem_negativo}")
print(f"Última fruta (sem índice negativo): {ultima_fruta_sem_negativo}")


primeira_fruta_com_negativo = frutas[0]
ultima_fruta_com_negativo = frutas[-1]
print(f"Primeira fruta (com índice negativo): {primeira_fruta_com_negativo}")
print(f"Última fruta (com índice negativo): {ultima_fruta_com_negativo}")

frutas.append('morango')
frutas.insert(2, 'kiwi')

print(f"Lista de frutas após adição e inserção: {frutas}")

frutas.remove('banana')

print(f"Lista de frutas após remover 'banana': {frutas}")

print("Números maiores que 15 na lista 'numeros':")
for numero in numeros:
    if numero > 15:
        print(numero)

numeros_crescente = sorted(numeros)
numeros_decrescente = sorted(numeros, reverse=True)

print(f"Lista 'numeros' original: {numeros}")
print(f"Lista 'numeros' em ordem crescente: {numeros_crescente}")
print(f"Lista 'numeros' em ordem decrescente: {numeros_decrescente}")
