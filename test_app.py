from app import*
num_1=int(input("Digite o valor principal: "))
num_2=int(input("Digite outro valor: "))
print(f"\n\tOperações matemáticas\n\nSomar: {somar(num_1,num_2)}\nSubtrair:{subtrair(num_1,num_2)}\nMultiplicacao: {multiplicacao(num_1,num_2)}\nDivisao:{divisao(num_1,num_2)}\nRaiz_quadrada: {raiz_quadrada(num_1)}\nPotencia:{potencia(num_1,num_2)}\n\n\tOperações trigonométricas\n\nSeno: {seno(num_1)}\nTangente: {tangente(num_1)}\nCosseno: {cosseno(num_1)}\n")