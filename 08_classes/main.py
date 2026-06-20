from Quadrado import Quadrado
from Bola import Bola
from Carro import Carro



idade = 10
carro1 = Carro("Pagani", "Zonda")

idade2 = 20
carro2 = Carro("Lamborghini", "Diablo")



print(carro1.marca)
print(carro1.modelo)
print("--------")
print(carro2.marca)
print(carro2.modelo)

print("--------")

carro2.modelo = "Fenomeno"

print(carro2.marca)
print(carro2.modelo)


print("--------")

carro2.mudar_modelo("Avantador")

print(carro2.marca)
print(carro2.modelo)


print("--------")

# mudar a marca do carro
## Crie um metodo para mudar a marca do carro

carro2.mudar_marca("Audi")

print(carro2.marca)
print(carro2.modelo)

print("--------")
## Crie um metodo para mudar a marca e o modelo do carro

carro2.mudar_dados("Ford", "Fiesta")

print(carro2.marca)
print(carro2.modelo)


print("--------")

"""
Classe Bola: Crie uma classe que modele uma bola: 
    Atributos: Cor, circunferencia, material
    Métodos: trocaCor e mostraCor
"""


bola = Bola("Amarela", 30, "plastico")

print(bola.cor)

bola.mostraCor()



print("--------------")

"""
Classe Quadrado: Crie uma classe que modele um quadrado: 
Atributos: 
    Tamanho do lado
Métodos:    
    Mudar valor do Lado, 
    Retornar valor do Lado 
    calcular Área; - def area(self):
                        return self.lado * self.lado

"""

q2 = Quadrado(4)
q3 = Quadrado(4)

q2.set_lado(16)

"""
Classe Retangulo: Crie uma classe que modele um retangulo: 

Atributos: LadoA, LadoB 
    (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos:
     Mudar valor dos lados, 
     Retornar valor dos lados, 
     calcular Área e calcular Perímetro;
     
Crie um programa que utilize esta classe.
 
"""

"""
Classe Pessoa: Crie uma classe que modele uma pessoa: 
Atributos: nome, idade, peso e altura
Métodos: 
    Envelhercer, 
    Engordar, 
    Emagrecer, 
    Crescer. 

Obs: Por padrão, a cada ano que nossa pessoa envelhece,
 sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
 
"""