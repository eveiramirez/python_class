class Pol_Regular(object):

    def __init__(self, nombre: str, no_lados: int, tam_lados: int):
        self.nombre = nombre
        self.no_lados = no_lados
        self.tam_lados = tam_lados

    def sum_ang_int(self):
        ang = 180*(self.no_lados-2)
        return ang

    def ang_cent(self):
        ang = 360 / self.no_lados
        return ang

    def ang_int(self):
        ang = 180 * (self.no_lados - 2)/self.no_lados
        return ang

    def ang_ext(self):
        ang_sup = self.ang_int()
        return 180 - ang_sup

    def perimetro(self):
        p = self.no_lados*self.tam_lados
        return p

    def area(self, apotema: int):
        a = (self.perimetro()*apotema)/2
        return a


class Cuadrado(Pol_Regular):
    def ang_int(self):
        return 90

    def ang_ext(self):
        return 90

    def ang_cent(self):
        return 90


class Triangulo(Pol_Regular):
    def sum_ang_int(self):
        return 180
