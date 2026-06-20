class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # return self.lado ** 2  # ** -> elevado
        # return pow(self.lado, 2)
        return self.lado * self.lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado