class Animal:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def hacer_sonido (self):
        return f"{self.nombre} hace n sonido"
    def moverse(self):
        return f"{self.nombre} se está moviendo"
class Perro(Animal):
    def __init__(self,nombre, edad, raza):
        super().__init__(nombre,edad)
        self.raza=raza

    def hacer_sonido(self):
        return f"{self.nombre} está ladrando"
    
    def se_para_en_2_patas(self):
        return f"{self.nombre} se para en 2 patas"

class Gallina(self):
    def __init__(self,nombre,edad,tipo):
        super().__init__(nombre,edad)
        self.tipo=tipo

    def hacer_sonido(self):
        return f"{self.nombre} está cacareando"
    def picotear(self):
        return f"{self.nombre} picotea"
    
Animaldepreuba=Animal("loro",5)
perro1=Perro("Toby",2,"caniche")
gallna1=Gallina("Manchita",1,"Brahma")
