from app import somar # importamos a função somar do arquivo app.py

def test_somar():
    assert somar(2, 3) == 5 # assert em Python é uma instrução para definir verificações de integridade em seu código
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0
    print("Deu tudo certo !") # se passar por todos os assert sem dar erro e imprimir esse print então nossa função está funciondo perfeitamente !

test_somar() # aqui chamamos nossa função para ela ser rodada