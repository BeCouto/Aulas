"""
Este é um comentário de várias linhas.

Docstring - texto de documentação

programação estruturada
2024.01
01/03/2024

Introdução a python
-Documentação código
-Saída de dados
-Tipos de dados
-Entrada de daos
-Variáveis
"""

# Este é um comentário de código.
# Fazemos uma marcação de comentário (#) para cada linha.
print("olá, mundo") # exibe uma informação na tela.

# saída de dados
print("olá, mundo", end="----")
print("olá,","mundo")
print("Ana tem", 22, "anos", sep="--")

# tipos de dados primitivos
print(4, 7, -10, 2)              # int
print(4.2, 5.0, -1.26, 11.48)    # float
print(True, False)               # bool
print("abc", "def")              # str
print(None)                      # NoneType

print(2)
print(2.0)
print("2")

print("olá, mundo")
print('olá, mundo')

# caractere de escape - escape char(\)
print("olá, \"mundo\"")
print("olá, \'mundo\'")
print('olá, "mundo"')
print("olá,\nmundo")
print("olá,\tmundo")
print("C:\\Projetos")
print("C:\\\\Projetos")

print("""Este é um texto
com multiplas linhas.""")
print('''Este é um texto
com múltiplas linhas''')

# Lendo dados do Usuário
print(input("informe o seu nome: "))

# Variáveis
# Convenção de nomeação de variáveis: snake_case
nome = input("Informe o seu nome: ")
print("Olá,", nome)

nome = "Gabriel"
print(nome)

# Python é uma linguagem de tipagem fraca e dinâmica
nome = 17

# Não existem constantes em Python
# ALL_CAPS
PI = 3.1415

