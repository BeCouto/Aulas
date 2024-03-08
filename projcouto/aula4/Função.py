"""
Programação Estruturada
2024.1
08/03/2024

Funções
- Encapsulamento
- Evitar ao máximo duplicidade de código
- organização do código
"""

PI = 3.14

def linha(largura, traco):
    print(traco * largura)

def cabecalho(título,largura=30, traco="."):
    linha(largura, traco)
    print(título)
    linha(largura, traco)

cabecalho("Folha de pagamento", 30)
cabecalho("Lista de fornecedores", 25)
cabecalho("DEMOSTRATIVO DE RESULTADOS", traco="=")

# Não é chamar a função, é indicar a referência da função
cabecalho
print(cabecalho)

def soma(a, b):
    return a + b

print(soma(4,8) + soma(2, -5))

#múltiplos retornos
def subsequentes(x):
    return x + 1, x + 2 # tupla

x, y = subsequentes(10)
print(x , y)
print(subsequentes(5))

print("-" * 30)
# Escopo de variáveis
x = 0 # escopo global

def func1(x):
    x = 1 # escopo local
    print(x)

def func2():
    x = 2
    print(x)

def func3():
    print(x)

def func4():
    global x # NÃO USAR!!!!!
    x = 4
    print(x)

print(x)
func1(x)
func2()
func3()
func4()
print(x)

# Evitem o uso de variáveis globais
# A não ser que sejam constantes (no início do arquivo)
