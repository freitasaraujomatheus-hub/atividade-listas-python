# -*- coding: utf-8 -*-
palavras = ['python', 'lista', 'programação', 'código', 'loop', 'função']
numeros = list(range(1, 21)) # 1 até 20

quadrados_1_a_10 = [x**2 for x in range(1, 11)]
print(f"1. Quadrados de 1 a 10: {quadrados_1_a_10}")

numeros_pares = [num for num in numeros if num % 2 == 0]
print(f"2. Números pares: {numeros_pares}")

comprimento_palavras = [len(palavra) for palavra in palavras]
print(f"3. Comprimento das palavras: {comprimento_palavras}")

palavras_mais_de_5_maiusculas = [palavra.upper() for palavra in palavras if len(palavra) > 5]
print(f"4. Palavras com mais de 5 letras (maiúsculas): {palavras_mais_de_5_maiusculas}")

tuplas_numero_quadrado = [(x, x**2) for x in range(1, 6)]
print(f"5. Tuplas (número, quadrado) para 1 a 5: {tuplas_numero_quadrado}")
