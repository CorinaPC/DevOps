# Importa todas as funções que serão testadas
from app import somar, subtrair, multiplicacao, divisao, raiz_quadrada, potencia, seno, cosseno, tangente

# Testa a função de soma
def test_somar():
    assert somar(2, 3) == 5

# Testa a subtração
def test_subtrair():
    assert subtrair(5, 3) == 2

# Testa a multiplicação
def test_multiplicacao():
    assert multiplicacao(4, 3) == 12

# Testa a divisão
def test_divisao():
    assert divisao(10, 2) == 5

# Testa raiz quadrada
def test_raiz_quadrada():
    assert raiz_quadrada(25) == 5

# Testa potência
def test_potencia():
    assert potencia(2, 3) == 8

# Testa seno de 30 graus (valor conhecido ≈ 0.5)
def test_seno():
    assert round(seno(30), 2) == 0.5

# Testa cosseno de 60 graus (≈ 0.5)
def test_cosseno():
    assert round(cosseno(60), 2) == 0.5

# Testa tangente de 45 graus (≈ 1)
def test_tangente():
    assert round(tangente(45), 2) == 1
