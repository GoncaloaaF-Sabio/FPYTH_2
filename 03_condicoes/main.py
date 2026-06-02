idade = 15

"""
>
<
>=
<=
== 
!= 

"""

if idade >= 18:
    print("Adulto")

idade = 18

# faça uma condição que verifique se a pessoa tem mais de 15 anos
if idade > 15:
    print("mais de 15 anos")

if 15 < idade:
    print("mais de 15 anos")

# faça uma condição que verifique se a pessoa tem 15 anos

if idade == 15:
    print("15 anos")

# faça uma condição que verifique se a pessoa nao tem 15 anos
if idade != 15:
    print("não tem  15 anos")


print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")

idade = 20


if idade >= 18:
    print("Adulto")
else:
    print("menor de 18 anos")

print("-----------------------")
print("-----------------------")
print("-----------------------")
print("-----------------------")


"""
se >= 18 -> adulto
se > 12 e  < 18 -> teen
se < 12 -> kid


"""
idade = 10

if idade >= 18:
     # código....
     print("Adulto")
     # código....
     # código....
elif idade > 12:
    print("teen")
    print("teen linha 2")
else: # executado se nenhuma das condições anteriores for valida
    print("kid")


print("Fim do programa")

# comentário de 1 so linha

""" (3 aspas) -> comentário multi-linha  

Faça um programa que receba uma hora (1 a 24)

se a hora for menor de 7 deve dizer madrugada
se for maior de 7 e menos de 13 deve dizer manha
se for maior de 13 e menos de 20 deve dizer tarde
se for maior de 20 deve dizer noite

usem a estrutura  if - elif - else  (o elif pode ser repetido as vezes que quiserem)

"""

# assumir que a hora está sempre entre 0 e 24

hora = 0

if hora <= 0:
    print("hora invalida")
elif hora < 7:
    print("Matrugada")
elif  hora < 13:
    print("Manha")
elif hora < 20:
    print("Tarde")
elif hora <= 24:
    print("Noite")
else:
    print("hora invalida")







"""
hora = 12
if hora > 0:
    print("hora invalida")
elif hora > 24:
    print("hora invalida")
else:
    if hora < 7:
        ......

"""


