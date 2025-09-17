def potencia_de_2(x):
    return 2**x

def raiz_n_de_x(x, indice=2):
    return x**(1/2)

def fluxo_de_operacao(numeros,operacao):
    resultado = []
    for x in numeros:
        resultado.append(operacao(x))

    print(resultado)
valores = [12, 3, 56, 456, 1, 13]
fluxo_de_operacao(valores,potencia_de_2)
fluxo_de_operacao(valores,raiz_n_de_x)