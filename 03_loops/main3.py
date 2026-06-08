
for i in range(1,10):

    if i % 2 == 0:
        continue # salta para a volta seguinte

    if i == 5:
        break # terminar o loop

    print(i)


"""

peça ao utilizado 3 números (n1, n2 e n3).

Crie um loop de  0 a n1
    mostre todos os valores mas aplique as condições antes de mostrar os números:
        
        quando o i for divisivel por n2 salte para a porxima iteração 
        quando i for igual a n3 termine o loop

% - > resto da div
// -> div int

>
>=
<
<=

==
!=

"""

print("Print 0")

for n in range(1,10): # 5 6 7 8 9
    if n % 2 == 0:
        print("Print 1")
        continue # termina a volta e passa para a proxima volta

    print("Print 2")


print("Print 3")

"""
num1 = int (input ("Insira o primeiro número: ")) # 20
num2 = int (input ("Insira o segundo número: ")) # 2
num3 = int (input ("Insira o terceiro número: "))

for i in range (num1+1):
    # print (i)
    if i % num2 == 0:
        continue

    print (i)


"""

"""
Crie um loop de  0 a n1 - Done        
quando o i for divisivel por n2 salte para a porxima iteração - Done

quando i for igual a n3 termine o loop
        
"""


n1 = 30  # int(input("Numero 1: "))
n2 = 2   # int(input("Numero 2: "))
n3 = 16  # int(input("Numero 3: "))

for i in range (n1+1):

    if i % n2 == 0:
        continue

    if i > n3:
        break

    print (i)


"""
Faça um programa que peça ao utilizador um número
mostre a tabuada desse número.

Exp 
num = 2

out:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
...
2 x 10 = 20
"""

num = int(input("Digite um número: "))

for i in range(1,11): # 1 a 10
    res = num * i
    print(f"{num} x {i:2} = {res:2}")


# peça ao utilizador N números, calcule a média desses valores (deve usar um for)
# o valor de N deve ser fornecido pelo usr


soma = 0
total_num = int(input("Digite quantos num quer: "))

for i in range(1, total_num+1):
    n = int(input(f"digite o num {i} de {total_num}: "))
    soma = soma + n

media = soma / total_num

print(f"a media é {media:.2f}")