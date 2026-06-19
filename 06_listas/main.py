import utils
from utils import sep

idade1 = 10
idade2 = 20
idade3 = 30
idade4 = 40
idade5 = 50


lista = [idade1, idade2, idade3, 12, idade4, idade5, 42, 31]
utils.mostrar_idade(lista)


idd = [10, 20, 30, 40, 50]


utils.mostrar_idade(idd)

print(idd[0])
print(idd[2])

#                                idx:  0    2    4
# cire uma lista com 5 nomes, mostre o 1º, o 3º e 5º

#          |               |                |
#          V               V                V
nomes = ["Ana", "Maria","Joana", "Diana", "Rita"]
#idx       0       1      2         3       4


print(nomes[0])
print(nomes[2])
print(nomes[4])

print(f"{nomes[0]}, {nomes[2]}, {nomes[4]}")
print(f"{nomes[0], nomes[2], nomes[4]}")


sep()


print(len(nomes)) ## len -> num de elm na lista
sep()

for i in range(len(nomes)): #range(n) 0 ate n-1
    print(nomes[i])

sep()

for elm in nomes:
    print(elm)


#
# Crie uma lista com 10 nomes
# mostre os nomes nas index par (0 é par)
#

sep()
nomes = ["Ana", "Maria","Joana", "Diana", "Rita",
         "Ana", "Maria","Joana", "Diana", "Rita"]


for i in range(0, len(nomes), 2):
    print(nomes[i])

sep()
sep()

for idx in range(len(nomes)):
    if idx % 2 == 0:
        print(nomes[idx])


sep()
sep()


lista = ["Ana"]
print(lista)

lista.append("Maria") ## adiciona um valor no final da lista, depois da última posição
print(lista)

lista.append("Catarina")
print(lista)

lista.insert(0, "Rui") # adiciona um valor na posição indicada
print(lista)

lista.insert(111111110, "Rui")
print(lista)

sep()
sep()
sep()

#
# Peça ao utilizador 5 nomes (for, input)
#    Adicoine os nomes pedidos ao final de uma lista (append)
#    Mostre todos os elementos da lista (for, print)
#

"""
nomes_ex3 = []

for i in range(1, 6):
    nome = input(f"Digite o {i}º nome: ")
    nomes_ex3.append(nome)

print("--nomes adicionados--")
for nome in nomes_ex3:
    print(nome)
    
"""

sep()
sep()

print(nomes)
n = nomes.remove("Rita") ## remover a 1 ocur do valor
nomes.remove("Rita")
# nomes.remove("Rita") # se o valor não existir -> Erro
print(nomes)
print(n)

n = nomes.pop() # sem valor remove o ultimo
print(nomes)
print(n)

nomes.pop(3) # com valor remove o elm no idx indicado (3)
print(nomes)

# nomes.pop(123) # # se o idx não existir -> Erro
print(nomes)


#
# Peça ao utilizador 5 nomes (for, input)
#    Adicoine os nomes pedidos ao final de uma lista (append)
#    Mostre todos os elementos da lista (for, print)
#    remova a um nome da lista (um nome qualquer, mas fornecido pelo programador)
#    remova o último elm da lista
#    remova o 2 nome da lista
#