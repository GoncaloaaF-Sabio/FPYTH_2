"""


Faça um programa que use a função valorPagamento para determinar o valor a ser pago
por uma prestação de uma conta.

O programa deverá solicitar ao utilizador o valor da prestação
e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.

 O programa deverá então exibir o valor a ser pago na tela.

 Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
 até que seja informado um valor igual a zero para a prestação.


 Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor
 total de prestações pagas no dia.

 O cálculo do valor a ser pago é feito da seguinte forma:
    Para pagamentos sem atraso, cobrar o valor da prestação.
    Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
                                                1d - 0,1
                                                2d - 0,2
"""



"""

pedir: 
valor da prestação
número de dias em atraso

"""

MULTA = 0.03
JURO_DIA = 0.001

def valorPagamento(valor_p: float, n_dias: int) -> float:
    if n_dias == 0:
        return valor_p

    multa = valor_p * MULTA
    juros = valor_p * (JURO_DIA * n_dias)

    return valor_p + multa + juros

total_prestacao = 0
qtd_prestacao = 0

while(True):

    valor_prestacao = float(input("Valor da prestação: "))
    num_dias = int(input("Número de dias em atraso: "))

    if valor_prestacao == 0:
        break
    resposta = valorPagamento(valor_prestacao, num_dias)

    total_prestacao += resposta # <=> total_prestacao = total_prestacao + resposta
    qtd_prestacao += 1

    print(f"valor da prestação {resposta:.2f}€")

print(f"foram pagas {qtd_prestacao} prestações num valor total de {total_prestacao:.2f}€")