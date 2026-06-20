class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mudar_modelo(self, modelo):
        self.modelo = modelo

    def mudar_marca(self, marca):
        self.marca = marca


    def mudar_dados(self, marca, modelo):
        self.modelo = modelo
        self.marca = marca




"""
class mesa:
    def __init__(self,ref, numero_prenas, tampo, gavetas):
        self.ref = ref
        self.numero_prenas = numero_prenas
        self.tampo = tampo
        self.gavetas = gavetas

"""