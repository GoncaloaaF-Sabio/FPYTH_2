"""

var
tipos de dados
in / out
op com var
condições
    if - elif - else
    match - case
range
loops
    while
    for

"""


def ola_mundo():
    print("ola mundo")

ola_mundo()
ola_mundo()

def msg(nome:str): # type hint
    print(f"ola mundo, {nome}")


def ola_mundo2(nome):
    print(f"ola mundo, {nome}")

ola_mundo2("Gonçalo")
ola_mundo2("Rui")


n = input("Digite o seu nome: ")
ola_mundo2(n)

msg("Ola")


def msg2(nome:str, ano:int): # type hint
    print(f"ola mundo, {nome} no ano {ano}")


msg2("Gonçalo", 2026)
msg2(nome="Gonçalo", ano=2026)
msg2("Gonçalo", ano=2026)


# crie uma func que receba 2 num e mostre a soma desses 2 num


def soma1(num1:int, num2:int):
    soma = num1 + num2
    print(f"{num1} + {num2} = {soma}")

soma(4, 5)


print("---------")
def soma2(num1:int, num2:int):
    soma = num1 + num2
    return soma

res = soma2(42, 5)
print(res)


res = soma2(90, 51)
print(res)

print(soma2(3,5))

# 1  Crie uma função que receba um num, diga se ele e positivo ou negativo --> print

def pos_v1(num:int):
    if num > 0:
        print("Positivo")
    else:
        print("Negativo")


# 2  Crie uma função que receba um num, devolva mensagem se ele e positivo ou negativo --> return
#   Mostre a mensagem

def pos_2(num:int):
    if num >= 0:
        return "Positivo"
    else:
        return "Negativo"

def msg_pos(resp:str):
    print(f"o número é {resp}")

pos_neg = pos_2(1)
print(f"o número é {pos_neg}")


# msg_pos(pos_neg)


