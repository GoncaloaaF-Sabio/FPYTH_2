
num = 10

while num > 0:
    print(f"o num é {num}")

    num -= 1


# refaça o ex tabuada, mas com usando o while em vez de um for

num = int(input("Digite um número: "))

max_val = 10
curr_val = 1
while curr_val <= max_val:

    res = num * curr_val
    print(f"{num} x {curr_val:2} = {res:2}")

    curr_val += 1


print("--V2--")


i = 1
while i <= 10 :

    res = num * i
    print(f"{num} x {i:2} = {res:2}")

    i += 1



# faça um programa que peça num a utilizador, quando for inserido um valor negativo o programa termina
    # tem de usar o while
    # o break e continue funcionam da mesma forma que no for



while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break

print("O programa terminou (V1)")
print("--V2--")

num = int(input("Digite um numero: "))
while num > 0:
    num = int(input("Digite um numero: "))


print("O programa terminou (V2)")


print("--V3--")

while int(input("Digite um numero: ")) > 0:
    pass # instrução para não da erro em blocos sem código

print("O programa terminou (V3)")














