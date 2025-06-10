# Importa a biblioteca matemática para usar funções como sqrt, sin, etc.
import math

# Soma dois números
def somar(num_1, num_2):
    return num_1 + num_2

# Subtrai dois números
def subtrair(num_1, num_2):
    return num_1 - num_2

# Multiplica dois números
def multiplicacao(num_1, num_2):
    return num_1 * num_2

# Divide dois números
def divisao(num_1, num_2):
    return num_1 / num_2  # Atenção: precisa tratar divisão por zero no futuro

# Retorna a raiz quadrada de um número
def raiz_quadrada(num_1):
    return math.sqrt(num_1)

# Calcula potência de num_1 elevado a num_2
def potencia(num_1, num_2):
    return math.pow(num_1, num_2)

# Retorna o seno de um número em graus
def seno(num_1):
    return math.sin(math.radians(num_1))

# Retorna a tangente de um número em graus
def tangente(num_1):
    return math.tan(math.radians(num_1))

# Retorna o cosseno de um número em graus
def cosseno(num_1):
    return math.cos(math.radians(num_1))
