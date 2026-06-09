
#1.1 Crie uma func que receba 2 números inteiros, devolva o resultado da soma dos dois números
#1.2   Crie uma func que calcule o dobro do rescultada do soma ( num inteiro ) e devolva o valor
#1.3   Crie uma func que mostre o dobro do resultado da soma (pode incluir uma msg personalizada)

#2.1 No mesmo programa crie uma func que receba 2 números inteiros, devolva o resultado da multiplicação dos dois números
#2.2   crie uma func que calcule o dobro do resultada do multiplicação e devolva o valor
#2.3   Crie uma func que mostre o dobro do resultado da multiplicação (pode incluir uma msg personalizada)
"""

def soma(n1:int, n2:int) -> int:
    return n1 + n2

"""
#                        o que func deve devolver, pode ser ocultado
def soma(n1:int, n2:int) -> int:
    soma = n1 + n2
    return soma

def multiplica(n1:int, n2:int) -> int:
    multip = n1 * n2
    return multip


def dobro(n:int) -> int:
    return n * 2


def msg(valor:int):
    print(f"O resultado da operação é: {valor}")


s = soma(5,10)

dobro_soma = dobro(s)

msg(dobro_soma)


s = multiplica(5,10)

dobro_m = dobro(s)

msg(dobro_m)
