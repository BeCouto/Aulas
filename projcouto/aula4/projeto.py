"""
Programação Estruturada
2024.1
08/03/2024

função - exemplo de aplicação
"""

def leitura_valores():
    a = float(input("Informe um número: "))
    b = float(input("Informe outro número: "))
    return a, b

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def main():
    x, y = leitura_valores()
    print("A soma é", soma(x, y), "e a subtração é", subtracao(x, y))

main()