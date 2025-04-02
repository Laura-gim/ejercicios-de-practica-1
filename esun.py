class Animal:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def hacer_sonido (self):
        return f"{self.nombre} hace n sonido"
    def moverse(self):
        return f"{self.nombre} se está moviendo"
