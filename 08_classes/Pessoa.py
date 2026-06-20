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
from soupsieve import select


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def emagrecer(self, kgs):
        self.peso -= kgs # self.pese = self.pese - kgs

    def engordar(self, kgs):
        self.peso += kgs


    def envelhecer(self, num_anos:int = 1):
        nova_idade = self.idade + num_anos

        for i in range(self.idade, self.minimo(22, nova_idade+1)):
            self.crescer()


    def minimo(self, v1, v2):
        if v1 > v2:
            return v1
        else:
            return v2



    def crescer(self, cm:float = 0.5 ):
        self.altura += cm

