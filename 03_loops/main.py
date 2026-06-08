"""
setup - Aula 1

tipos de dados  #
var             # Aula 2
op com var      #

condições               #
    if - elif - else    # Aula 3
    match               #

"""

# range

range(5) # -> 0, 1, 2, 3, 4 -> range(n) todos os valores de 0 ate n-1

range(5,10) # -> 5, 6, 7, 8, 9 -> range(m, n) todos os valores de m ate n-1
range(0,5) # <=>  range(5)


range(6,15,2) # 6, 8, 10, 12, 14 -> range(M, N, S) todos os valores de M ate N-1 de S em S

range(0,9,2) # 0, 2, 4, 6, 8


# for

# mostre a msg "ola Mundo" 20 vezes na consola
# adicoine o num da repetição depois da msg

for i in range(6, 21):
    print(f"Ola Mundo {i}")


# peça ao utilizador um número inteiro positivo

num = int(input("Numero: "))

# mostre todos os valores inteiros entre 0 e esse número

for i in range(0, num+1):
    print(i)

print("Terminado")
