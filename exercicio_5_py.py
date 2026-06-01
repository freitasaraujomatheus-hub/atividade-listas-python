# -*- coding: utf-8 -*-
import operator

turma = [
    ['Alice', 8.0, 7.5, 9.0],
    ['Bruno', 6.5, 7.0, 8.0],
    ['Carla', 9.5, 9.0, 9.5],
    ['Diego', 5.0, 6.0, 5.5],
    ['Elena', 7.0, 8.5, 7.5],
]

medias_alunos = {}

print("1. Nome e média de cada aluno:")
for aluno in turma:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)
    medias_alunos[nome] = media
    print(f"Aluno: {nome}, Média: {media:.2f}")

print("\n2. Aluno com maior média:")

aluno_maior_media = max(medias_alunos.items(), key=operator.itemgetter(1))
print(f"O aluno com maior média é: {aluno_maior_media[0]} com média {aluno_maior_media[1]:.2f}")

print("\n3. Alunos aprovados e reprovados:")
aprovados = []
reprovados = []
for nome, media in medias_alunos.items():
    if media >= 6.0:
        aprovados.append(nome)
    else:
        reprovados.append(nome)
print(f"Aprovados: {', '.join(aprovados)}")
print(f"Reprovados: {', '.join(reprovados)}")

print("\n4. Média geral da turma:")
media_geral_turma = sum(medias_alunos.values()) / len(medias_alunos)
print(f"Média geral da turma: {media_geral_turma:.2f}")

print("\n5. Adicionar novo aluno e re-imprimir ranking:")
novo_aluno = ['Felipe', 8.0, 7.5, 8.5]
turma.append(novo_aluno)

medias_alunos_atualizadas = {}
for aluno in turma:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)
    medias_alunos_atualizadas[nome] = media

ranking_turma = sorted(medias_alunos_atualizadas.items(), key=operator.itemgetter(1), reverse=True)

print("Ranking da turma (ordem decrescente de média):")
for nome, media in ranking_turma:
    print(f"- {nome}: {media:.2f}")
