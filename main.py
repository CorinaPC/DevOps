# Importa todas as funções do app.py
from app import *

# Pede dois valores para o usuário
num_1 = float(input("Digite o valor principal: "))
num_2 = float(input("Digite outro valor: "))

# Mostra os resultados das operações
print(f"""
\tOperações matemáticas

Somar: {somar(num_1, num_2)}
Subtrair: {subtrair(num_1, num_2)}
Multiplicação: {multiplicacao(num_1, num_2)}
Divisão: {divisao(num_1, num_2)}
Raiz quadrada (do primeiro número): {raiz_quadrada(num_1)}
Potência: {potencia(num_1, num_2)}

\tOperações trigonométricas (com base no primeiro número em graus)

Seno: {seno(num_1)}
Cosseno: {cosseno(num_1)}
Tangente: {tangente(num_1)}
""")
