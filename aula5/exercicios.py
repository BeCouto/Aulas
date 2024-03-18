"""
Programação Estruturada
2024.1
06/03/2024

Exercícios sobre estruturas de decisão
"""

"""
Exercício resolvido 02
Implemente um programa que receba dois números e retorne o maior deles.
"""
def maior(n1 , n2):
    return n1 if n2 < n1 else n2
print(maior(1, 3))

"""
Exercício resolvido 04
Faça um programa que verifique se uma letra é vogal ou consoante.
"""
def letra(vogal):
    match vogal:
        case "a" | "e" | "i" |"o"| "u":
            return "é vogal"
        case _:
            return "consoante"

print(letra("b"))

"""
Exercício resolvido 05
Faça um programa que receba três notas, calcule sua média
aritmética simples e apresente na tela uma das seguintes
informações:

- A mensagem “Aprovado”, se a média alcançada for maior ou
igual a sete;
- A mensagem “Reprovado”, se a média for menor do que sete;
- A mensagem “Aprovado com Distinção”, se a média for igual a
dez;
- A mensagem “Nota inválida!” toda vez que for inserido um valor
inválido.
"""

def nota_invalida(nota):
    return nota < 0 or nota > 10

def nota_valida(nota):
    return 0 <= nota <= 10

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    # if not (valida_nota(nota1) and valida_nota(nota2) and valida_nota(nota3)):
    if nota_invalida(nota1) or nota_invalida(nota2) or nota_invalida(nota3):
        print("Nota inválida")
    elif media == 10:
        print("Aprovado com Distinção")
    elif media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

calcular_media(10,10,10)
