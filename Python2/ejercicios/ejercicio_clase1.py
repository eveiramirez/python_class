class Animal(object):
    nombre = 0
    edad = 0

    def __init__(self, nombre: str, edad: int, ruido: str):
        self.nombre = nombre
        self.edad = edad
        self.ruido = ruido

    def haz_ruido(self):
        print(self.ruido)


class Perro(Animal):
    def haz_ruido(self):
        print("gdziejestbiaływęgorz")


class Gato(Animal):
    usa_arenero = True

    def haz_ruido(self):
        print("Me pareció ver un lindo gatito")


vaca = Animal("Vaquita", 4, "Muuu")
pug = Perro("Ojitos", 3, "uffff")
tom = Gato("Tom", 13, "Miau")

vaca.haz_ruido()
pug.haz_ruido()
tom.haz_ruido()
