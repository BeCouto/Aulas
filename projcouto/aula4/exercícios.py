"""
Programação Estruturada
2024.1
04/03/2024

Exercícios
Nota de aula 05
"""

"""

Exercício resolvido 01
Faça uma função media(), que recebe os parâmetros posicionais
ap1, ap2 e ac, e retorne a média de avaliações, utilizando a
fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""
def M(ap1, ap2, ac):
    return round ((ap1 + ap2) * 0.4 + ac * 0.2, 2)
print(M(5,2,7))
